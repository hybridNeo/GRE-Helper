import sys
import random
def type1(contents):
	print 'Provide meanings for these words'
	random.seed()
	while 1:
		i = random.randint(0,len(contents)-1)
		print '------------------------------------\n'
		q_as = contents[i].split('-')
		q = q_as[0]
		a = q_as[1]
		print '\t',q
		print '------------------------------------\n'
		raw_input("Enter answer\n")
		print "Answer: ",a

		raw_input("\nPress any key to continue\n")
		
def type2(contents):
	print 'Find the word for these meanings'

def main():
	if len(sys.argv) < 2:
		print "Provide Filename"
		exit(1)
	else:
		fname = sys.argv[1]
		fd = open(fname,"r")
		contents = fd.read().split("\n")
		contents = contents[0:-1]
		if(len(sys.argv) >= 3):
			if(sys.argv[2] == '-2'):
				type2(contents)
			else:
				type1(contents)
		else:
			type1(contents)

if(__name__ == '__main__'):
	main();
