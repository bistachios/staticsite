import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", None, {"class": "text", "id": "intro"})
        node2 = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        node3 = HTMLNode("p", "This is a paragraph", None, {"title": "text"})
        node.props_to_html()
        node2.props_to_html()
        node3.props_to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()
