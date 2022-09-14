import os
import sys

'''
扫描目标文件夹，返回文件相对路径列表
'''


# dir_name = 'D:\\testcert'
def getfilename(dir_name):
    filenamelist = os.listdir(dir_name)
    return filenamelist
'''
把filenamelist中的值遍历出来作为参数，传入到函数中
'''
def getBinData(filenamelist):
    i = 0
    while i < len(filenamelist):
        Data_list = []
        with open('D:\\test_wolfssl\\' + str(filenamelist[i]), 'rb') as fp:
            data = fp.read().hex()
        Data_str = data
        print(Data_str)
        for item in range(0, len(Data_str)):
            Data_list.append(Data_str[item])
        for j in range(0, len(Data_list)):
            if Data_list[j] == 'a':
                Data_list[j] = '10'

            if Data_list[j] == 'b':
                Data_list[j] = '11'

            if Data_list[j] == 'c':
                Data_list[j] = '12'

            if Data_list[j] == 'd':
                Data_list[j] = '13'

            if Data_list[j] == 'e':
                Data_list[j] = '14'

            if Data_list[j] == 'f':
                Data_list[j] = '15'

        Data_list_tran = []
        for k in range(0, len(Data_list)):
            s1 = bin(int(Data_list[k]))[2:].zfill(4)
            Data_list_tran.append(s1)

        l = Data_list_tran
        l = "".join(l)

        Data_list_bin = []
        str1 = ""
        addition_number = 0
        m = 1
        while addition_number < len(l):
            while m <= 8:
                if addition_number > len(l) - 1:
                    break
                else:
                    str1 = str1 + l[addition_number]
                    addition_number = addition_number + 1
                m = m + 1

            Data_list_bin.append(str1)
            str1 = ''
            m = 1

            '''
            把Data_list_bin存入到指定目录中
            '''
        dir_name1 = 'D:\\Test_bin_dir\\'
        if not os.path.exists(dir_name1):
            os.mkdir(dir_name1)

        fb = open(dir_name1 + filenamelist[i], mode='w', encoding='utf-8')
        for n in range(0, len(Data_list_bin) - 1):
            fb.write(Data_list_bin[n])

        i = i + 1
    print('文件创建完成')
    # print(Data_list_bin)
# dir_name = 'D:\\test_wolfssl'
# filename = getfilename(dir_name)
# getBinData(filename)
