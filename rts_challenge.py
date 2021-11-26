"""
Dan Rose
RTS Labs Coding Assignment
"""

"""  
Inputs: 
	int_list - unsorted collection of integers
	comp_val - comparison value
Outputs: dict with "above" and "below" keys
Purpose: Determines which values in the list are above and which are below the comparison value 
""" 
def aboveBelow(int_list, comp_val):
	counts = {
		"above": 0,
		"below": 0
	}

	if not isinstance(comp_val, int):
		raise TypeError("Inputs must all be of type: int")
		return

	for num in int_list:
		if not isinstance(num, int):
			raise TypeError("Inputs must all be of type: int")
			return
		
		if num > comp_val:
			counts['above'] += 1
		elif num < comp_val:
			counts['below'] += 1

	return counts


""" 
Inputs: 
	orig - string to be rotated
	rotations - number of rotations to perform on the string
Outputs: new string that rotates the original to the right the specified amount
Purpose: Rotates a string to the right a specified number of times 
"""
def stringRotation(orig, rotations):
	if not isinstance(rotations, int):
		raise TypeError("Rotations input must be of type: int")
		return
	if rotations <= 0:
		raise ValueError("Rotations input must be positive") 
		return
	if not isinstance(orig, str):
		raise TypeError("Original string must be of type: string")
		return

	length = len(orig)
	rotated = ['']*length
	for i in range(0, length):
		rotated[(i+rotations)%length] = orig[i]
	
	rotatedStr = ''
	for letter in rotated:
		rotatedStr += letter
	return rotatedStr
