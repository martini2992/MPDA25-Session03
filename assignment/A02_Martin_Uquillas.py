#r: networkx
#r: matplotlib

import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

#create a Graph
G = nx.Graph()

#add nodes
G.add_node('Madrid')
G.add_node('Toledo')
G.add_node('Cuidad Real')
G.add_node('Cordoba')
G.add_node('Sevilla')
G.add_node('Cadiz')
G.add_node('Granada')
G.add_node('Malaga')
G.add_node('Segovia')
G.add_node('Valladolid')
G.add_node('Zamora')
G.add_node('Palencia')
G.add_node('Leon')
G.add_node('Santiago')
G.add_node('Vigo')
G.add_node('A Coruna')
G.add_node('Ourense')
G.add_node('Guadalajara')
G.add_node('Zaragoza')
G.add_node('Huesca')
G.add_node('Lleida')
G.add_node('Tarragona')
G.add_node('Barcelona')
G.add_node('Girona')
G.add_node('Figueres')
G.add_node('Cuenca')
G.add_node('Albacete')
G.add_node('Alicante')
G.add_node('Valencia')
G.add_node('Castellon')

#add edges
G.add_edge('Madrid', 'Toledo')
G.add_edge('Toledo', 'Cuidad Real')
G.add_edge('Cuidad Real', 'Cordoba')
G.add_edge('Cordoba', 'Sevilla')
G.add_edge('Sevilla', 'Cadiz')
G.add_edge('Cordoba', 'Granada')
G.add_edge('Granada', 'Malaga')
G.add_edge('Madrid', 'Segovia')
G.add_edge('Segovia', 'Valladolid')
G.add_edge('Valladolid', 'Zamora')
G.add_edge('Valladolid', 'Palencia')
G.add_edge('Palencia', 'Leon')
G.add_edge('Santiago', 'Vigo')
G.add_edge('Santiago', 'A Coruna')
G.add_edge('Santiago', 'Ourense')
G.add_edge('Madrid', 'Guadalajara')
G.add_edge('Guadalajara', 'Zaragoza')
G.add_edge('Zaragoza', 'Huesca')
G.add_edge('Zaragoza', 'Lleida')
G.add_edge('Lleida', 'Tarragona')
G.add_edge('Tarragona', 'Barcelona')
G.add_edge('Barcelona', 'Girona')
G.add_edge('Girona', 'Figueres')
G.add_edge('Madrid', 'Cuenca')
G.add_edge('Cuenca', 'Albacete')
G.add_edge('Albacete', 'Alicante')
G.add_edge('Cuenca', 'Valencia')
G.add_edge('Valencia', 'Castellon')


#add position to display
pos = nx.spring_layout(G)

#draw serttings
fig = plt.figure(figsize=(30,30))
ax = plt.subplot()
ax.set_title('AVE', fontsize=70)
nx.draw(G, pos, node_size=10000, with_labels=True, node_color='black', font_size=18, font_color='white')

#draw the graph
plt.tight_layout()


#plot
path= r"C:\Users\marti\OneDrive\Documents\MPDA\14_AT_APY\XX_Content\session02-20250313T162204Z-001\session02\images\MDPA_plot1.png"
plt.savefig(path, format="PNG")