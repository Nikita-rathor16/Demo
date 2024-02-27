from collections import Counter

def most_common_characters(input_string):
   
    char_count = Counter(input_string)
    
   
    most_common = char_count.most_common(3)
    
   
    most_common_sorted = sorted(most_common, key=lambda x: (-x[1], x[0]))
    
    return most_common_sorted

try:
    input_string = input("Enter a string of characters: ")
    result = most_common_characters(input_string)
    print("Three most common characters along with their occurrence count:")
    for char, count in result:
        print(f"Character: {char}, Occurrence count: {count}")
except Exception as e:
    print("An error occurred:", e)