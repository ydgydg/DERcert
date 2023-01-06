'''
Parsing tool class
'''
class DERdumper(object):
    def get_tag(self, datastr, index):
        '''
        function:Get tag
        :param datastr: Data to be parsed
        :param index: Mark bit
        :return: tag and tag bit
        '''
        # global tag_str_signbit
        tag_str = datastr[index]
        tag_str_signbit = tag_str[2]
        tag_stru = tag_str[3:]
        '''
        What data type is the tag
        '''
        if tag_stru == '00001':
            type = 'boolean'
        elif tag_stru == '00010':
            type = 'INTER'
        elif tag_stru == '00011':
            type = 'BIT STRING'
        elif tag_stru == '00100':
            type = 'OCTET STRING'
        elif tag_stru == '00110':
            type = 'NULL'
        elif tag_stru == '00110':
            type = 'OBJECT IDENTIFIER'
        elif tag_stru == '01000':
            type = 'OBJECT DESCRIPTOP'
        elif tag_stru == '01001':
            type = 'EXTERNAL'
        elif tag_stru == '01010':
            type = 'REAL'
        elif tag_stru == '01011':
            type = 'ENUMERATED'
        elif tag_stru == '01100':
            type = 'UTF8STRING'
        elif tag_stru == '01101':
            print('RELATIVE-OID')
        elif tag_stru == '01110':
            type = 'SEQUENCE'
        elif tag_stru == '01111':
            type = 'SET'
        elif tag_stru == '10000':
            type = 'NUMERICSTRING'
        elif tag_stru == '10001':
            type = 'PRINATBLESTRING'
        elif tag_stru == '10010':
            type = 'TELETESTRING'
        elif tag_stru == '10011':
            type = 'VIDEOSTRING'
        elif tag_stru == '10100':
            type = 'IA5STRING'
        elif tag_stru == '10101':
            type = 'UTCTime'
        elif tag_stru == '10110':
            type = 'GeneralizedTime'
        elif tag_stru == '10111':
            type = 'GraphicString'
        elif tag_stru == '11000':
            type = 'VisibleString, ISO646String'
        elif tag_stru == '11001':
            type = 'GeneralString'
        elif tag_stru == '11010':
            type = 'UniversalString'
        elif tag_stru == '11011':
            type = 'CHARACTER STRING'
        elif tag_stru == '11100':
            type = 'BMPString'
        return tag_str, tag_str_signbit

    def is_constructed(self,datastr,index):
        '''
        function:Determines whether it is a nested structure
        :param datastr: Data to be parsed
        :param index: Mark bit
        :return:False or True
        '''
        tag_str_signbit = datastr[index][2]
        if tag_str_signbit == '1':
            return  True
        else:
            return False
    @staticmethod
    def get_length(datastr,index):
        '''
        function:Gets the value of length and the length of value
        :param datastr: Data to be parsed
        :param index: Mark bit
        :return:length and value of length
        '''
        length_str = datastr[index]
        length_str_signbit = length_str[0]
        if length_str_signbit == '0':
            Len_len = 1
            Len_value = length_str
            full_len_value = int(Len_value, 2)
        elif length_str_signbit == '1':
            Len_len = int(length_str[1:], 2)
            Len_value = datastr[index + 1:index + Len_len + 1]
            value = ''
            for i in range(0, len(Len_value)):
                value = value + Len_value[i]
            full_len_value = int(value, 2)
        return full_len_value, Len_len

    # @staticmethod
    # def getvaluelength():
    #     tup = DERdumper.getLength()
    #     return tup[0]
    def get_value(self, datastr,index):
        '''
        function:Get value
        :param datastr: Data to be parsed
        :param index: Mark bit
        :return: value
        '''
        tup = DERdumper().get_length(datastr,index)

        value = datastr[tup[1] + 1:tup[0] + 1]
        # ret = DERdumper.isConstrued(self)
        # if ret:
        #     DERdumper.getValue(self,value)
        return value



