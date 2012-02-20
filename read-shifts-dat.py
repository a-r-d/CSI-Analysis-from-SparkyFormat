
def get_shifts():
	fname = "shift-refs/csi.ha"
	ifile = open(fname, 'r')
	
	datlist = []
	i = 0
	while(i <= 21):
		line = ifile.readline()
		splitlist = line.split('\t')
		
		range = splitlist[2]
		range = range.replace('\n', '')
		
		dict = {"aa": splitlist[0], "shift": float(splitlist[1]), "range": float(range)}
		print dict
		
		datlist.append(dict)
		i += 1
	
	print datlist


def main():
	
	get_shifts()
	
	return 0


if __name__ == '__main__':
	main()
