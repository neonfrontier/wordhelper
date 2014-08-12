"""This is a module to facilitate iterative reading of letters in a list of words based on certain parameters, and match them to all in the master list. 
In other words, it's a crossword etc word helper/finder.
The word list is courtesy of: http://en.wikipedia.org/wiki/Moby_Project"""g
print("This is a word finder app designed to help you on a crossword puzzle or something similar.")
print("Instructions: Enter total amount of letters, and we will go through each letter and enter any clues. Just press enter to go to the next letter, if you have none.")
print("DISCLAIMER: I am not responsible if this thing fails.")

#assign variable to master file of words
wordslist = open('master.txt')
master = list(wordslist)
#assign variable to number of letters needed
letter_amount = int(input("Enter total number of letters: "))

#declare a list for the purpose of storing selected words
temp_words = []

#declare the count variable here so it can be used outside of the for loop.
count = 0

#seek out words with above required length. assign those words to a list.
for line in master:
	line = line.rstrip() 
	count = len(line)
	if count == letter_amount:
		temp_words.append(line)

#declare external list for using to store letters in the word.
chosen_letters = []
#declare var for number of real letters entered.
total_letters = 0

#enter variables to list according to length of the word.
for i in range(1, letter_amount+1):
	c = input("Enter letter %s: " %i)
	if c.isalpha():
		chosen_letters.append(c)
		total_letters += 1
	elif c == '':
		chosen_letters.append("0")

#create function that compares two lists of letters, giving total of matched letters.
def compare_letters(lista, listb):
	pairs = 0
	for i in range(min(len(lista), len(listb))):
		if lista[i] == listb[i]:
			pairs += 1
	return pairs

#declare list for final words.
final_words = []
#split word list into letters, compare to letter list, append positive words to list.
for a in temp_words:
	split_letters = list(a)
	amount = compare_letters(chosen_letters, split_letters)
	if amount == total_letters:
		final_words.append(a)

#print final deduced words list.
#optional. display links to dictionary/wiki/google next to each word for added bonus of word meanings.
print("Printing potential words! Possible wiktionary links have also been made available:")
for i in final_words:
	print(i+"    ( link: "+"http://en.wiktionary.org/wiki/"+i+" )")

wordslist.close()
