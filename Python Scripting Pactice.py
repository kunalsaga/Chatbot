
# def create_cast_list(filename):
#     cast_list = []
#     with open(filename) as f:
#         for line in f:
#             name=line.split(',')[0]
#             cast_list.append(name)
#     return cast_list

    
# print(create_cast_list('C:/Users/kunal/PycharmProjects/pythonProject/KK.txt'))

## Quize 2 ##

# import random

# # We begin with an empty `word_list`
# word_file = "C:/Users/kunal/PycharmProjects/pythonProject/my_sol.txt"
# word_list = []

# # We fill up the word_list from the `words.txt` file
# with open(word_file,'r') as words:
#         for line in words:
#         # remove white space and make everything lowercase
#             word = line.strip().lower()
#         # don't include words that are too long or too short
#             if 3 < len(word) < 8:
#                 word_list.append(word)

# # TODO: Add your function generate_password below
# # It should return a string consisting of three random words 
# # concatenated together without spaces
# def generate_password(l1):
#     string=""
#     i=0
#     while i<3:
#         string+=random.choice(l1)
#         i=i+1
#     return string
    


# Now we test the function
# print(generate_password(word_list))

## Quize 3 ##
"""
Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary.
 The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. 
 It should then use it to print the flower name with the same first letter (from dictionary created in the first function).
 """

## Answer 1 ##
# def dict_fl():
#     word_file = "C:/Users/kunal/PycharmProjects/pythonProject/flowers.txt"
#     ls=[]
#     with open(word_file,'r') as f:
#             for line in f:
#                 ls.append(line.split(":"))

#     d={} 

#     for i in ls:
#         d[i[0]]=i[1]
#     return d

# def main():
#     name=input("Enter your First [space] Last name only: ")
#     for key,value in dict_fl().items():
#         if name[0]==key:
#             flowername=value
#             print("Unique flower name with the first letter:"+value)
# main()


## ANSWER 2 ##

# function that creates a flower_dictionary from filename
# def create_flowerdict(filename):
#     flower_dict = {}
#     with open(filename) as f:
#         for line in f:
#             letter = line.split(": ")[0].lower() 
#             flower = line.split(": ")[1].strip()
#             flower_dict[letter] = flower
#     return flower_dict

# # Main function that prompts for user input, parses out the first letter
# # includes function call for create_flowerdict to create dictionary
# def main(): 
#     flower_d = create_flowerdict("C:/Users/kunal/PycharmProjects/pythonProject/flowers.txt")
#     full_name = input("Enter your First [space] Last name only: ")
#     first_name = full_name[0].lower()
    
# # print command that prints final input with value from corresponding key in dictionary
#     print("Unique flower name with the first letter: {}".format(flower_d[first_name]))

# main()

"""
    Question 5

    The counter function counts down from start to stop when start 
    is bigger than stop, and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.

"""

# def counter(start, stop):
# 	x = start
# 	if start>stop:
# 		return_string = "Counting down: "
# 		while x >= stop:
# 			return_string += str(x)
# 			if x>stop:
# 				return_string += ","
# 			x-=1
# 	else:
# 		return_string = "Counting up: "
# 		while x <= stop:
# 			return_string += str(x)
# 			if x<stop:
# 				return_string += ","
# 			x+=1
# 	return return_string

# print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1)) # Should be "Counting down: 2,1"
# print(counter(5, 5)) # Should be "Counting up: 5"


"""
Quize 6

"""
def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter.isalpha():
      result[letter.lower()]=1+result.get(letter.lower(),0)
    # Add or increment the value in the dictionary
    
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}