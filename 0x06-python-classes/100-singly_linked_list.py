#!/usr/bin/python3
"""Defines a class Node that creates a singly linked list"""


class Node:
    """Creates a node of a singly linked
    list."""

    def __init__(self, data, next_node=None):
        """Initialize a new_node
        Args:
            data: data part
            next_node: pointer to next node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get data part of the node"""
        return (self.__data)

    @data.setter
    def data(self, val):
        """Sets the data part of the node
        Args:
            val: the value to store at data"""
        if not isinstance(val, int):
            raise TypeError("data must be an integer")
        self.__data = val

    @property
    def next_node(self):
        """get the next node address"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, ptr):
        """Set the next node pointer
        Args:
            ptr: pointer to next node in the list"""
        if not isinstance(ptr, Node) and ptr is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = ptr


class SinglyLinkedList:
    """Defines a singly linked list from the Node class"""
    def __init__(self):
        """Initialize a new list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts new node in the list in a sorted way
        Args:
            value: the data part"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Modify the dunder str function to print readable data"""
        vals = []
        tmp = self.__head
        while tmp is not None:
            vals.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(vals))
