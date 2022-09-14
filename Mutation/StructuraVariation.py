'''
结构变异

1.左右子树调换
'''
# 多级引用
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
# d.value.append('00000010')
# d.value.append('00000011')
b.addchild(c_mute)
a.addchild(b)
a.addchild(d)
b.addchild(c_mute)


nodevlst = []
def getNodeValue(node):
    if node.value:
        for child in node.value:
            nodevlst.append(child)
    return nodevlst

class StructionVar:
    '''
    子节点使用列表存储，子树互换位置的话更改在子节点列表中的位置即可
    '''
    @staticmethod
    def bianli(root):
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

lst = StructionVar.bianli(a)
print(lst)
'''
交换位置
'''
# exchange = ''
# exchange = lst[0][0]
# lst[0][0] = lst[0][1]
# lst[0][1] = exchange
print(lst[0][1].value)
for i in range(0,len(lst) - 1):
    for j in range(0,len(lst[i])):
        print(lst[i][j].value)


