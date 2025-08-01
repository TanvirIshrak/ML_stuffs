name = 'Ishrak'

print(name[3])  #it will print index 3

print(name[0:4]) #it will print from 0 to 4-1 index

first = 1
second =4
print(name[first:second]) #it will print from 1 to second-1 index

#using negative index
print(name[-4:-1])


#skipping index
s='ishrakisastudent'
print(s[0::3]) #[first index : last index : which index to skip]
#it will print first to last and skip 2 values each
#as it skips i 'sh' r 'ak' i 'sa' s 'tu' d 'en' t