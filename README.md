# root
Microlib tutorial

Clone subpackages (how to work through)\
First, clone complete repository with '-n' argument:\
git clone -n https://github.com/emiltoft/root.git

Next, configue git to use sparse-checkout:\
git config core.sparsecheckout true

Next, add or chance ".git/info/sparse-checkout" file to include files and folders to pull.\
This can be done from terminal or changed directly in the file using a text editor.\
From the terminal:\
Mandatory files for full functionality:\
echo /.gitignore >> .git/info/sparse-checkout\
echo /setup.py >> .git/info/sparse-checkout\
echo /uninstall.py >> .git/info/sparse-checkout\
echo /requirements.txt >> .git/info/sparse-checkout\
echo macro-lib/__init__.py >> .git/info/sparse-checkout\

The ".git/info/sparse-checkout" now looks like (you can se it using this command: "head .git/info/sparse-checkout"):\
/.gitignore\
/setup.py\
/uninstall.py\
/requirements.txt\
macro-lib/__init__.py

Now, specify the packages from terminal (eg. package: "bar"):\
echo macrolib/bar/* >> .git/info/sparse-checkout

This adds an aditionally line to the "sparse-checkout" file (if manual editing just copy and paste the following lines to the "sparse-checkout" file - remember to change the packages names!)\
The sparse-checkout file ends up looking like (you can se it using this command: "head .git/info/sparse-checkout"):\
/.gitignore\
/setup.py\
/uninstall.py\
/requirements.txt\
macro-lib/__init__.py\
macrolib/bar/*

Next, now the sparse-checkout file is completed its time to update your local copy 
of the repository with the fils and folders specified in the "sparse-checkout" file. 
When changing the "sparse-checkout" file run the read-tree again to update the repository.\
git read-tree -mu HEAD

Once the setup is complete its possible to push and pull as normally done with git.
