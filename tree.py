import numpy as np

maxDepth = 5
minSamples= 2

#
class Node():

    def __init__(self, value, indexMSE, right, left,isLeaf):
        self.value = value
        self.right = right
        self.left = left
        self.indexMSE = indexMSE
        self.isLeaf = isLeaf



class Tree():

    #attributes are maximum depth, and min number of samples per split
    def __init__(self,maxDepth, minSamples):
        self.maxDepth = maxDepth
        self.minSamples = minSamples
        self.root = None
        

    #finds the square residual of a problem
    def square_riz(self,observed, actual):

        sqrRiz = 0
        for x in observed:
            sqrRiz = sqrRiz + (x - actual) ** 2
        return sqrRiz


    def find_best_split(self,data,col):
        
        bestsplit = float('inf')
        index = -1
        indexMSE = -1
        lowestSplit = float('inf')
        for y in range(1,col):

            #added a sorting algorithm before testing each split
            data = self.sort(data,y)
            for x in range(0,data.shape[1]-1):
                
                #find the averages for each side of the split
                average1 = np.average(data[y][0:x])
                average2 = np.average(data[y][x:])
        
                #find the square residual for the split
                sqrRiz1 = self.square_riz(data[y][0:x],average1)
                sqrRiz2 = self.square_riz(data[y][x:],average2)

                #check to see if square residual is best value
                if sqrRiz1 + sqrRiz2 < lowestSplit:
                    lowestSplit = sqrRiz1 + sqrRiz2
                    index = x
                    indexMSE = y
                    bestsplit = (data[y][x] + data[y][x + 1])/2
        
        return bestsplit,index,indexMSE


    def makeHelper(self,data,currDepth):
        

        data = np.asarray(data)
        
        if(currDepth >= self.maxDepth or len(data[0]) < self.minSamples):
            
            return Node(np.mean(data[0]), None, None, None,True)

        
        bestSplit,index,indexMSE = self.find_best_split(data,data.shape[0])
        
        leftData, rightData = self.split(data,index)
        left = self.makeHelper(leftData, currDepth + 1)
        right = self.makeHelper(rightData, currDepth + 1)

        return Node(bestSplit,indexMSE, right, left,False)


    #makes the tree
    def makeTree(self,data):
        # print(self.maxDepth)
        self.root = self.makeHelper(data,0)

    def split(self,data, index):
    
        left = []
        for row in range(0, data.shape[0]):
            array = np.array([])
            for column in range(0, index):
                array = np.append(array,data[row][column])
            left.append(array)
       
        right = []
        for row in range(0, data.shape[0]):
            array = np.array([])
            for column in range(index, data.shape[1]):
                array = np.append(array,data[row][column])
            right.append(array) 
    
        return left, right 
    

    def predict(self,values):
        node = self.root
        while node.isLeaf != True:
            
            feature = node.indexMSE
            if values[feature-1] < node.value:
                
                node = node.left
            else:
                
                node = node.right
        
        return node.value
    
    #need to make better sorting algorithm later
    #sorts data of a 2d array, runtime complexity is O(n^3)
    def sort(self,array, col):

        for i in range(0,len(array[0])-1):

            for j in range(0, len(array[0])-1):
            
                if(array[col][j] > array[col][j+1]):

                    for k in range(0,len(array)):
                        temp = array[k][j]
                        array[k][j] = array[k][j+1]
                        array[k][j+1] = temp
    
        return array