import geopandas
import matplotlib.pyplot as plt


map = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

map.plot()
plt.savefig("mygraph.png")

