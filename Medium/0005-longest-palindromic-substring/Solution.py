class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        mat = []

        i = 0 
        while i < len(chars):
            mat.append([None] * len(chars))
            i = i + 1

        ansi = -1
        ansj = -1
        anslen = 0
        j = 0
        while j < len(mat):
            i = 0
            while i < len(mat[j]):
                if i > j:
                    mat[i][j] = 0
                    if (j - i + 1) > anslen:
                        anslen = j - i + 1
                        ansi = i 
                        ansj = j
                elif i == j:
                    mat[i][j] = 1
                    if (j - i + 1) > anslen:
                        anslen = j - i + 1
                        ansi = i 
                        ansj = j
                else:
                    if ((i+1 > j-1) or mat[i+1][j-1]) and chars[i] == chars[j]:
                        mat[i][j] = 1
                        if (j - i + 1) > anslen:
                            anslen = j - i + 1
                            ansi = i 
                            ansj = j
                    else:
                        mat[i][j] = 0

                i = i + 1
            j = j + 1

        return s[ansi:ansj+1]
