# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5), 'Right', '3,4,5 is a Right triangle') #ID1
 
        
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4), 'Right', '5,3,4 is a Right triangle')#ID2

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(6,8,10), 'Right', '6,8,10 is a Right triangle')#ID3

    # Equilateral triangle tests
    def testEquilateralTriangle(self): 
        self.assertEqual(classifyTriangle(1,1,1), 'Equilateral', '1,1,1 should be Equilateral')#ID4
    
    # Isosceles triangle tests
    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles', '2,2,3 should be Isosceles')#ID5

    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isoceles', '5,5,8 should be Isosceles')#ID6
    
    # Scalene triangle tests
    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4,5,6 should be Scalene')#ID7
    
    # Invalid input tests
    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(0, 5, 6), 'InvalidInput', '0,5,6 should be InvalidInput')#ID8

    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(201, 5, 6), 'InvalidInput', '201,5,6 should be InvalidInput')#ID9

    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle(-1, 5, 6), 'InvalidInput', '-1,5,6 should be InvalidInput')#ID10

    def testInvalidInputD(self): 
        self.assertEqual(classifyTriangle(4.5, 5, 6), 'InvalidInput', '4.5,5,6 should be InvalidInput')#ID11

    # Not a triangle tests
    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle', '1,10,12 should be NotATriangle')#ID12

    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 should be NotATriangle')#ID13

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

