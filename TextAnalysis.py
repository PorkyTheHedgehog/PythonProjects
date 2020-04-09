from collections import defaultdict
import re, datetime

msgfile = open("Messages.txt", encoding="utf-8").read().splitlines()

datedict = defaultdict(int)
timedict = defaultdict(int)
persondict = defaultdict(int)
timepdict = defaultdict(lambda: defaultdict(int))
worddict = defaultdict(lambda: defaultdict(int))
counter = 0

dds = str(datetime.datetime.now().date())
hour = int(datetime.datetime.now().hour)
minute = int(datetime.datetime.now().minute)
dts = "{:02d}{:02d}Hrs".format(hour, minute)

change = []

for msg in msgfile:

	msg = msg.split()

	if msg == []:
		continue

	try:
		count = True
		re.search(r'(\d+/\d+/\d+)',msg[0]).group(1)
		change = []
	except AttributeError:
		count = False
		if change == []:
			earliermsgtext = msgfile[counter - 1].split()
			for word in range(3, len(earliermsgtext)):
				if ":" in earliermsgtext[word]:
					px = [' '.join(earliermsgtext[3: word + 1])]
					change = earliermsgtext[0:3]
					change.extend(px)
					break
		for word in change[::-1]:
			msg.insert(0, word)


	for word in range(2,len(msg)):
		if ":" in msg[word]:
			msg[3: word+1] = [' '.join(msg[3: word+1])]
			break

	if not count:
		counter += 1


	if msg[3:] == ['Messages', 'to', 'this', 'chat', 'and', 'calls', 'are', 'now', 'secured', 'with', 'end-to-end', 'encryption.', 'Tap', 'for', 'more', 'info.']:
		continue
	elif msg[4:] == ['<Media', 'omitted>']:
		continue
	else:
		for word in range(4,len(msg)):
			worddict[msg[3][:-1]][msg[word].lower()] += 1


	if count:
		datedict[msg[0][:-1]] += 1
		timedict[msg[1][:-3]] += 1
		persondict[msg[3][:-1]] += 1
		timepdict[msg[3][:-1]][msg[1][:-3]] += 1



