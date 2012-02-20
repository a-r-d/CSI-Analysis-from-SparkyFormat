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
		# in case we have endline chars:
		splits[pos] = splits[pos].replace('\n', '')
		histList.append(float(splits[pos]))
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
	

def get_diffs(list1, list2):
	# List 1 = experimental
	# list 2 = index
	
	diffs =[]
	i = 0
	for x in list1:
		diff = float(x) - float(list2[i])
		diffs.append(diff)
		i += 1
	
	print diffs
	return diffs
	
	
	
	
def make_plot_diffs(histList, f1):
	#nothing yet
	len_list = len(histList)
	plt.hist(histList, facecolor='g')
	plt.ylabel('Number of occurences')
	plt.xlabel("Diff btwn Shifts, for file %s" % f1)
	plt.axis([-5, 5, 0, len_list])
	plt.show()
	
	
def load_graph(filename):
	lines = import_results(filename)
	histList = read_line_position(lines, 2)
	make_plot(histList, filename)
	
	# load for diffs:
	#lines = import_results(filename)
	#histList1 = read_line_position(lines, 3)
	#histList2 = read_line_position(lines, 4)
	#histList3 = get_diffs(histList1, histList2)
	#make_plot_diffs(histList3, filename)
	
	
	
	
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
