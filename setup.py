import os
import subprocess
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


# REFERNECE: https://medium.com/@jherreras/python-microlibs-5be9461ad979

PACKAGE_NAME = 'macrolib'
SOURCES = {
    'macrolib.bar': 'macrolib/bar',
    'macrolib.foo': 'macrolib/foo',

}


def install_microlibs(sources, develop=False):
    """ Use pip to install all microlibraries.  """
    print("installing all microlibs in {} mode".format("development" if develop else "normal"))
    wd = os.getcwd()
    for k, v in sources.items():
        try:
            os.chdir(os.path.join(wd, v))
            if develop:
                _cmd = ['pip install', '-e', '.']
            else:
                _cmd = ['pip install', '.']

            cmd_str = " ".join(_cmd)
            print(cmd_str)
            subprocess.call(cmd_str, shell=True)

        except Exception as e:
            print("Oops, something went wrong installing", k)
            print(e)
        finally:
            os.chdir(wd)


class DevelopCmd(develop):
    """ Add custom steps for the develop command """
    def run(self):
        install_microlibs(SOURCES, develop=True)
        #print("#" * 100)
        #help(self)
        #print("#" * 100)
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
    install_requires=['numpy',],
    cmdclass={
        'install': InstallCmd,
        'develop': DevelopCmd,
    },
)