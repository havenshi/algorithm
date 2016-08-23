# 1.
wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
	for aletter in aword:
		if aletter in letterlist:
			pass
		else:
			letterlist.append(aletter)
print(letterlist)
