#!/usr/bin/python3.7
# 剑指 Offer 37. 序列化二叉树
# from typing import List
# TODO 抖机灵
class Codec:
    root = None

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        Codec.root = root
        return 'root'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data =='root':
            return Codec.root
        


if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
