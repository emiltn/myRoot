import os
import pip
from six import iteritems
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

#REFERENCE: https://medium.com/@jherreras/python-microlibs-5be9461ad979

PACKAGE_NAME = 'macrolib'
SOURCES = {
  'macrolib.foo': 'microlibs/foo',
  'macrolib.bar': 'microlibs/bar',
}

def install_microlibs(sources, develop=False):
    """ Use pip to install all microlibraries.  """
    print("installing all microlibs in {} mode".format("development" if develop else "normal"))
    wd = os.getcwd()
    for k, v in iteritems(sources):
        try:
            os.chdir(os.path.join(wd, v.root_dir))
            if develop:
                pip.main(['install', '-e', '.'])
            else:
                pip.main(['install', '.'])
        except Exception as e:
            print("Oops, something went wrong installing", k)
            print(e)
        finally:
            os.chdir(wd)

class DevelopCmd(develop):
    """ Add custom steps for the develop command """
    def run(self):
        install_microlibs(SOURCES, develop=True)
        develop.run(self)

class InstallCmd(install):
    """ Add custom steps for the install command """
    def run(self):
        install_microlibs(SOURCES, develop=False)
        install.run(self)
setup(
    name=PACKAGE_NAME,
    version="0.1.0",
    author="yourname",
    author_email="yourname@email.com",
    description="Macrolib's description",
    license="TBD",
    classifiers=[
        'Private :: Do Not Upload to pypi server',
    ],
    install_requires=[
        'future',
        'six',
    ],
    cmdclass={
        'install': InstallCmd,
        'develop': DevelopCmd,
    },
)