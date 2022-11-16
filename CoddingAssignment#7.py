#this function creates a path graph with the input being an interger n
def pathGraph(n):
    #create an empty dictionary
    path= {
    }
    #create an empty list in which would hold the keys for the graph
    keys = []
    #loop through from 0 to n in which the numbers are the keys from 0 to n
    for x in range(n):
    #append each integer to the keys list
        keys.append(x)
    #loop through each key in the list of keys
    for key in keys:
    #checks to see if the first key is 0 (checks to see if the key is the beginning)
        if(key == 0):
            #if it is the beginning of path graph only make the relation be connected to key+1
            vert = {key : [key+1]}
    #checks to see if the key is at the end
        elif(key == n-1):
            #if it is at the end of the path graph only make the relation be connected to key-1
            vert = {key : [key-1]}
        else:
    #everything else will be in between in which will be connected to the one in front and the one behind the key
            vert = {key : [key-1,key+1]}
    #update the main dictionary
        path.update(vert)
    #returns the path graph in dictionar form
    return path

#this function determines if a given graph is connected or not connected
def connected(graph):
#store the list of key from a given graph
    keys = list(graph.keys())
#creates an empty list called used_keys 
    used_keys = []
#while loop boolean
    loop = True
#sets the base key to the first key in the list of keys
    key = keys[0]
#appends the key to used_keys
    used_keys.append(key)
#base counter of 1 because we already are using the first key in which we will check from that key if the 
#graph is connected
    counter = 1
#while loop in which will keep going until it reaches a point where the keys appended are already in
    while(loop == True):
    #base boolean that checks if the list of elements in a key are already in used_keys
        already_in = True
    #for loop that goes through each element of the key
        for element in graph[key]:
    #checks whether or not the element is in used_keys
            if(element not in used_keys):
                #appends the key
                used_keys.append(element)
                #sets the already_in to false
                already_in = False
        #if no new key(element) is appended then it will set the loop to false which will stop it
        if(already_in == True):
            loop = False
        #will continue the loop and set the key to the ones in the used_key 
        else:
            key = used_keys[counter]
            counter += 1
    #checks to see if the list of keys we found are equal to the entire list of keys in the graph
    print(used_keys)
    print(keys)
    if(len(used_keys) != len(keys)):
        #returns false if the lists are not the same meaning the graph is not connected
        return False
    else:
        #returns true if the lists are the same which means that the graph is conncected
        return True

#test cases

output = pathGraph(4)
print("Path graph: " + str(output) )


test1 =  {0: [1], 1: [0, 2], 2: [1, 3], 3: [2,1]}
test2 = {3: [1,2,4], 2: [1,3], 1:[2,3], 4: [3]}
test3 = {1: [2], 2:[1,3], 3:[2,4], 4:[3]}
test4 = {4: [3], 2:[1,3], 3:[2,4], 1:[2]}
output = connected(test1)
print("connected: " + str(output))
output = connected(test4)
print("test2: " + str(output))


