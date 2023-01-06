from ParseCerts.derdumper import DERdumper as dp

import uuid
import copy
import json

der = dp


def to_binary(data):
    '''
    function:Convert to binary
    :param data: Data to be converted
    :return: Convert the successful eight bits binary number
    '''
    return bin(data).replace("0b", "").zfill(8)


def deep_copy(data):
    '''
    function:Copy data
    :param o: Data to be copied
    :return: Copied data
    '''
    return json.loads(json.dumps(data))


def dump(data):
    '''
    function:Parses digital certificate data
    :param data:Digital certificate data
    :return: Node of tree
    '''
    valuelst = []
    tree = []
    index = 0
    while index < len(data) - 1:

        ret = der().is_constructed(data, index)

        tagtup = der().get_tag(data, index)
        # print(tagtup[0])
        index = index + 1

        lengthtup = der().get_length(data, index)

        index = index + lengthtup[1]

        value = data[index:index + lengthtup[0]]
        if ret:
            temp = {
                "node-id": str(uuid.uuid4()),
                "tag": tagtup[0],
                "p-node-id": None,
                "length": lengthtup[0],
                "children": dump(value),
                "isNode": False,
                "value": f"T:{tagtup[0]}  |  L:{to_binary(lengthtup[0])}  |  []"
            }
            tree.append(temp)
        else:
            # print(value)
            temp = {
                "node-id": str(uuid.uuid4()),
                "tag": tagtup[0],
                "p-node-id": None,
                "length": lengthtup[0],
                "children": [],
                "isNode": True,
                "node-value": value,
                "value": f"T:{tagtup[0]}  |  L:{to_binary(lengthtup[0])}  |  V:{value}",
            }
            tree.append(temp)
            valuelst.append(value)
        index = index + lengthtup[0]
    return tree

edge = []
node = []





