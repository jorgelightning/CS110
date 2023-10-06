#Lab 4 - Files and Functions Part 2

def main():
	step_total = 0
	hr_total = 0
	sleep_total = 0
	count = 0
	fileOpen = open('fitness-data.txt',"r")

	steps = range(1,22)
	for n in steps:
		line = fileOpen.readline()
		line = line.strip()
		if(n <= 7):
			step_total += int(line) 
			print('1-7',line)
		if(n >= 8 and n <= 14):
			hr_total += int(line)
			print('8-14',line)
		if(n >= 15):
			sleep_total += float(line) 
			print('15 over',line)
	print('Steps:',step_total)
	print('Heart Rate:',hr_total)
	print('Sleeps:',sleep_total)	

main() 
