import unittest

from extract_markdown_images_and_links import extract_markdown_links, extract_markdown_images

class TestExtractMarkdownImagesAndLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_images_multiple(self):
        text = "![Img1](url1.jpg) some text ![Img2](url2.png)"
        expected = [("Img1", "url1.jpg"), ("Img2", "url2.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_images_empty_alt(self):
        text = "![](https://example.com/no-alt.gif)"
        expected = [("", "https://example.com/no-alt.gif")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_images_ignores_regular_links(self):
        text = "This is a [link](https://google.com), not an image."
        self.assertEqual(extract_markdown_images(text), [])

        # --- tests for links ---

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is a text with a link [to boot dev](https://www.boot.dev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_links_multiple(self):
        text = "[Link1](url1) and [Link2](url2)"
        expected = [("Link1", "url1"), ("Link2", "url2")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_links_ignores_images(self):
        """
        Crucial test: ensure the negative lookbehind prevents 
        images from being detected as regular links.
        """
        text = "![alt](image_url) and [text](link_url)"
        expected = [("text", "link_url")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_links_empty_text(self):
        text = "[](https://anonymous-link.com)"
        expected = [("", "https://anonymous-link.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_no_matches(self):
        text = "This is just plain text with no special markdown."
        self.assertEqual(extract_markdown_images(text), [])
        self.assertEqual(extract_markdown_links(text), [])

    def test_malformed_markdown(self):
        # Missing closing parenthesis or brackets shouldn't match
        text = "![alt(url) [link](url"
        self.assertEqual(extract_markdown_images(text), [])
        self.assertEqual(extract_markdown_links(text), [])

if __name__ == "__main__":
    unittest.main()
