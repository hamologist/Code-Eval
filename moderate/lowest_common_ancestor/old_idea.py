import sys

_tree = (
    30, 
        (8, 
            (3, 
                (None), 
                (None),
            ),
            (20, 
                (10, 
                    (None),
                    (None)
                ),
                (29, 
                    (None),
                    (None)
                )
            )
        ), 
        (52, 
            (None),
            (None)
        )
)


def find_node(num):
    node = _tree
    depth = 0
    while(node is not None and node != num):
        if (num < node):
            node = node[1]


def main():
    f = open(sys.argv[1])
    lines = f.read().strip().splitlines()

    for line in lines:
        print(line)

    print(_tree)

if __name__ == '__main__':
    main()
