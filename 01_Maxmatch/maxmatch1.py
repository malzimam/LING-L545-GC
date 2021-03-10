import sys


def maxmatch(sentence, dictionary):
	if sentence == '':
		return []
	for i in range(0, len(sentence)):
		firstword = sentence[0:-i]
		remainder = sentence[-i:]
		

		if firstword in dictionary:
			return [firstword] + maxmatch(remainder, dictionary)
	

	firstword = sentence[0]
	remainder = sentence[1:]
	return [firstword] + maxmatch(remainder, dictionary)

dictionary = [line.strip() for line in open("japanese.dic").readlines()]
fd = open(sys.argv[1]) 
line = fd.readline()


while line != '':
        print(' '.join(maxmatch(line.strip('\n'), dictionary)))
        line = fd.readline()


