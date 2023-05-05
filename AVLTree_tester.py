import random
from AVLTree import AVLTree, AVLNode

DIVIDER = "####################################"

t1 = AVLTree()
t2 = AVLTree()
t3 = AVLTree()

empty_t = AVLTree()
root_t = AVLTree()
root_t.insert(key=10, val="")

test_import_small = [9, 8, 7, 10, 11]
test_import_big = [9, 8, 7, 6, 36, 30, 31, 90, 95, 96, 4, 3, 2]

test_join_left = [317, 303, 325, 298]  # 7 num
test_join_right = [351, 363, 333, 357, 374]  # 10 num


def create_rand_keys(n: int, start: int = 0, end: int = 100):
    rand_test = set()

    if n == 1:
        return random.randint(start, end)

    while len(rand_test) < n:
        rand_test.add(random.randint(start, end))

    return rand_test


def test_import(t: AVLTree, keys, multiple_prints: bool = False, with_printing: bool = True):
    for key in keys:
        t.insert(key=key, val="")
        if multiple_prints and with_printing:
            t.printt()
            print(DIVIDER)

    if with_printing and not multiple_prints:
        t.printt()
        print(DIVIDER)

    return t


def test_join(tree_1: AVLTree, tree_2: AVLTree, tree_1_keys: list = None, tree_2_keys: list = None, pivot_node_key: int = None):
    rand_big_1 = create_rand_keys(n=20, start=200, end=500) if not tree_1_keys else tree_1_keys
    rand_big_2 = create_rand_keys(n=50, start=0, end=150) if not tree_2_keys else tree_2_keys
    rand_node = create_rand_keys(n=1, start=151, end=199) if not pivot_node_key else pivot_node_key

    print(f"t1 keys: {rand_big_1}")
    print(f"t2 keys: {rand_big_2}")
    print(f"\njoin node key: {rand_node}")

    print(DIVIDER)

    print("tree 1:")
    test_import(t=tree_1, keys=rand_big_1)

    print("tree 2:")
    test_import(t=tree_2, keys=rand_big_2)

    print("joined tree:")
    tree_1.join(tree=tree_2, key=rand_node, val="")

    tree_1.printt()


def test_split(tree: AVLTree, keys = None, pivot_node_rank: int = -1):

    rand_small = create_rand_keys(n=50, start=0, end=500) if not keys else keys
    pivot_node_rank = create_rand_keys(n=1, start=0, end=len(rand_small)) if pivot_node_rank == -1 else pivot_node_rank
    sorted_rand_small = sorted(rand_small)

    print(f"tested list: {rand_small}")
    print(f"tested list (sorted): {sorted_rand_small}")

    test_import(t=tree, keys=rand_small)

    rand_node = tree.select(i=pivot_node_rank)
    print(f"split node: {rand_node}")

    split_trees = tree.split(node=rand_node)

    print(DIVIDER)

    print(f"expected values in tree: {sorted_rand_small[:pivot_node_rank]}")
    split_trees[0].printt()

    print(DIVIDER)
    print(f"expected values in tree: {sorted_rand_small[pivot_node_rank:]}")
    split_trees[1].printt()

    print(DIVIDER)

# test_split(tree=t1)


# test_join(tree_1=t1, tree_2=t2, tree_1_keys=test_join_left, tree_2_keys=test_join_right, pivot_node_key=328)

exception_list = {128, 129, 138, 139, 270, 16, 273, 275, 149, 22, 153, 158, 415, 288, 416, 418, 293, 166, 165, 295, 429, 50, 180, 186, 315, 59, 58, 66, 452, 197, 201, 204, 77, 333, 463, 208, 465, 211, 469, 95, 352, 97, 354, 226, 99, 358, 486, 491, 375, 122}

test_split(tree=t1, keys=exception_list, pivot_node_rank=16)
