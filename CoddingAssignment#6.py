#This function takes in a relation and finds the transitive closure of it and returns a dictionary that contains the transitive closure of the relation
def transitiveClosure(relation):
    #gets all the keys in the relation/dictionary
    keys = list(relation.keys())
    #empty dictionary that will hold the transitive closure output of this function
    tClosure = {
    }
    #list that will hold each connection for a key
    connections = []
    #loop that goes through each key in the list of keys
    for key in keys:
        #empty list that will hold the elements inside of the key
        element = []
        #function that returns the elements in the relation with specified key from the loop
        element = findElement(key, relation)
        #while loop that goes through each key's element list and will stop if the element does not point to any other element 
        while len(element) != 0:
            #adds the element to the connections list in which gets the element of the element inside of the key
            connections.append(element[0])
            #makes the element the key and finds their element within the relation and set the element variable to that 
            element = findElement(element[0], relation)
        #sorts the list of connections in order
        connections.sort()
        #puts the key and conncetions into a dictionary format
        comp = {key : connections}
        #adds the smaller dictionary to the larger dictionary
        tClosure.update(comp)
        #resets the connections list
        connections = []
    #returns the dictionary that holds the transitive closure of the relation
    return tClosure

#This function takes in a key and a relation/dictionary and returns the element with the designated key
def findElement(key,relation):
    return relation[key]

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
        

#test functions
relation = {
    1: [3],
    2: [4],
    3: [],
    4: [1]
}

output = transitiveClosure(relation)
print("Input: " + str(relation))
print("Output: " + str(output))
output = transitive(output)
print(output)
output = transitive(relation)
print(output)