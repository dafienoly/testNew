#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/10/18 13:21:28
@Author  :   liuyang
@Version :   1.0
@Contact :   liuyang6890@163.com
@License :   (C)Copyright Liuyang
@Desc    :   None
'''

from Queue import Queue


class Solution(object):
    def upNum(self, cur):
        return str((int(cur) + 1) % 10)

    def downNum(self, cur):
        if cur == '0':
            return '9'
        return str(int(cur) - 1)

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        cur = '0000'
        visited = set(deadends)
        if cur in visited or target in visited:
            return -1
        q = Queue()
        q.put(cur)
        minCount = 0
        while not q.empty():
            size = q.qsize()
            for i in xrange(size):
                cur = q.get()
                if cur in visited:
                    continue
                if cur == target:
                    return minCount
                visited.add(cur)
                nums = list(cur)
                for i, num in enumerate(cur):
                    nums[i] = self.upNum(num)
                    q.put(''.join(nums))
                    nums[i] = self.downNum(num)
                    q.put(''.join(nums))
                    nums[i] = num
            minCount += 1
        return -1
