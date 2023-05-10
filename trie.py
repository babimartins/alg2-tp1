from functools import reduce


class Node:

    def __init__(self, value=-1):
        self.value = value
        self.children: list[Node] = []

    def update(self, value):
        self.value = value

    def get_child(self, key):
        if not self.children:
            self.children = list(map(Node, [-1] * 256))

        if ord(key) > 256:
            print(key, ord(key))
        return self.children[ord(key)]


class Trie:
    code = 1

    def __init__(self):
        self.root = Node(0)

    def insert(self, key):
        node = reduce(get_node, key, self.root)

        if node.value == -1:
            node.update(self.code)
            self.code += 1
        return node.value

    def find(self, key):
        node = reduce(get_node, key, self.root)

        return node.value


def get_node(node, char):
    return node.get_child(char)