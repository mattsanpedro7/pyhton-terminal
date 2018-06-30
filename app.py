import pymongo

# address of mongodb instance
uri = "mongodb://127.0.0.1:27017"

client = pymongo.MongoClient(uri)
database = client['python-udemy']
collection = database['students']

# pymongo print
print(collection)

students = collection.find({})

# this will print the cursor at a memory address
# print(students)

# # need to loop through entries
# for student in students:
#     print(student)

# # option 1: python does list comprehension
# student_list = []
# for student in students:
#     student_list.append(student)

# option 2: for each student in collection, put it inside new list
# shift + F6: renames variables
students = [student['name'] for student in collection.find({}) if student['mark'] == 99]

print(students)
