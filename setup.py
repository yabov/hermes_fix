from setuptools import setup, find_packages

setup(
    name='hermes_fix',
    version='0.0.1',
    description='Python based FIX engine',
    url='https://github.com/yabov/hermes_fix.git',
    author='Yevgeny Abov',
    author_email='yevgeny.abov@gmail.com',
    license='unlicense',
    packages=find_packages(exclude=['tests*', 'examples*']),
    zip_safe=False
)
