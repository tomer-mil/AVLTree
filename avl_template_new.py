#username - idofabian
#id1      - 208604660 
#name1    - Ido Fabian
#id2      - 206170219
#name2    - Niv Sagie Tenenbaum  

import random

"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	Complexity = O(1)
	"""
	def __init__(self, value= ""):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.rank = 1	

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	Complexity = O(1)
	"""
	def getLeft(self):
		return self.left

	"""returns the right child
	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	Complexity = O(1)
	"""
	def getRight(self):
		return self.right

	"""returns the parent 
	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	Complexity = O(1)
	"""
	def getParent(self):
		return self.parent

	"""return the value
	@rtype: str
	@returns: the value of self, None if the node is virtual
	Complexity = O(1)
	"""
	def getValue(self):
		if not (self.isRealNode()):
			return None
		return self.value

	"""returns the height
	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	Complexity = O(1)
	"""
	def getHeight(self):
		return self.height

	"""sets left child and updates node parent and self height
	@type node: AVLNode
	@param node: a node
	Complexity = O(1)
	"""
	def setLeft(self, node):
		self.left = node
		node.setParent(self)
		node.getParent().setHeight(node.getHeight() + 1)

	"""sets right child and updates node parent and self height
	@type node: AVLNode
	@param node: a node
	Complexity = O(1)
	"""
	def setRight(self, node):
		self.right = node
		node.setParent(self)
		node.getParent().setHeight(node.getHeight() + 1)

	"""sets parent
	@type node: AVLNode
	@param node: a node
	Complexity = O(1)
	"""
	def setParent(self, node):
		self.parent = node

	"""sets value
	@type value: str
	@param value: data
	Complexity = O(1)
	"""
	def setValue(self, value):
		self.value = value

	"""sets the height of the node
	@type h: int
	@param h: the height
	Complexity = O(1)
	"""
	def setHeight(self, h):
		self.height = h

	"""returns whether self is not a virtual node 
	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	Complexity = O(1)
	"""
	def isRealNode(self):
		return self.rank != 0

	"""
	@rtype: AVLNode
	@returns: the predecessor node of self
	Complexity = O(log n)
	"""
	def getPredecessor(self):
		if (self.getParent() == None) and (self.getLeft().rank == 0):
			return None
		
		if (self.getLeft().rank != 0):
			predecessor_node = self.getLeft()
			while(predecessor_node.getRight().isRealNode()):
				predecessor_node = predecessor_node.getRight()
			return predecessor_node

		elif (not(self.getLeft().isRealNode()) and (self.getParent().getRight() == self)):
			return self.getParent()
		
		elif (self.getParent().getLeft() == self):
			predecessor_node = self.getParent()
			while((predecessor_node.getParent().getLeft() == predecessor_node)):
				predecessor_node = predecessor_node.getParent()
			return predecessor_node.getParent()
	
	"""
	@rtype: AVLNode
	@returns: the Successor node of self
	Complexity = O(log n)
	"""
	def getSuccessor(self):

		if (self.getParent() == None) and (self.getRight().rank == 0):
			return None
	
		if(self.getRight().isRealNode()):
			successor_node = self.getRight()
			while(successor_node.getLeft().rank != 0):
				successor_node = successor_node.getLeft()
			return successor_node

		elif(not(self.getRight().isRealNode()) and (self.getParent().getLeft() == self)):
			return self.getParent()
		
		elif(self.getParent().getRight() == self):
			successor_node = self.getParent()
			while((successor_node.getParent().getRight() == successor_node)):
				successor_node = successor_node.getParent()
			return successor_node.getParent()
	
	"""
	Compute node's Balance Factor
	@rtype: int
	@returns: the BF of self
	Complexity = O(1)
	"""
	def balanceFactor(self):
		return self.getLeft().getHeight() - self.getRight().getHeight()
	
	"""
	Doing Left rotation as follow:
	Before:
		 1      father
		   2    rightSon
		     3 rightGrandson
	After:
		   2        rightSon
		 1   3  father    rightGrandson

	@type father: AVLNode
	Complexity = O(1)
	"""
	def leftRotate(father):
		# 1      father
		#   2    rightSon
		#     3 rightGrandson

		rightSon = father.getRight()
		father_parent = father.getParent()

		father.setRight(rightSon.getLeft())
		rightSon.setLeft(father)

		if (father_parent == None):
			rightSon.setParent(None)
		else:
			if father_parent.getRight().value == father.value:
				father_parent.setRight(rightSon)
			else:
				father_parent.setLeft(rightSon)
		#   2        rightSon
		# 1   3  father    rightGrandson

		father.setHeight(max(father.left.getHeight(), father.right.getHeight()) + 1)
		father.rank = father.getRight().rank + father.getLeft().rank + 1

		rightSon.setHeight(max(rightSon.getLeft().getHeight(), rightSon.getRight().getHeight()) + 1)
		rightSon.rank = rightSon.getRight().rank + rightSon.getLeft().rank + 1
	
	"""
	Doing Right rotation as follow:
	Before:
		 	 3  father
		   2    leftSon
	     1 		leftGrandson
	After:
		  2              leftSon
		1   3  leftGrandson    father

	@type father: AVLNode
	Complexity = O(1)
	"""
	def rightRotate(father):
		#     3  father
		#   2    leftSon
		# 1      leftGrandson
		leftSon = father.getLeft()
		father_parent = father.getParent()
		father.setLeft(leftSon.getRight())
		leftSon.setRight(father)
		if(father_parent == None):
			leftSon.setParent(None)
		else:
			if father_parent.getRight().value == father.value:
				father_parent.setRight(leftSon)
			else:
				father_parent.setLeft(leftSon)
		#   2               leftSon
		# 1   3  leftGrandson     father
		father.setHeight(max(father.left.getHeight(), father.right.getHeight()) + 1)
		father.rank = father.getRight().rank + father.getLeft().rank + 1

		leftSon.setHeight(max(leftSon.getLeft().getHeight(), leftSon.getRight().getHeight()) + 1)
		leftSon.rank = leftSon.left.rank + leftSon.right.rank + 1
	
	"""
	Updates Node rank and height after tree change
	Complexity = O(1)
	"""
	def setData(self):
		self.rank = self.getLeft().rank + self.getRight().rank + 1
		self.height = max(self.getLeft().getHeight(), self.getRight().getHeight()) + 1

	"""
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!For Tester!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	"""
	def getSize(self):
		return self.rank

"""
A class implementing the ADT list, using an AVL tree.
"""
class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.size = 0
		self.root = None
		self.maxnode = None
		self.minnode = None
		
	"""sets tree max node
	@type TreeList: AVLTreeList
	@param TreeList: a TreeList
	Complexity: O(log n)
	"""

	def setMaxNode(self):
		maxnode = self.getRoot()
		while maxnode.getRight() != None:
			maxnode = maxnode.getRight()
		self.maxnode = maxnode
	
	"""returns whether the list is empty
	@rtype: bool
	@returns: True if the list is empty, False otherwise
	Complexity: O(1)
	"""
	def empty(self):
		return (self.size == 0)


	"""retrieves the value of the i'th item in the list
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the value of the i'th item in the list
	Complexity: O(log n)
	"""
	def retrieve(self, i):
		if not(0 <= i < self.size):
			return None

		if(self.root.getLeft().rank == i):
			return self.root.value
	
		return self.retrieve_node_rec(self.root, i).value
	
	"""retrieves the node of the i'th item in the tree
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: AVLNode
	@returns: the node of the i'th item in the tree
	Complexity: O(log n)
	"""

	def retrieve_node(self, i):
		if not(0 <= i < self.size):
			return None

		if(self.root.getLeft().rank == i):
			return self.root
		
		return self.retrieve_node_rec(self.root, i)

	def retrieve_node_rec(self, node, i):
		if node.getLeft().rank == i:
			return node
		if i < node.getLeft().rank:
			return self.retrieve_node_rec(node.getLeft(), i)
		return self.retrieve_node_rec(node.getRight(), i-node.getLeft().rank-1)

	"""inserts val at position i in the list
	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	Complexity: O(log n)
	"""
	def insert(self, i, val):

		insert_node = AVLNode(val)
		insert_node.setLeft(self.virtual_node(insert_node))
		insert_node.setRight(self.virtual_node(insert_node))
		insert_node.setHeight(0)
		
		rotate_number = 0

		if not(0 <= i <= self.size):
			return None
		
		if(self.root == None):
			self.root = insert_node
			self.maxnode = insert_node
			self.minnode = insert_node

		elif (i == 0):
			self.minnode.setLeft(insert_node)
			self.minnode = insert_node

		elif (i == self.size):
			self.maxnode.setRight(insert_node)
			self.maxnode = insert_node
		
		elif (i < self.size):
			node_i = self.retrieve_node(i)
			if (node_i.getLeft().rank == 0):
				node_i.setLeft(insert_node)
			else:
				predecessor_node = node_i.getPredecessor()
				predecessor_node.setRight(insert_node)
		
		self.size += 1

		rotate_number = self.fixTree(False, insert_node.getParent())
		return rotate_number


	"""deletes the i'th item in the list
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	Complexity: O(log n)
	"""
		
	def delete(self,i):
		# Check if the index is legal
		if not(0 <= i < self.size):
			return -1

		# Special use cases = Tree.size < 2
		if(self.size <= 2):
			delete_node = self.retrieve_node(i)
			if(self.size == 1):
				self.size = 0
				self.root = None
				self.maxnode = None
				self.minnode = None
				return 0
			elif(delete_node == self.root):
				self.size = 1
				if(delete_node.getLeft().rank == 0):
					self.root = delete_node.getRight()
				else:
					self.root = delete_node.getLeft()
				self.maxnode = self.root
				self.minnode = self.root
				self.root.setParent(None)
				return 0

		delete_node = self.retrieve_node(i)
		delete_node_parent = delete_node.getParent()
		delete_node_right = delete_node.getRight()
		delete_node_left = delete_node.getLeft()
		
		if(delete_node == self.maxnode):
			self.maxnode = delete_node.getPredecessor()
		
		new_first = self.retrieve_node(0)
		if(i == 0):
			new_first = self.retrieve_node(1)
			self.minnode = new_first

		delete_node_right_rank = delete_node_right.rank
		delete_node_left_rank = delete_node_left.rank
		
		# If delete node is leaf
		if((delete_node_right_rank == 0) and (delete_node_left_rank == 0)):
			if(delete_node_parent.getLeft() == delete_node):
				delete_node_parent.setLeft(self.virtual_node(delete_node_parent))
			else:
				delete_node_parent.setRight(self.virtual_node(delete_node_parent))
			
			self.size -= 1			
			rotation_count = self.fixTree(True, delete_node_parent)
		
		# If delete node has only left child
		elif(delete_node_right_rank == 0):
			if(delete_node_parent.getLeft() == delete_node):
				delete_node_parent.setLeft(delete_node_left)
			else:
				delete_node_parent.setRight(delete_node_left)
			
			self.size -= 1
			rotation_count = self.fixTree(True, delete_node_parent)

		# If delete node has only right child
		elif(delete_node_left_rank == 0):
			if(delete_node_parent.getLeft() == delete_node):
				delete_node_parent.setLeft(delete_node_right)
			else:
				delete_node_parent.setRight(delete_node_right)
			
			self.size -= 1
			rotation_count = self.fixTree(True, delete_node_parent)
	
		# If delete node is has two children
		if((delete_node_right_rank !=0) and (delete_node_left_rank != 0)):
			delete_node_succesor = delete_node.getSuccessor()
			delete_node.value = delete_node_succesor.getValue()
			rotation_count = self.delete(i+1)
		
		return rotation_count
	
	"""returns the value of the first item in the list
	@rtype: str
	@returns: the value of the first item, None if the list is empty
	Complexity = O(1)
	"""
	def first(self):
		if not(self.empty()):
			return self.minnode.getValue()
		return None
	
	"""returns the value of the last item in the list
	@rtype: str
	@returns: the value of the last item, None if the list is empty
	Complexity = O(1)
	"""
	def last(self):
		if not(self.empty()):
			return self.maxnode.getValue()
		return None

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	Complexity = O(n)
	"""
	def listToArray(self):
		if(self.size == 0):
			return []
		return self.in_order(self.getRoot())
	
	def in_order(self, start_node):
		tree_array = []
		self.in_order_rec(start_node, tree_array)
		return tree_array
		
	def in_order_rec(self, node, tree_array):
		if not (node.isRealNode()):
			return
		self.in_order_rec(node.getLeft(), tree_array)
		tree_array.append(node.getValue())
		self.in_order_rec(node.getRight(), tree_array)
	
	"""returns the size of the list 
	@rtype: int
	@returns: the size of the list
	Complexity = O(1)
	"""
	def length(self):
		return self.size

	"""sort the info values of the list
	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	Complexity = O(n logn)
	"""
	def sort(self):
		sorted_tree = AVLTreeList()
		lst = self.listToArray()
		if (len(lst) == 0):
			return sorted_tree
		
		sorted_tree.root = AVLNode(lst[0])
		sorted_tree.root.setRight(self.virtual_node(sorted_tree.root))
		sorted_tree.root.setLeft(self.virtual_node(sorted_tree.root))
		sorted_tree.root.setHeight(1)

		sorted_tree.size = 1
		for i in range(1,len(lst)):
			insert_node = AVLNode(lst[i])
			insert_node.setRight(self.virtual_node(insert_node))
			insert_node.setLeft(self.virtual_node(insert_node))
			insert_node.setHeight(1)
			sorted_tree.insert_sort(sorted_tree.root, insert_node)
		return sorted_tree
		
	def insert_sort(self, checkNode, node):			
		if checkNode.value > node.value:
			if (checkNode.getLeft().isRealNode()):
				self.insert_sort(checkNode.left, node)
			else:
				checkNode.setLeft(node)
				self.fixTree(False, node)	
		else:
			if (checkNode.getRight().isRealNode()):
				self.insert_sort(checkNode.right,node)
			else:
				checkNode.setRight(node)
				self.fixTree(False, node)
		
	"""permute the info values of the list 
	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	Complexity = O(n logn)
	"""
	
	def permutation(self):
		perm_tree = AVLTreeList()
		if(self.size == 0):
			return perm_tree
		tree_as_list = self.listToArray()
		cnt = 0
		while cnt < len(tree_as_list):
			rand_ind = random.randint(0, len(tree_as_list) - 1)
			if (tree_as_list[rand_ind] != None):
				perm_tree.insert(0, tree_as_list[rand_ind])
				cnt += 1
				tree_as_list[rand_ind] = None
		return perm_tree

	"""concatenates lst to self
	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	Complexity = O(logn - logm) as n = max(self.length(), lst.length()) and m = min(self.length(), lst.length())
	"""
	def concat(self, lst):
		
		if (self.length() == 0 and lst.length() == 0):
			return 0

		elif (self.length() == 0):
			self.root = lst.root
			self.size = lst.size
			self.maxnode = lst.maxnode
			self.minnode = lst.minnode
			return self.getRoot().getHeight() + 1

		elif (lst.length() == 0):
			return self.getRoot().getHeight() + 1
		
		x_index = self.length()
		height_diff = abs(self.getRoot().getHeight() - lst.getRoot().getHeight())
	
		if (self.getRoot().getHeight() > lst.getRoot().getHeight()):
			b_node = self.concat_fixed(True, self, lst)
			self.fixTree(True, b_node)

		else:
			b_node = self.concat_fixed(False, lst, self)
			self.root = lst.getRoot()
			self.fixTree(True, b_node)
		
		#Update tree values
		self.size += lst.length() + 1
		self.maxnode = lst.maxnode
		self.delete(x_index)

		return height_diff

	def concat_fixed(self, self_is_high, high, low):
		# x_node is the relevant node in the highest tree so (self < x_node < lst)

		if (self_is_high):
			b_node, b_index = high.find_node_in_correct_height(low.getRoot().getHeight(), False)
		else:
			b_node, b_index = high.find_node_in_correct_height(low.getRoot().getHeight(), True)
		
		x_node = AVLNode("temp_node")
		c_node = b_node.getParent()

		if (self_is_high):
			x_node.setRight(low.getRoot())
			x_node.setLeft(b_node)
			c_node.setRight(x_node)

		else:
			x_node.setLeft(low.getRoot())
			x_node.setRight(b_node)
			c_node.setLeft(x_node)

		return b_node

	def find_node_in_correct_height(self, height, find_min):
		#Find the max/min node with the correct height
		
		node = self.getRoot()
		
		if (find_min):
			index = node.getLeft().rank
			while ((node.getLeft().isRealNode()) and (node.getHeight() >= height)):
				node = node.getLeft()
				index = node.getLeft().rank
		else:
			index = 0
			while (node.getRight().isRealNode() and (node.getHeight() != height)):
				index += node.getLeft().rank + 1
				node = node.getRight()
		
		return (node, index)

	"""searches for a *value* in the list
	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	Complexity = O(n)
	"""
	def search(self, val):
		tree_lst = self.listToArray()
		for i, lst_val in enumerate(tree_lst):
			if(val == lst_val):
				return i
		return -1

	"""returns the root of the tree representing the list
	@rtype: AVLNode
	@returns: the root, None if the list is empty
	Complexity = O(1)
	"""
	def getRoot(self):
		return self.root

	"""Rebalancing the tree and updates nodes params after change (insert, delete or concat)
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	Complexity = O(log n)
	"""
	def fixTree(self, after_delete, node):
		rotation = 0
		while node != None:
			node.setData()
			if (rotation == 0) or after_delete:
				rotation += self.reBalance(node)
			if node.getParent() == None:
				self.root = node
			node = node.getParent()
		return rotation
	
	"""Checking node's BF and making rotation if needed
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	Complexity = O(1)
	"""
	def reBalance(self, node):

		balanceFactor = node.balanceFactor()

		if (-1 <= balanceFactor <= 1):
			return 0

		node_right = node.getRight()
		node_left = node.getLeft()
		if balanceFactor < -1:
			# Only left rotation
			if node_right.balanceFactor() <= 0:
				node.leftRotate()
				return 1
			# Right then left rotation
			else:
				node_right.rightRotate()
				node.leftRotate()
				return 2

		elif balanceFactor > 1:
			# Only right rotation
			if node_left.balanceFactor() >= 0:
				node.rightRotate()
				return 1
			# Left then right rotation
			else:
				node_left.leftRotate()
				node.rightRotate()
				return 2
	
	"""Creating virtual node
	@rtype: AVLNode
	@returns: virtual node
	Complexity = O(1)
	"""
	def virtual_node(self, father):
		node = AVLNode()
		node.rank = 0
		node.parent = father
		return node
	
	"""
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!For tester!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	"""
	def print_tree(self, node):
		if (node.height > 0):
			print("value:",node.value)
		if(node != None and node.left.rank != 0):
			print("left:", node.left.value)
		if(node != None and node.right.rank != 0):
			print("right:", node.right.value)
		if(node != None and node.left.rank != 0):
			self.print_tree(node.left)
		if(node != None and node.right.rank != 0):
			self.print_tree(node.right)
	"""
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!For tester!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	"""
	def append(self, val):
		return self.insert(self.length(), val)
	"""
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!For tester!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	"""
	def getTreeHeight(self):
		return self.getRoot().height

