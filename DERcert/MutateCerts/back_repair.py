def to_binary(n):
    '''
    function:Convert to binary
    :param n: Data to be converted
    :return: Convert the successful eight bits binary number
    '''
    return bin(n).replace("0b", "").zfill(8)

def change_length(node_list, node_id, change_num=0):
    # Recursive termination condition
    '''
    function:Recursively fixes the length of the function
    :param node_list: Tree node list
    :param node_id: Tree Node ID
    :param change_num: Default change length
    :return: The node whose length has been modified
    '''
    if node_id is None:
        return
    # find node
    current_node = None
    for node in node_list:
        if node_id == node["node-id"]:
            current_node = node
            break
    # fix current code length
    current_node["length"] = current_node["length"] + change_num
    # show information
    # if current node is leaf
    if current_node["isNode"]:
        current_node[
            "value"] = f'T:{current_node["tag"]}  |  L:{to_binary(int(current_node["length"]))}  |  V:{current_node["node-value"]}'
    else:
        current_node["value"] = f'T:{current_node["tag"]}  |  L:{to_binary(int(current_node["length"]))}  |  []'
    # backrepair
    change_length(node_list, current_node["p-node-id"], change_num=change_num)

def repair_tag(node_list,node_id):
    '''
    function:Repair tag
    :param node_list: Tree node list
    :param node_id: Tree Node ID
    :return: The node that tag has been modified
    '''
    current_node = None
    for n in node_list:
        if n.get("node-id") == node_id:
            current_node = n
            break
    if current_node is None:
        return
    if not current_node.get("children",[]):
        current_node["tag"] = current_node["tag"][:2] + "0" + current_node["tag"][3:]
    if current_node["isNode"]:
        current_node["value"] = f'T:{current_node["tag"]}    |    L:{to_binary(int(current_node["length"]))}    |    V:{current_node["node-value"]}'
    else:
        current_node["value"] = f'T:{current_node["tag"]}    |    L:{to_binary(int(current_node["length"]))}    |    []'
    if current_node.get("p-node-id"):
        repair_tag(node_list,current_node.get("p-node-id"))







