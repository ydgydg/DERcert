# DERcert
This is a tool to generate new digital certificates based on DER encoded X.509 digital certificate mutation.The tool can effectively mutate X.509 certificates to generate diversified digital certificates.</br>
The flow chart of DERcert is shown below</br>
![Image text](https://github.com/ydgydg/DERcert/blob/main/image/%E5%B9%BB%E7%81%AF%E7%89%8714.JPG)
# Requirments
Windows10 or Ubuntu-20.04.3
Python ≥ 3.5</br>
openssl = 1.1.1f</br>
redis = 4.3.4</br>
requests = 2.27.1</br>
matplotlib = 3.5.1</br>
graphviz = 0.20</br>
or</br>
python setup.py install
# About OID
OBJECT IDENTIFIER(OID),Oid types represent standard specifications in a hierarchical form, defined with a dotted decimal decimal symbol.
OID is popular in public key algorithm standards and indicates which hash algorithm the certificate is bound to.</br>
OID encoding rule：</br>
IF the first two parts are defined as x.y, then they will synthesize a byte 40 * x + y,and thw rest will be encoded as a byte alone.
Each byte is first divided into a minimum number of seven digits without the head zero digit. 
The numbers are organized in Big-Endian format and grouped one after the other into bytes. The highest bit (bit 8) of all bytes except the last encoded byte is 1.</br>
Example:</br>
1.Convert 1.2.840.113549.2.5 into a word group{42, 840, 113549, 2, 5}.</br>
2.Then solit every byte into seven digits with the highest bit.{{0x2A},{0x86,0x48},{0x86,0xF7,0x0D},{0x02},{0x05}}.</br>
3.The final complete code is 0x06 08 2A 86 48 86 F7 0D 02 05.
# Usage
DERcert is very simple to use，You just need to call the appropriate function。Here are the instructions for using DERcert</br>
First, get a digital certificate on the network，as shown in the figure below：
![Image text](https://github.com/ydgydg/DERcert/blob/main/image/step_1.png)</br>
Select a certificate from the digital certificate library for parsing.This step parses the digital certificate into a tree structure and saves it as a binary character file.The parsing process is shown in the following figure：
![Image text](https://github.com/ydgydg/DERcert/blob/main/image/step_2.png)</br>
After the analysis, it enters the mutation process，as shown in the figure below：
![Image text](https://github.com/ydgydg/DERcert/blob/main/image/step_3.png)</br>
Finally, the mutated binary character file is saved as a digital certificate.
![Image text](https://github.com/ydgydg/DERcert/blob/main/image/step5.png)</br>
# Contact
You can contact me by email if you have any questions:yangdonggang_123@163.com
