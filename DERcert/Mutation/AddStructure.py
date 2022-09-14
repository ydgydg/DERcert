'''
结构变异：结构的增加
对叶结点结构的增加，增加之后需要修复长度
'''
import TreeTemplate as tree
import Backtorepair as br
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


class BackingRepalr(object):
    '''
    回溯修复叶节点类
    '''

    def getnewNodelen(self,TreeNode):
        '''
        :param tree:
        :return:获得变异后结点的value长度
        '''
        node_len = TreeNode.length
        lst = node_len[0]
        if lst[0] == '0':#length字段首位为0时判断Value长度
            newNodelen = str(int(lst,2))
        elif lst[0] == '1':#length字段首位为1时判断Value长度
            Len1 = str(int(lst[0],2))
            str3 = int(lst[1]) + str(lst[Len1])
            newNodelen =str(int(str3,2))
        return newNodelen
    def getOldNodelen(self,Treenode):
        '''
        :param Treenode:
        :return:变异之前结点的Value长度
        '''
        node_len = Treenode.length
        lst = node_len[0]
        if lst[0] == '0':#length字段首位为0时判断Value长度
            newNodelen = str(int(lst,2))
            return newNodelen
        elif lst[0] == '1':#length字段首位为1时判断Value长度
            Len1 = str(int(lst[0],2))
            str3 = int(lst[1]) + str(lst[Len1])
            Len3 =str(int(str3,2))
        return Len3


    def getLendif(self,TreeNode):
        newnodelen = self.getnewNodelen(TreeNode)
        oldnodelen = self.getOldNodelen(TreeNode)
        lendif = newnodelen - oldnodelen
        return lendif


    def repair(self,TreeNode,node):
        '''
        修复长度
        :return:
        '''
        #len = self.getLendif()#获取长度差
        try:
            len_newNode = self.getnewNodelen(TreeNode)#先获得变异后的Value长度
        except:
            print('参数错误')
        lst_faNode = node.length
        #lst先转成非字符型 然后再和长度差相加  或者直接拿newNodelen和父节点的长度相比较，再修改长度
        len_num = str(int(lst_faNode[0],2))#父节点Value长度
        #计算差值
        len_dif = int(len_num) - int(len_newNode)
        #更新父节点长度   int(len_newNode)
        newLen = int(len_num) + len_dif
        newFatherlen = bin(int(newLen))[2:].zfill(8)    
        node.length.pop(0)
        node.length.append(newFatherlen)
        return node.length
class AddStructure:
    '''
    增加结构
    '''
    @staticmethod
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
    @staticmethod
    def addstru(node,node1):
        '''
        :param node: 根节点
        :param node1: 待增加的节点
        :return:
        '''
        leanode_queue = AddStructure.cengxubianli(node)#叶子节点列表
        leanode = leanode_queue[0]#取一个叶子节点
        Copy_leanode = leanode
        leanode.value.append(node1)#在叶子节点的value字段增加一个新的节点





