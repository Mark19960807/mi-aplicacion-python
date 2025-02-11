import networkx as nx
import matplotlib.pyplot as plt

# Crea un grafo vacío
G = nx.DiGraph()

# Agrega nodos
G.add_node("Definición del Problema")
G.add_node("Especificaciones")
G.add_node("¿Requiere diseño de hardware?")
G.add_node("Sí")
G.add_node("No")
G.add_node("Selección de Componentes")
G.add_node("Diseño del Circuito")
G.add_node("Simulación")
G.add_node("¿La simulación es exitosa?")
G.add_node("Sí")
G.add_node("No")
G.add_node("Implementación Física")
G.add_node("Pruebas y Validación")
G.add_node("¿Las pruebas son exitosas?")
G.add_node("Sí")
G.add_node("No")
G.add_node("Documentación")
G.add_node("Fin")

# Agrega aristas
G.add_edge("Definición del Problema", "Especificaciones")
G.add_edge("Especificaciones", "¿Requiere diseño de hardware?")
G.add_edge("¿Requiere diseño de hardware?", "Sí")
G.add_edge("¿Requiere diseño de hardware?", "No")
G.add_edge("Sí", "Selección de Componentes")
G.add_edge("No", "Selección de Componentes")
G.add_edge("Selección de Componentes", "Diseño del Circuito")
G.add_edge("Diseño del Circuito", "Simulación")
G.add_edge("Simulación", "¿La simulación es exitosa?")
G.add_edge("¿La simulación es exitosa?", "Sí")
G.add_edge("¿La simulación es exitosa?", "No")
G.add_edge("Sí", "Implementación Física")
G.add_edge("No", "Diseño del Circuito")
G.add_edge("Implementación Física", "Pruebas y Validación")
G.add_edge("Pruebas y Validación", "¿Las pruebas son exitosas?")
G.add_edge("¿Las pruebas son exitosas?", "Sí")
G.add_edge("¿Las pruebas son exitosas?", "No")
G.add_edge("Sí", "Documentación")
G.add_edge("No", "Implementación Física")
G.add_edge("Documentación", "Fin")

# Visualiza el grafo
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_shape='s', node_color='lightblue')
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10)
plt.axis('off')
plt.show()