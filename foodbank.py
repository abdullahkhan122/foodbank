#importing pandas library
import pandas as pd
# Importing required module
from geopy.geocoders import Nominatim
import cv2
import matplotlib.pyplot as plt
  
# Using Nominatim Api
geolocator = Nominatim(user_agent="geoapiExercises")
  
print("Welcome to the Food Bank Locator ")
# Zipocde input
zipcode = input("Enter a Valid NJ Zipcode: ")
  
# Using geocode()
location = geolocator.geocode(zipcode)
  
# Displaying address details
print("\nZipcode: ",zipcode)
print("Details of the Zipcode: ")
print(location)


val = input("\nPress Enter to View Your Food Bank Info: ")

#checking to see which food bank the user falls under
if zipcode > '07000' and zipcode < '07700':
	#reading in the csv file (Hillside)
	dataframe = pd.read_csv('foodbank1.csv')
	print(dataframe)
	print("")

elif zipcode > '07701' and zipcode < '08022': 
	#reading in the csv file (Neptune City)
	dataframe = pd.read_csv('foodbank2.csv')
	print(dataframe)
	print("")

elif zipcode > '08023' and zipcode < '08989': 
	#reading in the csv file (Pennsauken)
	dataframe = pd.read_csv('foodbank3.csv')
	print(dataframe)
	print("")
else:
	print("Invalid NJ Zip Code. Please try again. ")

#importing an image using cv2 library
photo = cv2.imread('Hunger_fighter.jpg')
photo2 = cv2.imread('come_again.jpg')
#Asking the user to place an order
order = input('\nWould you like to place an order?\nIf yes, Enter y\nIf no, Enter n: ')

if order == 'y':
	count = 1
	while count > 0:
		print("Your order has been placed!")
		count = count - 1
		plt.imshow(photo)
		plt.show()
elif order == 'n':
	print("Thank You for checking in. See you later.")
	plt.imshow(photo2)
	plt.show()
else:
	print("Invalid Entry. Try Again")







