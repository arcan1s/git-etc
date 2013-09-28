import os
from distutils.core import setup

os.putenv('TAR_OPTIONS', '--owner root --group root --mode a+rX')

setup(
    name = 'ctrlconf',
    version = '2.2.2',
    license = 'GPL',
    description = 'GUI for git-etc daemon',
    url = 'https://github.com/arcan1s/git-etc',
    author = 'Evgeniy Alekseev',
    author_email = 'esalexeev@gmail.com',
    packages = ['ctrlconf'],
    py_modules = ['ctrlconf']
)
