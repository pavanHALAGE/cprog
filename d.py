student = {
    "name": "Rahul",
    "age": 22,
    "course": "Computer Science"
}

print("Original Dictionary:", student)

print("\nAccessing 'name':", student['name'])

print("Accessing 'age':", student.get('age'))

student['college'] = "NIT Karnataka"
print("\nAfter Adding 'college':", student)

student['age'] = 23
print("\nAfter Updating 'age':", student)

del student['course']
print("\nAfter Deleting 'course':", student)

print("\nLooping through dictionary:")
for key, value in student.items():
    print(key, ":", value)


if 'name' in student:
    print("\nKey 'name' exists!")


print("\nTotal items in dictionary:", len(student))

student_copy = student.copy()
print("\nCopied Dictionary:", student_copy)




good luck

