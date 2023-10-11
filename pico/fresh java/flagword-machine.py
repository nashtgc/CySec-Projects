import re 

file_path = '/mnt/c/Users/nmuni/Desktop/SHARED FOLDER/pico/fresh java/flagExtracts.txt'

with open(file_path, 'r') as file:
    input_string =file.read()
#print(input_string)

#Use Regular Expression to Extract words in single Quotes
extracted_words = re.findall(f"'(.*?)'", input_string)

#print(extracted_words)

result_string = ' '.join(extracted_words)
print(result_string)

#reversed string 
rev_st = ''.join(reversed(result_string))
print(rev_st.replace(" ", ""))