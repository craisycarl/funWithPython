engineers = {'John', 'Jane', 'Jack', 'Janice'}  # yes curly braces look like a dictionary but this is a set
programmers = {'Jack', 'Sam', 'Susan', 'Janice'}
managers = {'Jane', 'Jack', 'Susan', 'Zack'}

employees = engineers | programmers | managers  # union
print 'employees are:', employees

engineering_management = engineers & managers  # intersection
print 'engineering_management are:', engineering_management

full_time_management = managers - engineers - programmers  # difference
print full_time_management

engineers.add('Marvin')  # add element
print engineers 

print employees.issuperset(engineers)  # superset test

employees.update(engineers)  # update from another set
print employees.issuperset(engineers)

group = []
for group in [engineers, programmers, managers, employees]:
    group.discard('Susan')  # unconditionally remove element
    print group

if hasattr(group, '__iter__'):
    print 'yes you can iterate over this'
