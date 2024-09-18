#!/usr/bin/python3
"""
This module provides the class definitions for Node and SinglyLinkedList

"""


class Node:
    """
    Class definition for a Node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node with the given data and
        a reference to the next node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): A reference to the next node
            in the list (default is None).

        Raises:
            TypeError: If data is not an integer.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Validates and sets the data of the node.

        Args:
            value (int): The new data to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """
        Retrieves the next node in the list.

        Returns:
            Node: The next node in the list, or None if there is no next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Validates and sets the next node reference.

        Args:
            value (Node): The next node to reference, or None.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    Class definition for a singly linked list.

    Private Attributes:
        __head (Node): A reference to the first node of the linked list.
    """

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the singly linked list.

        The string contains the data from each node in the list, with each
        node's data printed on a new line.

        Returns:
            str: A string representation of the list,
            with each node's data on a new line.
        """
        retVal = []
        current_node = self.__head
        while current_node is not None:
            retVal.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(retVal)

    def sorted_insert(self, value):
        """
        Inserts a new node into the correct sorted position
        in the list (increasing order).

        Args:
            value (int): The data value for the new node.

        Raises:
            TypeError: If value is not an integer.

        The list is sorted in increasing order, and this method
        ensures the new node is inserted into its correct position
        based on the value of the data.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an int")

        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current_node = self.__head
        while (
            current_node.next_node is not None and
            current_node.next_node.data < value
        ):
            current_node = current_node.next_node

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
