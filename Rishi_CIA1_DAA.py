import numpy as np


seq1 = "AGTTGACAAACT"
seq2 = "TGTTACCAATAC"


match = 4
mismatch = -1
gap = -1


n = len(seq1) + 1
m = len(seq2) + 1
matrix = np.zeros((n, m))


directions = np.zeros((n, m), dtype=str)
directions[:] = "-"


for i in range(1, n):
    matrix[i][0] = matrix[i-1][0] + gap
    directions[i][0] = "up"
for j in range(1, m):
    matrix[0][j] = matrix[0][j-1] + gap
    directions[0][j] = "left"


for i in range(1, n):
    for j in range(1, m):
        diag_score = matrix[i-1][j-1] + match if seq1[i-1] == seq2[j-1] else matrix[i-1][j-1] + mismatch
        up_score = matrix[i-1][j] + gap
        left_score = matrix[i][j-1] + gap
        matrix[i, j], direction = max(((diag_score, "diag"), (up_score, "up"), (left_score, "left")), key=lambda x: x[0])
        directions[i][j] = direction

# Backtracking
align1, align2 = "", ""
i, j = n-1, m-1
while i > 0 and j > 0:
    if directions[i][j] == "diag":
        align1 += seq1[i-1]
        align2 += seq2[j-1]
        i -= 1
        j -= 1
    elif directions[i][j] == "left":
        align1 += "-"
        align2 += seq2[j-1]
        j -= 1
    elif directions[i][j] == "up":
        align1 += seq1[i-1]
        align2 += "-"
        i -= 1
    else:
        break
align1 = align1[::-1]
align2 = align2[::-1]

print("Aligned sequences:")
print(align1)
print(align2)

