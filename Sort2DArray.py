78"""
Google Phone Screen. Sort a 2D array.
Link: https://leetcode.com/discuss/interview-question/381172/google-phone-screen-sort-a-2d-array
Language: Python
"""

class Sort2D:
    def __init__(self, matrix):
        self.matrix = matrix

    def sort(self):
        for i in range(0, len(self.matrix)-1):
            for j in range(0, len(self.matrix[i])):
                r = self.find_min(i+1)
                if self.matrix[r][0] < self.matrix[i][j]:
                    self.swap(i, j, r, 0)
                    self.reorder(r)

    def find_min(self, x):
        r = x
        for i in range(x, len(self.matrix)):
            if self.matrix[r][0] > self.matrix[i][0]:
                r = i
        return r

    def reorder(self, r):
        l = 0
        for i in range(1, len(self.matrix[r])):
            if self.matrix[r][l] < self.matrix[r][i]:
                break
            self.swap(r, i, r, l)
            l = i

    def swap(self, x1, y1, x2, y2):
        self.matrix[x1][y1], self.matrix[x2][y2] = self.matrix[x2][y2], self.matrix[x1][y1]