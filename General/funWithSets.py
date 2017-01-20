from sets import Set
engineers = Set(['John', 'Jane', 'Jack', 'Janice'])
programmers = Set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = Set(['Jane', 'Jack', 'Susan', 'Zack'])
employees = engineers | programmers | managers           # union
print 'employees are:', employees
engineering_management = engineers & managers            # intersection
print 'engineering_management are:', engineering_management
fulltime_management = managers - engineers - programmers # difference
engineers.add('Marvin')                                  # add element
print engineers 


print employees.issuperset(engineers)     # superset test

employees.update(engineers)         # update from another set
print employees.issuperset(engineers)

for group in [engineers, programmers, managers, employees]: 
    group.discard('Susan')          # unconditionally remove element
    print group
    
if hasattr(group, '__iter__'):
    print 'yes you can iterate over this'