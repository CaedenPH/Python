  class Solution:
     def pathSum(self, root: TreeNode, sum: int) -> int:

         global result
         result = 0

         def dfs(node, target):
             if node is None: return
             find_path_from_node(node, target)
             dfs(node.left, target)
             dfs(node.right, target)

         def find_path_from_node(node, target):
             global result
             if node is None: return
             if node.val == target: result += 1
             find_path_from_node(node.left, target-node.val)
             find_path_from_node(node.right, target-node.val)

         dfs(root, sum)

         return result
