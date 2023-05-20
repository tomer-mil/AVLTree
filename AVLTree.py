# username - mildworth
# id1      - 316081355
# name1    - Tomer Mildworth
# id2      - 207702861
# name2    - Lior Bodner


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
        """
        Checks whether two nodes are equal, based on their key's value.

        Complexity: O(1)

        :param other: AVLNode
        :return: True if self.key == other.key or when nodes are None. Else False
        """

        if not other:
            if not self:
                return True
            else:
                return False
        return self.key == other.key

    def __lt__(self, other):
        """
        Less-than for nodes by comparing keys.

        Complexity: O(1)

        :param other: AVLNode
        :return: True if self.key < other.key
        """
        return self.key < other.key

    def __le__(self, other):
        """
        Less-than or equals for nodes by comparing keys.

        Complexity: O(1)

        :param other: AVLNode
        :return: True if self.key <= other.key
        """
        return self.key <= other.key

    def __gt__(self, other):
        """
        Greater-than for nodes by comparing keys.

        Complexity: O(1)

        :param other: AVLNode
        :return: True if self.key > other.key
        """
        return self.key > other.key

    def __ge__(self, other):
        """
        Greater-than or equals for nodes by comparing keys.

        Complexity: O(1)

        :param other: AVLNode
        :return: True id self.key >= other key
        """
        return self.key >= other.key

    """returns the key
    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        return self.key

    def get_relative_direction(self) -> str:
        """
        Determines the direction of the node in relation to his parent, i.e. whether the node is a left or right child.

        Complexity: O(1)

        :return: "left", "right" or "root"
        """
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

    def get_bf(self) -> int:
        """
        Returns the Balance-Factor of the node, or -99 if no node (real or dummy) on both sides.

        Complexity: O(1)

        :return: left.height - right.height
        """

        return self.left.height - self.right.height if (self.left and self.right) else -99

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

    def height_manager(self) -> bool:
        """
        Updates the nodes current height and returns a boolean indicating whether a height change occurred.

        Complexity: O(1)

        :return: True if height has changed
        """

        new_height = 1 + max(self.left.height, self.right.height)

        if self.height != new_height:
            self.height = new_height
            return True  # height changed
        return False  # height stayed the same

    """sets the size of node
    @type s: int
    @param s: the size
    """

    def set_size(self, s):
        self.size = s

    def update_size(self) -> None:
        """
        Updates the node's current size.

        Complexity: O(1)

        :return: None
        """
        self.set_size(s=(self.right.size + self.left.size + 1))

    """returns whether self is not a virtual node 
    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self) -> bool:
        return self.key is not None

    def has_dummy_child(self) -> bool:
        """
        Checks whether one of the node's children is a dummy node.

        Complexity: O(1)

        :return: True if has dummy node as child
        """

        return (not self.left.is_real_node()) or (not self.right.is_real_node())

    def is_leaf(self) -> bool:
        """
        Checks whether the node is a leaf (i.e. both children are dummies).

        Complexity: O(1)

        :return:
        """
        return (not self.left.is_real_node()) and (not self.right.is_real_node())

    def add_dummy_nodes(self) -> None:
        """
        Adds the node dummy nodes as children on both sides.

        Complexity: O(1)

        :return: None
        """
        self.add_left_dummy()
        self.add_right_dummy()

    def add_left_dummy(self) -> None:
        """
        Adds the node a dummy child node on the left side.

        Complexity: O(1)

        :return: None
        """

        dummy = AVLNode(height=-1)
        dummy.set_size(s=0)

        self.left = dummy

    def add_right_dummy(self):
        """
        Adds the node a dummy child node on the right side.

        Complexity: O(1)

        :return: None
        """

        dummy = AVLNode(height=-1)
        dummy.set_size(s=0)
        self.right = dummy

    def set_as_other_node(self, other, with_parent: bool = True) -> None:
        """
        Copies another node's parameters' values to the current node.

        Complexity: O(1)

        :param other: AVLNode - node to copy values from
        :param with_parent: bool (default True) - Whether to link this node to other's parent
        :return: None
        """

        if not other.is_real_node():  # Other node is dummy
            self.set_as_dummy()
            return

        self.key = other.key
        self.value = other.value
        self.height = other.height
        self.size = other.size

        if other.left.is_real_node():
            self.left = other.left
            self.left.parent = self
        else:  # Other's left child is dummy
            self.add_left_dummy()

        if other.right.is_real_node():
            self.right = other.right
            self.right.parent = self
        else:  # Other's right child is dummy
            self.add_right_dummy()

        self.parent = other.parent if with_parent else None

    def set_as_dummy(self) -> None:
        """
        Sets a node's parameters to a dummy node's parameters.

        Complexity: O(1)

        :return:
        """
        self.key = None
        self.value = None
        self.height = -1
        self.size = 0
        self.right, self.left = None, None
        self.parent = None


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def __init__(self, root: AVLNode = AVLNode()):
        self.root = root
        self.min = None
        self.max = None

    def __repr__(self):
        return f"root: {self.root.key} | s: {self.size()} | h: {self.root.height}"

    def is_empty(self) -> bool:
        """
        Checks if the current tree is an empty tree (i.e. has a non-dummy [real or not None] AVLNode as root)

        Complexity: O(1)

        :return: True if root is None or dummy node.
        """
        return not self.root.is_real_node()

    def should_update_min(self, node: AVLNode) -> bool:
        """
        Checks if the current inserted node's key is smaller than the current tree's saved minimum node.

        If no minimum node is saved, returns False.

        Complexity: O(1)

        :param node: AVLNode
        :return: True if node's key is smaller than tree's minimum
        """
        return node.key < self.min.key if self.min else True

    def should_update_max(self, node: AVLNode) -> bool:
        """
        Checks if the current inserted node's key is bigger than the current tree's saved maximum node.

        If no maximum node is saved, returns False.

        Complexity: O(1)

        :param node: AVLNode
        :return: True if node's key is bigger than tree's maximum
        """
        return node.key > self.max.key if self.max else True

    def get_subtree_min(self) -> AVLNode:
        """
        Returns the the current tree minimum node by going down the tree, starting from the root.

        Complexity: O(log(n))

        :return: AVLNode with minimal key
        """
        curr_node = self.root
        while curr_node.left.is_real_node():
            curr_node = curr_node.left
        return curr_node

    def get_subtree_max(self):
        """
        Returns the the current tree maximum node by going down the tree, starting from the root.

        Complexity: O(log(n))

        :return: AVLNode with maximal key
        """
        curr_node = self.root
        while curr_node.right.is_real_node():
            curr_node = curr_node.right
        return curr_node

    def init_min_max(self) -> None:
        """
        Initializes the tree's min and max attributes.

        Complexity: O(log(n))

        :return: None
        """
        if self.is_empty():
            return
        self.min = self.get_subtree_min()
        self.max = self.get_subtree_max()

    """searches for a value in the dictionary corresponding to the key
    
    Complexity: O(log(n))
    
    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode if found, else None
    @returns: the node corresponding to key.
    """

    def search(self, key) -> AVLNode | None:
        curr_node = self.root
        while curr_node.is_real_node():
            if curr_node.key == key:  # key found
                return curr_node
            if curr_node.key > key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        return None  # no such key was found

    def set_as_child_after_rotation(self, node: AVLNode, relative_direction: str) -> None:
        """
        Sets a given node as a child of his parent in a given direction by 'relative_direction'.

        The function is being called specifically while preforming a rotation.

        Complexity: O(1)

        :param node: AVLNode - the node that changes places
        :param relative_direction: str - the direction in which 'node' should be placed
        :return: None
        """
        if relative_direction == "root":
            setattr(self, relative_direction, node)
        else:
            setattr(node.parent, relative_direction, node)

    ####################
    ###### Insert ######
    ####################
    """Inserts val at position i in the dictionary
    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, key, val) -> int:
        """
        Inserts a new node to the tree with given key and value.

        Insertion starts with a basic Binary Search Tree (BST) insertion,
        then checks whether or not to update minimum and maximum attributes,
        and finally rebalances the tree going upwards from the inserted node using rotations.

        While rebalancing, the method counts the balance actions taken (as defined in the assignment) in order
        to make the tree a valid AVL tree.

        Complexity: O(log(n))

        :param key: int - The key of the inserted data
        :param val: Any - The value of the inserted data
        :return: int - Number of balance actions required for insertion
        """

        # Generates a new node with given params
        new_node = AVLNode(key=key, value=val)

        # Inserts the node with a classic BST algorithm
        self.BST_insert(node=new_node)

        # Update tree attributes if needed
        if self.should_update_min(node=new_node):
            self.min = new_node
        if self.should_update_max(node=new_node):
            self.max = new_node

        # Preforming balancing actions (rotations and attributes maintaining) while walking up the tree
        balance_actions = self.rebalance_up(start_node=new_node.get_parent())

        return balance_actions

    def rotate(self, node: AVLNode) -> int:
        """
        Preforms the rotation mechanism of AVL trees as learnt in class.

        The methods calls the correct rotation method (L, R, R then L or L then R) based on the balance factor
        and relative direction of the input node.
        :param node:
        :return:
        """

        # Check the relative direction of the node to its parent in order to connect the new node in the same location
        relative_direction = node.get_relative_direction()

        node_bf = node.get_bf()
        child_bf = node.left.get_bf() if node_bf == 2 else node.right.get_bf()

        if node_bf == 2:
            if child_bf == 1 or child_bf == 0:
                self.right_rotation(node=node, relative_direction=relative_direction)
                count_balance_actions_rotate = 1

            else:  # child_bf == -1
                self.left_then_right_rotation(node=node, relative_direction=relative_direction)
                count_balance_actions_rotate = 2

        else:  # node_bf == -2
            if child_bf == -1 or child_bf == 0:
                self.left_rotation(node=node, relative_direction=relative_direction)
                count_balance_actions_rotate = 1
            else:  # child_bf == 1
                self.right_then_left_rotation(node=node, relative_direction=relative_direction)
                count_balance_actions_rotate = 2

        # Attribute update #

        node.height_manager()
        node.update_size()

        return count_balance_actions_rotate

    def right_rotation(self, node: AVLNode, relative_direction: str | None):

        B = node
        A = node.left

        B.left = A.right
        B.left.parent = B
        A.right = B
        A.parent = B.parent

        if not relative_direction:  # Partial rotation (RL)
            A.parent.right = A
            B.height_manager()  # "6" is a leaf after partial-right rotation
            A.height_manager()  # "8" is a "6"'s parent after partial-right rotation

        else:
            self.set_as_child_after_rotation(node=A, relative_direction=relative_direction)

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

        if not relative_direction:  # Partial rotation (LR)
            A.parent.left = A
            B.height_manager()
            A.height_manager()

        else:
            self.set_as_child_after_rotation(node=A, relative_direction=relative_direction)

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
            self.root.size = 1

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

    """
    @pre: node is a real pointer to a node in self
    """
    def BST_delete(self, node: AVLNode):

        has_dummy_child = node.has_dummy_child()
        node_relative_direction = node.get_relative_direction()

        if has_dummy_child:
            new_node = AVLNode()

            # Case 1: x is leaf
            if node.is_leaf():

                # node is the only node on tree
                if node_relative_direction == 'root':
                    self.root = new_node
                    return

                else:
                    need_rebalance_from = node.parent

                    new_node.set_as_dummy()
                    new_node.parent = node.parent
                    setattr(node.parent, node_relative_direction, new_node)

                    return need_rebalance_from

            # Case 2: node has one child
            child_relative_direction = 'left' if node.left.is_real_node() else 'right'
            relevant_child = getattr(node, child_relative_direction)

            setattr(node, child_relative_direction + ".parent", node.parent)  # example : node.left.parent = node.parent
            setattr(node.parent, node_relative_direction, relevant_child)

            return relevant_child

        # Case 3: node has two children
        else:
            new_node = self.successor(node=node)  # y
            self.BST_delete(node=new_node)
            # node.set_as_other_node(other=new_node, with_parent=True)

            # new_node.set_as_other_node(other=node, with_parent=True)
            self.replace_nodes(original=node, new=new_node)

            return new_node

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
            while curr_node.parent.right == curr_node:
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
            while curr_node.parent.left == curr_node:
                curr_node = curr_node.parent

            return curr_node.parent if curr_node != self.root else curr_node

    """deletes node from the dictionary
    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node):

        if node.key == self.min.key:
            self.min = self.successor(node=self.min)

        if node.key == self.max.key:
            self.max = self.predecessor(node=self.max)

        rebalance_start_node = self.BST_delete(node=node)
        if rebalance_start_node:  # The tree is empty after deletion -> No need for rebalancing
            balance_actions = self.rebalance_up(start_node=rebalance_start_node)
            return balance_actions
        return 0


    """returns an array representing dictionary 
    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        arr = []

        if self.is_empty():
            return arr

        curr_node = self.min
        arr.append((curr_node.key, curr_node.value))

        while curr_node.key != self.max.key:
            curr_node = self.successor(node=curr_node)
            arr.append((curr_node.key, curr_node.value))

        return arr

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
            temp_node = AVLNode()
            if curr_node.get_relative_direction() == "right":

                temp_node.set_as_other_node(other=curr_node.parent.left, with_parent=False)

                temp_tree.root = temp_node
                temp_tree.init_min_max()

                left_tree.join(tree=temp_tree, key=curr_node.parent.key, val=curr_node.parent.value)

            else:  # curr_node.get_relative_direction() == "left":

                temp_node.set_as_other_node(other=curr_node.parent.right, with_parent=False)

                temp_tree.root = temp_node
                temp_tree.init_min_max()

                right_tree.join(tree=temp_tree, key=curr_node.parent.key, val=curr_node.parent.value)

            curr_node = curr_node.parent

        #  maintain min and max for the new splitted trees
        if not right_tree.is_empty():
            right_tree.max = self.max
            right_tree.min = self.successor(node=node)
            # right_tree.init_min()

        if not left_tree.is_empty():
            left_tree.min = self.min
            left_tree.max = self.predecessor(node=node)
            # left_tree.init_max()

        return [left_tree, right_tree]

    def get_sub_tree_root(self, direction: str, sub_tree_height: int):

        # this part is allowing us abstraction.
        # if the relative direction of the higher tree is right, then in order to get the correct sub-tree then we

        curr_node = self.root

        if direction == "right":
            while curr_node.height > sub_tree_height:
                if not curr_node.right.is_real_node():  # Edge-case of sub_tree_height == 0 -> Reaches dummy-node
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
        else:  # direction == "left"
            while curr_node.height > sub_tree_height:
                if not curr_node.left.is_real_node():    # Edge-case of sub_tree_height == 0 -> Reaches dummy-node
                    curr_node = curr_node.right
                else:
                    curr_node = curr_node.left

        return curr_node  # this is the sub-tree root!

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

        pivot_node = AVLNode(key=key, value=val)

        has_empty = self.is_empty() or tree.is_empty()

        if has_empty:  # Quick exit: one of the trees is empty
            height_difference = abs(self.root.height - tree.root.height) + 1
            self.join_with_dummy(tree=tree, pivot_node=pivot_node)
            return height_difference

        # Both trees are not empty
        join_direction = "left" if self.root.key > pivot_node.key else "right"

        if join_direction == "right":
            height_difference = self.join_right(other=tree, pivot_node=pivot_node)
            self.max = tree.max
        else:
            height_difference = self.join_left(other=tree, pivot_node=pivot_node)
            self.min = tree.min

        self.rebalance_up(start_node=pivot_node)  # rebalance from x(=new_node) upwards

        return height_difference

    def join_with_dummy(self, tree, pivot_node):

        if not tree.is_empty():  # self is empty
            tree.insert(key=pivot_node.key, val=pivot_node.value)
            self.set_as_other_tree(other=tree)

        else:  # tree is empty
            self.insert(key=pivot_node.key, val=pivot_node.value)

    def join_left(self, other, pivot_node):
        height_difference = self.root.height - other.root.height

        #  Simple joining
        if abs(height_difference) <= 1:
            self.root.parent = pivot_node
            other.root.parent = pivot_node

            pivot_node.right = self.root
            pivot_node.left = other.root

            self.root = pivot_node

        elif height_difference > 0:  # self is higher
            sub_tree = self.get_sub_tree_root(direction="left", sub_tree_height=other.root.height)

            pivot_node.left = other.root
            other.root.parent = pivot_node

            pivot_node.right = sub_tree
            pivot_node.parent = sub_tree.parent
            sub_tree.parent.left = pivot_node

            sub_tree.parent = pivot_node

        else:  # other is higher
            sub_tree = other.get_sub_tree_root(direction="right", sub_tree_height=self.root.height)

            pivot_node.right = self.root
            self.root.parent = pivot_node

            pivot_node.left = sub_tree
            pivot_node.parent = sub_tree.parent
            sub_tree.parent.right = pivot_node

            sub_tree.parent = pivot_node

            self.root = other.root
        return abs(height_difference) + 1

    def join_right(self, other, pivot_node):
        height_difference = self.root.height - other.root.height

        #  Simple joining
        if abs(height_difference) <= 1:
            self.root.parent = pivot_node
            other.root.parent = pivot_node

            pivot_node.left = self.root
            pivot_node.right = other.root

            self.root = pivot_node

        elif height_difference > 0:  # self is higher
            sub_tree = self.get_sub_tree_root(direction="right", sub_tree_height=other.root.height)

            pivot_node.right = other.root
            other.root.parent = pivot_node

            pivot_node.left = sub_tree
            pivot_node.parent = sub_tree.parent
            sub_tree.parent.right = pivot_node

            sub_tree.parent = pivot_node

        else:  # other is higher
            sub_tree = other.get_sub_tree_root(direction="left", sub_tree_height=self.root.height)

            pivot_node.left = self.root
            self.root.parent = pivot_node

            pivot_node.right = sub_tree
            pivot_node.parent = sub_tree.parent
            sub_tree.parent.left = pivot_node

            sub_tree.parent = pivot_node

            self.root = other.root
        return abs(height_difference) + 1

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

    def replace_nodes(self, original: AVLNode, new: AVLNode):

        original_relative_direction = original.get_relative_direction()

        new.left = original.left
        original.left.parent = new

        new.right = original.right
        original.right.parent = new

        if original.parent:  # If original is the root
            new.parent = original.parent
            setattr(original.parent, original_relative_direction, new)
        else:
            self.root = new
            new.parent = None

    def set_as_other_tree(self, other):
        self.root = other.root
        self.max = other.max
        self.min = other.min


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
