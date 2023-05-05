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


def test_split(tree: AVLTree):
    rand_small = create_rand_keys(n=50, start=0, end=500)

    exception_set = {131, 387, 259, 389, 265, 138, 267, 406, 407, 283, 28, 157, 159, 416, 164, 421, 423, 298, 428, 430, 303, 176, 182, 439, 56, 189, 317, 325, 455, 328, 74, 458, 204, 333, 205, 83, 473, 219, 476, 93, 479, 351, 482, 357, 235, 363, 494, 374, 247, 121}

    print(f"tested list (sorted): {sorted(exception_set)}")
    test_import(t=tree, keys=exception_set)
    rand_node = tree.select(i=23)

    print(f"split node: {rand_node}")
    split_trees = tree.split(node=rand_node)

    print(DIVIDER)

    split_trees[0].printt()

    print(DIVIDER)

    split_trees[1].printt()

    print(DIVIDER)

# test_split(tree=t1)


# test_join(tree_1=t1, tree_2=t2, tree_1_keys=test_join_left, tree_2_keys=test_join_right, pivot_node_key=328)
test_split(tree=t1)
[28, 56, 74, 83, 93, 121, 131, 138, 157, 159, 164, 176, 182, 189, 204, 205, 219, 235, 247, 259, 265, 267]