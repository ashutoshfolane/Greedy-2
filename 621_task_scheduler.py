"""
Leetcode: https://leetcode.com/problems/task-scheduler/

Approach: Greedy

Time Complexity: O(N), where N is a number of tasks to execute. This time is needed to iterate over the input
array tasks and compute the array frequencies. Array frequencies contains 26 elements, and hence all operations
with it takes constant time.

Space Complexity: O(1), to keep the array frequencies of 26 elements.
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n

        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)