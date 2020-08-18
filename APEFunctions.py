def IsPrime(n): #Version 2 (will be replaced with version 3 once developent on it ends as bugs may occur)
	"""Input n, returns True if n is prime and False if not."""
	if n > 1:
		x = 2
		while x * x <= n:  # x * x < n is much more efficient than x < sqrt(n)
			if (n % x) == 0:
				return False
			x += 1
		return True
	else:
		return False


def IsPrime3(n):  # Version 3 - Time 16.04
	"""Input n, returns True if n is prime and False if not."""

	if n > 1:
		x = 2
		while x * x <= n:  # x*x<n is much more efficient than x<sqrt(n)
			if (n % x) == 0:
				return False
			x += 2
		return True
	else:
		return False

def MakeBool(string):  # !!!I THINK THIS ALREADY EXISTS IN-BUILT - Pablo
	if string == "False":
		return False
	if string == "True":
		return True
	else:
		print("Impossible")

def InsertCommas(number):
	"""Inserts commas into the corresponding places in a number."""

	string = str(number)
	newString = string
	commasNeeded = len(str(number)[:-1]) // 3
	while commasNeeded > 0:
		newString = newString[:-(3 * commasNeeded)] + "," + newString[-(3 * commasNeeded):]
		commasNeeded -= 1
	return newString

def ReverseIt(inp):  # !!!I THINK THIS ALREADY EXISTS IN-BUILT - Pablo
	"""Takes string or int and return reversed version as string."""

	inp = str(inp)
	revNum = ""
	for x in range(len(inp)):
		digit = inp[len(inp) - x - 1]
		revNum += digit
	return revNum

def IsPalendromic(n):
	"""Returns True if n is palendromic and False if not."""

	n = str(n)
	for x in range(len(n)):
		if n[x] != n[len(n) - x - 1]:
			return False
	return True

def OccurencesInList(item, list1):  # !!!I THINK THIS ALREADY EXISTS IN-BUILT - Pablo
	"""Returns the amount of occurences of an item in a list."""

	count = 0
	for x in range(len(list1)):
		if list1[x] == item:
			count += 1
	return count


if __name__ == "__main__":
	"""Use the space below for testing. Any code here will not run when the file is imported as a
	module. Delete it once you're finished testing."""

	None
