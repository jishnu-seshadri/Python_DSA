"""
Tree_example

List of lists
"""
my_tree = ['a',             #root
           ['b',            #left subtree
            ['d', [], []],
            ['e', [], []] ],
           ['c',            #right subtree
            ['f', [], []],
            [] ]
           ]

print(my_tree)

print('root = ', my_tree[0])
print('left subtree = ', my_tree[1])
print('right subtree = ', my_tree[2])