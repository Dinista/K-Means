#distancia = ( ((vertice2.x - vertice1.x) ** 2) + ((vertice2.y - vertice1.y) ** 2) ** (1/2) )

conjuntos = {} #Aqui será o dicionário contendo os conjuntos de vertices //
chave = 0 #Contador que atribui a chave aos conjuntos no dicionário

class Vertice:
    def __init__ (self):
        x = None
        y = None

class Aresta:
    def __init__(self):
        u = None
        v = None
        dist = None

def cria_vertice (x1, y1):
    
    exemplo = Vertice()
    exemplo.x = x1
    exemplo.y = y1
    
    return exemplo

def cria_aresta (u, v, dist):
    
    aresta = Aresta()
    aresta.u = u
    aresta.v = v
    aresta.dist = dist
    
    return aresta

def distancia (vertice1, vertice2):
    
    dist = ((int(vertice2.x) - int(vertice1.x)) ** 2) + ((int(vertice2.y) - int(vertice1.y)) ** 2)
    
    return dist ** 0.5


def cria_grafo (total):
    global conjustos
    vertices = dict()
    for i in range(total):
        aux1 = []
        aux1.append(int(i) + 1)
        conjuntos[i] = aux1
        entrada = input ()
        aux = entrada.split(" ")
        vertices[i] = cria_vertice(aux[0], aux[1]) 
    return vertices

def lista_arestas (vertices):
    lista = list()
    for i in range(len(vertices)):
        for j in range (len(vertices)):
            if i == j :
                pass
            else:
                lista.append(cria_aresta(i, j, distancia (vertices[i], vertices[j])))

    elementos = len(lista) - 1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i].dist > lista[i+1].dist:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ordenado = False
    return lista

def find (vertice):
    key = None
    listOfItems = conjuntos.items()
    for item  in listOfItems:
        for i in range(len(item[1])):
            if item[1][i] == vertice:
                key = item[0]
    return key
    
def union (vertice1, vertice2):
    global conjuntos
    global chave
    key1 = find(vertice1)
    key2 = find(vertice2)
    
    if key1 == None and key2 == None:
        aux = list()
        aux.append(vertice1)
        aux.append(vertice2)
        conjuntos[chave] = aux
        chave = chave + 1
    
    if key1 != key2 :
        if key1 == None:
            conjuntos[key2].append(vertice1)
        elif key2 == None:
            conjuntos[key1].append(vertice2)
        else:
            conjuntos[key1] = conjuntos[key1] + conjuntos[key2]
            conjuntos.pop(key2, None)
    else:
        pass

def MTS (num_vert, agrupamento):
    global conjuntos
    i = 1
    agrupamento_global = list()
    grafo = cria_grafo(int(num_vert))
    ordenada = lista_arestas(grafo)
    while len(conjuntos) != int(agrupamento):
        union (int(ordenada[i].u) + 1, int(ordenada[i].v) + 1)
        i += 1

entrada = input()
aux = entrada.split(" ")

MTS (aux[0], aux[1])

for k in conjuntos:
    print(sorted(conjuntos[k]))