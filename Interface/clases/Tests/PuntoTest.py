import unittest

from ..clases import Punto

class MyTestCase(unittest.TestCase):
    testValue=1
    def test_getX(self):

        punto = Punto(self.testValue, 2)
        self.assertEqual(punto.getXCoordenade(),self.testValue )

    def test_getY(self):

        punto = Punto(1, self.testValue)
        self.assertEqual(punto.getYCoordenade(), self.testValue)  # add assertion here

    def test_setX(self):
        punto = Punto(10, 20)
        punto.setXCoordenade(self.testValue)
        self.assertEqual(punto.getXCoordenade(), self.testValue)

    def test_setY(self):

        punto = Punto(10, 20)
        punto.setYCoordenade(self.testValue)
        self.assertEqual(punto.getYCoordenade(), self.testValue)  # add assertion here


if __name__ == '__main__':
    unittest.main()
