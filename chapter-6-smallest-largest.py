# Previous code
    # largest = None
    # smallest = None
    # while True:
    #     num = input("Enter a number: ")
    #     if num == "done": 
    #         break
    #     try:
    #         num = int(num)
    #     except:
    #         num = print("Invalid input")
    #         continue
        
    #     if largest is None:
    #         largest = num
    #     elif num > largest:
    #         largest = num
    
    #     if smallest is None:
    #         smallest = num
    #     elif num < smallest:
    #         smallest = num

            
    # print("Maximum is", largest)
    # print("Minimum is", smallest)

# Instructions
    # 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
    # Once 'done' is entered, print out the largest and smallest of the numbers. 
    # If the user enters anything other than a valid number catch it with a try/except and 
    # put out an appropriate message and ignore the number. 
    # Enter 7, 2, bob, 10, and 4 and match the output below.

# Pseudocode
    # intialize list
    # 
    # While True:
    #      ask for user input
    #      if answer == 'done':
    #          break
    #   
    #      try:
    #          convert answer to integer
    #      except:
    #          print("please enter an integer")
    #          continue
    #
    #       list.append(answer)
    #
    # intiialize smallest = None
    # initialize largest = None
    #
    # For n in list:
    #   find the smallest
    #   find the largest
    #
    # print result

# Current Code: note that the previous code is better since it has fewer lines than the current.
numbers = list()

while True:

    user_input = input("Give me an intger.\nInteger(enter 'done' once you are done): ")

    if user_input == 'done':
        break

    try:
        user_input = int(user_input)
    except:
        print("Invalid input")
        continue
    
    numbers.append(user_input)

smallest = None
largest = None

for n in numbers:
    if smallest is None:
        smallest = n
    elif n <= smallest:
        smallest = n
    if largest is None:
        largest = n
    if n >= largest:
        largest = n

print('Maximum is', largest)
print('Minimum is', smallest)