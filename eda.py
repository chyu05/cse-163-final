""""
Charlie Yu
CSE 163 AD
"""
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

stops = pd.read_csv("data/stops.txt")
trips = pd.read_csv("data/trips.txt")
stop_times = pd.read_csv("data/stop_times.txt")
neighborhoods = gpd.read_file("data/neighborhood_map_layers_8055519324566792909.geojson")
frequent = gpd.read_file("data/Seattle_Transportation_Plan_Transit_Element_6449222131761451670.geojson")

datasets = {
    "stops": stops,
    "trips": trips,
    "stop_times": stop_times,
    "neighborhoods": neighborhoods,
    "frequent": frequent
}

stop_trips = pd.merge(
    stop_times,
    trips,
    on="trip_id",
    how="left"
)
# stop_trips.to_csv(
#     "data/stop_trips.txt",
#     index=False
# )

stop_frequency = (
    stop_trips.groupby("stop_id")
    .size()
    .reset_index(name="total_arrivals")
)

top_stops = stop_frequency.nlargest(10, "total_arrivals")
top_stops = pd.merge(
    top_stops,
    stops[["stop_id", "stop_name"]],
    on="stop_id",
    how="left"
)
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_stops,
    x="stop_name",
    y="total_arrivals",
    errorbar=None,
    color="orange"
)
plt.title("10 Bus Stops with the Most Scheduled Arrivals")
plt.xlabel("Bus Stop Name")
plt.ylabel("Number of Scheduled Arrivals")
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.30)
plt.tight_layout
plt.savefig("most-arrivals.png")

plt.figure(figsize=(10, 8))
plt.scatter(
    stops["stop_lon"],
    stops["stop_lat"],
    alpha=0.5,
    s=10,
    color="black"
)
plt.title("Geographic Distribution of Seattle Bus Stops")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("bus-stop-distribution.png")