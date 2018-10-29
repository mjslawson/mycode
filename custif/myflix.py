#!/usr/bin/env python3
def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False


message = 'The movie is about to begin, we recommend '
print('What is your connection speed in Mbps?')
connection = input()
if is_number(connection):

	if connection >= 25:
    		message = message + 'setting video to 4k.'
	elif connection >= 5:
    		message = message + 'setting video to 1080p.'
	elif connection >= 2:
    		message = message + 'setting video to 720p.'
	else:
    		message = message + 'finding another access network.'
	print(message)
else:
	print("Sorry that is not a number")