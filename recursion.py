print '------------------'
print '***BASIC EXERCISES***'
print '------------------'
# 1
print 'Exercise #1'
def print_num(times, i):
    if i <= times:
        print i
        print_num(times, i + 1)

print_num(10, 1)
print '------------------'

# 2
print 'Exercise #2'
def print_hello(names, i = 0):
    if i < len(names):
        print 'Hello ' + names[i]
        print_hello(names, i + 1)

names = ['Cody', 'Tim', 'Carolyn']
print_hello(names)
print '------------------'

print '------------------'
print '***LINKED LIST EXERCISES***'
print '------------------'
# 1
print 'Exercise #1'
class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

one = LLNode(1)
two = LLNode(2)
one.next = two
three = LLNode(3)
two.next = three
four = LLNode(4)
three.next = four

def ll_lookup(node, target):
    if node.data != target:
        node = node.next
        return ll_lookup(node, target)
    else:
        print 'Found target at node %r' % node.data
        return node

node = ll_lookup(one, 3)

print '------------------'

print '------------------'
print '***BINARY SEARCH TREES EXERCISES***'
print '------------------'
# 1
print 'Exercise #1'
import random

# A class representing a binary tree node
# it contains 3 attributes: data, left, right
class BTreeNode(object):
    def __init__(self, data):
        # the data that's associated with this node
        # this will be a number in this example
        # but can also be a string or any other data type
        # that can be ordered
        self.data = data
        # the left child node of this node
        self.left = None
        # the right child node of this nod
        self.right = None

    # __repr__ returns a string representation
    # of this binary tree node, it will look like, for example:
    # BTreeNode(4)
    def __repr__(self):
        return "BTreeNode(%r)" % self.data

# 3 routines for working with binary search trees below:
# 1. bst_lookup
# 2. bst_insert
# 4. bst_traverse

# Insert a new_node into the tree (or subtree) starting at node
# Parameters:
# * node - the root node of the tree (or subtree) to insert into
# * new_node - the new node to insert into the tree (or subtree)
def bst_insert(node, new_node):
    if node.data > new_node.data:
        if node.left is None:
            node.left = new_node
        else:
            bst_insert(node.left, new_node)
    else:
        if node.right is None:
            node.right = new_node
        else:
            bst_insert(node.right, new_node)

# Traverse the tree, call supplied function for each node in the tree
# Parameters:
# * node - the root node of the tree (or subtree) to traverse
# * fn - the function to call for each node. fn will take 2 parameters:
#     1. the current node
#     2. the tree level as a number
# * level (optional) - the current tree level in the traversal
def bst_pre_order_traverse(node, fn, level=0):
    if node is None:
        return
    fn(node, level)
    bst_pre_order_traverse(node.left, fn, level + 1)
    bst_pre_order_traverse(node.right, fn, level + 1)

root_node = BTreeNode(59)
numbers = [57, 13, 65, 6, 44, 29, 21, 82, 96, 95, 71]
for i in numbers:
    bst_insert(root_node, BTreeNode(i))

def printit(node, level):
    print node.data

bst_pre_order_traverse(root_node, printit)

def bst_lookup(node, target):
    if node:
        if target == node.data:
            print 'Found target at %r' % node
            return node
        elif target < node.data:
            return bst_lookup(node.left, target)
        else:
            return bst_lookup(node.right, target)

bst_lookup(root_node, 82)

def bst_in_order_traversal(node, target):
    if node is None:
        return
    #left
    bst_in_order_traversal(node.left, fn, level + 1)
    #center
    fn(node, level)
    #right
    bst_in_order_traversal(node.right, fn, level + 1)

bst_in_order_traversal(root_node, printit)

def bst_min(node):
    if node:
        if node.left:
            return nst_min(node.left)
        else:
            return node
print 'Min %r' % bst_min(root_node)
