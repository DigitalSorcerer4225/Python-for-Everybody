# Previous Code
    # text = "X-DSPAM-Confidence:    0.8475";

    # jaburwadab = text.find('0')-1
    # smakerpipi = text[jaburwadab:]

    # print(float(smakerpipi))

# Instructions:
    # 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
    # Convert the extracted value to a floating point number and print it out.

# Pseudocode
    #   1. Using find(), Find the number in the given text:
    #       text = "X-DSPAM-Confidence:    0.8475"
    #   2. Using string slicing, extract the number
    #   3. Convert the extracted value to floating point number
    #   4. Print the statement

# Current Code

text = "X-DSPAM-Confidence:    0.8475"

a = text.find('0')
extracted_num = text[a:a+6]
converted_num = float(extracted_num)
print(converted_num)