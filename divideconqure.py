def DivideAndConquerSingleSellProfit(arr):
    # Base case: If the array has zero or one elements in it, the maximum
    # profit is 0.
    print("leng:",len(arr))
    if len(arr) <= 1:
        return 0;
    left =arr[:15]
    right =arr[15:30]
    # Cut the array into two roughly equal pieces.
    #left  = arr[:len(arr)/2]
    #right = arr[len(arr)/2:]


    # Find the values for buying and selling purely in the left or purely in
    # the right.
    leftBest  = DivideAndConquerSingleSellProfit(left)
    rightBest = DivideAndConquerSingleSellProfit(right)

    # Compute the best profit for buying in the left and selling in the right.
    crossBest = max(right) - min(left)

    # Return the best of the three
    return max(leftBest, rightBest, crossBest)

a=[1,8108,8146,8116,7657,7327,7323,7270,7249,7510,7608,7778,7788,7568,7410,7381,7520,7412,7485,7588,7570,6953,7121,7273,7218,7275,7291,7149,7149,6935,7229]

b = DivideAndConquerSingleSellProfit(a)

print(b)