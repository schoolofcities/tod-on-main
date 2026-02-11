import pandas as pd
import numpy as np

# -----------------------------
# Load data
# -----------------------------
station_info = pd.read_excel("station-info.xlsx")
in_movers = pd.read_csv("in-movers-station-summary.csv").dropna()

df = in_movers.merge(
    station_info,
    how="inner",
    on="station_fid"
)
df['weights_cma'] = 1000000

# -----------------------------
# Helper to compute one summary row
# -----------------------------
def summarize(group, label):
    return pd.Series({
        "Group": label,
        "n_stations": group["station_fid"].nunique(),
        "Avg % low-income in-movers (station areas)": np.average(
            group["in_movers_lowinc_station"],
            weights=group["n_movers_in"]
        ),
        "Avg % low-income in-movers (CMA)": np.average(
            group["in_movers_lowinc_cma"],
            weights=group["weights_cma"]
        )
    })

# -----------------------------
# Build table parts
# -----------------------------

rows = []

# ---- TOTAL ----
rows.append(
    summarize(df, "Total")
)

# ---- BY DECADE ----
for decade, g in df.groupby("decade", dropna=False):
    rows.append(
        summarize(g, f"Opened {decade}")
    )

# ---- BY TECHNOLOGY ----
for tech, g in df.groupby("technology_x", dropna=False):
    rows.append(
        summarize(g, tech)
    )

# ---- BY CITY ----
for city, g in df.groupby("City", dropna=False):
    rows.append(
        summarize(g, city)
    )

# -----------------------------
# Final table
# -----------------------------
summary_table = pd.DataFrame(rows)

# Format percentages nicely
summary_table["Avg % low-income in-movers (station areas)"] = (
    summary_table["Avg % low-income in-movers (station areas)"] * 100
).round(1)

summary_table["Avg % low-income in-movers (CMA)"] = (
    summary_table["Avg % low-income in-movers (CMA)"] * 100
).round(1)

print(summary_table)

summary_table.to_csv("temp_inmovers.csv")