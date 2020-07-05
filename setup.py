import setuptools

with open('README.md') as fp:
    long_description = fp.read()
# long_description = None

setuptools.setup(
    name = 'BitIO2',
    version = '1.1.0',
    url = 'https://github.com/gaming32/BitIO',
    author = 'Gaming32',
    author_email = 'gaming32i64@gmail.com',
    license = 'License :: OSI Approved :: MIT License',
    description = 'A library for manipulating files via bits',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    install_requires = [
        'bitarray',
    ],
    py_modules = [
        'bitio',
    ],
)