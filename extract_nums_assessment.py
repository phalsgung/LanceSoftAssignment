'''
Loop char by char in input.
keep accumulating Number until char is encountered.
'.' DOT is part of decimal so when DOT is encountered check after DOT is number or not
'''

def ParseToDigit(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def extract_store_sort(InputStr):
	SPtr = 0
	FPtr = 0
	NumbersList = []

	while SPtr < len(InputStr):
		# Digit Case
		if InputStr[FPtr].isdigit():
			if FPtr < (len(InputStr)-1):
				FPtr+=1
			else:
				# FPrt reached end, do some finilising and clean up code
				# print(SPtr, FPtr)
				NumbersList.append(ParseToDigit(InputStr[SPtr:FPtr+1]))
				break
		# Char Case
		else:
			# DOT Case, only check if we have accumulated some digit before. if DOT comes without a digit ignore
			if InputStr[FPtr] == '.' and FPtr != SPtr:
				if (FPtr+1) < (len(InputStr)-1):
					if InputStr[FPtr+1].isdigit():
						if FPtr < (len(InputStr)-1):
							FPtr+=1
						else:
							NumbersList.append(ParseToDigit(InputStr[SPtr:FPtr]))
							break
					else:
						NumbersList.append(ParseToDigit(InputStr[SPtr:FPtr-1]))
						SPtr = FPtr
				else:
					NumbersList.append(ParseToDigit(InputStr[SPtr:FPtr]))
					SPtr = FPtr
					break

			# Non DOT Char encountered, save the substring between FPrt and SPtr and match SPrt to FPrt
			else:
				if FPtr != SPtr:
					NumbersList.append(ParseToDigit(InputStr[SPtr:FPtr]))
					SPtr = FPtr
				else:
					# since FPtr and SPtr are equal, just increment FPtr
					if FPtr < (len(InputStr)-1):
						FPtr+=1
						SPtr = FPtr
					else:
						# Reached end and nothing to process
						break
	NumbersList.sort()
	return NumbersList




if __name__=="__main__":

	InputList = ["AC*wv12n/:#e123we2.45oin  (fwoi6n#a98nfwb+owi", "1", "a1", "1a", "a2.", ".1a21.z"]

	for Inp in InputList:
		print("Input String:")
		print(Inp)
		print("Output:")
		print(extract_store_sort(Inp), end="\n\n")





