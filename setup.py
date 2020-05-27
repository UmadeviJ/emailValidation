from setuptools import setup

setup(
    name='mypackage',
    version='1.0',
    packages=['biogen'],
    url='https://github.com/UmadeviJ/emailValidation.git',
    license='MIT',
    author='uma',
    author_email='uma.omnn@gmail.com',
    download_url="",
    description='To Verify email',
    install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ]
)
