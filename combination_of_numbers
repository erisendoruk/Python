import itertools
input_list = list()
output_list = list()
while True :
    number = raw_input('Enter Your Integer: ')
    try :
        number = int(number)
        input_list.append(number)
    except :
        break
print 'Your Input:', input_list
sorted_input_list = sorted(input_list)
print 'Your Sorted Input:', sorted_input_list
expected_total = raw_input('Enter Your Expected Total: ')
for l in range(1, len(sorted_input_list)+1) :
    for subset in itertools.combinations(sorted_input_list, l) :
        if sum(subset) == int(expected_total) :
            if not subset in output_list :
                output_list.append(subset)
print 'All Combinations Are:', output_list
