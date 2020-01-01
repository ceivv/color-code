
#main screen
#1-color to value 
#2-value to color

# if 1:
	#read colors 
	#calculate the value 
	#give value
#if 2:
	#read value
	#define colors
	#give colors
#if 3:
	#exit
import os
from sys import exit
from colorama import Fore,Style

#main screen
def main_screen():
	os.system('cls')
	print("Made by:")
	print(f"""{Fore.BLUE}
	         ______   _____    ___    _     __
	        |  ___/  |  __/   /   |  | |   / /
	        | |      | |___  / /| |  | |  / /
	        | |      |  __/ /_/ | |  | | / /
	        | |____  | |___     | |  | |/ /
	        |_____/  |____/     |_|  |___/{Style.RESET_ALL}""");
	print("\n********************** COLOR CODE **********************\n1-Color to value\n2-Value to color\n3-Exit\n");

#getting colors from user
def color_get(x):
	print("color ",x," : ")
	color=str(input())
	return color

#calculate the value using colors
def value_calculation(x,y,z):
	return (x*10+y)*10**z

#change colors into numbers
def color_to_value (x):
	if x == "black" :
		return 0
	if x == "brown" :
		return 1
	if x == "red":
		return 2
	if x == "orange":
		return 3
	if x == "yellow" :
		return 4
	if x == "green" :
		return 5
	if x == "blue" :
		return 6
	if x == "violet" :
		return 7
	if x == "grey" :
		return 8
	if x == "white" :
		return 9

#change numbers into colors
def value_to_color(x):
	if x ==  0:
		return "black"
	if x ==  1:
		return "brown"
	if x == 2:
		return "red"
	if x == 3:
		return "orange"
	if x ==  4:
		return "yellow"
	if x ==  5:
		return "green"
	if x ==  6:
		return "blue"
	if x ==  7:
		return "violet"
	if x ==  8:
		return "grey"
	if x ==  9:
		return "white"

#main loop

while 1:
	main_screen()
	x='toodamnhot'
	while 1:
		try:
			x=int(input())
		except:
			print("Input must be a number!")
		if type(x)==int:
			break

	if x==1:
		print("********************** Color to value **********************\n")
		color1=color_get(1)
		color2=color_get(2)
		color3=color_get(3)
		color1=color_to_value(color1)
		color2=color_to_value(color2)
		color3=color_to_value(color3)
		print("\n",value_calculation(color1,color2,color3),"Ohm")

		input('\nPress Enter..')

	#value to color
	elif x==2:
		print("********************** Value to color **********************\n");
		k=str(input("\ngive resistance value : "))
		bar1=int(k[0])
		bar2=int(k[1])
		bar3=len(k)-2
		print("\ncolors are : {} {} {}".format(value_to_color(bar1),value_to_color(bar2),value_to_color(bar3)))

		input('\nPress Enter..')


	elif x==3:
		exit()
	else:
		print('\ninvalid choice!')
		
		input('\nPress Enter..')
