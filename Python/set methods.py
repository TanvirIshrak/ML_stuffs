# creating an empty set
c = set()
print(type(c))

# adding values to an empty set
c.add(3)
c.add(34)
c.add(23)
print(c)

#you can't add a list or dictionary in set
# c.add([1,3])
# c.add({12,23})

#you can add a tupple data in set
c.add((1,2,3,4))
print(c)

# removing any item from set
c.remove(3)
print(c)

# .pop() removed an atribute from the set and returns the element removed
print(c.pop())

# making the whole set empty
# print(c.remove())


c.add(3)
c.add(34)
c.add(23)
print(c)

# return the union value of 2sets
union_set = c.union({34,56,67})
print(union_set)
intersection_set=c.intersection({34,56,67})
print(intersection_set)