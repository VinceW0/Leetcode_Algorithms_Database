"""
1573. Number of Ways to Split a String
Medium

Given a binary string s (a string consisting only of '0's and '1's), we can split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).

Return the number of ways s can be split such that the number of characters '1' is the same in s1, s2, and s3.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: s = "10101"
Output: 4
Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"
Example 2:

Input: s = "1001"
Output: 0
Example 3:

Input: s = "0000"
Output: 3
Explanation: There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"
Example 4:

Input: s = "100100010100110"
Output: 12
 

Constraints:

s[i] == '0' or s[i] == '1'
3 <= s.length <= 10^5
"""


class Solution:
    def numWays(self, s: str) -> int:
        ones, n = s.count('1'), len(s)
        if ones == 0:
            return (n - 2) * (n - 1) // 2 % (10**9 + 7)
        if ones % 3 != 0:
            return 0
        ones //= 3
        count = lo = hi = 0
        for char in s:
            if char == '1':
                count += 1
            if count == ones:
                lo += 1
            elif count == 2 * ones:
                hi += 1
        return lo * hi % (10**9 + 7)

        
