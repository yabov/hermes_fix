from setuptools import setup, find_packages
import sys

# check minimum supported Python version
if sys.version_info[:2] < (3, 7):
    raise Exception("Python 3.7 or higher is required.")


setup(
    name='hermes_fix',
    version='0.2',
    description='Python based FIX engine',
    url='https://github.com/yabov/hermes_fix.git',
    author='Yevgeny Abov',
    author_email='yevgeny.abov@gmail.com',
    license='Apache 2.0',
    packages=find_packages(exclude=['tests*', 'examples*']),
    install_requires=[
        'sqlalchemy',
        'python-dateutil',
    ],
    zip_safe=False
)
