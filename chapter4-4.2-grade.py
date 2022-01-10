# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

# Previous Code
    # try:
    #     s = float(input("Input % Grade:"))
    # except:
    #     s = "wrong"

    # if s == "wrong":
    #     print("Error, please input % Grade using numerical symbols only")
    # elif s > 1:
    #     print("Please input in these range of numbers: 0-1")
    # elif s < 0:
    #     print("Negative numbers are not possible input")
    # elif s >= 0.9: print("A")
    # elif s >= 0.8: print("B")
    # elif s >= 0.7: print("C")
    # elif s >= 0.6: print("D")
    # elif s < 0.6: print("F")
# Pseudo Code:

    # if score is out of range:
    #     print an error
    # elif score is >= 0.9:
    #     print A
    # elif score is >= 0.8:
    #     print B
    # elif score is >= 0.7:
    #     print C
    # elif score is >= 0.6:
    #     print D
    # elif score is <0.6:
    #     print F
# Current Code:
score = input("Enter score between 0.0 and 1.0:")
s = float(score)

if s < 0.0 or s > 1.0 :
    print("Error. Please enter a number between 0.0 and 1.0!")
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s <0.6:
    print("F")