"""
Tree
List of lists
"""

def BinaryTree_list(r):
    return [r, [], []]

"""
To add a left subtree to the root of a tree, we need to insert 
a new list into the second position of the root list.
If the list already has something in the second position, we need 
to keep track of it and push it down the tree as the left child 
of the list we are adding.
We then add the new left child, installing the old left child 
as the left child of the new one. 
This allows us to splice a new node into the tree at any position.
"""

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:                          #if left branch notnot empty
        root.insert(1,[newBranch,t,[]])     #inserts newbranch then old stuff
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


# root = BinaryTree_list('a')
# insertLeft(root, 'b')
# insertRight(root, 'c')
# insertRight(getLeftChild(root),'d')

# insertLeft(getRightChild(root),'e')
# insertRight(getRightChild(root),'f')

# print(root)




