import avl_template_new as avl

def print_tree(node):
	if node is None:
		print("Empty tree!")
		return
	if (node.height > 0):
		print("value:",node.value, f'(Rank: {node.rank}, Height: {node.height})')
	if(node != None and node.left.rank != 0):
		print("left:", node.left.value, f'(Rank:{node.left.rank}, Height:{node.left.height})')
	if(node != None and node.right.rank != 0):
		print("right:", node.right.value, f'(Rank:{node.right.rank}, Height:{node.right.height})')
	if(node != None and node.left.rank != 0):
		print_tree(node.left)
	if(node != None and node.right.rank != 0):
		print_tree(node.right)


def build_tree(final_list, insert_list, index_order, P=True):
	
	avl_tree = avl.AVLTreeList()
	
	# Build tree - Insert test
	for i, val in enumerate(insert_list):
		avl_tree.insert(index_order[i], val)
	if P:
		print(f'----After insert final tree----')
		print_tree(avl_tree.root)
	print(avl_tree.listToArray())
	print(avl_tree.length())

	avl_tree_copy = avl_tree

	# Retrive test
	for i in range(len(final_list)):
		if(avl_tree.retrieve(i) != (final_list[i])):
			print(f'Error in retrieve test! i={i}: TreeNode value: {avl_tree.retrieve(i)}. List value (Real): {final_list[i]}.')
	print('Retrive Done')
	
	# Predecessor
	for i in range(len(final_list) - 1):
		if(avl_tree.retrieve_node(i+1).getPredecessor().value != (final_list[i])):
			print(f'Error in Predeccessor test! i={i+1}: TreeNode value: {avl_tree.retrieve_node(i+1).getPredecessor().value}. List value (Real): {final_list[i]}.')
	print('Predecessor Done')

	# Successor
	for i in range(len(final_list) - 1):
		if(avl_tree.retrieve_node(i).getSuccessor().value != (final_list[i+1])):
			print(f'Error in Successor test! i={i}: TreeNode value: {avl_tree.retrieve_node(i).getSuccessor().value}. List value (Real): {final_list[i+1]}.')
	print('Successor Done')

	# First and Last
	if (avl_tree.first() != final_list[0]):
		print(f'Error in First Test!: TreeNode value: {avl_tree.first()}. List value (Real): {final_list[0]}.')
	if (avl_tree.last() != final_list[-1]):
		print(f'Error in Last Test!: TreeNode value: {avl_tree.last()}. List value (Real): {final_list[-1]}.')
	print('First and Last Done')

	# Delete
	delete_list = final_list

	for i in range(4):
		delete_ind = 2
		delete_list.pop(delete_ind)
		avl_tree.delete(delete_ind)
		if P:
			print(f'\n****After delete {i} tree*****')
			print_tree(avl_tree.root)

		for i in range(len(delete_list)):
			if(avl_tree.retrieve(i) != (delete_list[i])):
				print(f'Error in delete test! i={i}: TreeNode value: {avl_tree.retrieve(i)}. List value (Real): {delete_list[i]}.')
	
	print(f'\n---After All delete tree---')
	print_tree(avl_tree.root)

	# Permutation
	for i in range(1):
		print(f'--------perm tree {i}----------')
		perm_tree = avl_tree_copy.permutation()
		# print_tree(perm_tree.getRoot())
		print(perm_tree.listToArray())

	# Sort tree
	print(f'====== sorted tree =========')
	b = perm_tree.sort()
	print_tree(b.getRoot())
	print(b.listToArray())

def test_concat():
	lst = avl.AVLTreeList()
	self = avl.AVLTreeList()
	letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
	for i in range (4,-1,-1):
		self.insert(0, letters[i])
	print("------------- lst --------------")
	# print_tree(self.getRoot())
	# for i in range (7,4,-1):
	# 	lst.insert(0,letters[i])
	print("------------- self --------------")
	# print_tree(lst.getRoot())


	print("------------- concat function --------------")
	first = lst
	sec = self
	print("first:",first.listToArray())
	print("second:",sec.listToArray())
	print("correct:",first.listToArray() + sec.listToArray())
	print(first.concat(sec))
	print("------------- concated --------------")
	print("concated:",first.listToArray())
	first.print_tree(first.root)

build_tree(['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['G', 'F', 'E', 'D', 'C', 'B', 'A'], [0 for _ in range(7)], True)
build_tree(['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['C', 'D', 'A', 'B', 'E', 'G', 'F'], [0, 1, 0, 1, 4, 5, 5], True)
build_tree(['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['C', 'A', 'B', 'E', 'D', 'G', 'F'], [0, 0, 1, 3, 3, 5, 5], True)
build_tree(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], ['F', 'H', 'G', 'E', 'A', 'B', 'C', 'D'], [0, 1, 1, 0, 0, 1, 2, 3], True)


print("---Finish----")
