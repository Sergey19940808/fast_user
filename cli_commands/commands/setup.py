from setuptools import setup

setup(
    name='cli_commands',
    version='0.1',
    py_modules=['filled_data'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        filled_data=filled_data:filled_user_store
    ''',
)