def main():
	infile = open('fitness-data.txt',"r")
	outfile = open('results.txt', 'w')
	steps_total, steps_max = steps_analyzer(infile)
	heart_rate_average = heart_rate_analyzer(infile)
	sleep_total, sleep_min = sleep_analyzer(infile)
	write_results_file(outfile,steps_total,steps_max,heart_rate_average,sleep_total,sleep_min)

#To get the display and write to file, I had to bring variables in this function 
def write_results_file(outfile,steps_total,steps_max,heart_rate_average,sleep_total,sleep_min):

	#Setting up for writing and printing 
	wsteps_total = str(f'The total number of steps taken this week were: {steps_total} .\n')
	wsteps_max = str(f'The maximum number of steps taken this week were: {steps_max} .\n')
	wheart_rate_average = str(f'The average heart rate for the week was: {"%.2f" % heart_rate_average} .\n')
	wsleep_total = str(f'The total number of hours slept this week was: {sleep_total} .\n')
	wsleep_min = str(f'The least amount of hours slept this week was: {sleep_min} .\n')

	#writing to file 
	outfile.write(wsteps_total)
	outfile.write(wsteps_max)
	outfile.write(wheart_rate_average)
	outfile.write(wsleep_total)
	outfile.write(wsleep_min)

	#displaying on screen 
	print('The total number of steps taken this week were:',steps_total)
	print('The maximum number of steps taken this week were:',steps_max)
	print('The average heart rate for the week was:',"%.2f" % heart_rate_average)
	print('The total number of hours slept this week was:',sleep_total)
	print('The least amount of hours slept this week was:',sleep_min)

#These functions below I use to iterate through 7 lines and do some math, I used list to find max and min 
def steps_analyzer(infile):
	steps_total = 0
	line_number = 1
	step_list = []
	for line in infile:
		line = line.strip()
		if(line_number <= 7):
				steps_total += int(line)
				step_list.append(int(line))
		line_number += 1
	steps_max = max(step_list)
	return steps_total, steps_max



def heart_rate_analyzer(infile):
	infile.seek(0) #This is used to reset the read file position 
	heart_rate_average = 0
	line_number = 1
	for line in infile:
		line = line.strip()
		if(line_number >= 8 and line_number <= 14):
				heart_rate_average += int(line)/7
		line_number += 1
	return heart_rate_average

def sleep_analyzer(infile):
	infile.seek(0) #This is used to reset the read file position 
	sleep_total = 0
	line_number = 1
	sleep_list = []
	for line in infile:
		line = line.strip()
		if(line_number >= 15):
				sleep_total += float(line)
				sleep_list.append(float(line))
		line_number += 1
	sleep_min = min(sleep_list)
	return sleep_total,sleep_min


main()