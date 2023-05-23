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

    def get_key(self) -> int:
        """
        Returns the node's key.

        Complexity: O(1)

        :return: int - The node's key
        """
        return self.key

    """returns the value
    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        """
        Returns the node's stored value.

        Complexity: O(1)

        :return: Any - The node's value
        """
        return self.value

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    def get_left(self):
        """
        Returns the node's left child.

        Complexity: O(1)

        :return: AVLNode - Node's left child
        """
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self):
        """
        Returns the node's right child.

        Complexity: O(1)

        :return: AVLNode - Node's right child
        """
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def get_parent(self):
        """
        Returns the node's parent

        Complexity: O(1)

        :return: AVLNode - Node's parent
        """
        return self.parent

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def get_height(self) -> int:
        """
        Returns the node's height.

        Complexity: O(1)

        :return: int - Node's height
        """
        return self.height

    """returns the size of the subtree

    @rtype: int
    @returns: the size of the subtree of self, 0 if the node is virtual
    """

    def get_size(self) -> int:
        """
        Returns the node's size.

        Complexity: O(1)

        :return: int - Node's size
        """
        return self.size

    def get_relative_direction(self) -> str:
        """
        Determines the direction of the node in relation to his parent, i.e. whether the node is a left or right child.

        Complexity: O(1)

        :return: "left", "right" or "root"
        """
        if not self.parent:
            return "root"
        return "left" if self == self.parent.left else "right"

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

    def set_key(self, key) -> None:
        """
        Sets a given key to the node.

        Complexity: O(1)

        :param key: int - Key to be set to the node
        :return:
        """
        self.key = key

    """sets value
    @type value: any
    @param value: data
    """

    def set_value(self, value) -> None:
        """
        Sets a given value to the node.

        Complexity: O(1)

        :param value: Any - Value to be set to the node
        :return:
        """
        self.value = value

    """sets left child
    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node) -> None:
        """
        Sets the node's left child.

        Complexity: O(1)

        :param node: AVLNode - The designated left child
        :return: None
        """
        self.left = node

    """sets right child
    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node) -> None:
        """
        Sets the node's right child.

        Complexity: O(1)

        :param node: AVLNode - The designated right child
        :return: None
        """
        self.right = node

    """sets parent
    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node) -> None:
        """
        Sets the node's parent.

        Complexity: O(1)

        :param node: AVLNode - The designated parent
        :return: None
        """
        self.parent = node

    """sets the height of the node
    @type h: int
    @param h: the height
    """

    def set_height(self, h: int) -> None:
        """
        Sets the node's height.

        Complexity: O(1)

        :param h: int - The height to set
        :return: None
        """
        self.height = h

    """sets the size of node
    @type s: int
    @param s: the size
    """

    def set_size(self, s: int) -> None:
        """
        Sets the node's size.

        Complexity: O(1)

        :param s: int - The size to set
        :return: None
        """
        self.size = s

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
        """
        Checks whether the node is a real node by checking if the node has a populated `key` attribute.

        Complexity: O(1)

        :return: True if node.key is not None
        """
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

    def add_dummy_nodes(self) -> None:
        """
        Adds the node dummy nodes as children on both sides.

        Complexity: O(1)

        :return: None
        """
        self.add_left_dummy()
        self.add_right_dummy()

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

    """returns the root of the tree representing the dictionary
    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self) -> AVLNode:
        """
        Returns the tree's root node.

        Complexity: O(1)

        :return: AVLNode - The tree's root node
        """
        return self.root

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

        Complexity: O(log(n)) - Going down an entire AVL tree is as its height, which is log(n).

        :return: AVLNode with minimal key
        """
        curr_node = self.root
        while curr_node.left.is_real_node():
            curr_node = curr_node.left
        return curr_node

    def get_subtree_max(self) -> AVLNode:
        """
        Returns the the current tree maximum node by going down the tree, starting from the root.

        Complexity: O(log(n)) - Going down an entire AVL tree is as its height, which is log(n).

        :return: AVLNode with maximal key
        """
        curr_node = self.root
        while curr_node.right.is_real_node():
            curr_node = curr_node.right
        return curr_node

    def init_min_max(self) -> None:
        """
        Initializes the tree's min and max attributes.

        Complexity: O(log(n)) - Going down an entire AVL tree is as its height, which is log(n), one time after the other.

        :return: None
        """
        if self.is_empty():
            return
        self.min = self.get_subtree_min()
        self.max = self.get_subtree_max()

    """searches for a value in the dictionary corresponding to the key
    
    Complexity: O(log(n)) - Going down an entire AVL tree is as its height, which is log(n)
    
    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode if found, else None
    @returns: the node corresponding to key.
    """

    def search(self, key: int) -> AVLNode | None:
        """
        Searches for a value in the dictionary corresponding to the key

        Complexity: O(log(n)) - Going down an entire AVL tree is as its height, which is log(n), preforming O(1) actions
                                in each step.

        :param key: int - The key to search in the tree
        :return: AVLNode | None - Returns the found node, is no node is found returns None
        """

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
        Sets a given node as a child of his parent in a given direction by `relative_direction`.

        The function is being called specifically while preforming a rotation.

        Complexity: O(1)

        :param node: AVLNode - the node that changes places
        :param relative_direction: str - the direction in which `node` should be placed
        :return: None
        """
        if relative_direction == "root":
            setattr(self, relative_direction, node)
        else:
            setattr(node.parent, relative_direction, node)

    def right_rotation(self, node: AVLNode, relative_direction: str | None) -> None:
        """
        Preforms an AVL right rotation.

        The method rotates the nodes and updates the relevant attributes accordingly

        Complexity: O(1)

        :param node: AVLNode - The node that rotates
        :param relative_direction: str - In case of a partial rotation, sets the node's correct final direction
        :return: None
        """

        # Naming nodes like the class presentation to maintain readability and consistency with pseudocode
        B = node
        A = node.left

        B.left = A.right
        B.left.parent = B
        A.right = B
        A.parent = B.parent

        if not relative_direction:  # Partial rotation (R then L)
            A.parent.right = A
            B.height_manager()
            A.height_manager()

        else:
            self.set_as_child_after_rotation(node=A, relative_direction=relative_direction)

        B.parent = A

        B.update_size()
        A.update_size()

    def left_rotation(self, node: AVLNode, relative_direction: str | None) -> None:
        """
        Preforms an AVL left rotation.

        The method rotates the nodes and updates the relevant attributes accordingly

        Complexity: O(1)

        :param node: AVLNode - The node that rotates
        :param relative_direction: str - In case of a partial rotation, sets the node's correct final direction
        :return: None
        """

        # Naming nodes like the class presentation to maintain readability and consistency with pseudocode
        B = node
        A = node.right

        B.right = A.left
        B.right.parent = B
        A.left = B
        A.parent = B.parent

        if not relative_direction:  # Partial rotation (L then R)
            A.parent.left = A
            B.height_manager()
            A.height_manager()

        else:
            self.set_as_child_after_rotation(node=A, relative_direction=relative_direction)

        B.parent = A

        B.update_size()
        A.update_size()

    def right_then_left_rotation(self, node: AVLNode, relative_direction: str) -> None:
        """
        Preforms an AVL right-then-left rotation.

        The method rotates the nodes and updates the relevant attributes accordingly

        Complexity: O(1)

        :param node: AVLNode - The node that rotates
        :param relative_direction: str - Sets the node's correct final direction
        :return: None
        """

        self.right_rotation(node=node.right, relative_direction=None)
        self.left_rotation(node=node, relative_direction=relative_direction)

    def left_then_right_rotation(self, node: AVLNode, relative_direction: str) -> None:
        """
        Preforms an AVL left-then-right rotation.

        The method rotates the nodes and updates the relevant attributes accordingly

        Complexity: O(1)

        :param node: AVLNode - The node that rotates
        :param relative_direction: str - Sets the node's correct final direction
        :return: None
        """

        self.left_rotation(node=node.left, relative_direction=None)
        self.right_rotation(node=node, relative_direction=relative_direction)

    def rotate(self, node: AVLNode) -> int:
        """
        Preforms the rotation mechanism of AVL trees as learned in class.

        The methods calls the correct rotation method (L, R, R then L or L then R) based on the balance factor
        and relative direction of the input node.

        The method returns the number of balance actions taken in the rotation as defined in the assignment.

        Complexity: O(1)

        :param node: AVLNode - The node to rotate
        :return: int - The number of balance actions taken in the rotation
        """

        # Check the relative direction of the node to its parent in order to connect the new node in the same location
        relative_direction = node.get_relative_direction()

        # Get the node's and relevant child's balance factors
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

        # Attribute update
        node.height_manager()
        node.update_size()

        return count_balance_actions_rotate

    def rebalance_up(self, start_node: AVLNode) -> int:
        """
        Maintaining AVL properties by going up the tree while preforming rotations and updating attributes if needed.
        The method starts from a given node in the tree and goes up until reaching the root.

        The method returns the number of balance actions required for the rebalance process as defined in the assignment.

        Complexity: O(log(n)) - In the WC wee must go up the entire tree, preforming actions with O(1) complexity on
                                each iteration, meaning a total of O(log(n))

        :param start_node: AVLNode - The node which we start going up from.
        :return: int - Number of balance actions taken in the call.
        """
        count_balance_actions = 0

        while start_node:  # While start_node is not None, meaning we reached the root

            did_height_change = start_node.height_manager()

            node_abs_bf = abs(start_node.get_bf())

            if node_abs_bf < 2:

                start_node.update_size()

                if did_height_change:
                    start_node = start_node.get_parent()
                    count_balance_actions += 1

                else:
                    return count_balance_actions

            else:  # node_abs_bf == 2:
                count_balance_actions += self.rotate(node=start_node)
                return count_balance_actions

    def BST_insert(self, node: AVLNode) -> None:
        """
        A classic Binary Search tree insertion as learned in class.

        The method goes down the tree to the correct insertion spot and updates size attribute while doing so.

        Complexity: O(log(n)) - Inserting to a BST is linear with its height. Since we are guaranteed we are inserting
                                a new node into a valid AVL tree, we know the height as log(n) maximum, hence a total of
                                O(log(n))

        :param node: AVLNode - the node being inserted
        :return: None
        """

        node.add_dummy_nodes()

        # If this is the first insertion or the tree is empty
        if self.is_empty():
            self.root = node
            self.root.size = 1

        else:
            higher_node = AVLNode()
            lower_node = self.root

            # Walking down the tree to the designated parent
            while lower_node.is_real_node():
                higher_node = lower_node

                higher_node.size += 1

                if node.key < lower_node.key:
                    lower_node = lower_node.left
                else:
                    lower_node = lower_node.right

            node.parent = higher_node

            # Inserting at the right relative direction
            if node.key < higher_node.key:
                higher_node.left = node
            else:
                higher_node.right = node

    """Inserts val at position i in the dictionary
    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, key: int, val) -> int:
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

    def successor(self, node: AVLNode) -> AVLNode | None:
        """
        Finds a given node's successor node.

        Complexity: O(log(n)) - In the WC, we would go up/down the entire tree, which means the complexity is
                                linear with the tree's height, which is log(n) at most.

        :param node: AVLNode - The successor of which node to find
        :return: AVLNode if successor found, None if input node is maximum or the tree is empty
        """

        # Quick exit for when the node is the maximum node or the tree is empty
        if node == self.max or self.is_empty():
            return None

        if node.right.is_real_node():
            curr_node = node.right
            while curr_node.left.is_real_node():
                curr_node = curr_node.left
            return curr_node

        # If I'm here- I'm not a root!
        else:
            curr_node = node  # For readability purposes, generally redundant
            while curr_node.parent.right == curr_node:
                curr_node = curr_node.parent

            return curr_node.parent if curr_node != self.root else curr_node

    def predecessor(self, node: AVLNode) -> AVLNode | None:
        """
        Finds a given node's predecessor node.

        Complexity: O(log(n)) - In the WC, we would go up/down the entire tree, which means the complexity is
                                linear with the tree's height, which is log(n) at most.

        :param node: AVLNode - The predecessor of which node to find
        :return: AVLNode if successor found, None if input node is minimum or the tree is empty
        """

        # Quick exit for when the node is the minimum node or the tree is empty
        if node == self.min or self.is_empty():
            return None

        if node.left.is_real_node():
            curr_node = node.left
            while curr_node.right.is_real_node():
                curr_node = curr_node.right
            return curr_node

        # If i'm here- I'm not a root!
        else:
            curr_node = node  # For readability purposes, generally redundant
            while curr_node.parent.left == curr_node:
                curr_node = curr_node.parent

            return curr_node.parent if curr_node != self.root else curr_node

    def replace_nodes(self, original_node: AVLNode, new_node: AVLNode) -> None:
        """
        Puts a new node in another node's place in the tree.

        Complexity: O(1)

        :param original_node: AVLNode - The present node in the tree
        :param new_node: AVLNode - The node to be replaced with
        :return: None
        """

        original_relative_direction = original_node.get_relative_direction()

        new_node.left = original_node.left
        original_node.left.parent = new_node

        new_node.right = original_node.right
        original_node.right.parent = new_node

        if original_node.parent:  # original_node has a parent
            new_node.parent = original_node.parent
            setattr(original_node.parent, original_relative_direction, new_node)

        else:  # original_node is the root
            self.root = new_node
            new_node.parent = None

    """
    @pre: node is a real pointer to a node in self
    """
    def BST_delete(self, node: AVLNode) -> AVLNode | None:
        """
        A classic Binary Search Tree deletion.

        The method differentiates between one of 3 possible cases and preforms the deletion accordingly.

        The methods returns the node from which the AVL tree should start its rebalancing process, or None if the
        deleted node was the only node in the tree.

        Complexity: O(log(n)) -
                                Cases 1 & 2 are both O(1) since they are changes of pointers. Case 3 in the WC
                                could be O(log(n)) because the recursion call would stop when reaching a leaf, and
                                that might require going down the entire tree and finding successors.
                                Since we guarantee this method is being called on an AVL tree, it would take up to
                                O(log(n)) time.

        :param node: AVLNode - The node to be deleted from the tree
        :return: AVLNode | None - The node from which rebalancing should start
        """

        has_dummy_child = node.has_dummy_child()
        node_relative_direction = node.get_relative_direction()

        if has_dummy_child:
            new_node = AVLNode()

            # Case 1: node is a leaf
            if node.is_leaf():

                # The node is the only node in the tree
                if node_relative_direction == "root":
                    self.root = new_node
                    return None

                # There's at least one more node
                else:
                    need_rebalance_from = node.parent

                    new_node.set_as_dummy()
                    new_node.parent = node.parent
                    setattr(node.parent, node_relative_direction, new_node)  # Replaces deleted node with a dummy

                    return need_rebalance_from

            # Case 2: node has one child
            child_relative_direction = 'left' if node.left.is_real_node() else 'right'
            relevant_child = getattr(node, child_relative_direction)

            # Passing the child to node's parent in the correct direction
            setattr(node, child_relative_direction + ".parent", node.parent)  # Example: node.left.parent = node.parent
            setattr(node.parent, node_relative_direction, relevant_child)

            return relevant_child

        # Case 3: node has two children
        else:
            new_node = self.successor(node=node)
            self.BST_delete(node=new_node)  # Disconnects node's successor from the tree
            self.replace_nodes(original_node=node, new_node=new_node)  # Replaces the successor with the original node

            return new_node

    """deletes node from the dictionary
    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node: AVLNode) -> int:
        """
        Deletes a given node in the tree.

        The method returns the number of balance actions required in the deletion process.

        Complexity: O(log(n)) - Successor/Predecessor: O(log(n)) + BST_delete: O(log(n)) + rebalance_up: O(log(n))

        :param node: AVLNode - The node to delete from the tree
        :return: int - The number of rebalance actions taken
        """

        # Updating min/max attribute
        if node.key == self.min.key:
            self.min = self.successor(node=self.min)
        if node.key == self.max.key:
            self.max = self.predecessor(node=self.max)

        rebalance_start_node = self.BST_delete(node=node)
        if rebalance_start_node:  # Checking if a rebalance starting node is present
            balance_actions = self.rebalance_up(start_node=rebalance_start_node)  # If so, start rebalancing
            return balance_actions
        return 0  # Else, the tree is empty after deletion meaning no need for rebalancing

    """returns the number of items in dictionary 
    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self) -> int:
        """
        Returns the tree's size.

        The method calls the root's size attribute.

        Complexity: O(1)

        :return: int - Size of the tree
        """
        return self.get_root().get_size()

    def set_as_other_tree(self, other) -> None:
        """
        Sets another tree as the current tree.

        Complexity: O(1)

        :param other: AVLTree - The tree that being set as self
        :return: None
        """
        self.root = other.root
        self.max = other.max
        self.min = other.min

    def get_subtree_root(self, direction: str, subtree_height: int) -> AVLNode:
        """
        Returns an AVLNode with desired height, going down a specific direction starting from the root.

        Complexity: O(log(n)) - In the WC we went down the entire tree, then the time complexity is linear with the
                                tree's height which is O(log(n))

        :param direction: str - "left" or "right". The direction in which walking down the tree goes.
        :param subtree_height: int - Non-negative int which is the desired subtree height
        :return: AVLNode - The found node from which the subtree stems
        """

        curr_node = self.root

        if direction == "right":
            while curr_node.height > subtree_height:
                if not curr_node.right.is_real_node():  # Edge-case of sub_tree_height == 0 -> Reaches dummy-node
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
        else:  # direction == "left"
            while curr_node.height > subtree_height:
                if not curr_node.left.is_real_node():    # Edge-case of sub_tree_height == 0 -> Reaches dummy-node
                    curr_node = curr_node.right
                else:
                    curr_node = curr_node.left

        return curr_node  # this is the subtree root!

    def join_with_dummy(self, other, pivot_node: AVLNode) -> None:
        """
        Joins a non-empty tree with an empty tree.

        Complexity: O(log(n)) - Same complexity as insert

        :param other: AVLTree - The tree to join.
        :param pivot_node: AVLNode - The "middle" node to join with
        :return: None
        """

        if not other.is_empty():  # self is empty
            other.insert(key=pivot_node.key, val=pivot_node.value)
            self.set_as_other_tree(other=other)

        else:  # tree is empty
            self.insert(key=pivot_node.key, val=pivot_node.value)

    def join_from_left(self, other, pivot_node: AVLNode) -> int:
        """
        Joins `other` with self when self is rightmost, meaning pivot_node.key < self.root.key

        The method differentiates between one of 3 possible cases and preforms the joining accordingly.

        Complexity:  O(|other.root.height - self.root.height| + 1) - The amount of levels we go up the tree is always the
                                                                 height difference of the joined trees WC.

        :param other: AVLTree - The tree to be joined to self
        :param pivot_node: AVLNode - The "middle" node to join the trees with
        :return: int - Absolute value of height difference between joined trees, plus 1
        """

        height_difference = self.root.height - other.root.height

        #  Simple joining - height difference (i.e. balance-factor of pivot_node) is <= 1
        if abs(height_difference) <= 1:
            self.root.parent = pivot_node
            other.root.parent = pivot_node

            pivot_node.right = self.root
            pivot_node.left = other.root

            self.root = pivot_node

        elif height_difference > 0:  # self is higher than other
            sub_tree = self.get_subtree_root(direction="left", subtree_height=other.root.height)

            pivot_node.left = other.root
            other.root.parent = pivot_node

            pivot_node.right = sub_tree
            pivot_node.parent = sub_tree.parent
            sub_tree.parent.left = pivot_node

            sub_tree.parent = pivot_node

        else:  # other is higher than self
            sub_tree = other.get_subtree_root(direction="right", subtree_height=self.root.height)

            pivot_node.right = self.root
            self.root.parent = pivot_node

            pivot_node.left = sub_tree
            pivot_node.parent = sub_tree.parent
            sub_tree.parent.right = pivot_node

            sub_tree.parent = pivot_node

            self.root = other.root
        return abs(height_difference) + 1

    def join_from_right(self, other, pivot_node: AVLNode) -> int:
        """
        Joins `other` with self when self is leftmost, meaning pivot_node.key > self.root.key

        The method differentiates between one of 3 possible cases and preforms the joining accordingly.

        Complexity:  O(|other.root.height - self.root.height| + 1) - The amount of levels we go up the tree is always the
                                                                 height difference of the joined trees WC.

        :param other: AVLTree - The tree to be joined to self
        :param pivot_node: AVLNode - The "middle" node to join the trees with
        :return: int - Absolute value of height difference between joined trees, plus 1
        """

        height_difference = self.root.height - other.root.height

        #  Simple joining - height difference (i.e. balance-factor of pivot_node) is <= 1
        if abs(height_difference) <= 1:
            self.root.parent = pivot_node
            other.root.parent = pivot_node

            pivot_node.left = self.root
            pivot_node.right = other.root

            self.root = pivot_node

        elif height_difference > 0:  # self is higher than other
            sub_tree = self.get_subtree_root(direction="right", subtree_height=other.root.height)

            pivot_node.right = other.root
            other.root.parent = pivot_node

            pivot_node.left = sub_tree
            pivot_node.parent = sub_tree.parent
            sub_tree.parent.right = pivot_node

            sub_tree.parent = pivot_node

        else:  # other is higher than self
            sub_tree = other.get_subtree_root(direction="left", subtree_height=self.root.height)

            pivot_node.left = self.root
            self.root.parent = pivot_node

            pivot_node.right = sub_tree
            pivot_node.parent = sub_tree.parent
            sub_tree.parent.left = pivot_node

            sub_tree.parent = pivot_node

            self.root = other.root
        return abs(height_difference) + 1

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

    def join(self, tree, key: int, val) -> int:
        """
        Joining two AVL trees using a given node that satisfies:
        self.max.key < node.key < tree.min.key

        The methods makes self the joined tree, and returns the height differences of the trees plus 1.
        After calling this method, the input tree is no longer usable.

        Complexity: O(|tree.root.height - self.root.height| + 1) - the amount of levels we go up the tree is always the
                                                                 height difference of the joined trees.

        :param tree: AVLTree - The tree to join with self
        :param key: int - The pivot node's key
        :param val: Any - The pivot node's value
        :return: int - Absolute value of height difference between joined trees, plus 1
        """

        pivot_node = AVLNode(key=key, value=val)

        has_empty = self.is_empty() or tree.is_empty()

        if has_empty:  # Quick exit: one of the trees is empty
            height_difference = abs(self.root.height - tree.root.height) + 1
            self.join_with_dummy(other=tree, pivot_node=pivot_node)
            return height_difference

        # Both trees are not empty
        join_direction = "left" if self.root.key > pivot_node.key else "right"

        if join_direction == "right":
            height_difference = self.join_from_right(other=tree, pivot_node=pivot_node)
            self.max = tree.max
        else:  # join_direction == "left"
            height_difference = self.join_from_left(other=tree, pivot_node=pivot_node)
            self.min = tree.min

        self.rebalance_up(start_node=pivot_node)  # rebalance from x(=new_node) upwards

        return height_difference

    """splits the dictionary at a given node
    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    def split(self, node: AVLNode) -> list:
        """
        Splits the current tree from a specific node into 2 non-usable trees, where one contains nodes with keys smaller
        than node.key, and the other with keys greater than node.key.

        The method uses split-by-joins as learned in class, meaning it generates 2 new trees and joins each one of
        them with a relevant subtree of self as described in `join`.

        Complexity: O(log(n)) - As learned in class and based on our implementation of the `join` method,
                                we are actually calculating a telescopic series of n-1 items that concludes to O(log(n))

        :param node: AVLNode - The node from which the method splits the tree
        :return: list[AVLTree, AVLTree] - A list with the 2 seperated trees in the following order: [smaller_than_tree, greater_than_tree]
        """

        # Initializing empty trees to be populated
        left_tree = AVLTree()
        right_tree = AVLTree()

        # Populating first nodes
        left_tree.root = node.left
        right_tree.root = node.right

        curr_node = node

        while curr_node.parent:  # Going up the tree until reaching the root
            temp_tree = AVLTree()
            temp_node = AVLNode()

            #  Creating subtrees and joining them with left/right_tree with subtree.root as pivot node
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

        #  Maintain minimum and maximum for the new seperated trees
        if not right_tree.is_empty():
            right_tree.max = self.max
            right_tree.min = self.successor(node=node)

        if not left_tree.is_empty():
            left_tree.min = self.min
            left_tree.max = self.predecessor(node=node)

        return [left_tree, right_tree]

    """compute the rank of node in the self
    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary which we want to compute its rank
    @rtype: int
    @returns: the rank of node in self
    """

    def rank(self, node: AVLNode) -> int:
        """
        Returns the rank of a given node in the tree.

        Complexity: O(log(n)) - As learned in class and recitations, because we maintain `size` attribute (which is dependant
                           only by the node's children and it's being calculated in O(1) time with their attributes) it
                           takes O(log(n)) calls of O(1) operations in the WC to get the rank.

        :param node: AVLNode - The node to calculate its rank. The node must be in the tree.
        :return: int - The rank of the node.
        """
        count = node.left.size + 1
        curr_node = node  # For readability purposes, generally redundant

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

    def select(self, i: int) -> AVLNode:
        """
        Returns the node with the corresponding input rank (i).

        The method checks whether the desired node is in the left/right subtree of the root and goes to the minimum/maximum
        accordingly. Then, the methods travels up the tree with successor/predecessor until it reaches the node with
        the i'th rank.

        Complexity: O(log(n)) - In the WC the method preforms max(i - 1, n - i) calls of successor/predecessor, which is
                                O(log(n)) as described in the `avl_to_array` method.

        :param i: int - The rank to look for
        :return: AVLNode - The node with i'th rank
        """

        # Quick exit: if `i` is the root's rank we don't need to go up the tree
        if i == self.root.left.size + 1:
            return self.root

        elif i <= self.root.left.size:
            curr_node = self.min  # Go to minimum
            for _ in range(1, i):  # i - 1 times
                curr_node = self.successor(node=curr_node)

        else:
            curr_node = self.max  # Go to maximum
            for _ in range(1, self.size() - i + 1):  # n - i times
                curr_node = self.predecessor(node=curr_node)

        return curr_node

    """returns an array representing dictionary 
    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self) -> list:
        """
        Returns an array with the tree's key-value pairs, sorted by the keys (ascending).

        The method does so by calling the tree's successor method n times starting from the tree's minimum.

        Complexity: O(n) - As proved in recitation 3 (Q4). In this case we preform n successor calls, meaning the total
                           time complexity is O(n + log(n)) => O(n)

        :return: list(int, Any) - key-value pairs, sorted by the keys (ascending)
        """
        arr = []

        if self.is_empty():
            return arr

        curr_node = self.min
        arr.append((curr_node.key, curr_node.value))

        while curr_node.key != self.max.key:
            curr_node = self.successor(node=curr_node)
            arr.append((curr_node.key, curr_node.value))

        return arr


