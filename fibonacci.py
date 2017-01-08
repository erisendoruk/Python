first_number = raw_input('Enter the beginning of the Serie: ')
count_of_number = raw_input('Enter the count of numbers: ')
x = 0
y = 1
lst = list()
while len(lst) < int(count_of_number) :
    y = x + y
    if y > int(first_number) :
        lst.append(y)
        if len(lst) == int(count_of_number) :
            break
    x = y + x
    if x > int(first_number) :
        lst.append(x)
        if len(lst) == int(count_of_number) :
            break
print sum(lst)
