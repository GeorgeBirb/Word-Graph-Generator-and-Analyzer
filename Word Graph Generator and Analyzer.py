#!/usr/bin/env python
# coding: utf-8

# In[1]:


import operator
import os
import random


#############
# Functions
#############
def get_words_from_text(file_path):
    # Reading the file
    with open(file_path, 'rt', encoding='utf-8') as f:
        # Getting as String
        text = f.read()

        # Replacing whitespaces with a single space
        text = ' '.join(text.split())

        # to Lower Case
        text = text.lower()

        # punctuations and numbers
        punctuations = '''|—!()-[]{};:\'\’\“\”\"\"\,<>./?@#$%^&*_~'''

        for i in text:
            if i in punctuations or i.isdigit():
                # Replacing punctuation with nothing
                text = text.replace(i, '')

        # Replacing unnecessary whitespaces - which may result from the elimination of punctuation marks - with space
        text = ' '.join(text.split())

    # Splitting the text based on spaces and get back a list of its words
    words = text.split()

    return words


def get_number_of_words(words):
    # Returning the number of elements (words) in the list
    return len(words)


def get_number_of_unique_words(words):
    # Converting the list to a set so that we keep the unique elements of the list
    # Returning the number of elements (unique words) of the set
    return len(set(words))


def get_5_least_frequent_words(words):
   # Create a dictionary which has the words as key and the number of their occurrences as value
    dict_of_occurrences = {}
    for item in words:
        if item in dict_of_occurrences:
            dict_of_occurrences[item] += 1
        else:
            dict_of_occurrences[item] = 1

    # Sort dictionary keys by their number of occurrences in ascending order
    sorted_list = sorted(dict_of_occurrences.items(), key=operator.itemgetter(1))  
    # Returning tuples, sorted ascending based in the 2nd element of the tuple 

    # Saving the 5 most rare elements of the list
    final_list = sorted_list[:5]

    # Creting the final list of rare elements
    least_words = []
    # Accessing the list with the tuples
    for key, value in final_list:
        least_words.append(key)

    return least_words


# Dynamic creation of graph
def graph_add_node(v1, v2):
    # checking if these are consecutive identical words
    if v1 == v2:
        return
    # Check if vertex v1 already exists
    if v1 in my_graph:
        # Check if vertex v2 already exists
        if v2 in my_graph[v1]:
            # finding the weight index of the pair
            w_index = my_graph[v1].index(v2) + 1
            # increase in weight by 1
            my_graph[v1][w_index] = my_graph[v1][w_index] + 1
        else:
            my_graph[v1].append(v2)
            my_graph[v1].append(1)
    else:
        # adding the new vertices
        temp_dict = {
            v1: [v2, 1]
        }
        my_graph.update(temp_dict)

#A' mode of operation
#Function to find top K words
def top_k_words(word, K):
    try:
           #list for top K words
           top_words = []
           #list to use for the candidate words
           cand = []
           #lsit of weights
           weights = []
           #list of words
           words = []
           for v in my_graph[word]:
                
           #If it is an integer, we update the list of weights
           #Otherwise we update the list of words
               if isinstance(v,int):
                   weights.append(v)
               else:
                   words.append(v)
           #counter initialization to find the top words
           i = 0
           #Make copies of the lists we will use
           #to find the candidate words
           weights2 = weights.copy()
           words2 = words.copy() 
           while i < K:
                #finding max weight
                max_w = max(weights)
                cand = []
                #traverse the list to find all words
                #which have a weight equal to max
                for w in weights:
                    if w == max_w:
                        #If we don't use the copies in the following
                        #delete commands, any change will modify
                        # the initial lists and the resulting output
                        #will be false
                        #find location of weight
                        w_index = weights2.index(w)
                        #find position of word with weight=w and add
                        #her to the candidates
                        cand.append(words2[w_index])
                        #delete from the lists-copies of the above weight and of
                        #above the word so that they are not taken into account in the next iteration
                        weights2.pop(w_index)
                        words2.pop(w_index)
                #If more than one word has maximum weight
                #return a random one, otherwise return the one with the maximum weight
                if len(cand) > 1:
                    #random word selection from those with maximum weight
                    toappend = random.choice(cand)
                    #add runner to return list
                    top_words.append(toappend)
                    #find the runner pointer in the original list
                    l_index = words.index(toappend)
                    #remove from initial runner-up lists
                    words.pop(l_index)
                    # and the weight corresponding to it
                    weights.pop(l_index)   
                else:
                    #same process as before, now the runner up is
                    #the 1st and only element of the cand list
                    toappend = cand[0]
                    top_words.append(toappend)
                    l_index = words.index(toappend)
                    words.pop(l_index)
                    weights.pop(l_index) 
                #update the copies so they don't contain the wildcard
                # and its weight for the next iteration
                weights2 = weights.copy()
                words2 = words.copy()
                #increment counter by one, until K words are selected
                i += 1
     
           print('Top ',K,'words are:')
           print(top_words)
    except:
        #in case more words are requested than there are
        #error will be handled here
        print('''There's no other word.''')
        #display all words found up to the error
        print('Top ',len(top_words),'words are:')
        print(top_words)


#B' mode of operation
#Function to select the most likely next word
#ie the one with the biggest weight
def graph_next_vertice(current):
    #We create a list which will contain only the weights
    # of the corresponding vertex
    w_list = []
    try:
        for w in my_graph[current]:
    #We select only integers
    #ie the weights
            if isinstance(w,int):
                w_list.append(w)
    
        #we find the max weight
        max_w = max(w_list)
        #list of candidate words
        cand = []
        #we create a copy of which we will
        #delete the candidate words
        temp_list = my_graph[current].copy()
        #traverse the list to find all words
        #which have a weight equal to max
        for w in temp_list:
            if w == max_w:
                #find the pointer to the position of the weight
                w_index = temp_list.index(w)
                #find the position of the corresponding word and
                #adding the word to candidates
                cand.append(temp_list[w_index - 1])
                #remove the weight from the list
                temp_list.pop(w_index)
        #If more than one word has maximum weight
        #return a random one, otherwise return the one with the maximum weight
        if len(cand) > 1:
            return random.choice(cand)
        else:
            #find the location of the maximum weight
            max_w_index = my_graph[current].index(max_w)
            # find the matching word and return it
            return my_graph[current][max_w_index - 1]
    except:
        print('There is no next word.')
        return ''

def seq_words_higher_probability(word, N):
    #add the user's word to the output message
    output = word
    #initialize variable to be used for
    #finding the next node
    next_vertice = word
    while N > 0:
        #call next node return function
        next_vertice = graph_next_vertice(next_vertice)
        #if no error occurred, then adds it
        #next word in output and decrements counter N
        if next_vertice != '':
            output += " " + next_vertice
            N = N - 1 
        else:
            #if an error occurred it completes the retry
            break
    print(output)
    
#C' mode of operation
def graph_next_probability_vertice_buckets(current):
    #We create a list of the vertices, one of the weights, one of the
    #probabilities and one representing the die
    v_list = []
    w_list = []
    p_list = []
    r=random.random()
    
    try:        
        #Iterate through the adjacency list for our vertex
        for i in range(len(my_graph[current])):
            #in the even positions are the names of the vertices
            if i%2==0:
                v_list.append(my_graph[current][i])
            #odds are the burdens
            else:
                w_list.append(my_graph[current][i])
    
        # Calculate probabilities for each vertex
        total_weight = sum(w_list)
        for w in w_list:
            probability = w/total_weight
            p_list.append(probability)
    
        # Using the choices function
        # return random.choices(v_list, weights=p_list, k=1)[0]
    
        # For each position in the probability list decrement r by the probability
        position = 0
        for i in range(len(p_list)):
            r=r-p_list[i]
            if r<0:
                position = i
                break
    
        # We return the next vertex
        return v_list[position]
    except:
        print('There is no next word.')
        return ''
    
def seq_words(word, N):
    #add the user's word to the output message
    output = word
    #initialize variable to be used for
    #finding the next node
    next_vertice = word
    while N > 0:
        #call next node return function
        next_vertice = graph_next_probability_vertice_buckets(next_vertice)
        if next_vertice != '':
            #if no error occurred, then adds it
            #next word in output and decrements counter N
            output += " " + next_vertice
            N = N - 1 
        else:
            break
    print(output)
    
#Function to input the user and check it
def user_input():
    word = input('Type the word: ').lower()
    #check if the given word is not in the set
    if word not in allwords:
        word = 'usererror'
        num = 'error'
        print('The word you entered does not exist in the set.')
        print('##########################\n')
        return word, num
    try:
        #check if input is an integer
        num = int(input('Enter an integer: '))
    except:
        print('The number you entered was not an integer.')
        print('##########################\n')
        num = 'error'
    else:
        #check if the integer is less than the total number of words
        if num > len(allwords)-1:
            num = 'error'
            print('The number you entered exceeds the number of words available.')
            print('##########################\n')
    return word, num

#Συνάρτηση εμφάνισης μενού
def menu():
    while(True):
        print('Select a function by typing the letter that corresponds to it:\n')
        print('Α - Return K most likely words\n')
        print('B - Generating a sequence of N most likely words\n')
        print('C - Generating a sequence of N words\n')
        print('D - End program\n')
        func = input('Give an option: ')
        
        if func == 'A':
            word, K = user_input()
            if word!= 'usererror' and K != 'error':
                #functionality A
                print('####### Έναρξη λειτουργίας Α #######\n')
                top_k_words(word, K)
                print('####### Τέλος λειτουργίας #######\n')
                pass
            else:
                continue
        elif func == 'B':
            word, N = user_input()
            if word!= 'usererror' and  N != 'error':
                print('####### Start operation Β #######\n')
                seq_words_higher_probability(word, N-1)
                print('####### End of operation #######\n')
            else:
                continue
        elif func == 'C':
            word, N = user_input()
            if word!= 'usererror' and  N != 'error':
                #functionality C
                print('####### Start operation C #######\n')
                seq_words(word, N-1)
                print('####### End of operation #######\n')
                pass
            else:
                continue
        elif func == 'D':
            break
        else:
            print("The option is wrong.\n")


############################
# Start main program
############################

# Current folder
current_dir = os.getcwd()

# List files in current directory
files_in_directory = os.listdir(current_dir)

# Counter for files
file_count = 0

# Final list of words
allwords = []

# Access the list of files in the current folder
for file in files_in_directory:
    # If the file is a text file
    if file.endswith('.txt'):
        # Retrieve the words from each file
        w = get_words_from_text(file)
        # Update the final list of words
        allwords.extend(w)
        file_count += 1


print('########## Basic statistics ##########')
print('Number of files trained: ', file_count)
print('Total number of words read: ', get_number_of_words(allwords))
print('Number of unique words read: ', get_number_of_unique_words(allwords))
print('The 5 rarest words: ', get_5_least_frequent_words(allwords))
print('##########################\n')
# Create the empty graph
my_graph = {}

#Inserting the vertices and calculating the weights in the graph
for i in range(len(allwords)):
    #adds the word pairs serially to the graph,
    #omitting the last word not followed by another
    if i != len(allwords) - 1:
        graph_add_node(allwords[i], allwords[i + 1])
    else:
        if allwords[i] in my_graph:
            continue
        else:
            temp_dict = {
                allwords[i]: []
            }
            my_graph.update(temp_dict)

#Function call to display the function menu
menu()


# In[ ]:




