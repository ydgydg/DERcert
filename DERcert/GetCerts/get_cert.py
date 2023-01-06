
import socket
from OpenSSL import SSL, crypto
from multiprocessing.pool import ThreadPool


cert = None

pool = ThreadPool(20)


def do_connect(hostname, p, level):
    '''
    function:Start the connection
    :param hostname:Hostname of website
    :param p:Address
    :param level:One of SSLv2_METHOD, SSLv3_METHOD, SSLv23_METHOD, or
        TLSv1_METHOD.
    :return:Certchain
    '''
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    context = SSL.Context(level)
    conn = SSL.Connection(context, s)
    conn.connect((hostname, p))
    conn.do_handshake()
    return conn.get_peer_cert_chain()


def get_certificate(hostname,port=443, file_path='./certs/', Thr=None):
    '''
    function:Get a digital certificate and download it
    :param hostname: Name of website
    :param port: Port number,default port num is 443
    :param file_path:Path to store digital certificates
    :param Thr:Thread
    '''
    global cert
    try:
        cert = do_connect(hostname, port, SSL.SSLv23_METHOD)
    except Exception:
        try:
            cert = do_connect(hostname, port, SSL.TLSv1_1_METHOD)
        except Exception:
            try:
                cert = do_connect(hostname, port, SSL.TLSv1_2_METHOD)
            except Exception as e:
                if Thr:
                    print(Thr)
                    Thr.emit('Get {domain} Error: {err}'.format(domain=hostname, err=e))
                else:
                    print('Get {domain} Error:'.format(domain=hostname), e)
                return

    print(cert)
    try:
        cert_nums = len(cert)
        now_num = 0
        for cert_item in cert:
            now_num += 1
            try:
                temp_certname = '{domain}_{num}.pem'.format(domain=file_path + hostname, num=now_num)

                with open(temp_certname, 'wb+') as output_file:
                    output_file.write(crypto.dump_certificate
                                      (crypto.FILETYPE_PEM, cert_item))
                if Thr:
                    print(Thr)
                    Thr.emit('Get {domain} \'s {num} cert!'.format(domain=hostname, num=now_num))
                else:
                    print('Get {domain} \'s {num} cert!'.format(domain=hostname, num=now_num))
            except IOError:
                if Thr:
                    print(Thr)
                    Thr.emit('Get {domain} Error: {err}'.format(domain=hostname, err=IOError.strerror))
                else:
                    print('Get {domain} Error:'.format(domain=hostname), IOError.strerror)
    except Exception as e:
        if Thr:
            print(Thr)
            Thr.emit('Get {domain} Error: {err}'.format(domain=hostname, err=e))
        else:
            print('Get {domain} Error:'.format(domain=hostname), e)


def get_cert_batch(web_site,port,store_path):
    '''
    function:Download digital certificates in batches according to the URL
    :param web_site: Website address
    :param port: Port number,using port 443
    :param store_path: Digital certificate storage path
    '''
    web_address = []
    for line in open(web_site):
        rs = line.rstrip('\n')
        web_address.append(rs)
    for item in web_address:
        get_certificate(item,port,store_path)
