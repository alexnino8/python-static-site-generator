import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()