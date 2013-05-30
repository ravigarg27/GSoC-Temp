
def getTerm(stream):
	block = []
	for line in stream:
		if line.strip() == "[Term]" or line.strip() == "[Typedef]":
			break
		else:
			if line.strip() != "":
				block.append(line.strip())
	return block

def parseTagValue(term):
	data = {}
	for line in term:
		tag = line.split(': ',1)[0]
		value = line.split(': ',1)[1]
		if not data.has_key(tag):
			data[tag] = []
		data[tag].append(value)
	return data

if __name__ == "__main__":
	file1 = open('hp.obo','r')
	file2 = open('dictionary1.csv','w')
	file3 = open('indexing.csv','w')
	#skip the file header lines
	getTerm(file1)
	count=0
	count_synonym=0
	count_exact=0
	while 1:
  		term = parseTagValue(getTerm(file1)) #term is the dictinary
  		if len(term) != 0:
			#print term['name'],term['id']
			file2.write(term['name'][0].split()[0]+'|'+term['name'][0]+'\n')
			file3.write(term['id'][0]+' '+term['name'][0]+'\n')
			if 'synonym' in term:
				count_synonym+=1
				for i in range(0,len(term['synonym'])):
					#print i
					if term['synonym'][i].find('EXACT') != -1:
						count_exact+=1
						synonym_term = term['synonym'][i].split('EXACT')[0][1:-2]
						file2.write(synonym_term.split()[0]+'|'+synonym_term+'\n')
						file3.write(term['id'][0]+' '+synonym_term+'\n')
				#print 'Synonym',term['synonym']
			count+=1
		else:
			break
	file1.close()
	file2.close()
	file3.close()
	print count
	print count_synonym
	print count_exact
			
