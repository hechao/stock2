#input and save
#print and check
#update and print 
#API update current price
 
import json

	
def menu ():
	print("1. input and save. ~2. print and check 3. update 4. create new database 5. del one stock all records")
	
	menu_value = raw_input("select in menu")
	if menu_value == '1':
		IN_SA()
	#elif menu_value == '2':
	#	P_C()		
	elif menu_value == '4':
		create_db()
	elif menu_value == '5':
		del_name()

	P_C()

def del_name ():
	with open('data.json') as json_file:
		data = json.load(json_file)

	name = raw_input('enter the name')

	del data[name]

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)

def create_db ():
	data = {'APPLE' :  {'price':1, 'share':1}}
	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)

	
def IN_SA ():
	with open('data.json') as json_file:
		data = json.load(json_file)
		
	#file = open('data.json', 'w+')
	#data = { "name": 'DBC', "share": 1, "price": 21.43 }

	name = raw_input("Stock name? ")
	share = raw_input("Share? ")
	price = raw_input("price? ")

	if data.has_key(name):
		data[name].append({'share':share, 'price': price})
	else:
		data[name] = {'share':share, 'price': price}

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)

def P_C ():
	with open('data.json') as json_file:
		data = json.load(json_file)
	print(json.dumps(data, indent=4, sort_keys=True))



menu()
