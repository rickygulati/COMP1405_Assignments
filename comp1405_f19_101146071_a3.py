#Student Name: Ricky Gulati
#Student Number: 101146071

#			sub-genre: Disaster
#1 "Sully" - disaster, released after year 1999, based on real incident
#2 "Godzilla(2014)" - disaster, released after year 1999, part of a franchise, not animated, not having a virus epidemic
#3 "Oblivion" - disaster, released after year 1999, post-apocalyptic world, story about survival, released after year 2010
#4 "Wall-E" - disaster, released after year 1999, post-apocalyptic world, story not about survival
#5 "I am Legend" - disaster, released after year 1999, post-apocalyptic world, story about survival, not released after year 2010
#6 "Ice Age: The Meltdown" - disaster, released after year 1999, part of a franchise, animated
#7 "Cast Away" - disaster, released after year 1999, not based on real incident
#8 "Independence Day" - disaster, not released after year 1999, has a sequel
#9 "Mission Impossible 2" - disaster, released after year 1999, part of a franchise, not animated, has a virus epidemic threat
#10 "Deep Impact" - disaster, not released after year 1999, does not have a sequel

#			sub-genre: Biopic
#1 "Chaplin" - not released after 2010, main character famous in media during lifetime, comedian
#2 "A Beautiful Mind" - not released after 2010, main character not famous in media during lifetime, got academy award for best picture, not longer than 3 hours
#3 "The Aviator" - not released after 2010, main character not famous in media during lifetime, did not get academy award for best picture
#4 "Walk The Line" - not released after 2010, main character famous in media during lifetime, not a sportsperson, not a comedian
#5 "The Imitation Game" - released after 2010, related to war, lead actor is english
#6 "American Sniper" - released after 2010, related to war, lead actor is not english
#7 "The Wolf of Wall Street" - released after 2010, not related to war, R-rated
#8 "The Theory of Everything" - released after 2010, not related to war, not R-rated
#9 "Ali" - not released after 2010, main character famous in media during lifetime, sportsperson
#10 "Schindler's List" - not released after 2010, main character not famous in media during lifetime, got academy award for best picture, not longer than 3 hours






#									beginning of code



print("\t\tWELCOME TO THE MovieTime Search Engine!\nDo you need instructions on how to use MovieTime? ", end = "")

ch = input()

if ch == "yes" or ch == "YES":
	print("\nFollowing is the set of instructions to use MovieTime\n1. Think of a movie in your head\n2. The search engine will ask you a few questions\n3. You must answer these questions truthfully\n4. Based on your answers, MovieTime will determine which movie you are thinking about\n\tENJOY!")

#start of looping structure

while True:

	print("Think of a movie now...")

#validation for choosing of sub-genre: if user answers no to both questions, then program terminates.
	ch = input("Is your movie in the sub-genre Disaster? ")

	flag = 1

	if ch == "yes" or ch == "YES":
		flag = 1
	elif ch == "no" or ch == "NO":
		ch = input("Is the movie in the sub-genre Biopic? ")
		if ch == "yes" or ch == "YES":
			flag = 2
		else:
			print("Invalid choices! Exiting program now...")
			break



#If movie is in sub-genre Disaster
	if flag == 1:
		ch = input("Was the movie released after the year 1999? ")
		if ch == "yes" or ch == "YES":
			ch = input("Is the movie part of a larger movie franchise? ")
			if ch == "yes" or ch == "YES":
				ch = input("Is the movie animated? ")
				if ch == "yes" or ch == "YES":
					print("The title of the movie is Ice Age: The Meltdown")
				else:
					ch = input("Is the movie about a virus epidemic threat? ")
					if ch == "yes" or ch == "YES":
						print("The title of the movie is Mission Impossible 2")
					else:
						print("The title of the movie is Godzilla(2014)")
			else:
				ch = input("Is the movie set in a post-apocalyptic world? ")
				if ch == "yes" or ch == "YES":
					ch = input("Is the movie about survival? ")
					if ch == "yes" or ch == "YES":
						ch = input("Was the movie released after 2010? ")
						if ch == "yes" or ch == "YES":
							print("The title of the movie is Oblivion")
						else:
							print("The title of the movie is I am Legend")
					else:
						print("The title of the movie is Wall-E")
				else:
					ch = input("Is this movie based on a real incident? ")
					if ch == "yes" or ch == "YES":
						print("The title of the movie is Sully")
					else:
						print("The title of the movie is Cast Away")
		else:
			ch = input("Does the film have a sequel? ")
			if ch == "yes" or ch == "YES":
				print("The title of the movie is Independence Day")
			else:
				print("The title of the movie is Deep Impact")



#If movie is in sub-genre Biopic
	else:
		ch = input("Was the movie released after the year 2010? ")
		if ch == "yes" or ch == "YES":
			ch = input("Is the movie related to the events of a war? ")
			if ch == "yes" or ch == "YES":
				ch = input("Is the lead actor of the movie of English nationality? ")
				if ch == "yes" or ch == "YES":
					print("The title of the movie is The Imitation Game")
				else:
					print("The title of the movie is American Sniper")
			else:
				ch = input("Is the movie R-rated? ")
				if ch == "yes" or ch == "YES":
					print("The title of the movie is The Wolf of Wall Street")
				else:
					print("The title of the movie is The Theory of Everything")
		else:
			ch = input("Was the main character of the movie famous in media during their lifetime? ")
			if ch == "yes" or ch == "YES":
				ch = input("Is the main character a sportsperson? ")
				if ch == "yes" or ch == "YES":
					print("The title of the movie is Ali")
				else:
					ch = input("Is the main character a comedian? ")
					if ch == "yes" or ch == "YES":
						print("The title of the movie is Chaplin")
					else:
						print("The title of the movie is Walk The Line")
			else:
				ch = input("Did this movie win the Academy Award for Best Picture? ")
				if ch == "yes" or ch == "YES":
					ch = input("Is this movie more than 3 hours long? ")
					if ch == "yes" or ch == "YES":
						print("The title of the movie is Schindler's List")
					else:
						print("The title of the movie is A Beautiful Mind")
				else:
					print("The title of the movie is The Aviator")

	ch = input("Do you wish to quit the program?(yes/no) ")
	if ch == "yes" or ch == "YES":
		print("Quitting now...")
		break

				
		
   

