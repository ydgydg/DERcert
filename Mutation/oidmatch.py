'''
证书数据和oid数据进行匹配
'''
from oidtohex import *
import re
oid_dict = {'Object Identifiers ': 'OID', 'Any Purpose ': '2.5.29.37.0', 'Attestation Identity Key Certificate ': '2.23.133.8.3', 'Certificate Request Agent ': '1.3.6.1.4.1.311.20.2.1', 'Client Authentication ': '1.3.6.1.5.5.7.3.2', 'Code Signing ': '1.3.6.1.5.5.7.3.3', 'CTL Usage ': '1.3.6.1.4.1.311.20.1', 'Digital Rights ': '1.3.6.1.4.1.311.10.5.1', 'Directory Service Email Replication ': '1.3.6.1.4.1.311.21.19', 'Disallowed List ': '1.3.6.1.4.1.311.10.3.30', 'Document Encryption ': '1.3.6.1.4.1.311.80.1', 'Document Signing ': '1.3.6.1.4.1.311.10.3.12', 'Domain Name System (DNS) Server Trust ': '1.3.6.1.4.1.311.64.1.1', 'Dynamic Code Generator ': '1.3.6.1.4.1.311.76.5.1', 'Early Launch Antimalware Driver ': '1.3.6.1.4.1.311.61.4.1', 'Embedded Windows System Component Verification ': '1.3.6.1.4.1.311.10.3.8', 'Encrypting File System ': '1.3.6.1.4.1.311.10.3.4', 'Endorsement Key Certificate ': '2.23.133.8.1', 'File Recovery ': '1.3.6.1.4.1.311.10.3.4.1', 'HAL Extension ': '1.3.6.1.4.1.311.61.5.1', 'IP security end system ': '1.3.6.1.5.5.7.3.5', 'IP security IKE intermediate ': '1.3.6.1.5.5.8.2.2', 'IP security tunnel termination ': '1.3.6.1.5.5.7.3.6', 'IP security user ': '1.3.6.1.5.5.7.3.7', 'KDC Authentication ': '1.3.6.1.5.2.3.5', 'Kernel Mode Code Signing ': '1.3.6.1.4.1.311.61.1.1', 'Key Pack Licenses ': '1.3.6.1.4.1.311.10.6.1', 'Key Recovery ': '1.3.6.1.4.1.311.10.3.11', 'Key Recovery Agent ': '1.3.6.1.4.1.311.21.6', 'License Server Verification ': '1.3.6.1.4.1.311.10.6.2', 'Lifetime Signing ': '1.3.6.1.4.1.311.10.3.13', 'Microsoft Publisher ': '1.3.6.1.4.1.311.76.8.1', 'Microsoft Time Stamping ': '1.3.6.1.4.1.311.10.3.2', 'Microsoft Trust List Signing ': '1.3.6.1.4.1.311.10.3.1', 'OCSP Signing ': '1.3.6.1.5.5.7.3.9', 'OEM Windows System Component Verification ': '1.3.6.1.4.1.311.10.3.7', 'Platform Certificate ': '2.23.133.8.2', 'Preview Build Signing ': '1.3.6.1.4.1.311.10.3.27', 'Private Key Archival ': '1.3.6.1.4.1.311.21.5', 'Protected Process Light Verification ': '1.3.6.1.4.1.311.10.3.22', 'Protected Process Verification ': '1.3.6.1.4.1.311.10.3.24', 'Qualified Subordination ': '1.3.6.1.4.1.311.10.3.10', 'Remote Desktop Authentication ': '1.3.6.1.4.311.54.1.2', 'Revoked List Signer ': '1.3.6.1.4.1.311.10.3.19', 'Root List Signer ': '1.3.6.1.4.1.311.10.3.9', 'Secure Email ': '1.3.6.1.5.5.7.3.4', 'Server Authentication ': '1.3.6.1.5.5.7.3.1', 'Smart Card Logon ': '1.3.6.1.4.1.311.20.2.2', 'SpcEncryptedDigestRetryCount ': '1.3.6.1.4.1.311.2.6.2', 'SpcRelaxedPEMarkerCheck ': '1.3.6.1.4.1.311.2.6.1', 'Time Stamping ': '1.3.6.1.5.5.7.3.8', 'Windows Hardware Driver Attested Verification ': '1.3.6.1.4.1.311.10.3.5.1', 'Windows Hardware Driver Extended Verification ': '1.3.6.1.4.1.311.10.3.39', 'Windows Hardware Driver Verification ': '1.3.6.1.4.1.311.10.3.5', 'Windows Kits Component ': '1.3.6.1.4.1.311.10.3.20', 'Windows RT Verification ': '1.3.6.1.4.1.311.10.3.21', 'Windows Software Extension Verification ': '1.3.6.1.4.1.311.10.3.26', 'Windows Store ': '1.3.6.1.4.1.311.76.3.1', 'Windows System Component Verification ': '1.3.6.1.4.1.311.10.3.6', 'Windows TCB Component ': '1.3.6.1.4.1.311.10.3.23', 'Windows Third Party Application Component ': '1.3.6.1.4.1.311.10.3.25', 'Windows Update ': '1.3.6.1.4.1.311.76.6.1', 'Microsoft CertSrv Infrastructure': 'OID', 'Certificate services Certification Authority (CA) version': '1.3.6.1.4.1.311.21.1', 'szOID_CERTSRV_PREVIOUS_CERT_HASH': '1.3.6.1.4.1.311.21.2', 'szOID_CRL_VIRTUAL_BASE': '1.3.6.1.4.1.311.21.3', 'szOID_CRL_NEXT_PUBLISH': '1.3.6.1.4.1.311.21.4', 'szOID_KP_CA_EXCHANGE': '1.3.6.1.4.1.311.21.5', 'szOID_KP_KEY_RECOVERY_AGENT': '1.3.6.1.4.1.311.21.6', 'szOID_CERTIFICATE_TEMPLATE': '1.3.6.1.4.1.311.21.7', 'szOID_ENTERPRISE_OID_ROOT': '1.3.6.1.4.1.311.21.8', 'szOID_RDN_DUMMY_SIGNER': '1.3.6.1.4.1.311.21.9', 'szOID_APPLICATION_CERT_POLICIES': '1.3.6.1.4.1.311.21.10', 'szOID_APPLICATION_POLICY_MAPPINGS': '1.3.6.1.4.1.311.21.11', 'szOID_APPLICATION_POLICY_CONSTRAINTS': '1.3.6.1.4.1.311.21.12', 'szOID_ARCHIVED_KEY_ATTR': '1.3.6.1.4.1.311.21.13', 'szOID_CRL_SELF_CDP': '1.3.6.1.4.1.311.21.14', 'szOID_REQUIRE_CERT_CHAIN_POLICY': '1.3.6.1.4.1.311.21.15', 'szOID_ARCHIVED_KEY_CERT_HASH': '1.3.6.1.4.1.311.21.16', 'szOID_ISSUED_CERT_HASH': '1.3.6.1.4.1.311.21.17', 'szOID_DS_EMAIL_REPLICATION': '1.3.6.1.4.1.311.21.19', 'szOID_REQUEST_CLIENT_INFO': '1.3.6.1.4.1.311.21.20', 'szOID_ENCRYPTED_KEY_HASH': '1.3.6.1.4.1.311.21.21', 'szOID_CERTSRV_CROSSCA_VERSION': '1.3.6.1.4.1.311.21.22', 'Key storage provider name': '1.3.6.1.4.1.311.21.25', 'Certificate': 'OID', 'subjectKeyIdentifier': '2.5.29.14', 'keyUsage': '2.5.29.15', 'privateKeyUsagePeriod': '2.5.29.16', 'issuerAltName': '2.5.29.18', 'basicConstraints': '2.5.29.19', 'cRLNumber': '2.5.29.20', 'reasonCode': '2.5.29.21', 'invalidityDate': '2.5.29.24', 'deltaCRLIndicator': '2.5.29.27', 'certificateIssuer': '2.5.29.29', 'cRLDistributionPoints': '2.5.29.31', 'authorityKeyIdentifier': '2.5.29.35', 'Certificate Extensions': 'OID', 'Authority Key Identifier': '2.5.29.19', 'Basic Constraints': '2.5.29.35', 'Certificate Policies': '2.5.29.32', 'CRL Distribution Points': '2.5.29.31', 'Enhanced Key Usage': '2.5.29.46', 'Issuer Alternative Name': '2.5.29.8', 'Key Usage': '2.5.29.15', 'Name Constraints': '2.5.29.30', 'Policy Constraints': '2.5.29.36', 'Policy Mappings': '2.5.29.33', 'Private Key Usage Period': '2.5.29.16', 'Subject Alternative Name': '2.5.29.17', 'Subject Directory Attributes': '2.5.29.9', 'Subject Key Identifier': '2.5.29.14', 'Extended Key': 'Enable Key Usage Extensions', 'Web Server Certificate': 'Digital Signature, Key Encipherment or Key Agreement', 'Web Client Certificate': 'Digital Signature and/or Key Agreement', 'File Signing .exe': 'Digital Signature', 'E-Mail Protection': 'Digital Signature, non-Repudiation, and/or Key Encipherment or Key Agreement', 'IPSEC Host or Router': 'Digital Signature, Key Encipherment or Key Agreement', 'IPSEC Tunnel': 'Digital Signature, Key Encipherment or Key Agreement', 'Timestamping': 'Digital Signature, non-Repudiation', 'Application': 'Key Usage Extensions', 'SSL Certificate for Client': 'Digital signature', 'SSL Certificate for Server': 'Key encipherment', 'S/MIME Signing': 'Digital signature', 'S/MIME Encryption': 'Key encipherment', 'Certificate Signing': 'Certificate signing', 'Object Signing': 'Digital signature', '': ''}
data = ['2.5.29.37.0', '2.23.133.8.3', '1.3.6.1.4.1.311.20.2.1', '1.3.6.1.5.5.7.3.2', '1.3.6.1.5.5.7.3.3', '1.3.6.1.4.1.311.20.1', '1.3.6.1.4.1.311.10.5.1', '1.3.6.1.4.1.311.21.19', '1.3.6.1.4.1.311.10.3.30', '1.3.6.1.4.1.311.80.1', '1.3.6.1.4.1.311.10.3.12', '1.3.6.1.4.1.311.64.1.1', '1.3.6.1.4.1.311.76.5.1', '1.3.6.1.4.1.311.61.4.1', '1.3.6.1.4.1.311.10.3.8', '1.3.6.1.4.1.311.10.3.4', '2.23.133.8.1', '1.3.6.1.4.1.311.10.3.4.1', '1.3.6.1.4.1.311.61.5.1', '1.3.6.1.5.5.7.3.5', '1.3.6.1.5.5.8.2.2', '1.3.6.1.5.5.7.3.6', '1.3.6.1.5.5.7.3.7', '1.3.6.1.5.2.3.5', '1.3.6.1.4.1.311.61.1.1', '1.3.6.1.4.1.311.10.6.1', '1.3.6.1.4.1.311.10.3.11', '1.3.6.1.4.1.311.21.6', '1.3.6.1.4.1.311.10.6.2', '1.3.6.1.4.1.311.10.3.13', '1.3.6.1.4.1.311.76.8.1', '1.3.6.1.4.1.311.10.3.2', '1.3.6.1.4.1.311.10.3.1', '1.3.6.1.5.5.7.3.9', '1.3.6.1.4.1.311.10.3.7', '2.23.133.8.2', '1.3.6.1.4.1.311.10.3.27', '1.3.6.1.4.1.311.21.5', '1.3.6.1.4.1.311.10.3.22', '1.3.6.1.4.1.311.10.3.24', '1.3.6.1.4.1.311.10.3.10', '1.3.6.1.4.311.54.1.2', '1.3.6.1.4.1.311.10.3.19', '1.3.6.1.4.1.311.10.3.9', '1.3.6.1.5.5.7.3.4', '1.3.6.1.5.5.7.3.1', '1.3.6.1.4.1.311.20.2.2', '1.3.6.1.4.1.311.2.6.2', '1.3.6.1.4.1.311.2.6.1', '1.3.6.1.5.5.7.3.8', '1.3.6.1.4.1.311.10.3.5.1', '1.3.6.1.4.1.311.10.3.39', '1.3.6.1.4.1.311.10.3.5', '1.3.6.1.4.1.311.10.3.20', '1.3.6.1.4.1.311.10.3.21', '1.3.6.1.4.1.311.10.3.26', '1.3.6.1.4.1.311.76.3.1', '1.3.6.1.4.1.311.10.3.6', '1.3.6.1.4.1.311.10.3.23', '1.3.6.1.4.1.311.10.3.25', '1.3.6.1.4.1.311.76.6.1',  '1.3.6.1.4.1.311.21.1', '1.3.6.1.4.1.311.21.2', '1.3.6.1.4.1.311.21.3', '1.3.6.1.4.1.311.21.4', '1.3.6.1.4.1.311.21.5', '1.3.6.1.4.1.311.21.6', '1.3.6.1.4.1.311.21.7', '1.3.6.1.4.1.311.21.8', '1.3.6.1.4.1.311.21.9', '1.3.6.1.4.1.311.21.10', '1.3.6.1.4.1.311.21.11', '1.3.6.1.4.1.311.21.12', '1.3.6.1.4.1.311.21.13', '1.3.6.1.4.1.311.21.14', '1.3.6.1.4.1.311.21.15', '1.3.6.1.4.1.311.21.16', '1.3.6.1.4.1.311.21.17', '1.3.6.1.4.1.311.21.19', '1.3.6.1.4.1.311.21.20', '1.3.6.1.4.1.311.21.21', '1.3.6.1.4.1.311.21.22', '1.3.6.1.4.1.311.21.25', '2.5.29.14', '2.5.29.15', '2.5.29.16', '2.5.29.18', '2.5.29.19', '2.5.29.20', '2.5.29.21', '2.5.29.24', '2.5.29.27', '2.5.29.29', '2.5.29.31', '2.5.29.35', '2.5.29.19', '2.5.29.35', '2.5.29.32', '2.5.29.31', '2.5.29.46', '2.5.29.8', '2.5.29.15', '2.5.29.30', '2.5.29.36', '2.5.29.33', '2.5.29.16', '2.5.29.17', '2.5.29.9', '2.5.29.14']
Data_list = []
str = ''
oid_data = []
count_lst = []
with open('test.cer','rb') as fp:
    cert_data = fp.read().hex()#证书数据
oiddata = tranoid(data)
for item in oiddata:
    oid_data.append("".join(item))
    pass
for oid in oid_data:
    count = cert_data.count(oid,0,len(cert_data))
    count_lst.append(count)
print(count_lst)
print('eeeeeeeeeeee')
lst = list(enumerate(count_lst))
lst_1 = [i for i,x in enumerate(count_lst) if x == 1]
lst_oidvalue = []
for i in lst_1:
    lst_oidvalue.append(data[i])
print(lst_oidvalue)

def get_keys(d, value):
    return [k for k,v in d.items() if v == value]

for value in lst_oidvalue:
    print(get_keys(oid_dict,value))


'''
字典根据value去重
'''
import json
func = lambda z: dict([(x, y) for y, x in z.items()])
new_oid_dict = func(oid_dict)
with open('new_oid_dict.txt','w',encoding='utf-8') as fp:
    json_str = json.dumps(new_oid_dict,indent=0)
    fp.write(json_str)
    fp.write('\n')


print(oid_dict.items())