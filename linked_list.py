class Node:
	"""
	An object for storing a single node of a linked list,
	Models two attributes - data and the link to the next
	node in the list
	"""
	data = None
	next_node = None

	def __init__(self, data):
		self.data = data

	def __repr__(self):
		return "<Node data: %s> " % self.data

class LinkedList:
	"""
		Singly linked list
	"""
	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head == None

	def size(self):
		"""
			Returns the number of node in the list
			Takes O(n) time
		"""
		current = self.head
		count = 0

		while current:
			count += 1
			current = current.next_node

		return count

	def add(self, data):
		"""
			Adds a new Node containing data at head of the list
			Takes O(1) time
		"""
		new_node = Node(data)
		# we need to keep the reference to the old head of the linked list
		new_node.next_node = self.head
		self.head = new_node

	def search(self, key):
		"""
			Sear for the first node containng data that matches the key
			Return the node or 'None ' if ont found

			Takes O(n) time
		"""

		current = self.head

		while current:
			if current.data == key:
				return current
			else:
				current = current.next_node

		return None

	def insert(self, data, index):
		"""
			Insert a new Node containning data at index position
			Insertion takes O(1) time but finding the node at the insertion
			point takes O(n) time.

			Takes overall O(n) time
		"""
		if index == 0:
			self.add(data)

		if index > 0:
			new = Node(data)

			position = index
			current = self.head

			while position > 1:
				current = current.next_node
				position -= 1

			prev_node = current
			next_node = current.next_node

			prev_node.next_node = new
			new.next_node = next_node

	def remove(self, key):
		"""
			Removes Node containing data that matches the key
			Returns the node or None if key doesn't exist
			Takes O(n) time
		"""
		current = self.head
		previous = None
		found = False

		while current and not found:
			if current.data == key and current is self.head:
				found = True
				self.head = current.next_node
			elif current.data == key:
				found = True
				previous.next_node = current.next_node
			else:
				previous = current
				current = current.next_node

		return current

	def remove_at_index(self, index):
		"""
			Removes Node at a given index
			Returns the node or None if index is out of range
			We need to confirm the size of the linked list so that takes O(n)
			The transversal search also takes O(n) and the remove node takes O(1)
		"""
		if index > self.size():
			return None

		current = self.head
		position = index

		if index == 0:
			self.head = current.next_node
			return current

		if index > 0:
			while position > 0 and current:
				previous_node = current
				current = current.next_node
				position -= 1

			previous_node.next_node = current.next_node
			current.next_node = None

			return current

		


	def __repr__(self):
		"""
			Rtunr a string represetnation of the list
			Takes O(n) time
		"""

		nodes = []
		current = self.head

		while current:
			if current is self.head:
				nodes.append("[Head: %s]" % current.data)
			elif current is None:
				nodes.append("Tail: %s" % current.data)
			else:
				nodes.append("[%s]" % current.data)

			current = current.next_node

		return ' => '.join(nodes)

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(14)
l.add(45)
n = l.search(14)
l.insert(13, 2)
print(l)
removed = l.remove_at_index(3)
print(removed, 'none')
print(n)
print(l)
