class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value #value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children #children of this node
        self.props = props #dictionary representing the attributes of the HTML tag.
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Value is empty")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"