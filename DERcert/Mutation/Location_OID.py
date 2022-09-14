import os



'''
定位OID的位置
oid编码规则：SO规定前两级格式为：第一级 * 40 + 第二级，即为 1*40 + 3 = 43，十六进制为 2b.
后面小于128的直接转换
.6.1.4.1.2011.11.11.0
06 01 04 01 (2011) 0b 0b 00
2011转化为15*128 + 101,为 (15,101),
15最高位置为1，为15+128=143,101最高位不变，为(143,101)
十六进制为 8f 65
'''

oid_lst = ['OID', '2.5.29.37.0', '2.23.133.8.3', '1.3.6.1.4.1.311.20.2.1', '1.3.6.1.5.5.7.3.2', '1.3.6.1.5.5.7.3.3', '1.3.6.1.4.1.311.20.1', '1.3.6.1.4.1.311.10.5.1', '1.3.6.1.4.1.311.21.19', '1.3.6.1.4.1.311.10.3.30', '1.3.6.1.4.1.311.80.1', '1.3.6.1.4.1.311.10.3.12', '1.3.6.1.4.1.311.64.1.1', '1.3.6.1.4.1.311.76.5.1', '1.3.6.1.4.1.311.61.4.1', '1.3.6.1.4.1.311.10.3.8', '1.3.6.1.4.1.311.10.3.4', '2.23.133.8.1', '1.3.6.1.4.1.311.10.3.4.1', '1.3.6.1.4.1.311.61.5.1', '1.3.6.1.5.5.7.3.5', '1.3.6.1.5.5.8.2.2', '1.3.6.1.5.5.7.3.6', '1.3.6.1.5.5.7.3.7', '1.3.6.1.5.2.3.5', '1.3.6.1.4.1.311.61.1.1', '1.3.6.1.4.1.311.10.6.1', '1.3.6.1.4.1.311.10.3.11', '1.3.6.1.4.1.311.21.6', '1.3.6.1.4.1.311.10.6.2', '1.3.6.1.4.1.311.10.3.13', '1.3.6.1.4.1.311.76.8.1', '1.3.6.1.4.1.311.10.3.2', '1.3.6.1.4.1.311.10.3.1', '1.3.6.1.5.5.7.3.9', '1.3.6.1.4.1.311.10.3.7', '2.23.133.8.2', '1.3.6.1.4.1.311.10.3.27', '1.3.6.1.4.1.311.21.5', '1.3.6.1.4.1.311.10.3.22', '1.3.6.1.4.1.311.10.3.24', '1.3.6.1.4.1.311.10.3.10', '1.3.6.1.4.311.54.1.2', '1.3.6.1.4.1.311.10.3.19', '1.3.6.1.4.1.311.10.3.9', '1.3.6.1.5.5.7.3.4', '1.3.6.1.5.5.7.3.1', '1.3.6.1.4.1.311.20.2.2', '1.3.6.1.4.1.311.2.6.2', '1.3.6.1.4.1.311.2.6.1', '1.3.6.1.5.5.7.3.8', '1.3.6.1.4.1.311.10.3.5.1', '1.3.6.1.4.1.311.10.3.39', '1.3.6.1.4.1.311.10.3.5', '1.3.6.1.4.1.311.10.3.20', '1.3.6.1.4.1.311.10.3.21', '1.3.6.1.4.1.311.10.3.26', '1.3.6.1.4.1.311.76.3.1', '1.3.6.1.4.1.311.10.3.6', '1.3.6.1.4.1.311.10.3.23', '1.3.6.1.4.1.311.10.3.25', '1.3.6.1.4.1.311.76.6.1', 'OID', '1.3.6.1.4.1.311.21.1', '1.3.6.1.4.1.311.21.2', '1.3.6.1.4.1.311.21.3', '1.3.6.1.4.1.311.21.4', '1.3.6.1.4.1.311.21.5', '1.3.6.1.4.1.311.21.6', '1.3.6.1.4.1.311.21.7', '1.3.6.1.4.1.311.21.8', '1.3.6.1.4.1.311.21.9', '1.3.6.1.4.1.311.21.10', '1.3.6.1.4.1.311.21.11', '1.3.6.1.4.1.311.21.12', '1.3.6.1.4.1.311.21.13', '1.3.6.1.4.1.311.21.14', '1.3.6.1.4.1.311.21.15', '1.3.6.1.4.1.311.21.16', '1.3.6.1.4.1.311.21.17', '1.3.6.1.4.1.311.21.19', '1.3.6.1.4.1.311.21.20', '1.3.6.1.4.1.311.21.21', '1.3.6.1.4.1.311.21.22', '1.3.6.1.4.1.311.21.25', 'OID', '2.5.29.14', '2.5.29.15', '2.5.29.16', '2.5.29.18', '2.5.29.19', '2.5.29.20', '2.5.29.21', '2.5.29.24', '2.5.29.27', '2.5.29.29', '2.5.29.31', '2.5.29.35', 'OID', '2.5.29.19', '2.5.29.35', '2.5.29.32', '2.5.29.31', '2.5.29.46', '2.5.29.8', '2.5.29.15', '2.5.29.30', '2.5.29.36', '2.5.29.33', '2.5.29.16', '2.5.29.17', '2.5.29.9', '2.5.29.14', 'Enable Key Usage Extensions', 'Digital Signature, Key Encipherment or Key Agreement', 'Digital Signature and/or Key Agreement', 'Digital Signature', 'Digital Signature, non-Repudiation, and/or Key Encipherment or Key Agreement', 'Digital Signature, Key Encipherment or Key Agreement', 'Digital Signature, Key Encipherment or Key Agreement', 'Digital Signature, non-Repudiation', 'Key Usage Extensions', 'Digital signature', 'Key encipherment', 'Digital signature', 'Key encipherment', 'Certificate signing', 'Digital signature', '']
oid_dict = {'Object Identifiers ': 'OID', 'Any Purpose ': '2.5.29.37.0', 'Attestation Identity Key Certificate ': '2.23.133.8.3', 'Certificate Request Agent ': '1.3.6.1.4.1.311.20.2.1', 'Client Authentication ': '1.3.6.1.5.5.7.3.2', 'Code Signing ': '1.3.6.1.5.5.7.3.3', 'CTL Usage ': '1.3.6.1.4.1.311.20.1', 'Digital Rights ': '1.3.6.1.4.1.311.10.5.1', 'Directory Service Email Replication ': '1.3.6.1.4.1.311.21.19', 'Disallowed List ': '1.3.6.1.4.1.311.10.3.30', 'Document Encryption ': '1.3.6.1.4.1.311.80.1', 'Document Signing ': '1.3.6.1.4.1.311.10.3.12', 'Domain Name System (DNS) Server Trust ': '1.3.6.1.4.1.311.64.1.1', 'Dynamic Code Generator ': '1.3.6.1.4.1.311.76.5.1', 'Early Launch Antimalware Driver ': '1.3.6.1.4.1.311.61.4.1', 'Embedded Windows System Component Verification ': '1.3.6.1.4.1.311.10.3.8', 'Encrypting File System ': '1.3.6.1.4.1.311.10.3.4', 'Endorsement Key Certificate ': '2.23.133.8.1', 'File Recovery ': '1.3.6.1.4.1.311.10.3.4.1', 'HAL Extension ': '1.3.6.1.4.1.311.61.5.1', 'IP security end system ': '1.3.6.1.5.5.7.3.5', 'IP security IKE intermediate ': '1.3.6.1.5.5.8.2.2', 'IP security tunnel termination ': '1.3.6.1.5.5.7.3.6', 'IP security user ': '1.3.6.1.5.5.7.3.7', 'KDC Authentication ': '1.3.6.1.5.2.3.5', 'Kernel Mode Code Signing ': '1.3.6.1.4.1.311.61.1.1', 'Key Pack Licenses ': '1.3.6.1.4.1.311.10.6.1', 'Key Recovery ': '1.3.6.1.4.1.311.10.3.11', 'Key Recovery Agent ': '1.3.6.1.4.1.311.21.6', 'License Server Verification ': '1.3.6.1.4.1.311.10.6.2', 'Lifetime Signing ': '1.3.6.1.4.1.311.10.3.13', 'Microsoft Publisher ': '1.3.6.1.4.1.311.76.8.1', 'Microsoft Time Stamping ': '1.3.6.1.4.1.311.10.3.2', 'Microsoft Trust List Signing ': '1.3.6.1.4.1.311.10.3.1', 'OCSP Signing ': '1.3.6.1.5.5.7.3.9', 'OEM Windows System Component Verification ': '1.3.6.1.4.1.311.10.3.7', 'Platform Certificate ': '2.23.133.8.2', 'Preview Build Signing ': '1.3.6.1.4.1.311.10.3.27', 'Private Key Archival ': '1.3.6.1.4.1.311.21.5', 'Protected Process Light Verification ': '1.3.6.1.4.1.311.10.3.22', 'Protected Process Verification ': '1.3.6.1.4.1.311.10.3.24', 'Qualified Subordination ': '1.3.6.1.4.1.311.10.3.10', 'Remote Desktop Authentication ': '1.3.6.1.4.311.54.1.2', 'Revoked List Signer ': '1.3.6.1.4.1.311.10.3.19', 'Root List Signer ': '1.3.6.1.4.1.311.10.3.9', 'Secure Email ': '1.3.6.1.5.5.7.3.4', 'Server Authentication ': '1.3.6.1.5.5.7.3.1', 'Smart Card Logon ': '1.3.6.1.4.1.311.20.2.2', 'SpcEncryptedDigestRetryCount ': '1.3.6.1.4.1.311.2.6.2', 'SpcRelaxedPEMarkerCheck ': '1.3.6.1.4.1.311.2.6.1', 'Time Stamping ': '1.3.6.1.5.5.7.3.8', 'Windows Hardware Driver Attested Verification ': '1.3.6.1.4.1.311.10.3.5.1', 'Windows Hardware Driver Extended Verification ': '1.3.6.1.4.1.311.10.3.39', 'Windows Hardware Driver Verification ': '1.3.6.1.4.1.311.10.3.5', 'Windows Kits Component ': '1.3.6.1.4.1.311.10.3.20', 'Windows RT Verification ': '1.3.6.1.4.1.311.10.3.21', 'Windows Software Extension Verification ': '1.3.6.1.4.1.311.10.3.26', 'Windows Store ': '1.3.6.1.4.1.311.76.3.1', 'Windows System Component Verification ': '1.3.6.1.4.1.311.10.3.6', 'Windows TCB Component ': '1.3.6.1.4.1.311.10.3.23', 'Windows Third Party Application Component ': '1.3.6.1.4.1.311.10.3.25', 'Windows Update ': '1.3.6.1.4.1.311.76.6.1', 'Microsoft CertSrv Infrastructure': 'OID', 'Certificate services Certification Authority (CA) version': '1.3.6.1.4.1.311.21.1', 'szOID_CERTSRV_PREVIOUS_CERT_HASH': '1.3.6.1.4.1.311.21.2', 'szOID_CRL_VIRTUAL_BASE': '1.3.6.1.4.1.311.21.3', 'szOID_CRL_NEXT_PUBLISH': '1.3.6.1.4.1.311.21.4', 'szOID_KP_CA_EXCHANGE': '1.3.6.1.4.1.311.21.5', 'szOID_KP_KEY_RECOVERY_AGENT': '1.3.6.1.4.1.311.21.6', 'szOID_CERTIFICATE_TEMPLATE': '1.3.6.1.4.1.311.21.7', 'szOID_ENTERPRISE_OID_ROOT': '1.3.6.1.4.1.311.21.8', 'szOID_RDN_DUMMY_SIGNER': '1.3.6.1.4.1.311.21.9', 'szOID_APPLICATION_CERT_POLICIES': '1.3.6.1.4.1.311.21.10', 'szOID_APPLICATION_POLICY_MAPPINGS': '1.3.6.1.4.1.311.21.11', 'szOID_APPLICATION_POLICY_CONSTRAINTS': '1.3.6.1.4.1.311.21.12', 'szOID_ARCHIVED_KEY_ATTR': '1.3.6.1.4.1.311.21.13', 'szOID_CRL_SELF_CDP': '1.3.6.1.4.1.311.21.14', 'szOID_REQUIRE_CERT_CHAIN_POLICY': '1.3.6.1.4.1.311.21.15', 'szOID_ARCHIVED_KEY_CERT_HASH': '1.3.6.1.4.1.311.21.16', 'szOID_ISSUED_CERT_HASH': '1.3.6.1.4.1.311.21.17', 'szOID_DS_EMAIL_REPLICATION': '1.3.6.1.4.1.311.21.19', 'szOID_REQUEST_CLIENT_INFO': '1.3.6.1.4.1.311.21.20', 'szOID_ENCRYPTED_KEY_HASH': '1.3.6.1.4.1.311.21.21', 'szOID_CERTSRV_CROSSCA_VERSION': '1.3.6.1.4.1.311.21.22', 'Key storage provider name': '1.3.6.1.4.1.311.21.25', 'Certificate': 'OID', 'subjectKeyIdentifier': '2.5.29.14', 'keyUsage': '2.5.29.15', 'privateKeyUsagePeriod': '2.5.29.16', 'issuerAltName': '2.5.29.18', 'basicConstraints': '2.5.29.19', 'cRLNumber': '2.5.29.20', 'reasonCode': '2.5.29.21', 'invalidityDate': '2.5.29.24', 'deltaCRLIndicator': '2.5.29.27', 'certificateIssuer': '2.5.29.29', 'cRLDistributionPoints': '2.5.29.31', 'authorityKeyIdentifier': '2.5.29.35', 'Certificate Extensions': 'OID', 'Authority Key Identifier': '2.5.29.19', 'Basic Constraints': '2.5.29.35', 'Certificate Policies': '2.5.29.32', 'CRL Distribution Points': '2.5.29.31', 'Enhanced Key Usage': '2.5.29.46', 'Issuer Alternative Name': '2.5.29.8', 'Key Usage': '2.5.29.15', 'Name Constraints': '2.5.29.30', 'Policy Constraints': '2.5.29.36', 'Policy Mappings': '2.5.29.33', 'Private Key Usage Period': '2.5.29.16', 'Subject Alternative Name': '2.5.29.17', 'Subject Directory Attributes': '2.5.29.9', 'Subject Key Identifier': '2.5.29.14', 'Extended Key': 'Enable Key Usage Extensions', 'Web Server Certificate': 'Digital Signature, Key Encipherment or Key Agreement', 'Web Client Certificate': 'Digital Signature and/or Key Agreement', 'File Signing .exe': 'Digital Signature', 'E-Mail Protection': 'Digital Signature, non-Repudiation, and/or Key Encipherment or Key Agreement', 'IPSEC Host or Router': 'Digital Signature, Key Encipherment or Key Agreement', 'IPSEC Tunnel': 'Digital Signature, Key Encipherment or Key Agreement', 'Timestamping': 'Digital Signature, non-Repudiation', 'Application': 'Key Usage Extensions', 'SSL Certificate for Client': 'Digital signature', 'SSL Certificate for Server': 'Key encipherment', 'S/MIME Signing': 'Digital signature', 'S/MIME Encryption': 'Key encipherment', 'Certificate Signing': 'Certificate signing', 'Object Signing': 'Digital signature', '': ''}
with open('certtest1','r',encoding='utf-8') as fp:
    data_cert = fp.read()
print(data_cert)

print('===============================================')

oid = '2.5.29.37.0'
single_oid = oid.split('.')
FirstTwo = bin(int(single_oid[0])*40 + int(single_oid[1]))[2:].zfill(8)#前两个字节转换
tranoid = [FirstTwo]
for i in range(2,len(single_oid)):
    n = bin(int(single_oid[i]))[2:].zfill(8)
    tranoid.append(n)

print(tranoid)


def same_start_end(p):
    n = len(p)  # 整个字符串长度
    j = 0  # 前缀匹配指向
    i = 1  # 后缀匹配指向
    s = []
    result_list = [0] * n
    while i < n:
        if j == 0 and s[j] != s[i]:  # 比较不相等并且此时比较的已经是第一个字符了
            result_list[i] = 0  # 值为０
            i += 1  # 向后移动
        elif s[j] != s[i] and j != 0:  # 比较不相等,将j值设置为ｊ前一位的result_list中的值，为了在之前匹配到的子串中找到最长相同前后缀
            j = result_list[j - 1]
        elif s[j] == s[i]:  # 相等则继续比较
            result_list[i] = j + 1
            j = j + 1
            i = i + 1
    return result_list
    pass


class OID_Location:
    '''
    oid定位类
    '''
    @staticmethod
    def OIDTranBin(oid_lst):
        '''
        原始的oid格式为xx.xx.xx.xx
        所以需要把原始oid转为二进制形式
        :return:
        '''
        fulloidlst = []
        x = 0
        while True:
            oid = oid_lst(x)
            single_oid = oid.split('.')
            FirstTwo = bin(int(single_oid[0]) * 40 + int(single_oid[1]))[2:].zfill(8)  # 前两个字节转换
            tranoid = [FirstTwo]
            for i in range(2, len(single_oid)):
                n = bin(int(single_oid[i]))[2:].zfill(8)
                tranoid.append(n)
            fulloidlst.append(tranoid)
            if x == len(oid_lst):
                break
            return fulloidlst#返回的列表中的元素也是列表，每个子列表都是一个完整的oid
    @staticmethod
    def locateOID(oid,data_cert):
        '''
        定义为一个静态函数，方便调用。
        1.直接在证书转为二进制代码的文件中定位
        2.在证书书中根据遍历算法进行定位
        :return: 1，返回要查找的oid在一个证书文件中的位置,字符串定位
        2.返回要查抄的oid在证书树中的位置

        这里采用第一种方法，找到在证书文件中的位置之后再在树中进行寻找
        利用kmp算法
        '''
        s_length = len(oid)
        p_length = len(data_cert)
        i = 0
        j = 0
        next = same_start_end(oid)
        while i < s_length:
            if oid[i] == data_cert[j]:  # 对应字符相同
                i += 1
                j += 1
                if j >= p_length:  # 完全匹配
                    return i - p_length
            elif oid[i] != data_cert[j]:  # 不相同
                if j == 0:  # 与模式比较的是模式的第一个字符
                    i += 1
                else:  # 取模式当前字符之前最长相同前后缀的前缀的后一个字符继续比较
                    j = next[j]
        if i == s_length:  # 没有找到完全匹配的子串
            return -1



