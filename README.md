# DERcert
This is a tool to generate new digital certificates based on DER encoded X.509 digital certificate mutation.The tool can effectively mutate X.509 certificates to generate diversified digital certificates.</br>
The flow chart of DERcert is shown below</br>
![Image text](https://github.com/ydgydg/DERcert/blob/main/image/%E5%B9%BB%E7%81%AF%E7%89%8714.JPG)
# Requirments
Python≥3.5</br>
openssl1.1.1f</br>
redis4.3.4</br>
requests2.27.1</br>
matplotlib3.5.1</br>
graphviz 0.20</br>
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

