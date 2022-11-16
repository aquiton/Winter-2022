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
        if(counter == len(keys)):
            loop = False
        else:
            if(already_in and counter == len(used_keys)):
                loop = False
            else:
                key = used_keys[counter]
                counter += 1

    #checks to see if the list of keys we found are equal to the entire list of keys in the graph
    if(len(used_keys) != len(keys)):
        #returns false if the lists are not the same meaning the graph is not connected
        return False
    else:
        #returns true if the lists are the same which means that the graph is conncected
        return True


big_tree = {
    1:[2,3],
    2:[1,4,5],
    3:[1,6,7],
    4:[2,8],
    5:[2],
    6:[3],
    7:[3,10,12],
    8:[4,9],
    9:[8,16,17],
    10:[7,11],
    11:[10],
    12:[7,13,14],
    13:[12],
    14:[12,15],
    15:[14],
    16:[9],
    17:[9,18],
    18:[17,19],
    19:[18,20],
    20:[19]
}

big_tree_notConnected = {
    1:[2,3],
    2:[1,4,5],
    3:[1,6,7],
    4:[2,8],
    5:[2],
    6:[3],
    7:[3,10,12],
    8:[4,9],
    9:[8,16],
    10:[7,11],
    11:[10],
    12:[7,13,14],
    13:[12],
    14:[12,15],
    15:[14],
    16:[9],
    17:[18],
    18:[17,19],
    19:[18,20],
    20:[19]
}

output = connected(big_tree)
print(output)
output = connected(big_tree_notConnected)
print(output)
