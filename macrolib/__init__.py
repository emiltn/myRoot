import os
packages = os.listdir(os.path.dirname(__file__))


for package in packages:
    if "bar" in package:
        from .bar.macrolib import bar
    elif "foo" in package:
        from .foo.macrolib import foo