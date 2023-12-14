lucky_numbers = [4,8,12,85,16,20]

friends = ["Mercy", "Viv", "Loise", "Adrian", "Maritim", "Adrian"]

print(friends)


# extend function  - takes a list and append another list onto it

friends.extend(lucky_numbers)
print(friends)

# append function   - adds an individual item to end of the list

friends.append("Rhoda")
print(friends)

# insert function - adds an item to a list but not at the end.
# takes 2 parameters
# 1. the index where to insert the item
# 2.name of the element you want to add.

friends.insert(2, "kelly")
print(friends)

# remove
friends.remove("Viv")
print(friends)

# clear - removes everything/resets
friends.clear()
print(friends)

# pop - pops an item off of the list(basically removes the last element from the list)

friends.pop()
print(friends)

# To check if an element exists in a list


print(friends.index("Rhoda"))

# count - shows the number of times an element appears

print(friends.count("Rhoda"))
print(friends.count("Adrian"))

# sort - sorts in ascending order
friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

# reverse

lucky_numbers.reverse()
print(lucky_numbers)

# copy

unlucky_numbers = lucky_numbers.copy()

print(unlucky_numbers)