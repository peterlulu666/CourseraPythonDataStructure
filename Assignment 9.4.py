# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent
# the greatest number of mail messages. The program looks for 'From ' lines and
# takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the
# dictionary using a maximum loop to find the most prolific committer.        
# Open file
import operator

paragraph = open("mbox-short.txt")
email_list = list()
for line in paragraph:
    if line.startswith("From "):
        email_list.append(line.split()[1])
# Count frequency
counts = dict()
for email in email_list:
    if email not in counts:
        counts[email] = 1
    else:
        counts[email] = counts[email] + 1
# Find the largest value in Python dictionary
largest_number = None
for key, value in counts.items():
    if largest_number is None:
        largest_number = value
    elif largest_number < value:
        largest_number = value
# Print the key with the largest value in Python dictionary
email_address = ""
for key, value in counts.items():
    if value == largest_number:
        email_address = key
print(email_address, largest_number)
# # Find the key with the maximum value in Python dictionary
# print(max(counts.items(), key=operator.itemgetter(1))[0])
# print(max(counts, key=counts.get))
# # Print the maximum value
# print(counts["cwen@iupui.edu"])
# print(max(counts, key=counts.get), counts[max(counts, key=counts.get)])
