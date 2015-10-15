try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    description='Tech@NYU API Python Client',
    author='TechatNYU',
    url='https://github.com/TechAtNYU/pytnyu',
    author_email='hello@techatnyu.org',
    version='0.0.4',
    install_requires=['requests'],
    namespace_packages=['pytnyu'],
    name='pytnyu',
)
