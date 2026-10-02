class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(current: str, opened: int, closed: int):
            if len(current) == 2 * n:
                res.append(current)
                return

            if opened < n:
                backtrack(current + "(", opened + 1, closed)
            if closed < opened:
                backtrack(current + ")", opened, closed + 1)

        backtrack("", 0, 0)
        return res