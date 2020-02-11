



def maxProfit(a):
    maxprofit=0
    startday=99
    endday=99

    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            #print(a[j])
            profit = a[j] - a[i]
            if(profit > maxprofit):
                maxprofit = profit
                startday=i
                endday=j

    return maxprofit,startday+1,endday+1



a= [8108,8146,8116,7657,7327,7323,7270,7249,7510,7608,7778,7788,7568,7410,7381,7520,7412,7485,7588,7570,6953,7121,7273,7218,7275,7291,7149,7149,6935,7229]

#b = DivideAndConquerSingleSellProfit(a)

m,i,j = maxProfit(a)
print(m,i,j)


