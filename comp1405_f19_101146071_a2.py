print("\t\t\tZOMBIE APOCALYPSE")

print("\nYou can be a part of five survival groups represented by their traits:\n1. Tradesman- get supplies for a low cost\n2. Blacksmith- extra strength against enemies\n3. Psychic- know of potential enemies just before they strike\n4. Medic- health kits restore more health\n ")

#takes input for class choice
Class = int(input())		

#checks if input is valid or not
while Class > 4 or Class == 0:										
	Class = int(input("\nInvalid choice!\nPlease enter your preferred class again:"))	

print("You are a survivor from the recent viral outbreak that has turned 90 percent of the population of Ottawa into violent mutants with no conscience. \nGo to Oracle Center and get as many supplies as you can. Make for the border of the city where you will find help from police. \nHurry, There is no time to lose.")

print("\n\nEnter the names of the four survivors you met who are now part of your team:")

#entering team member names
p1 = input("1.")			
p2 = input("2.")			
p3 = input("3.")			
p4 = input("4.")			
	
#Entering amounts of supplies to buy
print("\n\nYou are at Oracle Center. Following are the available supplies:\nShotgun(max 2): $175.50 per unit\nBullets: $8.50 for a box of ten bullets\nCrafting tools(You need atleast 25 pieces to craft basic instruments): $7.40 per piece\nFirst Aid(You need atleast two for emergencies): $45.75 per piece\nArmor(You need atleast two pieces of armor): $75.85 per piece")

balance = 0.00


shotgun = int(input("\nEnter the number of shotguns you wish to buy:"))

while shotgun > 2:
	shotgun = int(input("Invalid choice! Please enter again: "))

balance = balance + shotgun*175.35
print("Balance: ",format(balance, '.2f'))

bullets = int(input("\nEnter the number of bullet boxes you wish to buy:"))

balance += bullets*8.50
print("Balance: ",format(balance, '.2f'))

crafting = int(input("\nEnter the number of crafting pieces you wish to buy:"))

balance += crafting*7.40
print("Balance: ",format(balance, '.2f'))

firstaid = int(input("\nEnter the number of first aid kits you wish to buy:"))

balance += firstaid*45.75
print("Balance: ",format(balance, '.2f'))

armor = int(input("\nEnter the number of pieces of armor you wish to buy:"))

balance += armor*75.85
print("Balance: ",format(balance, '.2f'))

#order summary
print("\t\t\tORDER SUMMARY\n\nITEM\t\t\tAMOUNT\t\tCOST\nShotguns\t\t",shotgun,"\t\t$",format(shotgun*175.50,'.2f'),"\nBullets\t\t\t",bullets*10,"\t\t$",format(bullets*8.50,'.2f'),"\nCrafting tools\t\t",crafting,"\t\t$",format(crafting*7.40,'.2f'),"\nFirst Aid kits\t\t",firstaid,"\t\t$",format(firstaid*45.75,'.2f'),"\nArmor pieces\t\t",armor,"\t\t$",format(armor*75.85,'.2f'),"\n\n\tAmount to be paid:$",format(balance,'.2f'))








 
