from random import choice, choices
import uuid
import copy
import json
from MutateCerts.back_repair import change_length
from MutateCerts.back_repair import repair_tag
def to_binary(data):
    '''
    function:Convert the data into binary
    :param data: Data to be converted
    :return: The converted data
    '''
    return bin(data).replace("0b", "").zfill(8)

def deep_copy(data):
    '''
    function:Copy data
    :param data: Data to be copied
    :return: Copied data
    '''
    return json.loads(json.dumps(data))

def solve_tree(nodes: list, result_list, parent_node_id):
    '''
    function:Parse the digital certificate into a tree structure
    :param data: Data of the digital certificate
    :param nodes: List of nodes
    :param result_list: List of results
    :param parent_node_id: ID of the parent node
    '''
    # if data is None or data == []:
    #     return
    for n in nodes:
        if parent_node_id is not None:
            n["p-node-id"] = parent_node_id
        result_list.append(n)
    for n in nodes:
        if n.get("children") not in (None, []):
            solve_tree(n.get("children"), result_list, n["node-id"])

# Function of mutate
def change_value(node,_node):

    '''
    function:change value
    :param: List of node
    :param: _node: The node to be mutated
    '''
    _node["node-value"][-1] = "11111111"
    _node["value"] = f'T:{_node["tag"]}  |  L:{to_binary(int(_node["length"]))}  |  V:{_node["node-value"]}'
    _node["node-value"].append('00000001')
    change_length(node, _node["node-id"], -1)

def change_value_norepair(_node):
    _node["node-value"][-1] = "11111111"
    _node["node-value"].append('00000001')
    _node["value"] = f'T:{_node["tag"]}  |  L:{to_binary(int(_node["length"]))}  |  V:{_node["node-value"]}'

def delete(node,_node):
    '''
    function:Deleting a value
    :param node: List of node
    :param _node: The node to be mutated
    '''
    _node["node-value"] = _node["node-value"][:-1]
    _node["value"] = f'T:{_node["tag"]}  |  L:{to_binary(int(_node["length"]))}  |  V:{_node["node-value"]}'
    change_length(node, _node["node-id"], -1)
    repair_tag(node,_node)

def delete_norepair(_node):
    '''
    function:Deleting a value without repair
    :param data: List of data
    :param _node: The node to be mutated
    '''
    _node["node-value"] = _node["node-value"][:-1]
    _node["value"] = f'T:{_node["tag"]}  |  L:{to_binary(int(_node["length"]))}  |  V:{_node["node-value"]}'


def add(node,_node, _newValue):
    '''
    function:Value added
    :param data: List of data
    :param _node: The node to be mutated
    :param _newValue: The value of the variation
    '''
    _node["node-value"].append(_newValue)
    _node["value"] = f'T:{_node["tag"]}  |  L:{to_binary(int(_node["length"]))}  |  V:{_node["node-value"]}'
    change_length(node, _node["node-id"], +1)

def add_nopair(_node, _newValue):
    '''
    function:Value added without repair
    :param data: List of data
    :param _node: The node to be mutated
    :param _newValue: The value of the variation
    '''
    _node["node-value"].append(_newValue)
    _node["value"] = f'T:{_node["tag"]}  |  L:{to_binary(int(_node["length"]))}  |  V:{_node["node-value"]}'

def exchange(data,_node1, _node2):
    '''
    function:Exchange of nodes
    :param data: List of data
    :param _node1: Node 1 of the swap
    :param _node2: Node 2 of the swap
    '''
    node_1_length = _node1["length"]
    node_2_length = _node2["length"]
    node_1_change_length = node_2_length - node_1_length
    node_2_change_length = node_1_length - node_2_length
    _node1["tag"], _node2["tag"] = _node2["tag"], _node1["tag"]
    _node1["node-value"], _node2["node-value"] = _node2["node-value"], _node1["node-value"]
    change_length(data, _node1["node-id"], node_1_change_length)
    change_length(data, _node2["node-id"], node_2_change_length)

def exchange_nopair(_node1, _node2):
    '''
    function:Exchange of nodes without repair
    :param data: List of data
    :param _node1: Node 1 of the swap
    :param _node2: Node 2 of the swap
    '''
    node_1_length = _node1["length"]
    node_2_length = _node2["length"]
    node_1_change_length = node_2_length - node_1_length
    node_2_change_length = node_1_length - node_2_length
    _node1["tag"], _node2["tag"] = _node2["tag"], _node1["tag"]
    _node1["node-value"], _node2["node-value"] = _node2["node-value"], _node1["node-value"]

def partiation(l:str, n = 8):
    '''
    function:Every eight bits of binary is combined into an element
    :param l: String
    :param n: Default parameter 8 bits
    :return: Result list
    '''
    # print(l)
    _result = []
    _item_list = []
    for _i in l:
        _item_list.append(_i)
        if len(_item_list) == n:
            _result.append("".join(_item_list))
            _item_list = []
    if len(_item_list) > 0:
        _result.append("".join(_item_list))
    return _result

def result_to_binary(final_result: list):
    '''
    function: Save node data as binary data
    :param: final_result:Node list
    :return: The list of data
    '''
    def read(r: list, all_result):
        if r is None or r == []:
            return
        for i in r:
            _node_v = i.get("node-value")
            _node_tag = i.get("tag")
            all_result.append(_node_tag)
            _node_length = i.get("length")
            for item in partiation(to_binary(_node_length)):
                all_result.append(item)

            if _node_v is not None:
                for v in _node_v:
                    all_result.append(v)
            # all_result.append(_node_length)
            children = i.get("children", None)
            if children is not None and children != []:
                read(children, all_result)
    _r = []
    read(final_result, _r)
    return _r
