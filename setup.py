from setuptools import setup,find_packages
setup(
    name = 'DERcert',
    version = '1.0',
    install_requires = ['openssl=1.1.1f','redis=4.3.4','requests2.27.1',
                        'matplotlib=3.5.1','graphviz=-0.20']
)