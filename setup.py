'''
use pip install --editable . to install db_cli as system command
'''


from setuptools import setup


setup(
    name='db_cli',
    version='0.0.1',
    py_modules=['db_cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        db_cli=db_cli:cli
    ''',
)
