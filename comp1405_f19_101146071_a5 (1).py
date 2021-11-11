# Student number: 101146071
# Student name: Ricky Gulati


# Function to convert input string to uppercase and remove punctuation
def uppercase(original_str):
	changed_str = ""
	for ch in original_str:
		if ord(ch) >= 97 and ord(ch) <= 122:
			character = chr(ord(ch) - 32)
			changed_str = changed_str + character
		elif ch == " " or (ord(ch) >= 65 and ord(ch) <= 90):
			changed_str = changed_str + ch
	return changed_str

# Function to split a sentence
def split_str(original_str):
	list_of_words = []
	word = ""
	changed_str = original_str + " "
	for ch in changed_str:
		if ch == " ":
			list_of_words.append(word)
			word = ""
		else:
			word = word + ch
	return list_of_words
# Function to replace a phrase
def replace_sub(original_str):
	phrases = ["TOO MUCH INFORMATION", "BE RIGHT BACK", "FOR THE WIN", "FOR YOUR INFORMATION", "IN MY OPINION"]
	abbreviations = ["TMI", "BRB", "FTW", "FYI", "IMO"]
	list_of_words = split_str(original_str)
	
	c = 0
	
	changed_str = ""
	while c <= len(list_of_words) - 3:
		b = 0
		three_words = ""
		flag = True
		while b < 3:
			
			three_words += list_of_words[b + c] + " "
			b += 1
		for i in range(5):
			if three_words[:-1] == phrases[i]:
				changed_str = changed_str + abbreviations[i] + " "		
				flag = False
				c += 2
		
		if flag == True:
			changed_str = changed_str + list_of_words[c] + " "
		c += 1
		if c > len(list_of_words) - 3:
			for d in list_of_words[c:]:
				changed_str = changed_str + d + " "

	return changed_str

				
# FUnction to replace a word
def replace_word(original_str):
	words = ["OKAY", "HELLO", "WHAT", "AWESOME", "PROBABLY"]
	word_abs = ["OK", "HI", "WUT", "OSUM", "PROBS"]
	list_of_words = split_str(original_str)
	changed_str = ""
	for word in list_of_words:
		flag = False
	
		for check in range(5):
			if word == words[check]:
				changed_str = changed_str + word_abs[check] + " "
				flag = True
		if flag == False:	
			changed_str = changed_str + word + " "
	return changed_str

# function to replace a character
def replace_char(original_str, chars):
	changed_str = ""
	characters = ["Z", "X", "K", "D", "I", "L", "B", "C"]
	replacements = ["2", "><", "I<", "|)", "1", "|_", "|3", "("]
	for i in chars:
		if i not in characters:
			print("This program cannot replace the letter ", i)
	for ch in range(len(original_str)):
		flag = True
		for ch2 in range(len(characters)):
			if original_str[ch] == characters[ch2] and original_str[ch] in chars:
				changed_str += replacements[ch2]
				flag = False
		if flag == True:
			changed_str += original_str[ch]
	return changed_str

					



# this is the definition of your main function
def main():
	
	continue_choice = "YES"
	while True:
		our_string = input("Type the string to be translated: ")
		our_string = uppercase(our_string)
		print(our_string)
	
		phrase_choice = uppercase(input("Do you wish to replace phrases? "))
		while phrase_choice != "YES" and phrase_choice != "NO":
			phrase_choice = uppercase(input("Incorrect input!\nEnter again: "))	
		word_choice = uppercase(input("Do you wish to replace words? "))
		while word_choice != "YES" and word_choice != "NO":
			word_choice = uppercase(input("Incorrect input!\nEnter again: "))	
		character_choice = uppercase(input("Do you wish to replace characters? "))
		while character_choice != "YES" and character_choice != "NO":
			phrase_choice = uppercase(input("Incorrect input!\nEnter again: "))
		if character_choice == "YES":	
			chars_for_replacement = uppercase(input("Which characters to you wish to replace? "))	
		print("String for translation: ", our_string)
		if phrase_choice == "YES" and word_choice == "YES" and character_choice == "YES":
			our_string = replace_sub(our_string)
			print("After replacing phrases: ", our_string)
			our_string = replace_word(our_string)
			print("After replacing words: ", our_string)
			our_string = replace_char(our_string, chars_for_replacement)
			print("After replacing characters: ", our_string)
			print("\nThe translated string is: ", our_string)
		elif phrase_choice == "YES" and word_choice == "YES" and character_choice == "NO":
			our_string = replace_sub(our_string)
			print("After replacing phrases: ", our_string)
			our_string = replace_word(our_string)
			print("After replacing words: ", our_string)
			print("\nThe translated string is: ", our_string)
		elif phrase_choice == "YES" and word_choice == "NO" and character_choice == "YES":
			our_string = replace_sub(our_string)
			print("After replacing phrases: ", our_string)
			our_string = replace_char(our_string, chars_for_replacement)
			print("After replacing characters: ", our_string)
			print("\nThe translated string is: ", our_string)
		elif phrase_choice == "YES" and word_choice == "NO" and character_choice == "NO":
			our_string = replace_sub(our_string)
			print("After replacing phrases: ", our_string)
			print("\nThe translated string is: ", our_string)
		elif phrase_choice == "NO" and word_choice == "YES" and character_choice == "YES":
			our_string = replace_word(our_string)
			print("After replacing words: ", our_string)
			our_string = replace_char(our_string, chars_for_replacement)
			print("After replacing characters: ", our_string)
			print("\nThe translated string is: ", our_string)
		elif phrase_choice == "NO" and word_choice == "YES" and character_choice == "NO":
			our_string = replace_word(our_string)
			print("After replacing words: ", our_string)
			print("\nThe translated string is: ", our_string)
		elif phrase_choice == "NO" and word_choice == "NO" and character_choice == "YES":
			our_string = replace_char(our_string, chars_for_replacement)
			print("After replacing characters: ", our_string)
			print("\nThe translated string is: ", our_string)
		else:
			print("You did not do anything!\nHere! Take back your original string: ", our_string)
		continue_choice = uppercase(input("Do you wish to translate another string? "))
		while continue_choice != "YES" and continue_choice != "NO":
			continue_choice = uppercase(input("Incorrect input! Enter again: "))
		if continue_choice == "NO":
			print("Bye Bye")
			break
					
	
# these should be the last two lines of your submission
if __name__ == '__main__':
	main()	
