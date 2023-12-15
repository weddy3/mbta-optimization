import matplotlib.pyplot as plt
import geopandas as gpd

# opening the vector map
shapefile_path = "population_visualization/shapefiles/TOWNSSURVEY_POLYM.shp"

gdf = gpd.read_file(shapefile_path)


# list of towns we are interested in
towns_of_interest = [
    "BOSTON",
    "CHELSEA",
    "SOMERVILLE",
    "WINTHROP",
    "REVERE",
    "CAMBRIDGE",
    "WATERTOWN",
    "BROOKLINE",
    "NEWTON",
    "BELMONT",
    "ARLINGTON",
    "WALTHAM",
    "NEEDHAM",
    "WELLSLEY",
    "DEDHAM",
    "WESTWOOD",
    "DEDHAM",
    "MILTON",
    "QUINCY",
    "BRAINTREE",
    "HINGHAM",
    "EVERETT",
    "MALDEN",
    "MELROSE",
    "MEDFORD",
    "CANTON",
    "HOLBROOK",
    "WEYMOUTH",
    "DOVER",
    "WINCHESTER",
    "WOBOURN",
    "SAUGUS",
    "LYNN",
    "WINTRHOP",
    "SWAMPSCOTT",
]

small_gdf = gdf[gdf["TOWN"].isin(towns_of_interest)]


# TODO add a new column with more up to date population data
# TODO overlay mbta map onto this, or add in stops and draw lines manually, probs easier, just need coordinates
# TODO rescale boston population so color isn't off
# TODO use geopy to make the towns clickable which shows population

plot = small_gdf.plot(
    column="POP2010",
    legend=True,
    legend_kwds={"label": "Population by town in 2010", "orientation": "horizontal"},
)

# get crudley calculated center coordinates for labeling purposes
small_gdf["coords"] = small_gdf["geometry"].apply(
    lambda x: x.representative_point().coords[:]
)

# apply town name to plot
for _, row in small_gdf.iterrows():
    plt.annotate(
        text=row["TOWN"],
        xy=row["coords"][0],
        horizontalalignment="center",
        color="white",
        fontsize=6,
    )

# basic graph improvements
plot.set_facecolor("black")

plt.show()
