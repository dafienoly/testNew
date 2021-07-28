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

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS
import sys
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        minLen = sys.maxsize
        if root.left is not None:
            minLen = min(minLen, self.minDepth(root.left))
        if root.right is not None:
            minLen = min(minLen, self.minDepth(root.right))
        return minLen + 1


# BFS
import Queue
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        minDepth = 1
        q = Queue.Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            for i in xrange(size):
                node = q.get()
                if node.left is None and node.right is None:
                    return minDepth
                node.left and q.put(node.left)
                node.right and q.put(node.right)
            minDepth += 1
        return minDepth
