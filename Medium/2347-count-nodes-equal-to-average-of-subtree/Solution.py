class Solution(object):
    def averageOfSubtree(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return 0, 0

            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)

            total_sum = node.val + left_sum + right_sum
            total_cnt = 1 + left_cnt + right_cnt

            if total_sum // total_cnt == node.val:
                self.ans += 1

            return total_sum, total_cnt

        dfs(root)
        return self.ans