import random

# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info


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
        self.size = 1

    def __repr__(self):
        return f"key: {self.key} | h: {self.height} | BF: {self.get_bf()} | size: {self.get_size()}" if self.is_real_node() else "Dummy Node"

    def __eq__(self, other):
        if not other:
            if not self:
                return True
            else:
                return False
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __gt__(self, other):
        return self.key > other.key

    def __ge__(self, other):
        return self.key >= other.key

    """returns the key
    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        return self.key

    def get_relative_direction(self):
        if not self.parent:
            return "root"
        return "left" if self == self.parent.left else "right"

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

    def update_size(self):
        self.set_size(s=(self.right.size + self.left.size + 1))

    """returns whether self is not a virtual node 
    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        return self.key is not None

    def add_dummy_nodes(self):
        right_node = AVLNode(height=-1)
        right_node.set_size(s=0)

        left_node = AVLNode(height=-1)
        left_node.set_size(s=0)

        self.right = right_node
        self.left = left_node
        
    def get_subtree_min(self):
        curr_node = self
        while curr_node.left.is_real_node():
            curr_node = curr_node.left
        return curr_node
    
    def get_subtree_max(self):
        curr_node = self
        while curr_node.right.is_real_node():
            curr_node = curr_node.right
        return curr_node
            
		
"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def __init__(self, root: AVLNode = AVLNode()):
        self.root = root  # initializes with dummy node
        self.min = None
        self.max = None

    def __repr__(self):
        return f"root: {self.root.key} | s: {self.size()} | h: {self.root.height}"

    # add your fields here

    def is_empty(self):
        return not self.root.is_real_node()

    def should_update_min(self, node: AVLNode):
        return node < self.min if self.min else True

    def should_update_max(self, node: AVLNode):
        return node > self.max if self.max else True

    """searches for a value in the dictionary corresponding to the key
    @type key: int
    @param key: a key to be searched
    @rtype: any
    @returns: the value corresponding to key.
    """

    def search(self, key):
        curr_node = self.root
        while curr_node.is_real_node():
            if curr_node.key == key:
                return curr_node
            if curr_node.key > key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return None

    def set_as_child_after_rotation(self, node: AVLNode, relative_direction: str):
        if relative_direction == "root":
            setattr(self, relative_direction, node)
        else:
            setattr(node.parent, relative_direction, node)

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

        # update tree attributes if needed
        if self.should_update_min(node=new_node):
            self.min = new_node
        if self.should_update_max(node=new_node):
            self.max = new_node

        # Walking up the tree
        balance_actions = self.rebalance_up(start_node=new_node.get_parent())

        #
        # while curr_node:  # while curr_node's child (left or right) is not the root
        #
        # 	# update node attributes after BST insertion
        # 	did_height_change = curr_node.height_manager()
        # 	# curr_node.update_size()
        #
        # 	curr_node_abs_bf = abs(curr_node.get_bf())
        #
        # 	if not did_height_change and curr_node_abs_bf < 2:
        # 		curr_node.update_size()
        # 		return count_balance_actions
        #
        # 	elif did_height_change and curr_node_abs_bf < 2:
        # 		curr_node.update_size()
        # 		curr_node = curr_node.get_parent()
        # 		count_balance_actions += 1
        #
        # 	else:  # then: curr_node_abs_bf == 2:
        # 		count_balance_actions += self.rotate(node=curr_node)
        # 		return count_balance_actions

        return balance_actions

    def rotate(self, node: AVLNode):

        # Check the relative direction of the node to its parent in order to connect the new node in the same location
        relative_direction = node.get_relative_direction()

        node_bf = node.get_bf()
        child_bf = node.left.get_bf() if node_bf == 2 else node.right.get_bf()

        if node_bf == 2:
            if child_bf == 1:
                self.right_rotation(node=node, relative_direction=relative_direction)
                count_balance_actions_rotate = 1
            else:
                self.left_then_right_rotation(node=node, relative_direction=relative_direction)
                count_balance_actions_rotate = 2
        else:
            if child_bf == -1:
                self.left_rotation(node=node, relative_direction=relative_direction)
                count_balance_actions_rotate = 1
            else:
                self.right_then_left_rotation(node=node, relative_direction=relative_direction)
                count_balance_actions_rotate = 2

        # Attribute update #

        node.height_manager()
        node.update_size()

        return count_balance_actions_rotate  # TODO: make it more abstract

    def right_rotation(self, node: AVLNode, relative_direction: str | None):

        B = node
        A = node.left

        B.left = A.right
        B.left.parent = B
        A.right = B
        A.parent = B.parent

        # Partial rotation (RL)
        if not relative_direction:
            A.parent.right = A
            B.height_manager()  # "6" is a leaf after partial-right rotation
            A.height_manager()  # "8" is a "6"'s parent after partial-right rotation

        else:
            self.set_as_child_after_rotation(A, relative_direction=relative_direction)

        B.parent = A

        B.update_size()
        A.update_size()

    def left_rotation(self, node: AVLNode, relative_direction: str | None):

        B = node
        A = node.right

        B.right = A.left
        B.right.parent = B
        A.left = B
        A.parent = B.parent

        # Partial rotation (LR)
        if not relative_direction:
            A.parent.left = A
            B.height_manager()
            A.height_manager()

        else:
            self.set_as_child_after_rotation(A, relative_direction=relative_direction)

        B.parent = A

        B.update_size()
        A.update_size()

    def right_then_left_rotation(self, node: AVLNode, relative_direction: str):
        self.right_rotation(node=node.right, relative_direction=None)
        self.left_rotation(node=node, relative_direction=relative_direction)

    def left_then_right_rotation(self, node: AVLNode, relative_direction: str):
        self.left_rotation(node=node.left, relative_direction=None)
        self.right_rotation(node=node, relative_direction=relative_direction)

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

    ####################

    #####################
    #### Predecessor ####
    #####################

    def successor(self, node: AVLNode):
        if node == self.max or self.is_empty():
            return None

        if node.right.is_real_node():
            curr_node = node.right
            while curr_node.left.is_real_node():
                curr_node = curr_node.left
            return curr_node

        # If i'm here- I'm not a root!
        else:
            curr_node = node
            while curr_node.parent.right == curr_node:  # TODO: Make sure that curr_node != self.root is impossible
                curr_node = curr_node.parent

            return curr_node.parent if curr_node != self.root else curr_node

    def predecessor(self, node: AVLNode):
        if node == self.min or self.is_empty():
            return None

        if node.left.is_real_node():
            curr_node = node.left
            while curr_node.right.is_real_node():
                curr_node = curr_node.right
            return curr_node

        # If i'm here- I'm not a root!
        else:
            curr_node = node
            while curr_node.parent.left == curr_node:  # TODO: Make sure that curr_node != self.root is impossible
                curr_node = curr_node.parent

            return curr_node.parent if curr_node != self.root else curr_node

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

        left_tree = AVLTree()
        right_tree = AVLTree()

        left_tree.root = node.left
        right_tree.root = node.right

        curr_node = node

        while curr_node.parent:  # Up till the root
            temp_tree = AVLTree()
            if curr_node.get_relative_direction() == "right":
                temp_tree.root = curr_node.parent.left 
                left_tree.join(tree=temp_tree, key=curr_node.parent.key, val=curr_node.parent.value)

            if curr_node.get_relative_direction() == "left":
                temp_tree.root = curr_node.parent.right 
                right_tree.join(tree=temp_tree, key=curr_node.parent.key, val=curr_node.parent.value)

            curr_node = curr_node.parent
        
        #  maintain min and max for the new splitted trees
        right_tree.max = self.max
        right_tree.min = right_tree.root.get_subtree_min()
        left_tree.min = self.min
        left_tree.max =  right_tree.root.get_subtree_max()

        return [left_tree, right_tree]

    def get_sub_tree(self, higher_tree_relative_direction: str, sub_tree_height: int):

        # this part is allowing us abstraction.
        # if the relative direction of the higher tree is right, then in order to get the correct sub-tree then we
        # need to start walking up the tree starting from the maximum.

        curr_node = self.root
        if higher_tree_relative_direction == "left":
            while curr_node.height > sub_tree_height:
                curr_node = curr_node.right
        else:  # higher_tree_relative_direction == "right"
            while curr_node.height < sub_tree_height:
                curr_node = curr_node.left

        return curr_node  # this is the sub-tree root!

    # TODO: change function name
    """ 
    @pre: self is the higher tree
    """

    def join_everything(self, shorter_tree, node: AVLNode, higher_tree_relative_direction: str, sub_tree_height: int):

        shorter_tree_relative_direction = "left" if higher_tree_relative_direction == "right" else "right"

        # find the relevant sub tree root based on it's future relative direction
        sub_tree_root = self.get_sub_tree(higher_tree_relative_direction, sub_tree_height)

        # step 2: connect between the new node (x), the sub tree root (b), and the rest of the original tree (c- b's parent), and the other tree

        setattr(sub_tree_root.parent, shorter_tree_relative_direction, node)  # set x to be c's child
        node.parent = sub_tree_root.parent  # set c to be x's parent (x's relative direction=shorter_tree_relative_direction)

        sub_tree_root.parent = node
        setattr(node, higher_tree_relative_direction, sub_tree_root)  # set b to be x's child
        setattr(node, shorter_tree_relative_direction, shorter_tree.root)  # set the shorter tree to be x's child

        shorter_tree.root.parent = node  # set x as the shorter tree's parent

        return node

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

        # TODO: maintain min/max when joining

        new_node = AVLNode(key=key, value=val)

        left_tree = self if self.root <= tree.root else tree
        right_tree = tree if self.root <= tree.root else self

        height_difference = left_tree.root.height - right_tree.root.height  # if >0: left higher

        if abs(height_difference) <= 1:  # "Simple" joining
            new_node.left = left_tree.root
            left_tree.root.parent = new_node
            new_node.right = right_tree.root
            right_tree.root.parent = new_node

            self.root = new_node

        else:
            if height_difference > 0:
                sub_tree_height = right_tree.root.height  # h
                new_node = left_tree.join_everything(shorter_tree=right_tree,
                                                node=new_node,
                                                higher_tree_relative_direction="left",
                                                sub_tree_height=sub_tree_height)

                self.root = left_tree.root
            else:  # right_tree.root.height > left_tree.root.height
                sub_tree_height = left_tree.root.height
                new_node = right_tree.join_everything(shorter_tree=left_tree,
                                                node=new_node,
                                                higher_tree_relative_direction="right",
                                                sub_tree_height=sub_tree_height)
                self.root = right_tree.root

        self.rebalance_up(start_node=new_node)
        # rebalance from x(=new_node) upwards

        return height_difference

    def rebalance_up(self, start_node: AVLNode) -> int:
        count_balance_actions = 0

        while start_node:  # while start_node is not None, meaning we reached the root

            did_height_change = start_node.height_manager()

            node_abs_bf = abs(start_node.get_bf())

            if not did_height_change and node_abs_bf < 2:
                start_node.update_size()
                return count_balance_actions

            elif did_height_change and node_abs_bf < 2:
                start_node.update_size()
                start_node = start_node.get_parent()
                count_balance_actions += 1

            else:  # then: node_abs_bf == 2:
                count_balance_actions += self.rotate(node=start_node)
                return count_balance_actions

    """compute the rank of node in the self
    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary which we want to compute its rank
    @rtype: int
    @returns: the rank of node in self
    """

    def rank(self, node):
        count = node.left.size + 1
        curr_node = node

        while curr_node:
            if curr_node.get_relative_direction() == "right":
                count += curr_node.parent.left.size + 1
            curr_node = curr_node.parent

        return count

    """finds the i'th smallest item (according to keys) in self
    @type i: int
    @pre: 1 <= i <= self.size()
    @param i: the rank to be selected in self
    @rtype: int
    @returns: the item of rank i in self
    """

    def select(self, i):
        if i == self.root.left.size + 1:
            return self.root
        elif i <= self.root.left.size:  # Go to min (i-1 times)
            curr_node = self.min
            for _ in range(1, i):
                curr_node = self.successor(node=curr_node)
        else:  # Go to max (n-i times)
            curr_node = self.max
            for _ in range(1, self.size() - i + 1):
                curr_node = self.predecessor(node=curr_node)

        return curr_node

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
        if not t.is_real_node():
            thistr = "D"
        else:
            thistr = f"{t.key} | h: {t.height}, s: {t.size}, r: {self.rank(node=t)}" if bykey else str(t.get_value())

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


#################
#### Testing ####
#################

t1 = AVLTree()
t2 = AVLTree()

empty_t = AVLTree()
root_t = AVLTree()
root_t.insert(key=10, val="")

test_import_small = [9, 8, 7, 10, 11]
test_import_big = [9, 8, 7, 6, 36, 30, 31, 90, 95, 96, 4, 3, 2]

test_join_small = [1, 2, 3]  # 7 num
test_join_big = [50, 26, 41, 40, 35, 88, 89, 34, 29, 53]  # 10 num


def create_rand_keys(n: int, start: int = 0, end: int = 100):
    rand_test = set()
    while len(rand_test) < n:
        rand_test.add(random.randint(start, end))
    return rand_test


def test_tree(t: AVLTree, keys, multiple_prints: bool = False, with_printing: bool = True):
    for key in keys:
        t.insert(key=key, val="")
        if multiple_prints and with_printing:
            t.printt()
            print("################################")

    if with_printing and not multiple_prints:
        t.printt()
        print("################################")

    return t


rand_small = create_rand_keys(n=50, start=0, end=500)

exception_set = {0, 261, 6, 264, 138, 12, 270, 400, 18, 20, 404, 278, 151, 152, 281, 26, 21, 284, 287, 162, 166, 294, 425, 41, 302, 182, 310, 443, 315, 61, 66, 67, 453, 71, 328, 73, 74, 330, 329, 213, 476, 92, 489, 235, 366, 498, 373, 120, 250, 253}

print(f"rand small: {rand_small}")
t1 = test_tree(t=t1, keys=exception_set)
rand_node = t1.select(i=15)
split_trees = t1.split(node=rand_node)
split_trees[0].printt()
print("################################")
split_trees[1].printt()
print("################################")
print(f"split node: {rand_node}")