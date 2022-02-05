# Instructions:
    # Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
    # The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
    # The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
    #  After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
# Previous Code:

    # try:
    #     fhand = open(input('Enter text file:'))
    # except:
    #     print('Invalid Input. Quitting...')
    #     quit()

    # emails = list()
    # counter = dict()


    # for line in fhand:
    #     if line.startswith("From:"):
    #         continue
    #     elif line.startswith("From"):
    #         x = line.split()
    #         emails.append(x[1])
    #         # print(email)
    #         # break


    # for email in emails:
    #     counter[email] = counter.get(email,0) + 1

    # # print(counter,'\n\n\n')

    # largkv = None

    # for y in counter:
    #     # print(y, counter.get(y))
    #     if largkv is None or counter.get(y) > largkv: # This just prints the running largest so other values may not print
    #         largkv = counter.get(y)
    #         largk = y

    # print(largk, largkv)



    # # largk = max(counter) #This one is wrong! output should be cwen@iupui.edu': 5
    # # largkv = max(counter.values())
    # # print(largk,largkv)
# Pseudocode:

    # 1. Open mbox-short.txt as read.
    # 2. Loop through the file and look for lines that starts with 'From '.
    #   - if the line starts with from, 
    #       - take the second word and store it in a dictionary called leaderboard.
    #       - if the second word is not on leaderboard, assign to it the value 1.
    #       - if the second word is on leaderboard, take its current value and add one to it.
    #   - else, continue
    # 3. After producing the dictionary:
    #     a.) Loop through the dictionary
    #     b.) Find the key with the largest number of values
    #     c.) print it as key{1 space}value


leaderboard = {}    #intialize empty dictionary to be used for storing the sender and the corresponding number of sent mails.

with open('mbox-short.txt','r') as file_object: # In this and only this code block, open mbox-short.txt and set its alias as 'file_object'.
    for line in file_object:
                
        if line.startswith('From '):
            #print(line) #visually checks for line
            line = line.split() #store a list of words in the variable line where each entry is a word separated by whitespace of the previous 'line'.
            email = line[1]
            #print(email) #visually confirm if it got the emails.
            
            if email not in leaderboard:
                leaderboard[email] = 1 #if email is not in leaderboard, insert email into leaderboard and assign it with the value of 1.
            elif email in leaderboard:
                leaderboard[email] = leaderboard[email] + 1 #if email is already in leaderboard, take its previous value, and add one to it.


# print(leaderboard) #visually check if it got the right tally.

largest = None

for k in leaderboard:

    if largest == None:
        largest = (k,leaderboard[k])
    elif largest[1] > leaderboard[k]:
        continue
    elif largest[1] < leaderboard[k]:
        largest = (k,leaderboard[k])

print(f'{largest[0]} {largest[1]}')