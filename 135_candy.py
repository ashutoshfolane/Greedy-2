"""
Leetcode: https://leetcode.com/problems/candy/

Approach: Using one array, find ratings first for left side and then right side
Time complexity : O(n). The array candies of size n is traversed twice.
Space complexity : O(n). An array candies of size n is used.
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if ratings is None or len(ratings) is 0:
            return 0

        num_children = len(ratings)
        if num_children == 1:
            return 1

        candies = [1] * num_children

        # left side
        for i in range(1, num_children):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        sumc = candies[num_children - 1]

        # right side
        for i in reversed(range(num_children-1)):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1]+1, candies[i])
            sumc += candies[i]
        return sumc
