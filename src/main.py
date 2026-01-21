from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():

	node = TextNode("My name is Optimus Prime", TextType.BOLD)
	print(node)
	htmlnode = HTMLNode("a", "Click me", None, {"href": "https://boot.dev", "target": "_blank"})
	print(htmlnode)
	print(htmlnode.props_to_html())

main()
