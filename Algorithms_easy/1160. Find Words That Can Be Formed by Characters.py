"""
1160. Find Words That Can Be Formed by Characters
Easy

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        char_cnt = Counter(chars)
        for wd in words:
            wd_cnt = Counter(wd)
            for c in wd_cnt:
                if wd_cnt[c] > char_cnt[c]:
                    break
            else:
                res += len(wd)
        return res




class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(not Counter(w) - Counter(chars) and len(w) for w in words)


