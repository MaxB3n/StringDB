

def main():

    nodes = ['A','B','C','D','E','F']
    adj_mat = [[0,1,0,1,0,1],[1,0,0,0,1,1],[0,0,0,1,0,0],[1,0,1,0,0,0],[0,1,0,0,1,1],[1,1,0,0,1,0]]

###print_mat fxn
    def print_mat(nodes,adj_mat):
        first = " "
        for i in nodes:
            first += " " + i
        print(first)
        for i in range(len(nodes)):
            numstr = ''
            for j in adj_mat[i]:
                numstr += " " + str(j)
            print(nodes[i] + numstr)
        return

    print()
    print_mat(nodes,adj_mat)

###mat_to_list fxn
    def mat_to_list(nodes,adj_mat):
        adj_list = {}
        for i in nodes:
            adj_list[i] = []
        for i in range(len(nodes)):
            for j in range(len(adj_mat)):
                if adj_mat[i][j] == 1:
                    adj_list[nodes[i]] = adj_list[nodes[i]] + [nodes[j]]
        return adj_list

    adj_dict = mat_to_list(nodes, adj_mat)
    print()
###print_list fxn
    def print_list(adj_dict):
        print("Node : Neighbors")
        tuples = adj_dict.items()
        for i in tuples:
            string = i[0] +":"
            for j in i[1]:
                string += " " + j
            print(string)
        return

    print_list(adj_dict)
    print()

###Count nodes and edges from adj mat and list
    def count_from_adj_mat(adj_mat):
        nodesCt, edgesCt, selfEdgesCt = 0 , 0 , 0
        for i in range(len(adj_mat)):
            nodesCt += 1
            for j in range(len(adj_mat[i])):
                if adj_mat[i][j] == 1:
                    edgesCt += 1
                    if i == j:
                        selfEdgesCt += 1
        uniqueEdgesCt = int(((edgesCt-selfEdgesCt) / 2) + selfEdgesCt)
        return nodesCt, uniqueEdgesCt

    print("Nodes, Edges : " + str(count_from_adj_mat(adj_mat)))
    print()

    def count_from_adj_list(adj_dict):
        nodesCt, edgesCt, selfEdgesCt = 0 , 0 , 0
        tuples = adj_dict.items()
        for i in tuples:
            nodesCt += 1
            for j in i[1]:
                edgesCt += 1
                if j == i[0]:
                    selfEdgesCt += 1
        uniqueEdgesCt = int(((edgesCt-selfEdgesCt) / 2) + selfEdgesCt)
        return nodesCt, uniqueEdgesCt

    print("Nodes, Edges : " + str(count_from_adj_list(adj_dict)))
    print()

main()
