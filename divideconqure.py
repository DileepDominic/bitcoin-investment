
def Recursion(arr, lhs, rhs):
    if lhs == rhs:
        return (0, arr[lhs], arr[rhs])
    
    mid = lhs + (rhs - lhs) / 2

    (leftProfit,  leftMin,  leftMax) = Recursion(arr, lhs, mid)
    (rightProfit, rightMin, rightMax) = Recursion(arr, mid + 1, rhs)

    maxProfit = max(leftProfit, rightProfit, rightMax - leftMin)
    return (maxProfit, min(leftMin, rightMin), max(leftMax, rightMax))
    
a=[8108,8146,8116,7657,7327,7323,7270,7249,7510,7608,7778,7788,7568,7410,7381,7520,7412,7485,7588,7570,6953,7121,7273,7218,7275,7291,7149,7149,6935,7229]

m,n,o=Recursion(a,0,len(a)-1)
print(m,n,o)
