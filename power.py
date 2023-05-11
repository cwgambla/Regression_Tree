import pandas as pd
import tree
import numpy as np
#returns a dateframe after reading from a csv file
#parameter is the filepath to the .csv file
#NOTE: this is by far the most finicky part of this program
# ,as the file pathing can get messed up if used on a different operating system
#If there is a problem reading the csv file, its likely due to pathing issues
def getDataFrame(fileName):
    print("Filename: " + fileName)
    data = pd.read_csv(fileName)   
    df = pd.DataFrame(data)
    return df


#takes data from a pandas dataFrame and turns it into a 2D array
#parameters are the dataFrame, the starting row and the last row
#you want to parse data from
def parseArray(dataFrame, start_row, endRow, attributes):

    #this is an array of the names of the attributes that will be accessed 
    #the first attribute will be the factor that will be predicted
    #every other attribute afterwards will be the predicting factors

    data = []

    
    
    for i in range(0,len(attributes)):
        array = []
        curr_row = start_row
        while curr_row <= endRow:
            array.append(dataFrame.iloc[curr_row][attributes[i]])
            curr_row+=1
        data.append(array)
    
    return data
    


#will run a single test on the tree constructed
#attributes = [10,11]
#parameters: the regression tree object,numTrain: the number of elements you want in the training set
#dataFrame: the dataFrame with all the data, is a pandas dataFrame,attributes: which types of data will be predicting
#and which one will be predicted, and error: the allowed error for each guess to be considered accurate
def testAccurracy(Tree,numTrain, dataFrame,attributes, error):
    
    trainingData = parseArray(dataFrame, 0, numTrain,attributes)
    testData = parseArray(dataFrame, numTrain + 1, len(dataFrame.index)-1,attributes)
    # print(testData)
    Tree.makeTree(trainingData)
    print(Tree)
    total = len(testData[0])
    right = 0
    for currIndex in range(0,len(testData[0])):
        
        arrayPredictors = []

        for i in testData[1::]:

            arrayPredictors.append(i[currIndex])
        # print(testData[1::])

        prediction = Tree.predict(arrayPredictors)

        #print(arrayPredictors,prediction, testData[0][currIndex],(prediction - testData[0][currIndex])/testData[0][currIndex])
        
        if  (prediction - testData[0][currIndex])/testData[0][currIndex] < error and (prediction - testData[0][currIndex])/testData[0][currIndex] > -error:
            right += 1
    
    return right/total
def createTree(Tree,numTrain, dataFrame,attributes, error):
    
    trainingData = parseArray(dataFrame, 0, numTrain,attributes)
    testData = parseArray(dataFrame, numTrain + 1, len(dataFrame.index)-1,attributes)
    # print(testData)
    Tree.makeTree(trainingData)
    print(Tree)
    return Tree

def kTest(tree, numTrain, dataFrame,attributes, error, k):
    error = []
    for i in range(0,k):
        df_shuffled = dataFrame.sample(frac = 1)
        # print(df_shuffled)
        error.append(testAccurracy(tree,numTrain, dataFrame,attributes, error))
        # print(error)
    
    return error


#this method will return a new set of elements to be tested based off the covariance matrix, and
#an accetpable covariance level
#inputs:
# elements -> an array that holds which features will be tested
# covMtrx -> the covariance matrix for the various features input by elements
# covLevel -> the acceptable level of covariance between features. Will a number between -1 and 1, inclusive
#ouput:
# an array of new features to test

def newFeatures(elements, covMtrx, covLevel, accuracy):
    
    highly_correlated = []
    for i in range(covMtrx.shape[0]):
        for j in range(i+1, covMtrx.shape[1]):
            if abs(covMtrx[i,j]) > covLevel and i != j:
                # print(j,accuracy[j],i,accuracy[j])
                if(accuracy[j] > accuracy[j]):
                    highly_correlated.append(j)
                else:
                    highly_correlated.append(i)

    
    highly_correlated = (np.unique(highly_correlated))

    newElements = []
    for x in range(0, len(elements)):
        if(x not in highly_correlated ):
            newElements.append(elements[x])
    return newElements









    












    


