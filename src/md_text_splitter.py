from textnode import TextNode, TextType

def split_nodes_delimeter(old_nodes:list, delimeter, text_type) -> list:
    if len(old_nodes) < 1:
        raise Exception("no nodes provided for splitting")
    
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old_node)
            
        else:
            chunks = old_node.text.split(delimeter)
            nodes = []
            if len(chunks) % 2 == 0:
                raise Exception("invalid markdown")
            for i in range(len(chunks)):
                if i % 2 == 0 and chunks[i] != "":
                    nodes.append(TextNode(chunks[i], TextType.PLAIN_TEXT))
                elif i % 2 != 0 and chunks[i] != "":
                    nodes.append(TextNode(chunks[i], text_type))


            new_nodes.extend(nodes)
            
                

              

    return new_nodes
