from MDSplus import Tree, Float32Array, Float64, Int32Array

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

## writing speciifc data types replace Float64 with any of the following
# nt8 byte integer
# Uint8 unsigned byte integer
# Int16 short integer
# Uint16 unsigned short integer
# Int32 integer
# Uin32 unsigned integer
# Int64 long integer
# Uint64 unsigned long integer
# Float32 single precision float
# Float64 double precision float
# String character string
myTree = Tree('my_tree', -1)
n1 = myTree.getNode('NODE1')
n1.putData(Float64(3.14))


# you can do the same with array classes
# Int8Array byte integer array
# Uint8Array unsigned byte integer array
# Int16Array short integer array
# Uint16Array unsigned short integer array
# Int32Array integer array
# Uin32Array unsigned integer array
# Int64Array long integer array
# Uint64Array unsigned long integer array
# Float32Array single precision float array
# Float64Array double precision float array
# StringArray character string array
myTree = Tree('my_tree', -1)
n1 = myTree.getNode('NODE1')
n1.putData(Int32Array([1, 2, 3, 4]))

# References to other nodes in the tree
myTree = Tree('my_tree', -1)
node1 = myTree.getNode('NODE1')
node2 = myTree.getNode('NODE2')
node1.putData(node2)

# building complex expressions
# this basically means find whatever is in NODE1 and add2 to it then place that in node2
myTree = Tree('my_tree', -1)
node2 = myTree.getNode('NODE2')
node2.putData(myTree.tdiCompile("2 + NODE1"))

# printing data
myTree = Tree('my_tree', -1)
node1 = myTree.getNode('NODE1')
data = node1.getData()
print('Data read from NODE1: {data}')

# bidimensional arrays
arrD = Int32Array([[1, 2], [11, 22], [111, 222]])
npa = arrD.data()
type(npa)
# you access via arrD[2,1]

# can be used to print the path name of all the nodes on my tree
my_tree = Tree('my_tree', -1)
nodeArr = my_tree.getNodeWild('***')
print (nodeArr.getPath())

# editing trees
tree = Tree('my_tree', -1, 'NEW')
tree.addNode(":NUM1", "NUMERIC")
tree.addNode(":NUM2", "NUMERIC")
tree.addNode(":NUM3", "NUMERIC")
tree.addNode(":TXT", "TEXT")
# create a parent node under the root node and navigate to it
tree.setDefault(tree.addNode(".SUB1", "STRUCTURE"))

# create a subnode under sub1
tree.addNode(":SUB_NODE1", "NUMERIC")
tree.addNode(".SUB2", "STRUCTURE")

# create a node inside of sub2 whilst still as the tree pointing to sub1
tree.addNode(".SUB2:SUB_NODE2", "NUMERIC").addTag("TAG1")
tree.write()

# creating a shot where shot is an integer
shot: int = 21
tree.createPulse(shot)
