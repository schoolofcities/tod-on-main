import pandas as pd

station_info = pd.read_excel("station-info.xlsx")

# print(station_info)

in_movers = pd.read_csv("in-movers-station-summary.csv")

# print(in_movers)


df = in_movers.merge(
    station_info,
    how="left",
    on="station_fid"
)

avg_lowinc_cma = df["in_movers_lowinc_cma"].mean()

valid = df[["in_movers_lowinc_station", "n_movers_in"]].dropna()
valid = valid[valid["n_movers_in"] > 0]

weighted_avg_lowinc_station = (
    (valid["in_movers_lowinc_station"] * valid["n_movers_in"]).sum()
    / valid["n_movers_in"].sum()
)


print(avg_lowinc_cma)

print(weighted_avg_lowinc_station)


mean_by_city = (
    df
    .groupby("City", dropna=False)["in_movers_lowinc_cma"]
    .mean()
    .reset_index(name="avg_in_movers_lowinc_cma")
)


df_valid = (
    df
    .dropna(subset=["in_movers_lowinc_station", "n_movers_in"])
    .query("n_movers_in > 0")
    .assign(
        weighted_value=lambda x: x["in_movers_lowinc_station"] * x["n_movers_in"]
    )
)

summary_by_city = (
    df
    .groupby("City", dropna=False)
    .agg(
        n_records=("City", "size"),
        avg_in_movers_lowinc_cma=("in_movers_lowinc_cma", "mean")
    )
    .reset_index()
    .merge(
        df_valid
        .groupby("City", dropna=False)
        .agg(
            weighted_sum=("weighted_value", "sum"),
            weight_sum=("n_movers_in", "sum")
        )
        .assign(
            weighted_avg_in_movers_lowinc_station=lambda x: x["weighted_sum"] / x["weight_sum"]
        )
        .reset_index()
        [["City", "weighted_avg_in_movers_lowinc_station"]],
        how="left",
        on="City"
    )
)

print(summary_by_city)






