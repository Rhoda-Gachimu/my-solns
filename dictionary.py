# stores info with key value pairs
# use curly brackets
# keys can be strings or numbers

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
}

print(monthConversions["Mar"])
print(monthConversions.get("Mar"))

# use .get
# to pass a default value to be printed out incase value is not found

print(monthConversions.get("Nov", "Not a valied key"))