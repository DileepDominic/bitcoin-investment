'''
Application : Clubhouse Application
Authors:
    *. Vinutha K.S
    *. Nayaz Basha H M
    *. Dileep Dominic
    *. M R Rahamath 

Application is designed using python 3.7

'''

#global Variable

class bitcoinprofit:

    #Function to initialize path of input, output and Prompt files
    def __init__(self):
        self.inputfile="data/inputPS8.txt"
        self.outputfile="data/outputPS8.txt"

    #Function to Read Input file inputPS8.txt, this function internally calls insertAppDetails & write_toFile
    def readfile(self):
        arr = []
        arr2 = []

        with open(self.inputfile) as inputFile:
            for record in inputFile:
                recordAttributes = record.replace('\n','').split("/")
                #print("recordAttributes",recordAttributes[2])
                arr.append(int(recordAttributes[1]))              

        print(arr)
        profitLinear,profitStart,profitEnd = self.maxProfitLinear(arr)
        
        profitDivandConquer = self.DivideAndConquerProfit(arr)

        with open(self.outputfile,'a') as outputFile:
            outputFile.truncate(0)
        Insert_Details="Maximum Profit (Iterative solution): "+ str(profitLinear) +"\n Day to buy:" + str(profitStart) + "\n Day to sell : " + str(profitEnd) + "\n" + "Maximum Profit (Divide and Conquer): "+ str(profitDivandConquer) +"\n"
       
        global write_toFile
        #Function to write required details to output file
        self.write_toFile(self.outputfile,Insert_Details)

    def maxProfitLinear(self,a):
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

        
    def DivideAndConquerProfit(self,arr):

        if len(arr) <= 1:
            return 0

        # Cut the array into two roughly equal pieces.
        left  = arr[ : int(len(arr) / 2)]
        right = arr[int(len(arr) / 2) : ]

        # Find the values for buying and selling purely in the left or purely in
        # the right.
        leftBest = self.DivideAndConquerProfit(left)
        rightBest = self.DivideAndConquerProfit(right)

        # Compute the best profit for buying in the left and selling in the right.
        crossBest = max(right) - min(left)

        # Return the best of the three
        m = max(leftBest, rightBest, crossBest)
        return m

    #Function to write required details to output file
    @staticmethod         
    def write_toFile(outputLocation,OutputValue):
        with open(outputLocation,'a') as outputFile:
            outputFile.write(str(OutputValue))


bitcoinprofit_Object = bitcoinprofit()  
bitcoinprofit_Object.readfile()







