alt_map = {'ins':'0'}
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

with open("/data/reverse_complement_data.txt", "r") as seq:

	def reverse_complement(seq):    
	    for k,v in alt_map.iteritems():
	        seq = seq.replace(k,v)
	    bases = list(seq) 
	    bases = reversed([complement.get(base,base) for base in bases])
	    bases = ''.join(bases)
	    for k,v in alt_map.iteritems():
	        bases = bases.replace(v,k)
	    return bases


