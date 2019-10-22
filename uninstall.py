import os
import pkgutil
import subprocess

def uninstall_microlibs(sources):
    """ Use pip to install all microlibraries.  """
    if not sources:
        print("Found no packages to uninstall with name: %s" %PACKAGE_NAME)
        return

    print("uninstalling all microlibs")
    for microlib in sources:
        try:
            _cmd = ['pip uninstall -y', microlib]

            cmd_str = " ".join(_cmd)
            print(cmd_str)
            subprocess.call(cmd_str, shell=True)

        except Exception as e:
            print("Oops, something went wrong uninstalling", microlib)
            print(e)


PACKAGE_NAME = 'macrolib'
PRINT = False
if __name__ == '__main__':

    libs = []

    pip_list = os.popen("pip list").readlines()
    for module in pip_list:
        if not PACKAGE_NAME in module: continue
        if PRINT:
            module = module.replace("\n", "")
            print(module)
        name, version = module.split(maxsplit=1)
        libs.append(name)

    uninstall_microlibs(libs)
