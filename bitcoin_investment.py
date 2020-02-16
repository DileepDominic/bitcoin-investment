'''
Application : Clubhouse Application
Authors:
    *. Vinutha K.S
    *. Nayaz Basha H M
    *. Dileep R Dominic
    *. M R Rahamath 

Application is designed using python 3.7

'''

import sys 
#global Variable

class bitcoinprofit:

    #Function to initialize path of input, output and Prompt files
    def __init__(self):
        self.inputfile="data/inputPS8.txt"
        self.outputfile="data/outputPS8.txt"

    def LinearMaxProfit(self,a):
        maxprofit = 0
        startday = 0 
        endday = 0

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

        # Cuttig the array into two
        leftArray  = arr[ : int(len(arr) / 2)]
        rightArray = arr[int(len(arr) / 2) : ]

        # Find the values for buying and selling purely in the left or purely in
        # the right.
        leftBest = self.DivideAndConquerProfit(leftArray)
        rightBest = self.DivideAndConquerProfit(rightArray)

        # Compute the best profit for buying in the left and selling in the right.
        crossBest = max(rightArray) - min(leftArray)

        # Return the best of the three
        m = max(leftBest, rightBest, crossBest)
        return m

    #Function to write required details to output file
    @staticmethod         
    def write_toFile(outputLocation,OutputValue):
        with open(outputLocation,'a') as outputFile:
            outputFile.write(str(OutputValue))

    #Function to Read Input file inputPS8.txt, this function internally calls insertAppDetails & write_toFile
    def readfile(self):
        arr = []
        count = 0
        with open(self.inputfile) as inputFile:
            for record in inputFile:
                recordAttributes = record.replace('\n','').split("/")
                arr.append(int(recordAttributes[1]))              
                count = count + 1
                #A check to make sure a max of month is only taken. 
                if count>31:
                    print("Max input for a month has reached")
                    sys.exit(0)


        profitLinear,profitStart,profitEnd = self.LinearMaxProfit(arr)
        
        if (profitLinear == 0 ):
            profitStart = 0
            profitEnd = 0

        profitDivandConquer = self.DivideAndConquerProfit(arr)

        with open(self.outputfile,'a') as outputFile:
            outputFile.truncate(0)
        Insert_Details="Maximum Profit (Iterative solution): "+ str(profitLinear) +"\n Day to buy : " + str(profitStart) + "\n Day to sell : " + str(profitEnd) + "\n" + "Maximum Profit (Divide and Conquer): "+ str(profitDivandConquer) +"\n"
       
        global write_toFile
        #Function to write required details to output file
        self.write_toFile(self.outputfile,Insert_Details)


bitcoinprofit_Object = bitcoinprofit()  
bitcoinprofit_Object.readfile()







