import random
from AVLTree_theory_experiment_q2 import AVLTree, AVLNode

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


def test_import(t: AVLTree, keys = None, multiple_prints: bool = False, with_printing: bool = True):
    rand_small = create_rand_keys(n=50, start=0, end=500) if not keys else keys
    # print("done building rand_small")
    for key in rand_small:
        t.insert(key=key, val="")
        if multiple_prints and with_printing:
            t.printt()
            print(DIVIDER)

    if with_printing and not multiple_prints:
        t.printt()
        print(DIVIDER)
    print(f"\nORIGIN\nMin: {t.min} | Max: {t.max}")
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


def test_split(tree: AVLTree, keys = None, pivot_node_rank: int = -1, is_random_split = True):
    n = 1500*(2**1)
    rand_small = create_rand_keys(n=n, start=0, end=n) if not keys else keys
    pivot_node_rank = create_rand_keys(n=1, start=0, end=len(rand_small)) if pivot_node_rank == -1 else pivot_node_rank
    sorted_rand_small = sorted(rand_small)

    test_import(t=tree, keys=rand_small, with_printing=False)

    print(f"tested list: {rand_small[-10:]}")
    #print(f"tested list (sorted): {sorted_rand_small}")

    rand_node = tree.select(i=pivot_node_rank) if is_random_split else tree.predecessor(tree.root)
    print(f"tree's root {tree.root}")
    print(f"split node: {rand_node}")

    joins_data = tree.split(node=rand_node)

    joins_costs_arr = joins_data[0]
    num_join_run = joins_data[1]

    # MEAN COST
    mean_cost = sum(joins_costs_arr) / num_join_run

    # MAX COST
    max_cost = max(joins_costs_arr)

    print(DIVIDER)

    # print("T_LEFT")
    # print(sorted_rand_small[:pivot_node_rank - 1])
    # print(f"Min: {split_trees[0].min} | Max: {split_trees[0].max}")
    # split_trees[0].printt()

    print(DIVIDER)

    # print("T_RIGHT")
    # print(sorted_rand_small[pivot_node_rank:])

    print(f"joins_costs_arr {joins_costs_arr}")
    print(f"Mean cost: {mean_cost} | Max cost: {max_cost}  | d: {num_join_run}")
    # split_trees[1].printt()

    print(DIVIDER)
    print(DIVIDER)
    return rand_small


def test_BST_delete(tree: AVLTree, pivot_node_rank: int = -1, keys = None):
    rand_small = create_rand_keys(n=50, start=0, end=500) if not keys else keys
    test_import(t=tree, keys=rand_small, with_printing=False)
    print(f"tested list: {rand_small}")

    if pivot_node_rank == -1:
        pivot_node_rank = create_rand_keys(n=1, start=0, end=len(rand_small))
        pivot_node_delete =  tree.select(i=pivot_node_rank)
    else:
        pivot_node_delete = tree.select(i=pivot_node_rank)

    print(f"node to delete: {pivot_node_delete}")
    print(DIVIDER)
    print(f"tree before BST_delete:")

    tree.printt()

    print(DIVIDER)


    need_rebalance_from = tree.BST_delete(pivot_node_delete)

    print(DIVIDER)
    print("tree after BST_delete:")
    tree.printt()


def test_delete(tree: AVLTree, pivot_node_rank: int = -1, keys = None):
    rand_small = create_rand_keys(n=50, start=0, end=500) if not keys else keys
    test_import(t=tree, keys=rand_small, with_printing=False)
    print(f"tested list: {rand_small}")

    if pivot_node_rank == -1:
        pivot_node_rank = create_rand_keys(n=1, start=0, end=len(rand_small))
        pivot_node_delete =  tree.select(i=pivot_node_rank)
    else:
        pivot_node_delete = tree.select(i=pivot_node_rank)

    print(f"node to delete: {pivot_node_delete}")

    print(DIVIDER)

    print(f"tree BEFORE delete:")
    # tree.printt()

    print(DIVIDER)

    tree.delete(node=pivot_node_delete)

    print(f"tree AFTER delete:")
    # tree.printt()


exception_list = {385, 130, 261, 135, 145, 146, 401, 20, 277, 273, 23, 149, 408, 155, 412, 158, 160, 288, 291, 168, 297, 437, 441, 317, 319, 63, 196, 454, 71, 199, 455, 326, 337, 82, 339, 212, 468, 86, 216, 348, 223, 97, 104, 107, 108, 110, 367, 241, 379, 380}

# test_import(t=t1, keys=exception_list)

#while True:
    #test_split(tree=t1)
    #test_import(t=t1)
    # print(f"Min: {t1.min} | Max: {t1.max}")
    #t1 = AVLTree()
t1 = AVLTree()
t2 = AVLTree()
rand_small = []
n = 1500*(2**10)
for i in range(1, n+1):
    rand_small.append(i)
random.shuffle(rand_small)

same = test_split(tree=t1, keys=rand_small)
print(same[-10:])
test_split(tree=t2,keys=same,is_random_split=False)