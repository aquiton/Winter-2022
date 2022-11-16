#this function checks to see if the relation is reflexive  
def reflexive(dictionary):
    reflexive = True #sets the base boolean of reflexive to true and then will find the first instance that is false and return it otherwise will return true if the whole relation is reflexive
    keys = list(dictionary.keys()) #gets the list of keys from the dictionary and puts them into a list called keys
    for key in keys: # goes through each key in the list of keys
        if(key not in dictionary[key]): #checks whether or not if the key is in the list of elements it is related to
            return False #returns false if the key is not in the list of elements that it is related to
    return reflexive #returns true if the whole relation is reflexive

#this functin checks to see if the realtion is symmetric
def symmetric(dictionary):
    symmetric = True #sets the base boolean of symmetric to true and will find the first instance that there is no symmetric relation in the dictionary and will return false
    keys = list(dictionary.keys()) #gets the list of keys from the dictionary and puts them into a list called keys
    for key in keys: #goes through each key in the list of keys
        for element in dictionary[key]: #goes through each element of the key
            if(key not in dictionary[element]): #checks whether or not the key is in the second keys(element from first key) list 
                return False #returns false if it is not
    return symmetric # returns true if the relation is symmetric
        
#this function checks the equivalence classes of the relation
def equivalenceClasses(relation):
    keys = list(relation.keys()) #creates a list of keys from the dictionary/relation
    related = [] #creates empty list for all the keys that are equal to each other
    relations = [] #creates empty list for all the other list that are related to each other
    for key in keys: #goes through each key in keys
        for sKey in keys: #goes through each key in keys again to check if the keys elements are equal to each other
            if(relation[key] == relation[sKey]): #checks to see if the first key and the second key are equal to each other
                if(sKey not in related): #checks to see if they are not in the related list
                    related.append(sKey) #appends them to the related list
        if(related not in relations): #checks to see if the related list is not already in the relations list
            relations.append(related) #appends the related list to the relations list
        related = [] #resets the related list
    
    return relations #returns the list of related of list in which contain keys that are equal to each other
    
        


#test cases

dictionary = {
    1 : [2,3],
    2 : [5,10],
    3 : [47],
    5 : [1,2],
    10 : [3,2],
    47 : []
}

dictionary2 = {
    2 : [5,10],
    5 : [2],
    10 : [2]
}

symmetric_dict = {
    1 : [2,3],
    2 : [1,3], 
    3 : [1,2]
}

notSymmetric_dict = {
    1 : [2,3],
    2 : [1,3],
    3 : []
}

output = reflexive(dictionary)
print("reflexive: " + str(output))
output = symmetric(symmetric_dict)
print("symmetric: " + str(output))




relation = {
    1 : [1,2,3],
    2 : [1,2,3],
    3 : [1,2,3],
    4 : [4,5],
    5 : [4,5]
}

output = equivalenceClasses(relation)
print("equivalence classes: " + str(output))