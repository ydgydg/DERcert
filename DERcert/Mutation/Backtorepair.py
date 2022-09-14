import TreeTemplate as tree
'''
先定义一个叶节点变异前的树，再定义一一个变异后的叶节点，把变异后的叶节点的值赋给变异前的树
'''
# c_mute = tree.TreeNode(['00000010'],['00000010'],['00000001','00000011'])
'''
创建一棵树
'''
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
'''
定义一个变异后的叶节点
'''
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
            length_str = lst
            Len_len = int(length_str[1:], 2)  # length字段标志位为1时，首先获取length字段本身的长度
            Len_value = lst[1:len(lst) + 1]  # length字段的值
            value = ''  # 中间变量 将Len_value中的元素拼接起来成为一整个元素
            for i in range(0, len(Len_value)):
                value = value + Len_value[i]
            full_len_value = int(value, 2)
        return full_len_value


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
# c_mute = tree.TreeNode(['00000010'],['00000010'],['00000001','00000011'])
# c_mute.tag.append('00000010')
# c_mute.length.append('00000010')
# c_mute.value.append('00000001')
# c_mute.value.append('00000011')
# r = BackingRepalr()
# print(r.repair(c_mute))
# print(r.getnewNodelen(c_mute))