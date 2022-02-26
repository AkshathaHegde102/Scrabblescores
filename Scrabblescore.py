'''
Created on 2/3/2022
@author:   Akshatha Vasant Hegde
filename: hw2.py
pledge: I pledge my honor that I have abided by the Stevens Honor System.
CS515 - Hw 2
'''
import sys
import functools
from functools import reduce
#from dict import *
# Remove # from above if you want to import the big dictionary

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Global values
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Functions implemented here

def letterScore(letter,scorelist):
    ''' Returns the score of the letter '''
    if letter == scorelist[0][0] :
        return scorelist[0][1]    
    else :
        return letterScore(letter,scorelist[1:])
        

def wordScore (S, scorelist):
    ''' Returns the word score - sum of all letter scores in the word '''
    if len(S) == 0 :
        return 0
    else :
        x = letterScore(S[0], scorelist) + wordScore(S[1:],scorelist);
        return x


def wordcomp(word, r):
    ''' Checks if word can be made with rack '''
    if len(word) == 0 :
        return True
    elif word[0] in r :
        r.remove(word[0])
        return wordcomp(word[1:], r)
    else :
        return False

def listele(diction):
    ''' Gives the word and its score in a list '''
    r = Rack.copy()
    if wordcomp(diction, r) is True:
        x = [diction]
        y = [wordScore(diction, scrabbleScores)]
        return x + y
    else :
        return []

def TFfunc(a):
    ''' For the filter function. Returns True or False '''
    if a == []:
        return False
    else:
        return True

def scoreList(x):
    ''' Returns a list of words possible with their scores '''
    global Rack
    Rack = x;
    z = filter(TFfunc,map(listele,Dictionary))
    return (list(z))

def bestWord(x):
    ''' Returns a list of words possible with their scores '''
    s = scoreList(x)
    if s == [] :
        return ['', 0]
    else :
        m = reduce(maxx,s)
        return m


def maxx(a,b):
    ''' Find the max of two given lists'''
    if a == ['',0] or b ==['',0] :
        return ['',0]
    elif (b[1]) > (a[1]) :
        return b
    else :
        return a
'''

# test functions

import unittest
import operator
import hw2
class Test(unittest.TestCase):
    def test01(self):
        self.assertEqual(hw2.letterScore('a', hw2.scrabbleScores), 1)
        self.assertEqual(hw2.letterScore('c', hw2.scrabbleScores), 3)
        self.assertEqual(hw2.letterScore('q', hw2.scrabbleScores), 10)
        self.assertEqual(hw2.letterScore('t', hw2.scrabbleScores), 1)
        self.assertEqual(hw2.letterScore('x', hw2.scrabbleScores), 8)
    def test02(self):
        self.assertEqual(hw2.wordScore('a', hw2.scrabbleScores), 1)
        self.assertEqual(hw2.wordScore('spam', hw2.scrabbleScores), 8)
        self.assertEqual(hw2.wordScore('apple', hw2.scrabbleScores), 9)
        self.assertEqual(hw2.wordScore('computer', hw2.scrabbleScores), 14)
        self.assertEqual(hw2.wordScore('wow', [['o', 10], ['w', 42]]), 94)
    def test03(self):
        scores = hw2.scoreList(['a', 's', 'm', 't', 'p'])
        # Sort by scores
        scores.sort(key=operator.itemgetter(1))
        self.assertEqual(scores, [['a', 1], ['at', 2], ['am', 4], ['spam', 8]])
    def test04(self):
        scores = hw2.scoreList(['r', 's', 't', 'n', 'l', 'e', 'a'])
        # Sort by scores
        scores.sort(key=operator.itemgetter(1))
        self.assertEqual(scores, [['a', 1], ['at', 2]])
    def test05(self):
        scores = hw2.scoreList(['b', 't', 'f', 'c', 'a', 'o'])
        # Sort by scores
        scores.sort(key=operator.itemgetter(1))
        self.assertEqual(scores, [['a', 1], ['at', 2], ['bat', 5]])
    def test06(self):
        scores = hw2.scoreList(['a', 's', 'm', 'o', 'f', 'o'])
        # Sort by scores
        scores.sort(key=operator.itemgetter(1))
        self.assertEqual(scores, [['a', 1], ['am', 4], ['foo', 6]])
    def test07(self):
        self.assertEqual(hw2.bestWord(['a']), ['a', 1])
    def test08(self):
        self.assertEqual(hw2.bestWord(['a', 's', 'm', 't', 'p']), ['spam', 8])
    def test09(self):
        self.assertEqual(hw2.bestWord(['g', 'y', 'e']), ['', 0])
    def test10(self):
        self.assertEqual(hw2.bestWord(['b', 'b', 'b', 'l', 'r', 'a', 'e']), 
['babble', 12])
if __name__ == "__main__":
    unittest.main()


'''   
