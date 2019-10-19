import sys, pygame
import matplotlib.pyplot as plt
from pygame.locals import *
import networkx as nx
import os, time
        
Grafo = nx.DiGraph()
########AGREGAR NODOS########
Grafo.add_node('A')
Grafo.add_node('B')
Grafo.add_node('C')
Grafo.add_node('D')
Grafo.add_node('E')
Grafo.add_node('F')
########AGREGAR ARISTAS########
#Grafo.add_edge("A","B")
########DIBUJAR GRAFO########
nx.draw_shell(Grafo, with_labels=True, node_color='blue', node_size=500)
########GENERAR IMAGEN########
plt.savefig('graph.png',dpi=(140))#transparent=True, facecolor="w"
########INICIO PYGAME########
pygame.init()
window = pygame.display.set_mode((896,672))
pygame.display.set_caption("Grafo completo")
########CARGA IMAGEN INICIAL NODOS########
#My_imageII = pygame.image.load("fondo.jpg")
#window.blit(My_imageII,(0,0))
My_imageI = pygame.image.load("graph.png")
window.blit(My_imageI,(0,0))
pygame.display.update()
plt.clf()
########METODO PINTAR ARISTAS########

def draw_edges():
    tupla = [("A","B"), ("B","C"), ("C","D"), ("D","E"), ("E","F"),("F","A"),("A","D")]
    for i in range(0,len(tupla)):
        time.sleep(0.2)
        Grafo.add_edge(tupla[i][0], tupla[i][1])
        nx.draw_circular(Grafo, with_labels=True, node_color='b', node_size=500)
        plt.savefig('graph.png',dpi=(140))#transparent=True, facecolor="w"
        My_image = pygame.image.load("graph.png")
        window.blit(My_image,(0,0))
        pygame.display.update()
    #print(nx.shortest_path(Grafo, source="A", target="D"))
    #print(nx.shortest_path(Grafo))
def delete_edges():
    tupla = [("A","B"), ("B","C"), ("C","D"), ("D","E"), ("E","F"),("F","A"),("A","D")]
    for i in range(0,len(tupla)):
        time.sleep(0.2)
        Grafo.remove_edge(tupla[i][0], tupla[i][1])
        plt.clf()
        nx.draw_circular(Grafo, with_labels=True, node_color='b', node_size=500)
        plt.savefig('graph.png',dpi=(140))#transparent=True, facecolor="w"
        My_image = pygame.image.load("graph.png")
        window.blit(My_image,(0,0))
        pygame.display.update()
    #print(nx.shortest_path(Grafo, source="A", target="D"))
    #print(nx.shortest_path(Grafo))
########CICLO PYGAME########
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_a:
                draw_edges()
            elif event.key == K_d:
                delete_edges()
    pygame.display.update()