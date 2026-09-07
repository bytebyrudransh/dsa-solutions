class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for i in letters:
            if ord(i) > ord(target):
                return i

        return letters[0]


        