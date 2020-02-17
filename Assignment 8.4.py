# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line
# check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
list_remove_duplicates = list()
for line in fh:
    lst = lst + line.rstrip().split()
# # Remove duplicates in list
# lst = list(dict.fromkeys(lst))
for word in lst:
    if word not in list_remove_duplicates:
        list_remove_duplicates.append(word)
list_remove_duplicates.sort()
print(list_remove_duplicates)        
