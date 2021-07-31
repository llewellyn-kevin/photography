class ColorTree:
    """Simple binary tree implementation for storing rgb color values.

    This tree has not been fully optimized, having a somewhat lengthy encoding process for
    all the values before being stored and is not self-balancing. But it does guarantee no
    duplicate entries and that the list will be sorted.
    """

    def __init__(self):
        self.root = None

    def append(self, value: tuple):
        """Recursively adds the value to the tree if it has not already been added."""

        encoded_value = self._color_to_node_value(value)
        if self.root is None:
            self.root = ColorNode(encoded_value)
        else:
            self.root.append(encoded_value)

    def has(self, needle: tuple) -> bool:
        """Determines if the tree has the given value."""

        if self.root is None:
            return False
        encoded_needle = self._color_to_node_value(needle)
        return self.root.find(encoded_needle)

    def to_list(self) -> list:
        """Creates a decoded list based on in order traversal of the tree."""

        if self.root is None:
            return []
        decoded_values = []
        for i in self.root.traverse([]):
            decoded_values.append(self._node_value_to_color(i))
        return decoded_values

    # Converts a tuple holding RGB values to an integer for storage in a tree.
    def _color_to_node_value(self, color: tuple) -> int:
        return color[0] * 10 ** 6 + color[1] * 10 ** 3 + color[2]

    # Converts an integer from the tree into a node containing RGB information.
    def _node_value_to_color(self, value: int) -> tuple:
        return (
            int(value / 10 ** 6),
            int(value % 10 ** 6 / 10 ** 3),
            int(value % 10 ** 3)
        )

class ColorNode:
    """Represents a node on a ColorTree.

    Stored values are encoded integers representing RGB tuples.
    """

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def append(self, value: int):
        """Adds a new child with the given value if necessary.

        Determines if the value should be passed on the left or right side and appends to the child if present,
        otherwise makes a new child with the given value. If the value is equal to this node it is discarded.
        """

        if value < self.value:
            if self.left is None:
                self.left = ColorNode(value)
            else:
                self.left.append(value)
        elif value > self.value:
            if self.right is None:
                self.right = ColorNode(value)
            else:
                self.right.append(value)

    def find(self, needle: int) -> bool:
        """Recursive search for a value on this node or its children.

        Truthy if the needle is equal to this nodes value. Otherwise it passes the check to its child.
        If no child is present on the proper side, the method is falsey.
        """

        if self.value == needle:
            return True
        elif self.value > needle:
            return False if self.left is None else self.left.find(needle)
        return False if self.right is None else self.right.find(needle)

    def traverse(self, items: list) -> list:
        """Does an in order traversal of all connected nodes and adds them to the provided list."""

        if self.left is not None:
            self.left.traverse(items)
        items.append(self.value)
        if self.right is not None:
            self.right.traverse(items)
        return items
