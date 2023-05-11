import tkinter as tk
import numpy as np
import tree
import power
import setPow
import warnings

import tkinter as tk
 # file name:/home/cgambla/Documents/Personal_Projects/Python/Regression_Tree/CO2_emission.csv
    # file name shipping:/home/cgambla/Documents/Personal_Projects/Python/Regression_Tree/shipping_data.csv
# Create the tkinter window


# Define a function to get the user input

def predict1():
    print("predict")
    substrings = predict2.get().split(",")
    # split the string into individual substrings based on comma delimiter
    numeric_list = [float(x) for x in substrings]
    print(window.finalTree.predict(numeric_list))

def train_tree():
    user_input = file_name.get()

    maxDepth = 10
    if(len(max_depth.get())>0):
        maxDepth = int(max_depth.get())
    print("MaxDepth: ", maxDepth)

    minSplit = 8
    if(len(min_split.get())>0):
        minSplit = int(min_split.get())
    print("MinSplit: ", minSplit)
    myTree = tree.Tree(maxDepth,8)

    degreeOfAccuracy = 0.05
    if(len(degree_acc.get())>0):
        degreeOfAccuracy= float(degree_acc.get())
    print("Degree of Accuracy: ",degreeOfAccuracy )

    cov_level = 0.05
    if(len(cov_acc.get())>0):
        cov_level= float(cov_acc.get())
    print("Maximum Number of Features: ",cov_level)

    sizeTrain = int(size_train.get())

   
    df = power.getDataFrame(user_input)

    substrings = features_tested.get().split(",")
    # split the string into individual substrings based on comma delimiter
    numeric_list = [int(x) for x in substrings]

# convert the substrings to a numeric type using astype method
    elementToTest = numeric_list
    elementPredict = int(predict.get())
    # elementToTest = [7,8,9]
    data = power.parseArray(df, 0, len(df.index)-1, elementToTest)
    labels = df.columns
    print(labels)

    newLabels = []
    for x in elementToTest:
        newLabels.append(labels[x])
    # print(labels)
    
    

# add items to the Listbox
    
    

# pack the Listbox widge
        
    index1 = 0

    #array of good features to test
    accFeat = []
    results = []
    accTh = float(accThresh.get())
    # covMtrx = np.corrcoef(data)
    # print(covMtrx)


    # for x in elementToTest:
    #     temp = [elementPredict, x]
    #     result = power.testAccurracy(myTree,sizeTrain,df,temp,degreeOfAccuracy)
    #     print(labels[x],x,result)
    #     results.append(result)
    #     if result > accTh:
    #         accFeat.append(x)
    #     index1+=1
    
    # data = power.parseArray(df, 0, len(df.index)-1, accFeat)
    # labels = df.columns

    elementToTest.insert(0,elementPredict)
    print(df)
    print(elementToTest)
    print(sizeTrain)
    
    newTree = tree.Tree(maxDepth,8)
    print(power.testAccurracy(newTree,sizeTrain,df,elementToTest,degreeOfAccuracy))
    window.finalTree = power.createTree(newTree,sizeTrain,df,elementToTest,degreeOfAccuracy)
    print(window.finalTree)

    
def get_input():
    user_input = file_name.get()

    maxDepth = 10
    if(len(max_depth.get())>0):
        maxDepth = int(max_depth.get())
    print("MaxDepth: ", maxDepth)

    minSplit = 8
    if(len(min_split.get())>0):
        minSplit = int(min_split.get())
    print("MinSplit: ", minSplit)
    myTree = tree.Tree(maxDepth,8)

    degreeOfAccuracy = 0.05
    if(len(degree_acc.get())>0):
        degreeOfAccuracy= float(degree_acc.get())
    print("Degree of Accuracy: ",degreeOfAccuracy )

    cov_level = 0.05
    if(len(cov_acc.get())>0):
        cov_level= float(cov_acc.get())
    print("Maximum Number of Features: ",cov_level)

    sizeTrain = int(size_train.get())

   
    df = power.getDataFrame(user_input)

    substrings = features_tested.get().split(",")
    # split the string into individual substrings based on comma delimiter
    numeric_list = [int(x) for x in substrings]

# convert the substrings to a numeric type using astype method
    elementToTest = numeric_list
    elementPredict = int(predict.get())
    # elementToTest = [7,8,9]
    data = power.parseArray(df, 0, len(df.index)-1, elementToTest)
    labels = df.columns
    print(labels)

    newLabels = []
    for x in elementToTest:
        newLabels.append(labels[x])
    # print(labels)
    
    

# add items to the Listbox
    
    

# pack the Listbox widge
        
    index1 = 0

    #array of good features to test
    accFeat = []
    results = []
    accTh = float(accThresh.get())
    covMtrx = np.corrcoef(data)
    print(covMtrx)


    for x in elementToTest:
        temp = [elementPredict, x]
        result = power.testAccurracy(myTree,sizeTrain,df,temp,degreeOfAccuracy)
        print(labels[x],x,result)
        results.append(result)
        if result > accTh:
            accFeat.append(x)
        index1+=1
    
    data = power.parseArray(df, 0, len(df.index)-1, accFeat)
    labels = df.columns


    set = [elementPredict]
    acc = 0
    accMulti = []
    resultsMulit = []
    for x in accFeat:
        temp = set.copy()
        temp.append(x)
        df = df.sample(frac = 1)
        result = power.testAccurracy(myTree,sizeTrain,df,temp,0.05)
        print("Result for ",temp, ":",result )
        resultsMulit.append(result)
        del temp[0]
        accMulti.append(temp)
        if result > acc:
            set.append(x)
            acc = result
    newLabels = []
    for x in elementToTest:
        newLabels.append(labels[x])
    # print(labels)
    # covMtrx = np.corrcoef(data)
    print(covMtrx)
    root = tk.Tk(className = "Information x")
    root.geometry("1000x800")

   
    #labels for column Headers
    label = tk.Label(root, text="Feature", padx=10, pady=5)
    label.grid(row = 0, column=0)
    label = tk.Label(root, text="Accuracy", padx=10, pady=5)
    label.grid(row = 0, column=1)

    for j in range(len(elementToTest)):
        label = tk.Label(root, text=labels[elementToTest[j]], padx=10, pady=5)
        label.grid(row=j+1, column=0)

    # create labels for column headers
    for j in range(len(results)):
        label = tk.Label(root, text=results[j], padx=10, pady=5)
        label.grid(row=1+j, column=1)
    
    for j in range(len(accMulti)):
        txt = ""
        for x in accMulti[j]:
            txt = txt +  " | " +labels[x]
        label = tk.Label(root, text=txt ,padx=10, pady=5)
        label.grid(row=j+len(elementToTest) + 2, column=0)
    
    print("resultsMulit:", resultsMulit)
    for j in range(len(resultsMulit)):
        label = tk.Label(root, text=resultsMulit[j], padx=10, pady=5)
        label.grid(row=2+j + len(elementToTest), column=1)

    
    
    
    print(covMtrx, covMtrx.shape)

    label = tk.Label(root, text="", padx=10, pady=5)
    label.grid(row = 3+ len(elementToTest), column=0)
    label = tk.Label(root, text="", padx=10, pady=5)
    label.grid(row = 5+ len(elementToTest), column=0)
    label = tk.Label(root, text="Covariance Matrix", padx=10, pady=5)
    label.grid(row = 6+ len(elementToTest), column=1)


    for j in range(covMtrx.shape[0]):
        label = tk.Label(root, text=labels[elementToTest[j]], padx=10, pady=5)
        label.grid(row = 7 + len(elementToTest), column=j+1)

    # create labels for row headers and matrix elements
    for i in range(len(covMtrx)):
        # create label for row header
        label = tk.Label(root, text=labels[elementToTest[i]], padx=10, pady=5)
        label.grid(row = 8 + i + len(elementToTest), column=0)

    # create labels for matrix elements
        for j in range(len(covMtrx[i])):
            label = tk.Label(root, text=covMtrx[i][j], padx=10, pady=5)
            label.grid(row = 8 + i + len(elementToTest), column=j+1)

    
    # elementToTest = power.newFeatures(elementToTest,covMtrx, 0.8,accFeat)
    # tests = setPow.powerSetNoEmpty(accFeat,len(accFeat))
    # for i in tests:
    #     temp = i.copy()
    #     temp.insert(0,elementPredict)
    #     df = df.sample(frac = 1)
    #     print("Testing results for ", i, "Accuracy:", power.testAccurracy(myTree,sizeTrain,df,temp,degreeOfAccuracy))
    #     if(len(temp) > 2):    
    #         print("Testing results for ", i, "Accuracy:", power.testAccurracy(myTree,sizeTrain,df,temp,degreeOfAccuracy))
    
    


window = tk.Tk(className='Main Menu')
window.geometry("700x700")

#GET FILE NAME
# Create a label widget to display instructions
instructions_label = tk.Label(window, text="Enter a file to run data:")
instructions_label.pack()

# Create an entry widget to get user input
file_name= tk.Entry(window)
file_name.pack()


#MAXIMUM TREE DEPTH
instructions_label2 = tk.Label(window, text="Enter a tree maxdepth:")
instructions_label2.pack()

# Create an entry widget to get user input
max_depth = tk.Entry(window)
max_depth.pack()


#MINIMUM SPLIT SIZE
instructions_label3 = tk.Label(window, text="Enter a tree minimum split size:")
instructions_label3.pack()

# Create an entry widget to get user input
min_split = tk.Entry(window)
min_split.pack()


#ACCEPTABLE DEGREE OF ACCURACY
instructions_label4 = tk.Label(window, text="Enter acceptable degree of accuracy(between 0 and 1):")
instructions_label4.pack()

# Create an entry widget to get user input
degree_acc = tk.Entry(window)
degree_acc.pack()


#GET ACCEPTABLE COVARIANCE LEVEL
instructions_label5 = tk.Label(window, text="Enter Maximum Number of features :")
instructions_label5.pack()

# Create an entry widget to get user input
cov_acc = tk.Entry(window)
cov_acc.pack()


#SIZE OF TRAINING DATA
instructions_label6 = tk.Label(window, text="Enter size of training set")
instructions_label6.pack()

# Create an entry widget to get user input
size_train = tk.Entry(window)
size_train.pack()

#SIZE OF TRAINING DATA
instructions_label7 = tk.Label(window, text="Enter the features wishing to be evaluated training set. Or, if you are creating a tree to use,\n then enter which feautres you would like to use in the tree")
instructions_label7.pack()

# Create an entry widget to get user input
features_tested = tk.Entry(window)
features_tested.pack()

#SIZE OF TRAINING DATA
instructions_label8 = tk.Label(window, text="Enter the feature wishing to predict")
instructions_label8.pack()

# Create an entry widget to get user input
predict= tk.Entry(window)
predict.pack()

#SIZE OF TRAINING DATA
instructions_label9 = tk.Label(window, text="Enter acceptable threshold level(If an individual feature's accuracy \nfails to meet the threshold, it will not be included in the \nmulti tree calculations)")
instructions_label9.pack()

# Create an entry widget to get user input
accThresh= tk.Entry(window)
accThresh.pack()



# Create a button to trigger the function
button = tk.Button(window, text="Run analysis")
button['command'] = get_input
button.pack()



# #SIZE OF TRAINING DATA
# instructions_label9 = tk.Label(window, text="Enter the features wishing to be evaluated training set to construct tree")
# instructions_label9.pack()

# # Create an entry widget to get user input
# features_tested2 = tk.Entry(window)
# features_tested2.pack()

# #SIZE OF TRAINING DATA
# instructions_label10 = tk.Label(window, text="Enter the feature wishing to predict to construct tree")
# instructions_label10.pack()

# # Create an entry widget to get user input
# predict2= tk.Entry(window)
# predict2.pack()

window.finalTree = 0
button1 = tk.Button(window, text="Create Tree")
button1['command'] = train_tree
button1.pack()
print(window.finalTree)
#SIZE OF TRAINING DATA
predict2 = tk.Label(window, text="Enter the data set to predict value of")
predict2.pack()

# Create an entry widget to get user input
predict2= tk.Entry(window)
predict2.pack()

button2 = tk.Button(window, text="Predict")
button2['command'] = predict1
button2.pack()
#disabling warnings
warnings.filterwarnings('ignore')
window.mainloop()
