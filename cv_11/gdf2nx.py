import geopandas
import networkx as nx
import matplotlib.pyplot as plt

gdf = geopandas.read_file("streets.geojson")

G = nx.Graph()

for idx, r in gdf.iterrows() :
    coords = r.geometry.coords
    print(coords)

    mempoint = coords[0]

    for point in coords[1:]:
        G.add_edge(mempoint, point, index=idx)
        mempoint = point

print(nx.info(G))
nx.draw(G, pos = {n: [n[0], n[1]] for n in list(G.nodes)} ,with_labels = True)

plt.show()




    