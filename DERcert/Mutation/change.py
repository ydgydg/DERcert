'''
更改

'''

# data = ['00110000', '00001011', '00000110', '00001001', '00101010', '10000110', '01001000', '10000110', '11110111',
#         '00001101', '00000001', '00000001', '00001011']

import TreeTemplate as tree
import Backtorepair as br
# a = tree.TreeNode()
# a.tag.append('00110000')
# a.length.append('00001010')
# b = tree.TreeNode()
# b.tag.append('00110000')
# b.length.append('00000011')
# c = tree.TreeNode()
# c.tag.append('00000010')
# c.length.append('00000001')
# c.value.append('00000010')
# c_mute = tree.TreeNode()
# c_mute.tag.append('00000010')
# c_mute.length.append('00000010')
# c_mute.value.append('00000001')
# c_mute.value.append('00000011')
# d = tree.TreeNode()
# d.tag.append('00000010')
# d.length.append('00000100')
# d.value.append('00000001')
# d.value.append('00000010')
# d.value.append('00000011')
# b.addchild(c_mute)
# a.addchild(b)
# a.addchild(d)

def cengxubianli(node):
    que = [node]
    res = []
    while que:
        middle = []  # 中间变量列表
        next_node = []  # 初始下一层的节点列表为空
        for node in que:
            if type(node.value[0]) == tree.TreeNode:
                middle.extend(node.value)
                # print(middle)
                for node1 in middle:
                    if type(node1.value[0]) == str:
                        res.append(node1)
                    elif type(node1.value[0]) == tree.TreeNode:
                        next_node.append(node1)
            elif type(node.value[0]) == str:
                res.append(node)
        que = next_node
    return res


def change(res):
    '''
    :param data:
    :return: change the last bit
    '''
    leafnode = res[len(res) - 1]
    lst = leafnode.value
    value_last = lst[len(lst) - 1][7]
    if value_last == 1:
        value_last = 0
    else:
        value_last = 1
    return res
    pass

