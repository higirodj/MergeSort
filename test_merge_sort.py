#!/usr/bin/python

import unittest
import random

from merge_sort import mergeSort 

class test_merge_sort(unittest.TestCase):
    
    # Test sequence of arbitrarily ordered positive random numbers
    def test_mergeSort(self):
        a = [random.random() for i in range(10000)]
        self.assertEqual(a.sort(), mergeSort(a))
    
    # Test sequence of arbitrarily ordered negative random numbers
    def test_mergeSortNegativeNumbers(self):
        a = [random.random()*-1 for i in range(10000)]
        self.assertEqual(a.sort(), mergeSort(a))
    
    # Test sequence of random numbers in descending order
    def test_mergeSortDescending(self):
        a = [random.random() for i in range(100)]
        a.sort()
        b = a[::-1]
        self.assertEqual(b.sort(), mergeSort(b))

    # Test sequence of arbitrarily ordered random numbers with an odd length
    def test_mergeSortOddLength(self):
        a = [random.random() for i in range(111)]
        self.assertEqual(a.sort(), mergeSort(a))

    # Test sequence of arbitrarily ordered random numbers with an even length
    def test_mergeSortEvenLength(self):
        a = [random.random() for i in range(110)]
        self.assertEqual(a.sort(), mergeSort(a))
    
    # Test sequence with single element
    def test_mergeSortSinglElement(self):
        a = [i for i in range(1)]
        self.assertEqual(a.sort(), mergeSort(a))

    # Test a sequence of duplicate numbers
    def test_mergeSortDuplicates(self):
        a = [2]*100
        self.assertEqual(a.sort(), mergeSort(a))

if __name__ == '__main__':
    unittest.main()
    



