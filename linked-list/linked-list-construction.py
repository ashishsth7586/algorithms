"""
A linked list is a linear data structure where each element is a 
seperate object. Each element (refered to as Node) of a list
comprises two items - the data and a reference to the next node.
The last node has a reference to null. The entry point into a 
linked list is called the head of the list. 

A linked list is a dynamic data structure. The number of nodes in a
list is not fixed and can grow or shrink on demand. Any application
to deal with an unknown number of objects will need to use a 
linked list.

Disadvantage:
A linked list does not allow direct access to the individual
elements. If we want to access a particular item then we have to 
start at the head and follow the references until we get to that item,
"""

# Implementation various operations on DoublyLinkedList

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def setHead(self, node):
		"""
		Time Complexity: O(1)
		Space Complexity: O(1)
		"""
		if self.head is None:
			self.head = node
			self.tail = node
			return
		self.insertBefore(self.head, node)

	def setTail(self, node):
		"""
		Time Complexity: O(1)
		Space Complexity: O(1)
		"""
		if self.tail is None:
			self.setHead(node)
			return
		self.insertAfter(self.tail, node)

	def insertBefore(self, node, nodeToInsert):
		"""
		Time Complexity: O(1)
		Space Complexity: O(1)
		"""
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert

	def insertAfter(self, node, nodeToInsert):
		"""
		Time Complexity: O(1)
		Space Complexity: O(1)
		"""
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

	def insertAtPosition(self, position, nodeToInsert):
		"""
		Time Complexity: O(position)
		Space Complexity: O(1)
		"""
		if position == 1:
			self.setHead(nodeToInsert)
			return
		node = self.head
		currentPosition = 1
		while node is not None and currentPosition != position:
			node = node.next
			curentPosition += 1
		if node is not None:
			self.insertBefore(node, nodeToInsert)
		else:
			self.setTail(nodeToInsert)

	def removeNodesWithValue(self, value):
		"""
		Time Complexity: O(n)
		Space Complexity: O(1)
		"""
		node = self.head
		while node is not None:
			nodeToRemove = node
			node = node.next
			if nodeToRemove.value == value:
				self.remove(nodeToRemove)


	def remove(self, node):
		"""
		Time Complexity: O(1)
		Space Complexity: O(1)
		"""
		if node == self.head:
			self.head = self.head.next
		if node == self.tail:
			self.tail = self.tail.prev
		# Null <-- 1 --> Null
		self.removeNodeBindings(node)

	def conainsNodeWithValue(self, value):
		"""
		Time Complexity: O(n)
		Space Complexity: O(1)
		"""
		node = self.head
		while node is not None and node.value != value:
			node = node.next

		return node is not None

	def removeNodeBindings(self, node):
		"""
		Here the order is very important!!!
		"""
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev = None
		node.next = None





