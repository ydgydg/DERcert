import os
import subprocess

def save_der():
    '''
    function:Call C# to save the certificate
    :return: Saved successfully
    '''
    subprocess.getstatusoutput('mono save_as_der.exe')


