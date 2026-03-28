import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_is_None(self):
        node = HTMLNode("p", "this is a paragraph")
        node2 = HTMLNode("p", "this is a paragraph", "children")
        self.assertEqual(node.props_to_html(), "")
        self.assertEqual(node2.props_to_html(), "")

    def test_one_prop(self):
        node = HTMLNode("p", "this is a paragraph", "children", {"href":"https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_two_prop(self):
        node = HTMLNode("p", "this is a paragraph", "children", {"href":"https://www.google.com", "target":"_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_to_html_a_with_prop(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "this is plain text")
        self.assertEqual(node.to_html(), "this is plain text")

if __name__ == "__main__":
    unittest.main()