'''
结构变异：删除叶节点的
'''
import TreeTemplate as tree
import Backtorepair as br
import treelib as t
t.node
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

class Delete:
    '''
    删除结构
    '''

    @staticmethod
    def cengxubianli(root):
        '''

        :param root:
        :return: 叶节点列表
        '''
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
    @staticmethod
    def deletestru(node):
        '''
        可以定义一个空节点，即长度为0的节点当作变异后的节点
        :param node:
        :return:
        '''
        midenode = tree.TreeNode()
        midenode.value.append('00000000')
        midenode.length.append('00000000')
        leafnode = Delete.cengxubianli(node)
        leafnode.pop(len(leafnode) )
        afterdel = leafnode#删除叶子节点

        #再调用回溯修复函数
        br.BackingRepalr.repair(leafnode[len(leafnode) - 1],midenode)
        pass

