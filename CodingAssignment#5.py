#This function is suppose to determine if a giving dictionary/relation is transitive or not
def transitive(dictionary):
    #creates a list of keys from the dictionary and put them into a variable called keys that holds them
    keys = list(dictionary.keys()) 
    #We have a boolean variable 'transitive' in which is default to true and determinds whether or not the relation is true in being transitive
    transitive = True
    #we have a for loop that goes through each key in the list of keys
    for key in keys:
        #we have another for loop that goes through each element in the key of the dictionary
        for element in dictionary[key]:
            #we have a second for loop that goes through each element called sElement in which the previous for loop element is the key for the dictionary
            for sElement in dictionary[element]:
                #an if statement that checks whether or not the sElement is in the first iteration of the dictionary key
                if(sElement not in dictionary[key]):
                    #if the sElement is not in the dictionary key the relation is not Transitive and thus returns False
                    return False
    #if the sElemet is in the dictionary[key] for all the keys, then the relation is Transitive and returns True
    return transitive
        
#This function determines if a giving dictionary/relation is anti-symmetric or not
def anti_symmetric(dictionary):
    #creates a list of keys from the dictionary and put them into a variable called 'keys' 
    keys = list(dictionary.keys())
    #boolean variable called anti_symm in which determinds if the relation is anti-symmetric
    anti_symm = True
    #A for loop that iterates through each key in the list of keys
    for key in keys:
        #For loop that goes through each element of the key
        for element in dictionary[key]:
            #if statement that checks if the key is in the dictionary of the dictionary[element] in which the element is the key
            if(key in dictionary[element]):
                #if the key is not equal to the element then the relation is not anti-symm because aRb and bRa is only allowed if a = b
                if(key != element):
                    #returns False because there is a symmetric relationship but they are not equal to each other
                    return False
    #returns true if the function does not find a symmetric relationship in which the only symmetric relationship is aRb and bRa only if a = b
    return anti_symm

#This function creates a composition dictionary of two dictionaries
def composition(dictionary1,dictionary2):
    #creates a list of keys from the first dictionary and puts them into a variable called 'dictkeys'
    dictKeys = list(dictionary1.keys())
    #creates an empty dictionary called composition in which would will contian the composition of the two dictionaries
    composition = {
    }
    #list of elements that come from the second dictionary and the keys are from the first dictionary elements
    elements = []
    #for loop that goes through the keys of the first dictionary
    for key in dictKeys:
        #for loop that goes through the elements of the key's in the first dictionary
        for element in dictionary1[key]:
            #Another for loop that takes the elements from the keys of the first dictionary and goes through the elements of the second dictionary
            #with the first dictionaries elements being the keys for the second dictionary
            for sElement in dictionary2[element]:
                #appends the elements to a list
                elements.append(sElement)
        #sorts them in order
        elements.sort()
        #creates a small dictionary in which will be added to the bigger one
        comp = {key : elements}
        #updates the composition dictionary by apending the smaller dictionary to it
        composition.update(comp)
        #resets the elements list
        elements = []
    #returns the big dictionary that contains the composition of the two dictionaries
    return composition
    



#test cases
dictionary = {
    1 : [2,3],
    2 : [5,10], 
    3 : [47],
    5 : [1,2],
    10 : [3,2],
    47 : []
}

transitive_dict = {
    1 : [2,3],
    2 : [3],
    3 : []
}

anti_dict = {
    1 : [1,2],
    2 : []
}

dictOne = {
    1 : [2,3],
    2 : [3],
    3 : [4],
    4 : [1,3]
}

dictTwo = {
    1 : [3],
    2 : [1,4],
    3 : [2],
    4 : [1,2]
}

output = transitive(dictionary)
print("Transitive: " + str(output))

output = anti_symmetric(dictionary)
print("anti-symmetric: " + str(output))

output = composition(dictOne,dictTwo)
print("Composition: " + str(output))