import pandas as pd
import numpy as np

# -----------------------------
# Constants
# -----------------------------
Z = 1.96  # 95% confidence

# -----------------------------
# Load data
# -----------------------------
station_info = pd.read_excel("station-info.xlsx")
in_movers = pd.read_csv("in-movers-station-summary.csv")

# Merge data (in_movers is main table)
df = in_movers.merge(
    station_info,
    how="left",
    on="station_fid"
)

# -----------------------------
# Compute station-level MOE
# -----------------------------
valid_station = df[["decade", "in_movers_lowinc_station", "n_movers_in"]].dropna()
valid_station = valid_station[valid_station["n_movers_in"] > 0]

# MOE for a proportion: sqrt(p*(1-p)/n) * z
valid_station["moe_station"] = Z * np.sqrt(
    valid_station["in_movers_lowinc_station"] * 
    (1 - valid_station["in_movers_lowinc_station"]) / 
    valid_station["n_movers_in"]
)

# -----------------------------
# Compute CMA-level MOE
# -----------------------------
valid_cma = df[["decade", "in_movers_lowinc_cma", "n_movers_in"]].dropna()
valid_cma = valid_cma[valid_cma["n_movers_in"] > 0]

valid_cma["moe_cma"] = Z * np.sqrt(
    valid_cma["in_movers_lowinc_cma"] *
    (1 - valid_cma["in_movers_lowinc_cma"]) /
    valid_cma["n_movers_in"]
)

# -----------------------------
# Aggregate by City
# -----------------------------
summary_by_city = (
    valid_station
    .groupby("decade", dropna=False)
    .apply(lambda g: pd.Series({
        # weighted station-level proportion
        "weighted_avg_in_movers_lowinc_station": np.average(
            g["in_movers_lowinc_station"], weights=g["n_movers_in"]
        ),
        # weighted average of station MOEs
        "avg_moe_in_movers_lowinc_station": np.average(
            g["moe_station"], weights=g["n_movers_in"]
        ),
        "n_records_station": len(g),
        "total_movers_in": g["n_movers_in"].sum()
    }))
    .reset_index()
)

# CMA-level average and MOE by City (weighted by n_movers_in)
cma_summary = (
    valid_cma
    .groupby("decade", dropna=False)
    .apply(lambda g: pd.Series({
        "avg_in_movers_lowinc_cma": np.average(
            g["in_movers_lowinc_cma"], weights=g["n_movers_in"]
        ),
        "avg_moe_in_movers_lowinc_cma": np.average(
            g["moe_cma"], weights=g["n_movers_in"]
        ),
        "n_records_cma": len(g)
    }))
    .reset_index()
)

# Merge station and CMA summaries
summary_by_city = summary_by_city.merge(cma_summary, on="decade", how="left")

# -----------------------------
# Show final table
# -----------------------------
print(summary_by_city)















import pandas as pd
import numpy as np

# -----------------------------
# Constants
# -----------------------------
Z = 1.96  # 95% confidence

# -----------------------------
# Load data
# -----------------------------
station_info = pd.read_excel("station-info.xlsx")
out_movers = pd.read_csv("out-movers-station-summary.csv")

# Merge data (out_movers is main table)
df = out_movers.merge(
    station_info,
    how="left",
    on="station_fid"
)

# -----------------------------
# Compute station-level MOE
# -----------------------------
valid_station = df[["decade", "out_movers_lowinc_station", "n_movers_out"]].dropna()
valid_station = valid_station[valid_station["n_movers_out"] > 0]

valid_station["moe_station"] = Z * np.sqrt(
    valid_station["out_movers_lowinc_station"] *
    (1 - valid_station["out_movers_lowinc_station"]) /
    valid_station["n_movers_out"]
)

# -----------------------------
# Compute CMA-level MOE
# -----------------------------
valid_cma = df[["decade", "out_movers_lowinc_cma", "n_movers_out"]].dropna()
valid_cma = valid_cma[valid_cma["n_movers_out"] > 0]

valid_cma["moe_cma"] = Z * np.sqrt(
    valid_cma["out_movers_lowinc_cma"] *
    (1 - valid_cma["out_movers_lowinc_cma"]) /
    valid_cma["n_movers_out"]
)

# -----------------------------
# Aggregate by City
# -----------------------------
summary_by_city = (
    valid_station
    .groupby("decade", dropna=False)
    .apply(lambda g: pd.Series({
        "weighted_avg_out_movers_lowinc_station": np.average(
            g["out_movers_lowinc_station"], weights=g["n_movers_out"]
        ),
        "avg_moe_out_movers_lowinc_station": np.average(
            g["moe_station"], weights=g["n_movers_out"]
        ),
        "n_records_station": len(g),
        "total_movers_out": g["n_movers_out"].sum()
    }))
    .reset_index()
)

# CMA-level average and MOE by City
cma_summary = (
    valid_cma
    .groupby("decade", dropna=False)
    .apply(lambda g: pd.Series({
        "avg_out_movers_lowinc_cma": np.average(
            g["out_movers_lowinc_cma"], weights=g["n_movers_out"]
        ),
        "avg_moe_out_movers_lowinc_cma": np.average(
            g["moe_cma"], weights=g["n_movers_out"]
        ),
        "n_records_cma": len(g)
    }))
    .reset_index()
)

# Merge station and CMA summaries
summary_by_city = summary_by_city.merge(cma_summary, on="decade", how="left")

# -----------------------------
# Compute overall averages across all cities
# -----------------------------
overall_summary = pd.Series({
    "decade": "All cities",
    "weighted_avg_out_movers_lowinc_station": np.average(
        valid_station["out_movers_lowinc_station"], weights=valid_station["n_movers_out"]
    ),
    "avg_moe_out_movers_lowinc_station": np.average(
        valid_station["moe_station"], weights=valid_station["n_movers_out"]
    ),
    "n_records_station": len(valid_station),
    "total_movers_out": valid_station["n_movers_out"].sum(),
    "avg_out_movers_lowinc_cma": np.average(
        valid_cma["out_movers_lowinc_cma"], weights=valid_cma["n_movers_out"]
    ),
    "avg_moe_out_movers_lowinc_cma": np.average(
        valid_cma["moe_cma"], weights=valid_cma["n_movers_out"]
    ),
    "n_records_cma": len(valid_cma)
})

# Append overall summary to city-level table
summary_by_city = pd.concat([summary_by_city, overall_summary.to_frame().T], ignore_index=True)

# -----------------------------
# Show final table
# -----------------------------
print(summary_by_city)
