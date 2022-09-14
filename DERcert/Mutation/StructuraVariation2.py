'''

树的上下层结构交换
'''
import TreeTemplate as tree
a = tree.TreeNode()
a.tag.append('00110000')
a.length.append('00001010')
b = tree.TreeNode()
b.tag.append('00110000')
b.length.append('00000011')
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


def isvaluelstempty(node):
    '''
    判断结点的孩子列表是否为空
    :param node:
    :return:
    '''
    retval = False
    list_child = node.value
    if len(list_child) == 0:
        retval = True
    return retval

def fineleInvalue(node):
    '''
    找到value列表中最后一个元素用与交换次序
    :param node:
    :return: last ele in valuelist
    '''
    retval = isvaluelstempty(node)
    if retval == True:
      return
    elif retval == False:
        elelist = node.value
        ele = elelist[len(elelist-1)]#获取value列表的最后一个元素
    return ele
def ismiddlenode(node):
    '''
    判断是否为中间结点
    :param node:
    :return:
    '''
    retval = isvaluelstempty(node)
    if retval == True:
        print('This node is leafnode,not middle node')
    elif retval == False:
        return node

class StructuVariation2:
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
     def levelMute(node):
         '''
         输入一棵树 进行层次顺序交换
         :return:
         '''
         res = StructuVariation2.cengxubianli(node)#首先调用层序遍历函数 得到结果列表
         #通过res列表元素判断中间结点和最后一层的结点
         lst = StructuVariation2.cengxubianli(node)
         value = lst[0]#中间变量
         lst[1] = value
         lst[0] = lst[1]
         return lst

lst = StructuVariation2.levelMute(a)
print(lst)