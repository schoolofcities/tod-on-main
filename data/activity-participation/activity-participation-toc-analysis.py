import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon

# load in stations, filter just for GO and Subway
stations = gpd.read_file("current-stations.geo.json").to_crs(epsg=32617)
stations = stations[(stations['TECHNOLOGY'] == 'Subway') | (stations['TECHNOLOGY'] == 'GO Rail')]
stations["geometry"] = stations["geometry"].apply(lambda g: g.buffer(0) if not g.is_valid else g)

# load in TTS data, join, filter for just GTA
tts_zones = gpd.read_file("ttszones-2022.gpkg").to_crs(epsg=32617)
tts_metrics = pd.read_csv("tts2022-metrics-taz.csv")
tts_zones = tts_zones[tts_zones['Reg_no'] < 6]
tts_zones = tts_zones.merge(tts_metrics, how='left', left_on='TTS2022', right_on='tts22_hhld')
tts_zones["geometry"] = tts_zones["geometry"].apply(lambda g: g.buffer(0) if not g.is_valid else g)




def area_pop_weighted_average_with_pop_and_moe(
    poly, zones_gdf,
    value_col="activities_mean",
    pop_col="persons_5up",
    sample_col="hhld_sample"
):
    """
    Compute area- and population-weighted average of a variable for a polygon,
    estimate total population, and approximate margin of error using zone sample sizes.
    
    Parameters
    ----------
    poly : shapely.geometry.Polygon or MultiPolygon
        The target polygon.
    zones_gdf : geopandas.GeoDataFrame
        GeoDataFrame of source zones (must have a geometry column).
    value_col : str
        Column in zones_gdf containing the variable to interpolate.
    pop_col : str
        Column in zones_gdf containing population counts.
    sample_col : str
        Column in zones_gdf containing the sample size (for margin of error).
    
    Returns
    -------
    dict
        {
            "weighted_mean": float or None,
            "population": float or None,
            "moe_95": float or None
        }
    """
    overlap = zones_gdf[zones_gdf.intersects(poly)].copy()
    if overlap.empty:
        return {"weighted_mean": None, "population": 0, "moe_95": None}

    # Compute intersection area fraction (relative to zone area)
    overlap["intersection_area"] = overlap.intersection(poly).area
    overlap["zone_area"] = overlap.area
    overlap["area_fraction"] = overlap["intersection_area"] / overlap["zone_area"]

    # Estimate population within the overlap
    overlap["pop_overlap"] = overlap["area_fraction"] * overlap[pop_col]
    total_pop = overlap["pop_overlap"].sum()
    if total_pop == 0:
        return {"weighted_mean": None, "population": 0, "moe_95": None}

    # Weighted mean
    weighted_mean = (overlap[value_col] * overlap["pop_overlap"]).sum() / total_pop

    # --- Approximate margin of error ---
    # Filter out zones with zero or missing sample
    overlap = overlap[overlap[sample_col] > 0].copy()
    if overlap.empty:
        moe_95 = None
    else:
        # Standard error of each zone mean (proportion approximation)
        # Avoid division by zero
        overlap["se_zone"] = (overlap[value_col] * (1 - overlap[value_col]) / (overlap[sample_col] + 1e-6)).pow(0.5)
        # Weighted SE
        overlap["weight"] = overlap["pop_overlap"] / total_pop
        se_weighted = (overlap["se_zone"]**2 * overlap["weight"]**2).sum()**0.5
        # 95% MoE
        moe_95 = 1.96 * se_weighted

    return {"weighted_mean": weighted_mean, "population": total_pop, "moe_95": moe_95}




mimico_station = stations.loc[stations["LOCATION_N"] == "Finch"].buffer(800)

if mimico_station.empty:
	print("No station named Mimico found.")
else:
	# Get the geometry of that station
	mimico_geom = mimico_station.geometry.iloc[0]

	# Compute the area-weighted average
	print(area_pop_weighted_average_with_pop_and_moe(mimico_geom, tts_zones, "activities_mean", "persons_5up", "hhld_sample"))
	print(area_pop_weighted_average_with_pop_and_moe(mimico_geom, tts_zones, "activities_mean_nocar_lowinc", "hhld_sample", "person_ind_low_income_no_car_hhld"))







# # total comparisons

from shapely.ops import unary_union

# --- Step 1: Create 800m buffers around all stations and dissolve overlaps ---
station_buffers = stations.geometry.buffer(800)
combined_buffer = unary_union(station_buffers)

# --- Step 2: Compute area- and population-weighted mean + MoE inside the combined buffer ---

# Metric 1
result_metric1 = area_pop_weighted_average_with_pop_and_moe(
    combined_buffer,
    tts_zones,
    value_col="activities_mean",
    pop_col="persons_5up",
    sample_col="hhld_sample"
)
pop_buffer_1 = result_metric1["population"]
activities_mean_buffer_1 = result_metric1["weighted_mean"]
moe_buffer_1 = result_metric1["moe_95"]

# Metric 2
result_metric2 = area_pop_weighted_average_with_pop_and_moe(
    combined_buffer,
    tts_zones,
    value_col="activities_mean_nocar_lowinc",
    pop_col="person_ind_low_income_no_car_hhld",
    sample_col="hhld_sample"
)
pop_buffer_2 = result_metric2["population"]
activities_mean_buffer_2 = result_metric2["weighted_mean"]
moe_buffer_2 = result_metric2["moe_95"]

# --- Step 3: Compute stats for outside the buffer (complement) ---

# Metric 1
pop_total_1 = tts_zones["persons_5up"].sum()
activities_mean_total_1 = (tts_zones["activities_mean"] * tts_zones["persons_5up"]).sum() / pop_total_1
pop_outside_1 = pop_total_1 - pop_buffer_1
activities_mean_outside_1 = (activities_mean_total_1 * pop_total_1 - activities_mean_buffer_1 * pop_buffer_1) / pop_outside_1

# Approximate MoE for outside using sqrt(weighted variances) propagation
# Assuming independence between inside/outside (approximation)
moe_outside_1 = moe_buffer_1 * (pop_buffer_1 / pop_outside_1)**0.5 if moe_buffer_1 is not None else None

# Metric 2
pop_total_2 = tts_zones["person_ind_low_income_no_car_hhld"].sum()
activities_mean_total_2 = (tts_zones["activities_mean_nocar_lowinc"] * tts_zones["person_ind_low_income_no_car_hhld"]).sum() / pop_total_2
pop_outside_2 = pop_total_2 - pop_buffer_2
activities_mean_outside_2 = (activities_mean_total_2 * pop_total_2 - activities_mean_buffer_2 * pop_buffer_2) / pop_outside_2

moe_outside_2 = moe_buffer_2 * (pop_buffer_2 / pop_outside_2)**0.5 if moe_buffer_2 is not None else None

# --- Step 4: Print results ---
print("=== Metric 1: activities_mean weighted by persons_5up ===")
print(f"Population inside buffer: {pop_buffer_1:.0f}")
print(f"Weighted mean inside buffer: {activities_mean_buffer_1:.4f} ± {moe_buffer_1:.4f}")
print(f"Population outside buffer: {pop_outside_1:.0f}")
print(f"Weighted mean outside buffer: {activities_mean_outside_1:.4f} ± {moe_outside_1:.4f}\n")

print("=== Metric 2: activities_mean_nocar_lowinc weighted by person_ind_low_income_no_car_hhld ===")
print(f"Population inside buffer: {pop_buffer_2:.0f}")
print(f"Weighted mean inside buffer: {activities_mean_buffer_2:.4f} ± {moe_buffer_2:.4f}")
print(f"Population outside buffer: {pop_outside_2:.0f}")
print(f"Weighted mean outside buffer: {activities_mean_outside_2:.4f} ± {moe_outside_2:.4f}")








# by line

results = []

for line_name in stations["NAME"].unique():
    # Get all stations for this line
    line_stations = stations[stations["NAME"] == line_name]
    
    # Create 800m buffers around these stations
    buffers = line_stations.geometry.buffer(800)
    
    # Dissolve overlapping buffers
    combined_buffer = unary_union(buffers)
    
    # Compute weighted mean, population, and MoE for low-income/no-car group
    result = area_pop_weighted_average_with_pop_and_moe(
        combined_buffer,
        tts_zones,
        value_col="activities_mean_nocar_lowinc",
        pop_col="person_ind_low_income_no_car_hhld",
        sample_col="hhld_sample"
    )
    
    # Append results
    results.append({
        "line_name": line_name,
        "population": result["population"],
        "weighted_mean": result["weighted_mean"],
        "moe_95": result["moe_95"]
    })

# Convert to pandas DataFrame
df_line_stats = pd.DataFrame(results)

# Optional: sort by line name
df_line_stats = df_line_stats.sort_values("line_name").reset_index(drop=True)

# Display
print(df_line_stats)




# by station

results_stations = []

# Loop over each station
for idx, station in stations.iterrows():
    station_name = station["LOCATION_N"]
    line_name = station["NAME"]
    
    # Create 800m buffer around the station
    buffer = station.geometry.buffer(800)
    
    # Compute weighted mean, population, and MoE for low-income/no-car group
    result = area_pop_weighted_average_with_pop_and_moe(
        buffer,
        tts_zones,
        value_col="activities_mean_nocar_lowinc",
        pop_col="person_ind_low_income_no_car_hhld",
        sample_col="hhld_sample"
    )
    
    # Append results
    results_stations.append({
        "station_name": station_name,
        "line_name": line_name,
        "population": result["population"],
        "weighted_mean": result["weighted_mean"],
        "moe_95": result["moe_95"]
    })

# Convert to pandas DataFrame
df_station_stats = pd.DataFrame(results_stations)

# Optional: sort by line and station name
df_station_stats = df_station_stats.sort_values(["line_name", "station_name"]).reset_index(drop=True)

# Save to CSV
df_station_stats.to_csv("station_activities_lowinc_nocar.csv", index=False)

# Display first few rows
print(df_station_stats.head())