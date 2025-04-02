import unittest

from textnode import TextNode, TextType, text_node_to_html_node, extract_markdown_images, extract_markdown_links 


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Here's a [link to a website](https://example.com)"
        )
        self.assertListEqual([("link to a website", "https://example.com")], matches)

    def test_multiple_links(self):
        text = "Here's [one link](https://example.com) and [another](https://test.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([
            ("one link", "https://example.com"),
            ("another", "https://test.com")
        ], matches)

    def test_no_links(self):
        matches = extract_markdown_links("This text has no links in it")
        self.assertListEqual([], matches)

    def test_multiple_images(self):
        text = "Here's ![one image](https://example.com/img1.jpg) and ![another](https://example.com/img2.jpg)"
        matches = extract_markdown_images(text)
        self.assertListEqual([
            ("one image", "https://example.com/img1.jpg"),
            ("another", "https://example.com/img2.jpg")
        ], matches)

    def test_no_images(self):
        matches = extract_markdown_images("This text has no images in it")
        self.assertListEqual([], matches)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")




if __name__ == "__main__":
    unittest.main()
