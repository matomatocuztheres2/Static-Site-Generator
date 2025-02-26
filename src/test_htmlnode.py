import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
class TestLeafNode(unittest.TestCase):
    def test_to_leaf_multi_props(self):
        node = LeafNode(
        "div",
            "Hello, world!",
            {"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="greeting" href="https://boot.dev">Hello, world!</div>'
        )
    
    def test_to_leaf_error(self):
        node = LeafNode(
        "div",
            ""
        )
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_raw(self):
        node = LeafNode(None, "This is what should print out")
        self.assertEqual(
            node.to_html(),
            'This is what should print out'
        )
    
    def test_to_leaf_props(self):
        node = LeafNode(
        "div",
            "Hello, world!",
            {"href": "https://boot.dev"}
        )
        self.assertEqual(
            node.to_html(),
            '<div href="https://boot.dev">Hello, world!</div>'
        )
 


if __name__ == "__main__":
    unittest.main()