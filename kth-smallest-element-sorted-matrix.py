def kthSmallest(matrix, k):
    def count_less_equal(matrix, mid):
        count = 0
        row, col = len(matrix) - 1, 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] <= mid:
                count += row + 1  # Count the entire column
                col += 1
            else:
                row -= 1
        return count

    left, right = matrix[0][0], matrix[-1][-1]
    while left < right:
        mid = left + (right - left) // 2
        count = count_less_equal(matrix, mid)
        if count < k:
            left = mid + 1
        else:
            right = mid

    return left
