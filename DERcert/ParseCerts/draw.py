edge = []
node = []

def draw(data,final_result, fname):
    '''
    function:Function of visualization
    :param data:Digital Certificate Data
    :param final_result: Node list
    :param fname: The name of the visual image
    '''
    def __solve(parent, nodes: list):
        if data is None or data == []:
            return
        for n in nodes:
            __node.append((n["node-id"], n["value"]))
        if parent is not None:
            for n in nodes:
                __edge.append((parent, n["node-id"]))
        for n in nodes:
            if n.get("children") not in (None, []):
                __solve(n["node-id"], n.get("children"))

    __edge = []
    __node = []

    __solve(None, final_result)
    from graphviz import Digraph

    g = Digraph(fname)


    for n in __node:
        g.node(name=n[0], label=n[1], shape="box")

    for e in __edge:
        g.edge(e[0], e[1])

    g.view()

