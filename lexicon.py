def scan(stuff):
	s = stuff.lower()
	words = s.split()
	directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
	verbs = ['go', 'stop', 'kill', 'eat']
	stops = ['the','in', 'of', 'from', 'at', 'it']
	nouns = ['door', 'bear', 'princess', 'cabinet']
	a = []		
	for word in words:
		if word in directions:
			b = ('direction', word)
		elif word in verbs:
			b = ('verb', word)	
		elif word in stops:
			b = ('stop', word)
		elif word in nouns:
			b = ('noun', word)
		else:
			try:
				c = int(word)
				b = ('number', c)
			except ValueError:
				b = ('error', word)

		a.append(b)			

	return a
