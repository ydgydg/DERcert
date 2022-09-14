'''
树模板  解析完TLV的时候要用  进行回溯修复的时候要用
'''


class TreeNode():
    '''
    结点类  把value定义为一个列表
    '''

    def __init__(self,tag = None,length = None,value = None):
        self.tag = []
        self.length = []
        self.value = []


    def addchild(self,node):
        '''
        添加结点到value
        :return:
        '''
        self.value.append(node)
    def addvalue(self,str):
        '''
        添加值
        :param str:
        :return:
        '''

        self.value.append(str)


    def delechild(self,node):
        '''

        :param node:
        :return: 删除value列表中某个值
        '''
        self.value.remove(node)
    def delevalue(self,str):
        '''
        删除value值
        :param str:
        :return:
        '''
        self.value.remove(str)




