'''
在value列表里增加元素
'''
import TreeTemplate as tree
a = tree.TreeNode()
a.tag.append('00110000')
a.length.append('00001010')
b = tree.TreeNode()
b.tag.append('00110000')
b.length.append('00000011')
c = tree.TreeNode()
c.tag.append('00000010')
c.length.append('00000001')
c.value.append('00000010')
c_mute = tree.TreeNode()
c_mute.tag.append('00000010')
c_mute.length.append('00000010')
c_mute.value.append('00000001')
c_mute.value.append('00000011')
d = tree.TreeNode()
d.tag.append('00000010')
d.length.append('00000100')
d.value.append('00000001')
d.value.append('00000010')
d.value.append('00000011')
b.addchild(c_mute)
a.addchild(b)
a.addchild(d)
b.addchild(c_mute)


def cengxubianli(root):
    que = [root]
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

def add(res):
    addele = '00001111'
    node = res[len(res) - 1]
    node.value.append(addele)
    return res
    pass

res = cengxubianli(a)
res1 = add(res)
print(res1[len(res1) - 1].value)

