def reverse_wordwise(input_string):
    words = input_string.split()  
    reversed_string = ""
    for i in range(len(words) - 1, -1, -1): 
        reversed_string += words[i] + " "  
    return reversed_string.rstrip()  


input_string = input("Enter a string: ")
reversed_string = reverse_wordwise(input_string)
print("Reversed word-wise string:", reversed_string)
