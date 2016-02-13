import arff
import sys

def naiveBaesClassifier(trainFile, testFile):
    classes = {}
    for row in arff.load(trainFile):
        className = row[len(row)-1]
        if(classes.has_key(className)):
            classes[className] = classes.get(className)+1
        else:
            classes[className] = 2
    
    classNames = classes.keys()
    sum = classes[classNames[0]]  + classes[classNames[1]]
    classes[classNames[0]] = float(classes[classNames[0]])/float(sum) #precison
    classes[classNames[1]] = float(classes[classNames[1]])/float(sum)
    
    attrProb = {}
    attrLength = len(row)-2
    
    for row in arff.load(trainFile):
        classNameRow = row[len(row)-1]
        for i in range(attrLength):
            if(attrProb.has_key(row[i]+':'+str(i) + ':' + classNames[0])!=True):
                attrProb[str(row[i])+':'+ str(i) + ':' +classNames[0]] = 1
            if(attrProb.has_key(row[i]+':'+str(i) + ':' + classNames[1])!=True):
                attrProb[str(row[i])+':'+ str(i) + ':' +classNames[1]] = 1
                
            if(attrProb.has_key(row[i]+':'+str(i) + ':' + classNameRow)):
                attrProb[str(row[i])+':'+str(i) + ':' +classNameRow] = attrProb.get(str(row[i])+':'+str(i) + ':' +classNameRow)+1
    print attrProb

    attributeFrequency = attrProb.keys()
    for i in range(len(attributeFrequency)):
        entriesWithSameClass = [value for key, value in attrProb.items() if attributeFrequency[i][attributeFrequency[i].index(':'):] in key.lower()]
        classSum = 0.0
        for j in range(len(entriesWithSameClass)):
            classSum = classSum + entriesWithSameClass[j]
        attrProb[attributeFrequency[i]] = float(attrProb[attributeFrequency[i]])/classSum
    print attrProb
    
    correctClassification = 0
    for row in arff.load(testFile):
        actualClassName = row[len(row)-1]
        n1=1
        n2=1
        for i in range(attrLength):
            print attrProb[row[i]+':'+str(i) + ':' + classNames[0]], ' ', attrProb[row[i]+':'+str(i) + ':' + classNames[1]]
            n1 = n1*attrProb[row[i]+':'+str(i) + ':' + classNames[0]]
            n2 = n2*attrProb[row[i]+':'+str(i) + ':' + classNames[1]]
        
        n1 = n1*classes[classNames[0]]
        n2 = n2*classes[classNames[1]]
        
        if(n1>n2):
            if(actualClassName == classNames[0]):
                correctClassification = correctClassification+1
            print classNames[0], ' ' , actualClassName, ' ' , n1/(n1+n2)
        else:
            if(actualClassName == classNames[1]):
                correctClassification = correctClassification+1
            print classNames[1], ' ' , actualClassName, ' ' , n2/(n1+n2)
    
    print 'correct classification = ' , correctClassification
def TANClassifier(trainFile, testFile):
    print 'hi'
    
if __name__ == "__main__":
    sysArguments = sys.argv
    trainFile = 'lymph_train.arff'
    testFile = 'lymph_test.arff'
    #trainFile = sysArguments[0]
    #testFile = sysArguments[1]
    classifier = 'n' #sysArguments[2]
    if(classifier=='n'):
        naiveBaesClassifier(trainFile, testFile)
    else:
        TANClassifier(trainFile, testFile)
#for row in arff.load('lymph_train.arff'):
#    print(row[len(row)-1])

