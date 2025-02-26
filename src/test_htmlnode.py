import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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

class TestParentNode(unittest.TestCase):
    def test_parent_with_mixed_children(self):
        parent = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode("p", [LeafNode("i", "Italic text")])
            ]
        )
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_node_empty_children_list(self):
        parent = ParentNode("div", [])
        self.assertRaises(ValueError, parent.to_html)

    def test_parent_node_empty_tag(self):
        child_node = LeafNode("span", "child")
        parent = ParentNode(None, [child_node])
        self.assertRaises(ValueError, parent.to_html)
    
    def test_parent_node_empty_string_tag(self):
        child_node = LeafNode("span", "child")
        parent = ParentNode("", [child_node])
        self.assertRaises(ValueError, parent.to_html)
 


if __name__ == "__main__":
    unittest.main()