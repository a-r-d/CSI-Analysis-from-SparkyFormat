import matplotlib.pyplot as plt



def import_results(filename):
	f = open(filename)
	lines = []
	while(1):
		line = f.readline()
		
		if line == "":
			break
		
		lines.append(line)
	#print lines
	return lines
	

def read_line_position(lines, pos):
	histList = []
	for line in lines:
		splits = line.split(' ')
		print splits[pos]
		histList.append(int(splits[pos]))
	return histList


def make_plot(histList, f1):
	len_list = len(histList)
	plt.hist(histList, facecolor='g')
	plt.ylabel('Number of occurences')
	plt.xlabel("Category for CSI, for file %s" % f1)
	plt.axis([-1, 1, 0, len_list])
	
	neg1 = 0
	for x in histList:
		if( x == -1): 
			neg1 += 1
	
	freq_neg1 = ((float(neg1) / float(len_list)) * 100.0)
	freq_neg1 = "%3.2f percent" % freq_neg1
	plt.text(-1, (len_list * 0.9), freq_neg1)
	
	neg1 = 0
	for x in histList:
		if( x == 0): 
			neg1 += 1
	
	freq_neg1 = ((float(neg1) / float(len_list)) * 100.0)
	freq_neg1 = "%3.2f percent" % freq_neg1
	plt.text(0, (len_list * 0.9), freq_neg1)
	
	neg1 = 0
	for x in histList:
		if( x == 1): 
			neg1 += 1
	
	freq_neg1 = ((float(neg1) / float(len_list)) * 100.0)
	freq_neg1 = "%3.2f percent" % freq_neg1
	plt.text(0.75, (len_list * 0.9), freq_neg1)
	
	plt.show()

def load_graph(filename):
	lines = import_results(filename)
	histList = read_line_position(lines, 2)
	make_plot(histList, filename)


def main():
	f1 = "results/ca.txt"
	f2 = "results/cb.txt"
	f3 = "results/co.txt"

	#load_graph(f1)
	#load_graph(f2)
	load_graph(f3)
	return 0



if __name__ == '__main__':
	main()
