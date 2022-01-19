# Previous Code:
    # # Use the file name mbox-short.txt as the file name
    # fname = input("Enter file name: ")
    # fh = open(fname)


    # count = 0
    # total = 0

    # for line in fh:
    #     if not line.startswith("X-DSPAM-Confidence:"):
    #         continue
    #     else:
    #         count = count + 1
    #         x = line.find('0')
    #         total = total + float(line[x:])

    # print("Average spam confidence:", total/count)

# Instructions:
    # 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
    # X-DSPAM-Confidence:    0.8475
    # Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce 
    # an output as shown below. Do not use the sum() function or a variable named sum in your solution.
    # You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Pseudocode:
    # Intialize counter variable
    # Intialize total variable
    # Get user input for a filename
    # Open the file in read mode
    # Look for the lines of the form X-DSPAM-Confidence:    0.8475
    # Count the lines found above
    # Extract the floating point values from each of the lines above
    # compute the average of those values

# Extra Notes:
    # In this code, I have assumed that the user knows what to input in the filename so that i dont have to use try-except block to make the code simpler.

# New code:

    count = 0
    total = 0

    #file_name = 'mbox-short.txt'

    file_name = input('Enter filename: ')
    with open(file_name, 'r') as f_object:
        for line in f_object:
            if not line.startswith('X-DSPAM-Confidence'):
                continue
            else:
                count = count + 1
                x = line.find('0')
                number = line[x : x+6]
                total = total + float(number)

    print(f'Average spam confidence: {total/count}')