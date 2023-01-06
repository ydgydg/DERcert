import subprocess
import os
def filenamelist(filepath):
    '''
    :param filepath: Path to store the DER certificate
    :return: The list of certname
    '''
    DERcertnamelst = os.listdir(filepath)
    return DERcertnamelst


def convert(file_path_pem, file_path_der):
    '''
    :param filepath: Path to store the DER certificate
    '''
    cmd_ret_list = []
    cmd_context_list = []
    pemcertnamelst = filenamelist(file_path_pem)
    for i in range(0, len(pemcertnamelst)):
        try:
            cmd_ret, cmd_context = subprocess.getstatusoutput(
                "openssl x509 -inform pem -in {0} -out {1}".format(file_path_pem + pemcertnamelst[i],
                                                                                      file_path_der + str(i) + ".der"))
            cmd_ret_list.append(cmd_ret)
            cmd_context_list.append(cmd_context)
        except:
            print("Error in converting")


