def most_common_characters(s):
    char_count={}
    for char in s:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    sorted_chars=sorted(char_count.items(),key=lambda x:x[1],reverse=True)
    count=0
    for char,frequency in sorted_chars:
        if count==3:
          break
        print(f"Character: {char}, Occurrence count: {count}")
        count+=1
input_string=input("enter any string  ")
most_common_characters(input_string)
