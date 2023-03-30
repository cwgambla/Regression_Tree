import unittest as un
import numpy as np
import tree
import power
import setPow

class TestTree(un.TestCase):

    # def test1(self):

    #     myTree = tree.Tree(10,2)
    #     #test1
    #     arrExp = np.array([1,2,3,4,5])
    #     result = myTree.square_riz(arrExp, 3)
    #     self.assertEqual(10,result)

    #     #test2
    #     arrExp = np.array([5,4,3,2,1])
    #     result = myTree.square_riz(arrExp, 3)
    #     self.assertEqual(10,result)

    #     #test3
    #     arrExp = np.array([3,5,4,1,2])
    #     result = myTree.square_riz(arrExp, 3)
    #     self.assertEqual(10,result)

    #     #test4
    #     arrExp = np.array([5,4,3,2,1])
    #     result = myTree.square_riz(arrExp, 3)
    #     self.assertEqual(10,result)

    #     #test5
    #     arrExp = np.array([5,4,3,2,1])
    #     result = myTree.square_riz(arrExp, 3)
    #     self.assertEqual(10,result)

    #     #test6
    #     arrExp = np.array([2,1])
    #     result = myTree.square_riz(arrExp, 3)
    #     self.assertEqual(5,result)

    #     #test7            
    #     arrExp = np.array([1,2])
    #     result = myTree.square_riz(arrExp, 3)
    #     self.assertEqual(5,result)


    # def testBestSplit(self):
    #     myTree = tree.Tree(10,2)
    #     arrData = np.array([[0,0,0,0,100,100,45],[0,0,0,10,20,24,50]]) #first array is values that are to be predicted, second array onwards are values used to predict values 
        
    #     print("bestSplit: ",myTree.find_best_split(arrData,2))

    # def testMakeTree(self):
    #     myTree = tree.Tree(10, 2)
    #     arrData = np.array([[0,0,0,0,100,100,45],[0,0,0,10,20,21,22]])
    #     myTree.makeTree(arrData)
    #     print("prediction:", myTree.predict([22]))
    
    # def testMakeTree2(self):
    #     myTree = tree.Tree(10,2)
    #     arrData = np.array([[0,0,0,0,20,20,20,20,100,100,100,100],[0,0,0,0,10,10,10,10,51,52,53,54]])
    #     myTree.makeTree(arrData)
    #     print("prediction for 10:", myTree.predict([10]))
    #     print("prediction: for 100", myTree.predict([100]))
    #     print("prediction: for 52", myTree.predict([52]))

    # def testMakeTreeMultiple(self):
    #     myTree = tree.Tree(10,2)
    #     arrData = np.array([[0,0,0,0,20,20,20,20,100,100,100,100],[0,0,0,0,10,10,10,10,51,52,53,54],[0,0,0,0,0,10,10,10,51,52,53,54]])
    #     myTree.makeTree(arrData)
    #     print("prediction for 10:", myTree.predict([10,0]))
    #     print("prediction: for 100", myTree.predict([100,0]))
    #     print("prediction: for 52", myTree.predict([52,0]))

    
    def testPrediction1(self):

        myTree = tree.Tree(100,8)
        df = power.getDataFrame("/home/cgambla/Documents/Personal_Projects/Python/Regression_Tree/CO2_emission.csv")
        elementPredict = 9
        elementToTest = [7,8]
        data = power.parseArray(df, 0, len(df.index)-1, elementToTest)
        
        
        
        print("Correlation Matrix:")
        print(np.corrcoef(data))

        tests = setPow.powerSetNoEmpty(elementToTest,len(elementToTest))
        for i in tests:
            temp = i.copy()
            temp.insert(0,elementPredict)
            df = df.sample(frac = 1)
            
            print("Testing results for ", i, "Accuracy:", power.testAccurracy(myTree,700,df,temp,0.05))
        # print("Testing result:", power.testAccurracy(myTree, 700, df, [10,7,9],10))

    
if __name__ == '__main__':
    un.main()