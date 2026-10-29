class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        flat = [v for row in mat for v in row]
        if len(flat) != r * c:
            return mat
        return [flat[i * c:(i + 1) * c] for i in range(r)]
