print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

# This will give an index error so comment out
if counties[3] != 'Jefferson':
    print(counties[2])

# Break
temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

# What is the score?
score = int(input("What is your test score?"))

# Determine the grade
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

# if-elif-else statements are better sometimes
# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

# Determine if "El Paso" is in the counties list
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else: 
    print("El Paso is not in the list of counties.")

# Break
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# Another check
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# Repetition practice
x = 0
while x <= 5:
    print(x)
    x = x + 1

# Iterate through list of counties... I had county, but I changed it to "i" to see if it would work (it does, and the iterator doesn't matter here)
for i in counties:
    print(i)

# Basically, i is the variable, and the for loop is setting it each time

# Using Range
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

# Don't do above, do this:
for num in range(5):
    print(num)

# Interesting - if I just print num, it gives me "4" because num = 4 is the last stored variable

# Indexing... just remember that 'i' is a variable here.  I is used for symplicity, but any variable can be used.
for i in range(len(counties)):
    print(counties[i])

# Iterate through a tuple the same way
counties_tuple = ("Arapahoe","Denver","Jefferson")
counties_tuple
for ctys in range(len(counties_tuple)):
    print(counties_tuple[ctys])

# Practice to answer question
for i in range(len(counties_tuple)):
    print(counties_tuple[i])

for founty in counties_tuple:
    print(founty)

# Iterate through dictionaries
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

print(counties_dict.keys())

for voters in counties_dict.values():
    print(voters)

# Both of these give the values

for county in counties_dict:
    print(counties_dict.get(county))

for county in counties_dict:
    print(counties_dict[county])

# Key Values
for county, voters in counties_dict.items():
    print(county, voters)

# Skill drill
for county, voters in counties_dict.items():
    print(str(county) + " county has " + str(voters) + " registerd voters.")

# Get dictionaries in a list of dictionaries

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

for i in range(len(voting_data)):
    print(i)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# This doesn't work because it prints every value as a list
for county_dict in voting_data:
    print(county_dict.values())

# This doesen't work because you're not using the values method after county_dict
for county_dict in voting_data:
    for value in county_dict:
        print(value)

# This doesn't work because it will print every value from each dictionary
for county_dict in voting_data:
     for key, value in county_dict.items():
         print(value)

# This gives you just the values
for county_dict in voting_data:
     print(county_dict['registered_voters'])

# This gives us just the keys of the dictionaries
for county_dict in voting_data:
    print(county_dict['county'])

# f strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

# New
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

message_to_candidate = (
    f"You received {my_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {my_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

# Skill drill
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    message = (f"{county} county has {voters:,} registered voters.")
    print(message)

# Skill drill 2
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for count_dict in voting_data:
    my_message = (f"{count_dict['county']} county has {count_dict['registered_voters']:,} registered voters.")
    print(my_message)
