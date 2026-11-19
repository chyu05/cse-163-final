""""
Charlie Yu
CSE 163 AD
"""

import pandas as pd
import geopandas as gpd
import plotly

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

def test_kingcounty_dataset():
    assert stops.shape[0] == 6265 and stops.shape[1] == 13
    assert stops.isnull().sum().sum() == 18795
    assert stop_times.shape[0] == 1126734 and stop_times.shape[1] == 10
    assert trips.shape[0] == 32635 and trips.shape[1] == 12

def test_neighborhood_dataset():
    assert neighborhoods.shape[0] == 95 and neighborhoods.shape[1] == 143
    assert neighborhoods.isnull().sum().sum() == 0
def test_frequent_transit_dataset():
    assert frequent.shape[0] == 841 and frequent.shape[1] == 15
    assert frequent.isnull().sum().sum() == 96

def main():
    """Runs all 3 dataset tests
    """
    test_kingcounty_dataset()
    test_neighborhood_dataset()
    test_frequent_transit_dataset()
    print("All tests passed!")

if __name__ == "__main__":
    main()