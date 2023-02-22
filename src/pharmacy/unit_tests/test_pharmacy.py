# https://docs.python.org/3/library/unittest.html

import sys, unittest
from importlib.machinery import  SourceFileLoader

#   Dear world, I am sorry about this narfangley file structure.  "Poetry" made me do it... after a series of
#       unfortunate decisions compounded.     DRL   2023-02-18
pharmacy = SourceFileLoader("pharmacy", "../pharmacy/__init__.py").load_module()
print( f' {pharmacy.__version__}  ')

class InitTest(unittest.TestCase):
    def test_version(self):
        pass


if __name__ == "__main__":
    unittest.main()


