from realcel.color_tree import ColorTree

class TestColorTree:
    def test_it_converts_rgb_tuples_to_ints(self):
        tree = ColorTree()
        assert tree._color_to_node_value((0, 0, 255)) == 255
        assert tree._color_to_node_value((0, 255, 0)) == 255000
        assert tree._color_to_node_value((255, 0, 0)) == 255000000
        assert tree._color_to_node_value((1, 1, 1)) == 1001001

    def test_it_converts_ints_to_rgb_tuples(self):
        tree = ColorTree()
        assert tree._node_value_to_color(255) == (0, 0, 255)
        assert tree._node_value_to_color(255000) == (0, 255, 0)
        assert tree._node_value_to_color(255000000) == (255, 0, 0)
        assert tree._node_value_to_color(1001001) == (1, 1, 1)

    def test_it_adds_nodes_to_the_tree(self):
        tree = ColorTree()
        tree.append((0, 255, 255))
        tree.append((255, 100, 0))
        tree.append((255, 0, 0))
        tree.append((0, 0, 0))
        assert tree._node_value_to_color(tree.root.value) == (0, 255, 255)
        assert tree._node_value_to_color(tree.root.left.value) == (0, 0, 0)
        assert tree._node_value_to_color(tree.root.right.value) == (255, 100, 0)
        assert tree._node_value_to_color(tree.root.right.left.value) == (255, 0, 0)

    def test_it_creates_an_in_order_list(self):
        tree = ColorTree()
        tree.append((0, 255, 255))
        tree.append((255, 100, 0))
        tree.append((255, 0, 0))
        tree.append((0, 0, 0))
        assert tree.to_list() == [
            (0, 0, 0),
            (0, 255, 255),
            (255, 0, 0),
            (255, 100, 0),
        ]

    def test_it_does_not_duplicate_values(self):
        tree = ColorTree()
        tree.append((0, 255, 255))
        tree.append((0, 0, 0))
        tree.append((0, 0, 0))
        tree.append((0, 255, 255))
        tree.append((0, 0, 0))
        assert tree.to_list() == [
            (0, 0, 0),
            (0, 255, 255),
        ]

    def test_it_searches_for_existing_values(self):
        tree = ColorTree()
        values = [
            (0, 255, 255),
            (0, 0, 0),
            (255, 100, 0),
            (255, 0, 0),
        ]
        for value in values:
            tree.append(value)
        for value in values:
            assert tree.has(value)
        assert not tree.has((100, 100, 100))
        assert not tree.has((255, 255, 255))

    def test_searching_an_empty_tree_returns_false(self):
        tree = ColorTree()
        assert not tree.has((0, 0, 0))
