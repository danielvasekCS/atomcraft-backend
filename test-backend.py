from MDSplus import Tree, Float32Array

# This is how to create the tree
myTree = Tree('my_tree', -1)

# how to access a specific node in the tree
node1 = myTree.getNode('NUM1')

# this is how to set the default path for later
myTree.setDefault(myTree.getNode('SUB1'))

# how to access a tree node that is positioned at SUB1->SUB_NODE1
subNode = myTree.getNode('SUB_NODE1')


# copying data from one tree node to another
myTree = Tree('my_tree', -1)
n1 = myTree.getNode('NODE1')
n2 = myTree.getNode('NODE2')

d = n1.getData()
n2.putData(d)

