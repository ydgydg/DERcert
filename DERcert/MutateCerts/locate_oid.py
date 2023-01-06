def hex_to_bin(h):
    '''
    function:The hexadecimal is converted to binary
    :param h: Data to be converted
    :return: The converted data
    '''
    r = []
    for i in h:
        r.append(bin(int(i, 16))[2:].zfill(4))
    return "".join(r)

def find_oid_node(nodes: [dict], value) -> (dict, int, int):
    '''
    function:Locating OID Data
    :param nodes: Digital certificate tree node
    :param value: OID need to be located like 551d0f
    :return: The OID data is located
    '''
    find_bin = hex_to_bin(value)
    for _n in nodes:
        # print(_n.get("node-value"))
        # print("".join(_n.get("node-value")))
        node_v = "".join(_n.get("node-value"))
        if find_bin in node_v:
            index = node_v.index(find_bin)

            start = index - 4 * 8
            len_index = start + 1 * 8
            len_bin = node_v[len_index: len_index + 1 * 8]
            len_int = int(len_bin, 2)
            end = len_index + 1 * 8 + (len_int * 8)
            # print(len_bin)
            # print(node_v)
            return _n, start // 8, end // 8


def parse_oid(parent, nodes: list):
    '''
    function:Parse the OID into a tree structure
    :param parent: Parent node
    :param nodes: OID node
    :return:
    '''
    oid_node = []
    oid_edge = []
    if nodes is None or nodes == []:
        return
    for n in nodes:
        oid_node.append((n["node-id"], n["value"]))
    if parent is not None:
        for n in nodes:
            oid_edge.append((parent, n["node-id"]))
    for n in nodes:
        if n.get("children") not in (None, []):
            parse_oid(n["node-id"], n.get("children"))



