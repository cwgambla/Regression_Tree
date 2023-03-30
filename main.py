import numpy as np
import tree
import power
import setPow
import warnings

def main():
    myTree = tree.Tree(100,8)
    df = power.getDataFrame("/home/cgambla/Documents/Personal_Projects/Python/Regression_Tree/CO2_emission.csv")
    elementPredict = 9
    elementToTest = [4,5,7,8,10,11]
    data = power.parseArray(df, 0, len(df.index)-1, elementToTest)
    
    accIndFeat = []
    for x in elementToTest:
        temp = [elementPredict, x]
        accIndFeat.append(power.testAccurracy(myTree,700,df,temp,0.05))
    
    print("Individual Accurracies:", accIndFeat)
    print("Correlation Matrix:")
    covMtrx = np.corrcoef(data)
    print(covMtrx)
    elementToTest = power.newFeatures(elementToTest,covMtrx, 0.8,accIndFeat)

    tests = setPow.powerSetNoEmpty(elementToTest,len(elementToTest))
    for i in tests:
        temp = i.copy()
        temp.insert(0,elementPredict)
        df = df.sample(frac = 1)
        if(len(temp) > 2):    
            print("Testing results for ", i, "Accuracy:", power.testAccurracy(myTree,700,df,temp,0.05))


#disabling warnings
warnings.filterwarnings('ignore')

main()