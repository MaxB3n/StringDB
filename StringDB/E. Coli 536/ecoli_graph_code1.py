from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph
import sys
import time
import os
import re



def main():
    file = "C:\\Users\\14153\\github\\Protein_Graphs\\362663.protein.links.full.v11.5.txt"
    ecoliRows, ecoliCols = textToRowsCols(file, " ")

    print(f"Converting nodes to edges @ {time.time()} ... \n")
    edgeList = nodesToEdges(ecoliCols[0][1:],ecoliCols[1][1:])
    saveList(edgeList, "ecEdges.txt")

    print(f"Converting edges to nodes @ {time.time()} ... \n")
    nodeList = edgesToNodes(edgeList)
    saveList(nodeList, "ecNodes.txt")

#    toyNodes = ['A','B','C','D','E']
#    toyEdges = [['A','B'], ['C','A'], ['D','B'], ['C','D']]

    ecEdges = readEdges("C:\\Users\\14153\\github\\Protein_Graphs\\ecEdges.txt")
    print("num edges :" + str(len(ecEdges)) + "\n" + str(ecEdges[:10]))

    return

### HELPER FUNCTIONS ###

#   separated txt file -> rows and columns list

def textToRowsCols(filepath , separator = ","):

    with open(filepath, 'r') as f:
        rows = f.read().splitlines()

    columns = [[] for i in range(len(rows[0].split(separator)))]
    for i in rows:
        row = i.split(separator)
        for n in range(len(row)):
            columns[n] += [row[n]]

    return rows, columns

#   2 lists of nodes -> list of edges as list of paired nodes (str)

def nodesToEdges(nodes1,nodes2):

    if len(nodes1) != len(nodes2):
        print("\n ERROR: node lists are different lengths. Input should be two ordered lists of nodes that are the same size. \n")
        return

    edgeList = [[] for i in range(len(nodes1))]
    for i in range(len(nodes1)):
        edgeList[i] = [str(nodes1[i]),str(nodes2[i])]

    return edgeList

#   list of edges as paired nodes -> list of unique nodes (str)

def edgesToNodes(edgeList):

    nodes = []
    for i in edgeList:
        for n in range(1):
            if i[n] not in nodes:
                 nodes += [str(i[n])]

    return nodes

#   Save a list to be accessed later

def saveList(lst, filename = "temp.txt"):
    lng = len(lst)-1
    text = ""
    n = 0

    while n < lng:
        text += str(lst[n]) + "\n"
        n+=1
    text += str(lst[n])

    f = open(filename, "w")
    f.write(text)
    f.close()
    return

#   grabs a list of strings separated by \n from a txt file
def readNodes(filepath):
    with open(filepath, 'r') as f:
        nodes = f.read().splitlines()
    return nodes

#   grabs a list of lists of paired strings separated by \n from a txt file
def readEdges(filepath):
    with open(filepath, 'r') as f:
        edgeStr = f.read().splitlines()
    edges = [[] for i in range(len(edgeStr))]
    for i in range(len(edgeStr)):
        edges[i] = edgeStr[i][2:-2].split("', '")
    return edges



def create_gs_graph():
    return



if __name__ == '__main__':
	main()
