# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/palindrome-number/#/description
# Author: Wang Hao
# Date  : 2017-06-29

'''

9. Palindrome Number -- Easy

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

    Some hints:
    Could negative integers be palindromes? (ie, -1)

    If you are thinking of converting the integer to string,
    note the restriction of using extra space.

    You could also try reversing an integer.
    However, if you have solved the problem "Reverse Integer",
    you know that the reversed integer might overflow.
    How would you handle such case?

    There is a more generic way of solving this problem.

'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False
            x = (x % ranger) / 10
            ranger /= 100

        return True

    def isPalindromeTest(self):
        tDict = {
            1: {'in': -1, 'out': False},
            2: {'in': 0, 'out': True},
            3: {'in': 12321, 'out': True},
            4: {'in': 3443, 'out': True},
        }

        for tNo, case in tDict.iteritems():
            print tNo,
            print 'ok' if case['out'] == self.isPalindrome(case['in']) else 'fail'

Solution().isPalindromeTest()
