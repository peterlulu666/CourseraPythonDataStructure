# 10.2 Write a program to read through the mbox-short.txt and figure out
# the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by
# finding the time and then splitting the string a
# second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

# paragraph = open("mbox-short.txt")
# hour_list = list()
# counts = dict()
# for line in paragraph:
#     line_list = line.rstrip().split()
#     if line.startswith("From "):
#         # Print the hour
#         hour = line_list[5][0:2]
#         # Count hour frequency
#         if hour not in counts:
#             counts[hour] = 1
#         else:
#             counts[hour] = counts[hour] + 1
# # Print key and value in sorted order
# for key, value in sorted(counts.items()):
#     print(key, value)

# Open file
paragraph = open("mbox-short.txt")

# Store hour in hour_list
hour_list = list()
for line in paragraph:
    if line.startswith("From "):
        hour_list.append(line.rstrip().split()[5][0:2])

# Count hour frequency
counts = dict()
for hour in hour_list:
    if hour not in counts:
        counts[hour] = 1
    else:
        counts[hour] = counts[hour] + 1
for key, value in sorted(counts.items()):
    print(key, value)
