import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
        

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)
        
    def test_link_in_image(self):
        node = TextNode("this is an image", TextType.IMAGE_TEXT, "https://www.image.com")
        node2 = TextNode("this is an image", TextType.IMAGE_TEXT, "https")
        self.assertIsNotNone(node.url)
        self.assertIsNotNone(node2.url)

    def test_link_not_in_image(self):
        node = TextNode("this is an image", TextType.IMAGE_TEXT)
        node2 = TextNode("this is an image", TextType.IMAGE_TEXT)
        self.assertIsNone(node.url)
        self.assertIsNone(node2.url)

    

if __name__ == "__main__":
    unittest.main()