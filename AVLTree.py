import random

#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  


"""A class representing a node in an AVL tree"""


class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int or None
	@param key: key of your node
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key: int = None, height: int = 0, value=None):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = height
		self.size = 0

	def __repr__(self):
		return f"key: {self.key} | h: {self.height} | BF: {self.get_bf()} | size: {self.get_size()}" if self.is_real_node() else "Dummy Node"

	"""returns the key
	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height

	"""returns the size of the subtree

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual
	"""
	def get_size(self):
		return self.size

	def get_bf(self):
		return self.left.height - self.right.height if (self.left and self.height) else -99

	"""sets key
	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key

	"""sets value
	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value

	"""sets left child
	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left = node

	"""sets right child
	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node

	"""sets parent
	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node

	"""sets the height of the node
	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h

	def height_manager(self):
		new_height = 1 + max(self.left.height, self.right.height)
		if self.height != new_height:
			self.height = new_height
			return True  # height changed
		return False  # height stays the same


	"""sets the size of node
	@type s: int
	@param s: the size
	"""
	def set_size(self, s):
		self.size = s

	"""returns whether self is not a virtual node 
	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.key is not None

	def add_dummy_nodes(self):
		self.right = AVLNode(height=-1)
		self.left = AVLNode(height=-1)


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = AVLNode()  # initializes with dummy node
		self.min = None
		# add your fields here

	def is_empty(self):
		return not self.root.is_real_node()

	"""searches for a value in the dictionary corresponding to the key
	@type key: int
	@param key: a key to be searched
	@rtype: any
	@returns: the value corresponding to key.
	"""
	def search(self, key):
		return None

	####################
	###### Insert ######
	####################
	"""inserts val at position i in the dictionary
	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val):
		new_node = AVLNode(key=key, value=val)

		self.BST_insert(node=new_node)

		curr_node = new_node.get_parent()


		# walking up the tree
		while curr_node:  # while curr_node's child (left or right) is not the root
			print(curr_node.get_parent())
			# update node attributes after BST insertion
			did_height_change = curr_node.height_manager()

			curr_node_abs_bf = abs(curr_node.get_bf())

			if not did_height_change and curr_node_abs_bf < 2:
				return
			elif did_height_change and curr_node_abs_bf < 2:
				curr_node = curr_node.get_parent()
			else:  # then: curr_node_abs_bf == 2:
				self.rotate(node=curr_node)
				return

		return -1

	def rotate(self, node: AVLNode):
		print("On rotate")

		node_bf = node.get_bf()
		child_bf = node.left.get_bf() if node_bf == 2 else node.right.get_bf()

		if node_bf == 2:
			if child_bf == 1:
				self.right_rotation(node=node)
			else:
				self.left_then_right_rotation(node=node)
		else:
			if child_bf == -1:
				self.left_rotation(node=node)
			else:
				self.right_then_left_rotation(node=node)

		# Attribute update #
		# height update
		node.height_manager()

	def right_rotation(self, node: AVLNode, is_partial: bool = False):

		B = node
		A = node.left

		B.left = A.right
		B.left.parent = B
		A.right = B
		A.parent = B.parent

		if is_partial:
			A.parent.right = A
			B.height_manager()  # "6" is a leaf after partial-right rotation
			A.height_manager()  # "8" is a "6"'s parent after partial-right rotation
		else:
			if A.parent:  # A.parent is not the root
				A.parent.left = A
			else:
				self.root = A  # rotated the root (before rotation: self.root == node)

		B.parent = A

	def left_rotation(self, node: AVLNode, is_partial: bool = False):

		B = node
		A = node.right

		B.right = A.left
		B.right.parent = B
		A.left = B
		A.parent = B.parent

		if is_partial:
			A.parent.left = A
			B.height_manager()
			A.height_manager()

		else:
			if A.parent:  # A.parent is not the root
				A.parent.right = A
			else:
				self.root = A  # rotated the root (before rotation: self.root == node)

		B.parent = A

	def right_then_left_rotation(self, node: AVLNode):
		self.right_rotation(node=node.right, is_partial=True)
		self.left_rotation(node=node)

	def left_then_right_rotation(self, node: AVLNode):
		self.left_rotation(node=node.left, is_partial=True)
		self.right_rotation(node=node)

	def BST_insert(self, node: AVLNode):

		node.add_dummy_nodes()

		if self.is_empty():
			self.root = node
			self.root.size += 1

		else:
			higher_node = AVLNode()
			lower_node = self.root

			# walking down the tree
			while lower_node.is_real_node():
				higher_node = lower_node

				higher_node.size += 1

				if node.key < lower_node.key:
					lower_node = lower_node.left
				else:
					lower_node = lower_node.right

			node.parent = higher_node

			# inserting at the right place
			if node.key < higher_node.key:
				higher_node.left = node
			else:
				higher_node.right = node

			# if higher_node.need_height_change():
			# 	self.update_height(node=higher_node)

	####################

	"""deletes node from the dictionary
	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		return -1

	"""returns an array representing dictionary 
	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None

	"""returns the number of items in dictionary 
	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.get_root().get_size()
	
	"""splits the dictionary at a given node
	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		return None

	"""joins self with key and another AVLTree
	@type tree: AVLTree 
	@param tree: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree are larger than key,
	or the other way around.
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def join(self, tree, key, val):
		return None

	"""compute the rank of node in the self
	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node):
		return None

	"""finds the i'th smallest item (according to keys) in self
	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""
	def select(self, i):
		return None

	"""returns the root of the tree representing the dictionary
	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root

	#########################
	##### Print Methods #####
	#########################
	def printt(self):
		out = ""
		for row in self.printree(self.root):  # need printree.py file
			out = out + row + "\n"
		print(out)

	def printree(self, t, bykey=True):
		# for row in trepr(t, bykey):
		#        print(row)
		return self.trepr(t, True)

	def trepr(self, t, bykey=False):
		if t == None:
			return ["#"]

		thistr = f"{t.key}, h: {t.height}" if bykey else str(t.get_value())

		return self.conc(self.trepr(t.left, bykey), thistr, self.trepr(t.right, bykey))

	def conc(self, left, root, right):

		lwid = len(left[-1])
		rwid = len(right[-1])
		rootwid = len(root)

		result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

		ls = self.leftspace(left[0])
		rs = self.rightspace(right[0])
		result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid *
					  " " + "\\" + rs * "_" + (rwid - rs) * " ")

		for i in range(max(len(left), len(right))):
			row = ""
			if i < len(left):
				row += left[i]
			else:
				row += lwid * " "

			row += (rootwid + 2) * " "

			if i < len(right):
				row += right[i]
			else:
				row += rwid * " "

			result.append(row)

		return result

	def leftspace(self, row):
		# row is the first row of a left node
		# returns the index of where the second whitespace starts
		i = len(row) - 1
		while row[i] == " ":
			i -= 1
		return i + 1

	def rightspace(self, row):
		# row is the first row of a right node
		# returns the index of where the first whitespace ends
		i = 0
		while row[i] == " ":
			i += 1
		return i


test_import = [8, 9, 10, 3, 2, 1, 100, 36, 30, 31, 11, 12, 13, 14, 15]

t = AVLTree()

for num in test_import:
	t.insert(num, "")

t.printt()
