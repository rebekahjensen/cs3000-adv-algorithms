import random
import string

def longestPalindromeSubsequence(s:str) -> str:
	#memoization, don't calculate same thing multiple times, faster!!
	#store results in table {}
	memo = {}

	def utilize(start,end):
		# Base cases, single or empty
		if start >= end:
			return s[start:end + 1] #return single or empty
		
		#has this been done?
		if (start,end) in memo:
			return memo[(start,end)]
		
		#recursively, do they match?
		if s[start] == s[end]:
			result = s[start] + utilize(start + 1, end - 1) + s[end]
		else: #attempt
			keepFirst = utilize(start +1, end)
			keepLast = utilize(start, end - 1)
			result = keepFirst if len(keepFirst) > len(keepLast) else keepLast

		memo[(start,end)] = result #store in memo table
		return result
	
	return utilize(0,len(s)-1)

	# # Base cases
	# if len(s) <= 1:
	# 	# Just return it, as a length 1 is a palindrome
	# 	return s
	# if len(s) == 2:
	# 	# If they match, then we have a palindrome
	# 	if s[0] == s[1]: 
	# 		return s
	# 	# No match means no luck
	# 	return ""
	# # Recursive cases
	# # Fist and last match - add that to the longest in the middle
	# if s[0] == s[-1]:
	# 	return s[0] + longestPalindromeSubsequence(s[1:len(s)-1]) + s[-1]
	# # First and last don't match - either keep the first, or keep the last, whichever is larger
	# keepFirst = longestPalindromeSubsequence(s[0:len(s)-1])
	# keepLast = longestPalindromeSubsequence(s[1:])
	# if len(keepFirst) > len(keepLast):
	# 	return keepFirst
	# return keepLast

# Dr B - I put this together for testing
def generatePalindromeWithAnswer(size):
	aLeftSide = ""
	aRightSide = ""
	pLeftSide = ""
	pRightSide = ""
	for i in range(size):
		c = random.choice(string.ascii_letters)
		if random.random() > .5 or i == size-1:
			aLeftSide += c
			aRightSide = c + aRightSide
			pLeftSide += c
			pRightSide = c + pRightSide
		else:
			pLeftSide += c
	return [aLeftSide+aRightSide, pLeftSide+pRightSide]

if __name__ == "__main__":
	print("Longest palindrome subsequence for 'character' = " + longestPalindromeSubsequence("character"))
	
	for i in range(10,50):
		problem = generatePalindromeWithAnswer(i)
		returned = longestPalindromeSubsequence(problem[1])
		print("Size: " + str(i))
		print("\tProblem : " + str(problem[1]))
		print("\tAnswer  : " + str(problem[0]))
		print("\treturned: " + str(returned))

