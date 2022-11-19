def Knapsack01(profits, weights, maxWeight):
    n = len(profits)
    K = [[0 for x in range(maxWeight + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(maxWeight + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(profits[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][maxWeight]


if __name__ == '__main__':
    maxWeight = 50  # int(input("Enter max weight"))
    weights = [10, 20, 30]  # list(map(int, input("Enter values of weight").split()))
    profits = [60, 100, 120]  # list(map(int, input("Enter values of profit").split()))

    print(Knapsack01(profits, weights, maxWeight))