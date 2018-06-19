

# Two Sum IV - Input is a BST
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# straightforward method
class Solution(object):

    def findTarget(self, root, k):
        if not root: return False
        bfs, s = [root], set()
        for el in bfs:
            if k - el.val in s: return True
            s.add(el.val)
            if el.left: bfs.append(el.left)
            if el.right: bfs.append(el.right)
        return False

# dfs method
def search(root, cur, val):
    if root is None:
        return False
    return (root.val == val and root != cur) or ((root.val < val) and search(root.right, cur, val)) or ((root.val > val) and search(root.left, cur, val))


def dfs(root, cur, k):
    if cur is None:
        return False
    return search(root, cur, k - cur.val) or dfs(root, cur.left, k) or dfs(root, cur.right, k)


class Solution(object):

    def findTarget(self, root, k):
        return dfs(root, root, k)
