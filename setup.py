from setuptools import setup,find_packages
setup(
    name = 'DERcert',
    version = '1.0',
    install_requires = ['openssl','redis','requests',
                        'matplotlib=3.5.1','graphviz']
)