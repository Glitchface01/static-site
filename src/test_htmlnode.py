import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank"
        })

        result = node.props_to_html()
        possible_results = [
            ' href="https://www.google.com" target="_blank"',
            ' target="_blank" href="https://www.google.com"'
        ]
        self.assertIn(result, possible_results)

if __name__ == "__main__":
    unittest.main()

#  OR

#import unittest
#from htmlnode import HTMLNode


#class TestHTMLNode(unittest.TestCase):
#    def test_to_html_props(self):
#        node = HTMLNode(
#            "div",
#            "Hello, world!",
#            None,
#            {"class": "greeting", "href": "https://boot.dev"},
#        )
#        self.assertEqual(
#            node.props_to_html(),
#            ' class="greeting" href="https://boot.dev"',
#        )

#    def test_values(self):
#        node = HTMLNode(
#            "div",
#            "I wish I could read",
#        )
#        self.assertEqual(
#            node.tag,
#            "div",
#        )
#        self.assertEqual(
#            node.value,
#            "I wish I could read",
#        )
#        self.assertEqual(
#            node.children,
#            None,
#        )
#        self.assertEqual(
#            node.props,
#            None,
#        )

#    def test_repr(self):
#        node = HTMLNode(
#            "p",
#            "What a strange world",
#            None,
#            {"class": "primary"},
#        )
#        self.assertEqual(
#            node.__repr__(),
#            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
#        )


#if __name__ == "__main__":
#    unittest.main()