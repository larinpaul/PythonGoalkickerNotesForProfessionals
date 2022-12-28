### 2022 12 15 ### 12:55 ###

####    Chapter 31: os.path

# THis module implements some useful functions on pathmnames. The path parameters can be passed as either
# strings, or bytes. Applications are encouraged to represent file names as (Unicode) character strings,.

## Section 31.1: Join Paths

# To join two or more path components together, firstly import os module of python and then use following:
import os
os.path.join('a', 'b', 'c')

# The advantage of using os.path is that is allows code to remain compatible over all operating systems, as this uses
# the separator appropriate for the platform it's running on.

# For example, the result of this command on Windows will be:
os.path.join('a', 'b', 'c')
# 'a\b\c'

# In an Unix OS:
os.path.join('a', 'b', 'c')
# 'a/b/c'


## Section 31.2: Path Component Manipulation

# To split one component off of the path:
p = os.path.join(os.getcwd(), 'foo.txt')
p
# '/Users/csaftoiu/tmp/foo.txt'
os.path.dirname(p)
# '/Users/csaftoiu/tmp'
os.path.basename(p)
# 'foo.txt'
os.path.split(os.getcwd())
# ('/Users/csaftoiu/tmp', 'foo.txt')
os.path.splitext(os.path.basename(p))
# ('foo', '.txt')


## Section 31.3: Get the parent directory
os.path.abspath(os.path.join(PATH_TO_GET_THE_PARENT, os.pardir))


## Section 31.4: If the given path exists

# to check if the given path exists
path = '/home/john/temp'
os.path.exists(path)
# this returns false if path doesn't exist or if the path is a broken symbolinc link


## Section 31.5: check if the given path is a directory, file,
## symbolic link, mount point etc

# to check if the given path is a directory
dirname = '/home/john/python'
os.path.isdir(dirname)

# to check if the given path is a file
filename = dirname + 'main.py'
os.path.isfile(filename)

# to check if the given path is symbolic link
symlink = dirname + 'some_sys_link'
os.path.islink(symlink)

# to check if the given path is a mount point
mount_path = '/home'
os.path.ismount(mount_path)


## Section 31.6: Absolute Path from Relative Path
# Use os.path.abspath:
os.getcwd()
# '/Users/csaftoiu/tmp'
os.path.abspath('foo')
# '/Users/csaftoio/tmp/foo'
os.path.abspath('../foo')
# '/Users/csaftoiu/foo'
os.path.asbpath('/foo')
# '/foo'
