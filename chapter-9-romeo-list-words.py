# Previous Code:
    # fname = input("Enter file name: ")

    # fh = open(fname)

    # current = list()

    # for xline in fh:
    # 	x = xline.split()
    # 	for yword in x:
    # 		if yword in current:
    # 			continue
    # 		else:
    # 			current.append(yword)

    # current.sort()
    # print(current)

# Instructions/Pseudocode:
    # Open the file romeo.txt and read it line by line. 
    # For each line, split the line into a list of words using the split() method. 
    # The program should build a list of words. 
    # For each word on each line check to see if the word is already in the list and if not append it to the list. 
    # When the program completes, sort and print the resulting words in alphabetical order.
    # Open the file romeo.txt and read it line by line. 
    # For each line, split the line into a list of words using the split() method. 
    # The program should build a list of words. 
    # For each word on each line check to see if the word is already in the list and if not append it to the list. 
    # When the program completes, sort and print the resulting words in alphabetical order.

#Pseudocode:

#Open romeo.txt
#Read each line
#split each line into a list of words
#for each word in the list of words
#if the word is on the list, continue
#otherwise, append the word to the list of words.
#sort the list of words
#print the resulting words.



words = list()

with open('romeo.txt', 'r') as f_object:

    for line in f_object:
        list_words = line.split()
        
        for word in list_words:
            if word in words:
                continue
            else:
                words.append(word)
                
    #Why does these code snippets do not work?
        # for word in list_words:
        #     if word in words == True:
        #         continue
        #     else:
        #         words.append(word)
        
        #for word in list_words:
        #    if word in words == False:
        #        words.append(word)
        #    else:
        #        continue

words.sort()          
print(words)