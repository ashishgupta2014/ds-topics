"""
https://workat.tech/problem-solving/practice/gcd

https://www.geeksforgeeks.org/program-to-find-gcd-or-hcf-of-two-numbers/
"""
class Solution:
	def gcd(self, firstNum: int, secondNum: int) -> int:
		if secondNum == 0:
			return firstNum
		return self.gcd(secondNum, firstNum%secondNum)

solve = Solution()
print(solve.gcd(8,12))