import unittest
import numpy as np

class TestBasic(unittest.TestCase):
    def test_drake_import_and_foo(self):
        from foo_binding import foo
        print("foo imported")
        x1 = np.ones((3,))
        x2 = -5*np.ones((3,))
        self.assert_(np.allclose(-4*np.ones((3,1)), foo(x1,x2)))
        print(f"numpy version {np.__version__}")
        from pydrake.all import (RobotDiagramBuilder,
                         LoadModelDirectives,
                         ProcessModelDirectives,
                         SceneGraphCollisionChecker,
                         QueryObject, 
                         SceneGraphInspector)
  

if __name__ == "__main__":
  unittest.main()