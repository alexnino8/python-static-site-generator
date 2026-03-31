import unittest

from text_to_html_converter import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestConverter(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("this is a bold text node", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "this is a bold text node")

    def test_image(self):
        node = TextNode("this is the alt text", TextType.IMAGE_TEXT, "this is the link to the image")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "this is the link to the image")
        self.assertEqual(html_node.props["alt"], "this is the alt text")

    def test_invalid_text_type(self):
        node = TextNode("this is a text node", "Bold")
        self.assertRaises(BaseException, text_node_to_html_node, node)