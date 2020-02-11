#https://pythoncs.wordpress.com/2015/08/21/question-maximum-single-sell-profit-divide-and-conquer/
def MaxProfit(numbers, left=0, right=None):
    if right is None:
        right = len(numbers)
    if right - left <= 1:
        return 0
    mid = (right + left) / 2
    result = max(numbers[mid:right]) - min(numbers[left:mid])
    return max(result,MaxProfit(numbers, left, mid),MaxProfit(numbers, mid, right))
 
def getMinIndex(a,i,j):
    min = i
    for k in range(i+1,j):
        if(a[k]<a[min]):
            min = k
    return min

def getMaxIndex(a,i,j):
    max = i
    for k in range(i+1,j):
        if(a[k]>a[max]):
            max = k
    return max

a=[8108,8146,8116,7657,7327,7323,7270,7249,7510,7608,7778,7788,7568,7410,7381,7520,7412,7485,7588,7570,6953,7121,7273,7218,7275,7291,7149,7149,6935,7229]

start = 0
end = len(a)-1
result,startindex,endindex = MaxProfit(a,start,end)

print(result,startindex,endindex)
