import csv
import os
from subprocess import call
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import sys

# def solve(data):

PATH = str(sys.argv[1])
opcodes_list = ['mov', 'push', 'call', 'pop', 'cmp', 'jz', 'lea', 'test', 'jmp', 'add', 'jnz', 'retn', 'xor', 'and', 'bt', 'fdivp', 'fild', 'fstcw', 'imul', 'int', 'nop', 'pushf', 'rdtsc', 'sbb', 'setb', 'setle', 'shld', 'std', '(bad)']
headers = ['name']
headers.extend(opcodes_list)

if not os.path.exists('./test1.csv'):
	with open("test1.csv", "w") as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		writer.writerow(headers)

for i in os.listdir(PATH)[:1000]:
	row = [0]*(len(headers)-1)
	file = os.path.join(PATH, i)
	if os.path.isfile(file):
		row[0] = file
		call('objdump -M intel -D ' + file[2:] + ' > hello.txt', shell=True)
		with open('hello.txt', 'r') as f:
			for l in f:
				if ':' in l:
					for i, opcode in enumerate(opcodes_list):
						if opcode in l:
							row[i+1] += 1

		with open("test1.csv", "a") as csv_file:
			writer = csv.writer(csv_file, delimiter=',')
			writer.writerow(row)