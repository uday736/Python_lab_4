# Write a program to create dictionary emp=[id,name,designation,salary]and delete designation key,update name.f

emp = {
    'id': 101,
    'name': 'uday chandrapal',
    'designation': 'Software Engineer',
    'salary': 75000
}

print("Original dictionary:", emp)

del emp['designation']

emp['name'] = 'uday chandrapal'


print("Updated dictionary:", emp)
