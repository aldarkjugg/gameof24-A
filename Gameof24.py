#Game of 24
#Input four numbers (1~13), and this program will find a way to make 24 out of these four numbers
#only use these operators: (, ), +, -, *, /
#May not always have a solution

import itertools


user_input = raw_input('please enter four numbers between 1 and 13, seperated by space\n')


#user_input = '7 10 10 13'

a, b, c, d = user_input.split()
user_input = itertools.permutations([float(a), float(b), float(c), float(d)])
calculation = []

for i in list(user_input):
	operators = itertools.combinations_with_replacement(['+', '-', '*', '/','+', '-', '*', '/','+', '-', '*', '/'], 3)
	for j in list(operators):

		calculation.append( str(i[0]) + j[0] + str(i[1]) + j[1] + str(i[2]) + j[2] + str(i[3]) )
		calculation.append( '(' + str(i[0]) + j[0] + str(i[1]) + ')' + j[1] + str(i[2]) + j[2] + str(i[3]) )
		calculation.append( '(' + str(i[0]) + j[0] + str(i[1]) + j[1] + str(i[2]) + ')' + j[2] + str(i[3]) )
		calculation.append( str(i[0]) + j[0] + '(' + str(i[1]) + j[1] + str(i[2]) + ')' + j[2] + str(i[3]) )
		calculation.append( str(i[0]) + j[0] + '(' + str(i[1]) + j[1] + str(i[2]) + j[2] + str(i[3]) + ')' )
		calculation.append( str(i[0]) + j[0] + str(i[1]) + j[1] + '(' + str(i[2]) + j[2] + str(i[3]) + ')' )
		calculation.append( '(' + str(i[0]) + j[0] + str(i[1]) + ')' + j[1] + '(' + str(i[2]) + j[2] + str(i[3]) + ')' )

new_num = list(set(calculation))

for k in new_num:
	try:
		if eval(k) == 24.0:
			print k, 'OKAY!!'
	except ZeroDivisionError:
		print 'there is a /0 calculation'

