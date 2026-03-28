

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        sprops = ""
        if self.props is not None:
            for prop, val in self.props.items():
                sprops += f' {prop}="{val}"'
        return sprops
    
    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None: 
            raise ValueError()
        if not self.tag:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    
    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})" 