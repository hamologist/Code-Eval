import sys

_tree_data = [30, 8, 52, 3, 20, 10, 29]


class Node:
    
    def __init__(self, data, depth=0):
        self.data = data
        self.parent = None
        self.depth = depth
        self.left = None
        self.right = None

    def add(self, data, pos=0):
        pos += 1

        if self.data == data:
            return False
        elif self.data > data:
            if self.left == None:
                self.left = Node(data)
                self.left.parent = self
                self.left.depth = pos
                return True
            else:
                return self.left.add(data, pos)
        else:
            if self.right == None:
                self.right = Node(data)
                self.right.parent = self
                self.right.depth = pos
                return True
            else:
                return self.right.add(data, pos)

    def find(self, data):
        if self.data == data:
            return self
        elif self.left is not None and self.data > data:
            return self.left.find(data)
        elif self.right is not None and self.data < data:
            return self.right.find(data)
        else:
            return None


class Tree:

    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            self.head.add(data)

    def find(self, data):
        if self.head is None:
            return None
        else:
            return self.head.find(data)


def main():
    f = open(sys.argv[1])
    lines = f.read().strip().splitlines()
    tree = Tree()

    for data in _tree_data:
        tree.add(data)

    for line in lines:
        line = [ int(x) for x in line.split(' ') ]
        x = tree.find(line[0])
        y = tree.find(line[1])

        while x.data != y.data:
            if x.depth > y.depth:
                x = x.parent
            else:
                y = y.parent
        print(x.data)

if __name__ == '__main__':
    main()
