import ipdb
import re
import string

class Solution:
  def isPalindrome(self, text: str) -> bool:
    comparison = self.create_comparison(text.lower())
    return comparison[0] == comparison[1]

  def create_comparison(self, text) -> str:
    translator = str.maketrans('', '', string.punctuation)
    scrubbed = text.translate(translator)
    joined = re.sub(' ', '', scrubbed)
    return (joined, joined[::-1])

