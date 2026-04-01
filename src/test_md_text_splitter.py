import unittest

from md_text_splitter import split_nodes_delimeter
from textnode import TextNode, TextType

class TestSplitNodesDelimeter(unittest.TestCase):
    def test_no_nodes_provided(self):
        old_nodes = []
        delimeter = "**"
        text_type = TextType.BOLD_TEXT
        self.assertRaises(Exception, split_nodes_delimeter, old_nodes, delimeter, text_type)

    def test_text_with_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimeter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.PLAIN_TEXT),
    TextNode("code block", TextType.CODE_TEXT),
    TextNode(" word", TextType.PLAIN_TEXT),
        ])

    def test_text_with_bold_block(self):
        node = TextNode("This is text with **bold** text_", TextType.PLAIN_TEXT) 
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.PLAIN_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text_", TextType.PLAIN_TEXT)
        ])



if __name__ == "__main__":
    unittest.main() 