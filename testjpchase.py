def max_score(stack_height):
    stack = [stack_height] + [1] * (stack_height - 1)
    n = len(stack)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            max_score = 0
            for k in range(i, j):
                score = dp[i][k] + dp[k + 1][j] + stack[i] * stack[j]
                max_score = max(max_score, score)
            dp[i][j] = max_score

    return dp[0][n - 1]

# Example usage
print(max_score(4)//2)