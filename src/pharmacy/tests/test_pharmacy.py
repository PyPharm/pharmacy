import sys, unittest
from importlib.machinery import  SourceFileLoader

pharmacy = SourceFileLoader("pharmacy", "../pharmacy/__init__.py").load_module()
print( f' {pharmacy.__version__}  ')

class InitTest(unittest.TestCase):
    def test_version(self):
        pass


if __name__ == "__main__":
    unittest.main()


