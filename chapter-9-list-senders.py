# Previous Code:
    # fname = input("Enter file name: ")
    # if len(fname) < 1 : fname = "mbox-short.txt"

    # fh = open(fname)
    # count = 0

    # for x in fh:
    #     if x.startswith('From:'):
    #         continue
    #     elif x.startswith('From'):
    #         count = count + 1
    #         y = x.split()
    #         print(y[1])

    # print("There were", count, "lines in the file with From as the first word")


# Instructions:
    # 8.5 Open the file mbox-short.txt and read it line by line. 
    # When you find a line that starts with 'From ' like the following line:
    # From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    # You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
    # Then print out a count at the end.
    # Hint: make sure not to include the lines that start with 'From:'. 
    # Also look at the last line of the sample output to see how to print the count.

    # You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 

#Pseudocode:
    # Open file mbox-short.txt
    # Read the opened file line by line.
    # Find a line that starts with 'From'. Don't include the lines that start with 'From:'
    # Parse the line that starts with 'From' using split()
    # Print out the second word in the line (address of the person who sent the message)
    # Print the total number of the extracted email addresses
    # 



#Pseudocode:
    # Open file mbox-short.txt
    # Read the opened file line by line.
    # Find a line that starts with 'From'. Don't include the lines that start with 'From:'
    # Parse the line that starts with 'From' using split()
    # Print out the second word in the line (address of the person who sent the message)
    # Print the total number of the extracted email addresses

count = 0
    
with open('mbox-short.txt', 'r') as file_object:
    for line in file_object:
        if line.startswith('From:'): continue
        elif line.startswith('From'):
            #print(line)
            count = count + 1
            sender = line.split()
            print(sender[1])

print(f'There were {count} lines in the file with From as the first word')