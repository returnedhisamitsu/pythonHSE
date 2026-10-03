class Solution(object):
    def balancedStringSplit(self, s):
        answerCount = 0
        counter = 0
        for symb in s:
            if symb == 'R':
                counter += 1
            else:
                counter -= 1
            if counter == 0:
                answerCount += 1
        return answerCount