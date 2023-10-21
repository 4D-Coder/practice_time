import ipdb
import re

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    word = s
    anagram = t
    if len(word) != len(anagram):
      return False

    for letter in word:
      anagram = re.sub(letter, '', anagram, count=1)

    return bool(not anagram)
