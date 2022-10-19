# DERcert
## Background
X.509 certificates are encoded by Distinguished Encoding Rules (DER),DER coding always follows a specific data structure,tis data structure consists of three fields: Tag, Length and Value, so it is called TLV structure.Each field consists of one or more bytes. The label specifies the type of the data structure, the length indicates the length of the Value, and the value field stores the data content.</br>
## About OID
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
## Overview
This is a tool to generate new digital certificates based on DER encoded X.509 digital certificate mutation.The tool can effectively mutate X.509 certificates to generate diversified digital certificates.</br>
The flow chart of DERcert is shown below</br>
![process](https://github.com/ydgydg/DERcert/blob/main/image/process_flow.jpg)
## ParseCert
Parse the DER encoded digital certificate into a tree structure. After parsing, an operable binary character file will be obtained.</br>
## Mutation process
We classify the mutation process as OID-guided and non-OID-guided。</br>
### Non-OID-guided mutation process is as follows：</br>
1.Firstly, a digital certificate is selected from the digital certificate library as a seed digital certificate.</br>
2.The seed digital certificate is sent to the certificate parser for parsing，The parser parses the seed digital certificate into a tree structure.</br>
The flow chart of tree structure is shown below</br>                                                             
![Image_test](https://github.com/ydgydg/DERcert/blob/main/image/tree_stru/1.JPG)
3.We mutate based on the tree structure:</br>
  * Leaf node value mutation</br>
  * Deleting a leaf node</br>
  * Add a leaf node</br>
  * Delete the middle node</br>
  * Add the middle node</br>
  * The left and right nodes in the middle are swapped</br>
### OID-guided mutation process is as follows:</br>
We select an OID and locate its position in the tree,and then,we mute the selected OID.The mutation method is the same as that described in Step 3 of non-OID-guided mutation.</br>
## SaveCert
Re-save the mutated binary character file as a digital certificate.</br>
# Requirments
Windows10 or Ubuntu-20.04.3
Python ≥ 3.5</br>
openssl = 1.1.1f</br>
redis = 4.3.4</br>
requests = 2.27.1</br>
matplotlib = 3.5.1</br>
graphviz = 0.20</br>
We provide a Ubuntu environment in floder named "environment"
or</br>
python setup.py install
# Usage
DERcert is very simple to use，You just need to call the appropriate function。Here are the instructions for using DERcert</br>
First, get a digital certificate on the network，as shown in the figure below：
![Image text](https://github.com/ydgydg/DERcert/blob/main/image/step_1.png)</br>
Select a certificate from the digital certificate library for parsing.This step parses the digital certificate into a tree structure and saves it as a binary character file.The parsing process is shown in the following figure：
![Image text](https://github.com/ydgydg/DERcert/blob/main/image/step_2.png)</br>
After parsing, a tree structure will be formed, as shown below.</br>
![Image text](https://github.com/ydgydg/DERcert/blob/main/image/幻灯片11.JPG)</br>
After the parsing, it enters the mutation process，as shown in the figure below：
![Image text](https://github.com/ydgydg/DERcert/blob/main/image/step_3.png)</br>
Finally, the mutated binary character file is saved as a digital certificate.
![Image text](https://github.com/ydgydg/DERcert/blob/main/image/step5.png)</br>

# License
DERCert is licensed under the Mozilla Public License Version2.0.</br>
See the [LICENSE](https://github.com/ydgydg/DERcert/blob/main/LICENSE)
# Contact
You can contact me by email if you have any questions:yangdonggang_123@163.com
