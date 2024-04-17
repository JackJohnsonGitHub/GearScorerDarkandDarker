import sys
import os
##########
#Constants
##########

item = ["nill", "Junk", "Poor", "Common", "Uncommon", "Rare", "Epic", "Legendary", "Unique"]

twoHanded = [0, 15, 22, 30, 45, 60, 90 , 120, 175]
primaryWeapon = [0, 9, 13, 18, 27, 36, 54, 72, 125]
secondWeapon = [0, 7, 10, 14, 21, 28, 42, 56, 100]
HHF = [0, 4, 6, 8, 12, 16, 24, 32, 40] #Heads, Hands, Foot
CLB = [0, 5, 7, 10, 15, 20, 30, 40, 50] #Chest, Legs, Back
NR = [0, 0, 0, 0, 9, 12, 18, 24, 30] #Necklace, Ring
##########
lowBrac = [0, 0, 199]
medBrac = [0, 200, 399]
highBrac = [0, 400]
##########

playerInvintory = []


def matchQuality(quality):
	match quality:
			case "black":
				grade = 1
			case "grey":
				grade = 2
			case "white":
				grade = 3
			case "green":
				grade = 4
			case "blue":
				grade = 5
			case "purple":
				grade = 6
			case "orange":
				grade = 7
			case "yellow":
				grade = 8	
			case _:
				grade = 0
	return grade

def getGear():
	
	grade = 0
	player = []
	Armor = ["head: ", "chest: ", "legs: ", "hands: ", "back: ", "foot: ", "ringOne: ", "ringTwo: ", "neck: "]
	for i in range (0, 9):
		#Takes user input of the quality
		quality = input(Armor[i])
		#checks the quality and selects the grade 
		quality = quality.lower()
		qual = matchQuality(quality)

#int(hhf = [0, 3, 5])
#int(clb = [1, 2, 4])
#int(nr = [6, 7, 8])

		#Head Hands Foot
		if i == 0 or i == 3 or i == 5:
			if matchQuality(quality) == 0:
				ele = [Armor[i], item[1], HHF[1]]
				player.append(ele)
				playerInvintory.append(ele)
			else:
				ele = [Armor[i], quality, HHF[qual]]
				player.append(ele)
				playerInvintory.append(ele)
		#Chest Legs Back
		if i == 1 or i == 2 or i == 4:
			if matchQuality(quality) == 0:
				ele = [Armor[i], item[1], CLB[1]]
				player.append(ele)
				playerInvintory.append(ele)
			else:	
				ele = [Armor[i], quality, CLB[qual]]
				player.append(ele)
				playerInvintory.append(ele)
		#Necklaces Ring
		if i == 6 or i == 7 or i == 8:
			if matchQuality(quality) == 0:
				ele = [Armor[i], "None", 0]
				player.append(ele)
				playerInvintory.append(ele)
			else:
				ele = [Armor[i], quality, NR[qual]]
				player.append(ele)
				playerInvintory.append(ele)
	total = player[0][2] + player[1][2] + player[2][2] + player[3][2] + player[4][2] + player[5][2] + player[6][2] + player[7][2] + player[8][2]
	total = int(total)
	return total

def getWeapons():
	grade = 0
	player = []
	weaponType = input("Is the weapon two handed or one handed: ")
	weaponType = weaponType.lower()
	if weaponType == "two":
		weapons = ["primary Weapon: ", "second Weapon: "]
		for i in range (0, 2):
			quality = input(weapons[i])
			ele = [weapons[i], quality, twoHanded[matchQuality(quality)]]
			player.append(ele)
			playerInvintory.append(ele)
		total = player[0][2] + player[1][2]
		return total
	elif weaponType == "one":
		weapons = ["primary Weapon 1: ", "second Weapon 1: ", "primary Weapon 2: ", "second Weapon 2: "]
		for i in range (0, 4):
			quality = input(weapons[i])
			if i == 0 or i == 2:
				ele = [weapons[i], quality, primaryWeapon[matchQuality(quality)]]
				player.append(ele)
				playerInvintory.append(ele)
			elif i == 1 or i == 3:
				ele = [weapons[i], quality, secondWeapon[matchQuality(quality)]]
				player.append(ele)
				playerInvintory.append(ele)
		total = player[0][2] + player[1][2] + player[2][2] + player[3][2]
		total = int(total)
		return total
	else:
		total = 0
		return total

def calc(armorAmount, weaponAmount):
	total = armorAmount + weaponAmount
	print("Your total is: ", total)
	if total <= lowBrac[2]:
		print("Low gear bracket")
	elif total >= medBrac[1] & total >= medBrac[2]:
		print("MediumG gear bracket")
	elif total >= highBrac[1]:
		print("High gear bracket")
	prtotal = "Your total score is: " + str(total)
	playerInvintory.append(prtotal)
	return total

def writeFile():
	with open("GearScored.txt", "w") as f:
		for i in range (0 , len(playerInvintory)):
			write = playerInvintory[i]
			write = str(write)
			f.write(write + "\n")


def getUtil():
	bag = ["Potions", "Throwables", "Kits"]


if __name__ == "__main__":
	calc(getGear(), getWeapons())
	writeFile()