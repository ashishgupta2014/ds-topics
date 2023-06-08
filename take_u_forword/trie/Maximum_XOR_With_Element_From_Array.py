"""
https://leetcode.com/problems/maximum-xor-with-an-element-from-array/description/
https://takeuforward.org/trie/maximum-xor-queries-trie/

"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert_bits(self, num):
        bit_num = bin(num)[2:].zfill(32)
        node = self.root
        for bit in bit_num:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def find_max_xor(self, num):
        bit_num = bin(num)[2:].zfill(32)
        node = self.root
        max_xor = ''
        for bit in bit_num:
            if bit == '0':
                oppo_bit = '1'
            elif bit == '1':
                oppo_bit = '0'

            if oppo_bit in node.children:
                max_xor += oppo_bit
                node = node.children[oppo_bit]
            else:
                max_xor += bit
                node = node.children[bit]

        return int(max_xor, 2) ^ num
    def maximizeXor(self,  nums: List[int], queries: List[List[int]]) -> List[int]:
        for num in nums:
            self.insert_bits(num)

        result = [-1]*len(queries)
        for i, ele in enumerate(queries):
            x = ele[0]
            m = ele[1]
            for num in nums:
                if num <= m:
                    result[i] = max(result[i], num ^ x)

        return result

solve = Solution()
print(solve.maximizeXor(nums=[0,1,2,3,4], queries=[[3,1],[1,3],[5,6]]))