from random import choice
import time

def print_table(table):
	for row in table:
		print row,'\n'
		
	
def gen_row(table, row_no):
	row = []
	for column in range(9):
		exclude = list(row)
		for _row in range(row_no):
			exclude.append(table[_row][column])
		exclude = list(set(exclude))
		choices = [n for n in range(1,10) if n not in exclude]
		if not choices:
			return
		row.append(choice(choices))	
	return row
		
def gen_sudoku():
	table = []
	for i in range(9):
		row = []
		while not row:
			row = gen_row(table, i)
		table.append(row)
	return table

	
if __name__ == '__main__':
	table = gen_sudoku()		
	print_table(table)
