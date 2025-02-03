#map
number = [3,6,7,2]
squared_num = map(lambda num:num *num, number)
print(list(squared_num))

#filter

odd_nums = filter(lambda num :num % 2!=0,number)
print(list(odd_nums))

