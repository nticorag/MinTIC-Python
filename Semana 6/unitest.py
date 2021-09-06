import unittest
from parqueadero import *

class Prueba(unittest.TestCase):
    def testCrearParqueadero(self):
        p = Parqueadero(4,3,5000,2000)
        self.assertEqual(len(p.matriz),4)
        self.assertEqual(len(p.matriz[0]),3)

    def prueba(self):
        self.assertTrue(True)


if __name__ ==  "__main__":
    unittest.main()