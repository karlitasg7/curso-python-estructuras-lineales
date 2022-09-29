from node import Node

if __name__ == '__main__':
    node1 = None
    node2 = Node("A", None)
    node3 = Node("B", node2)

    print(node2.data)
    print(node2.next)

    print(node3.next.data)
