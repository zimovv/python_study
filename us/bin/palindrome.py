#!/usr/bin/env python
import sys
lst = ['Radar', 'Lemon', 'aka', 'Do geese see God']

def is_palindrome(letters):
    #TODO: implement the algorithm
    letters = ''.join(letters.split())
    letters_v = letters[::-1]
    if letters_v.lower() == letters.lower():
        return letters


if __name__ == '__main__':
    #TODO: Use built-in functions map or filter to filter out the palindromes
    #it = map(...)
    #it = filter(...)
    
    #it = map(is_palindrome, lst)  #This will give out redundant 'None'
    it = filter(is_palindrome, lst)
    
    #Print palindroms
    for i in it:
        print i
