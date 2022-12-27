"""
https://workat.tech/problem-solving/practice/excel-column

https://www.geeksforgeeks.org/find-excel-column-number-column-title/
"""
class Solution:
	def getColumnNumber(self, excelColumnNumber: str) -> int:
		result = 0
		for i in excelColumnNumber:
			result *= 26
			result += ord(i)-ord('A')+1
		return result

solve = Solution()
print(solve.getColumnNumber(excelColumnNumber='AA'))
print(solve.getColumnNumber(excelColumnNumber='CDA'))
print(solve.getColumnNumber(excelColumnNumber='ABAC'))