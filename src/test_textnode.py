import unittest
from htmlnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("Wikipedia", TextType.PLAIN, "wikipedia.org")
        node2 = TextNode("Wikipedia", TextType.PLAIN, "wikipedia.org")
        self.assertEqual(node, node2)

    def test_not_eq_diff_text(self):
        node = TextNode("Soundwave superior", TextType.CODE)
        node2 = TextNode("Soundwave superb", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_not_eq_diff_type(self):
        node = TextNode("Arise, ye Tarnished", TextType.ITALIC)
        node2 = TextNode("Arise, ye Tarnished", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()
