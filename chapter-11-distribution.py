# Instructions:
    # 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
    # You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
    #   From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    # Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# Previous Code:
    # # 2) find() We can use this Python method also to find the position of a character in a given string. ...
    # # Example: y = 'Hello world' y.find('H') -> 0

    # try:
    #     # fhand = open(input('Enter a file name: '))
    #     fhand = open('mbox-short.txt')

    # except:
    #     print("Invalid input or file does not eixst. Quitting program")
    #     quit()

    # counter = dict()

    # for line in fhand:
    #     if line.startswith("From:"):
    #         continue
    #     elif line.startswith("From"):
    #         # print(line[line.find(":")-2:line.find(":")+6]) #used to find the time string
    #         timef = line.find(":")
    #         # print(line[timef-2:timef+6]) # compact version of finding the time string
    #         timestr = (line[timef-2:timef+6])
    #         # print(timestr)
    #         ts = timestr.split(":")
    #         # print(ts[0])
    #         hr = ts[0]
    #         counter[hr] = counter.get(hr,0) + 1

    # # print(counter)

    # lst = list()
    # for (hr,count) in counter.items():
    #     lst.append((hr,count))

    # lst.sort(reverse=False)
    # # print(lst)

    # for (hr, count) in lst:
    #     print(hr, count)


    #     # else:
    #     #     print("No 'From' detected. Quitting Program...")
    #     #     quit()
# Pseudocode:
	# 0. Create an empty dictionary and an empty list.
    # 1. Open mbox-short.txt as read.
    # 2. In mbox-short.txt, find the lines that starts with 'From '.
    # 3. In each 'From ' line, find the hour with the three-colon format.
    # 4. Store what you found in #3 in a variable.
	# 5. Split the variable in #4 using colons as a delimiter.
    
    # 6. Make a distribution of the frequency of the hours.
  	#		- For each of the list containing the 'splitted hour',
    #		- if the hour is already in the dictionary in #1, change its current value to its previous value plus one.
    #		- if not, add it to the dictionary and assign it the value of 1.
    
    # 7. Data treatment (sorting):
    #		- For each of the key-value in the dictionary, append it as an elemnt of the list created at #0 as a two-tuple.
    #		- After appending all the values in the dictionary to the list, sort the list.
    # 
    # 8. Print the tuples in the sorted list in the following format: 'key', 'value'.
counts = dict()
counts_l = list()
with open('mbox-short.txt','r') as file_object:
    
    for line in file_object:
        if line.startswith('From '):
            x = line.find(':')
            line = line[x-2:x+7]
            line = line.split(':')
            hour = line[0]
            
            if hour in counts:
                counts[hour] = counts[hour] + 1
            
            elif hour not in counts:
                counts[hour] = 1

    for k,v in counts.items():
        counts_l.append((k,v))

counts_l.sort()

for count in counts_l:
    print(count[0], count[1])