from random import choice


import string
strings = 	string.ascii_lowercase+' '
def gen_string():
	chars = [choice(strings) for i in range(28) ]
	ret = ''.join(chars)
	print 'string generated:',ret
	return ret
	
target_string = "methinks it is like a weasel"
def rate_string(s):
	rate = 0
	for i, char in enumerate(target_string):
		if char == s[i]:
			rate += 1
	score =  rate/float(len(s))
	print 'score:',score
	return score
	
def run():
	best_score = 0
	best_string = ''
	for i in range(1000):
		s = gen_string()
		rate = rate_string(s)
		if rate>best_score:
		 	best_score = rate
		 	best_string = s
	print 'best score is:', best_score
	print 'And the string is:', best_string
	
if __name__ == '__main__':
	run()
