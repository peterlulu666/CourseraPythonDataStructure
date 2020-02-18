# When we encounter a new name, we need to add a new entry in the dictionary and
# if the second or later time we have seen the name, we simply add one to the
# count in the dictionary under that name.
def count_name_frequency(name_list):
    name_list = list(name_list)
    counts = dict()
    for name in name_list:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts[name] + 1
    return counts


# The pattern of checking to see if a key is already in a dictionary and assuming
# a default value if the key is not there is so common that there is a method
# called get() that does this for us.
def count_name_list_frequency(name_list):
    name_list = list(name_list)
    counts = dict()
    for name in name_list:
        # We can use get() and provide a default value of zero when the key
        # is not yet in the dictionary and then just add one
        # If name is not in counts dictionary the counts.get(name, 0) returns the default value 0
        # If name is in counts dictionary the counts.get(name, 0) return counts[name] dictionary value
        counts[name] = counts.get(name, 0) + 1

    return counts


def main():
    name_list = ["computer", "computer", "programming"]
    print(count_name_frequency(name_list))
    print(count_name_list_frequency(name_list))


main()
