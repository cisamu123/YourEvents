from datetime import datetime as dt
def main():
	print("What do you want to do? Read file (R), Write new event to file (W)")
	userinput = input()
	if (userinput == "R"):
		read_event()
	if (userinput == "W"):
		write_event()
def write_event():
	event = input("Enter event: ")
	event_year = input("Enter event year: ")
	print(f'Event: {event} event year: {event_year}')
	ques = input("Is everything right? y/n: ")
	if (ques == "y"):
		f = open("events.txt", "a")
		f.write(f'Event: {event} event year: {event_year}, SAVED: ' + str(dt.now()) + '\n')
		f.close()
		print("Ok. Its writed to file, file: events.txt")
		input()
		main()
	elif (ques == "n"):
		main()
	else:
		print("I do not understand you. \ntry again")
		input()
		main()
def read_event():
	f = open("events.txt", "r")
	print(f.read())
	input()
	main()
main()