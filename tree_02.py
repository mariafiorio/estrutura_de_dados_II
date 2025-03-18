from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

n1=Node("root node")
n2=Node("left child node")
n3=Node("right child node")
n4=Node("left grandchild node")

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4


def levelordertransversal(root_node):
    list_of_nodes = []
    transvel_queue = deque([root_node])
    while len(transvel_queue) > 0:
        node = transvel_queue.popleft()
        list_of_nodes.append(node.data)
        if node.left_child:
            transvel_queue.append(node.left_child)
        if node.right_child:
            transvel_queue.append(node.right_child)
    return list_of_nodes


print(levelordertransversal(n1))