import random
import json
from datetime import datetime
from tkinter import *

with open("name_pharmacies.json", "r") as file:
	data_of_pharm = json.load(file)


with open("pills_in_pharmacies.json", "r") as file1:
	data_of_pills_pharm = json.load(file1)


with open("provider.json", "r") as file2:
	data_of_provider = json.load(file2)


file3 = open("pills_provider.json", "r")
data_of_pills_prov = json.load(file3)

global flag_delete 
class Pills:
	def __init__(self):
		self.id_pharm = None
		self.id_pills = None
		self.name = None
		self.size = None
		self.price = None
		self.expiration = None
		self.quantity = None


	def _template_with_data(self):
		new_pills = {
			   "ID pharmacy": self.id_pharm,
			   "ID pills": self.id_pills,
			   "name": self.name,
			   "size": self.size,
			   "price": self.price,
			   "expiration": self.expiration,
			   "quantity": self.quantity
			}
		return new_pills

	def write_to_file(self, name_of_file, mode, data_to_write):
		with open(name_of_file, mode) as file:
			file.write(data_to_write)


	def enter_name_pharm(self, screen):
		global user_inform_pharm
		user_inform_pharm = StringVar()
		global pharmacy_entered_name
		Label(screen, text = "Enter pharmacy", bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14)).place(x = 30, y = 50)
		pharmacy_entered_name = Entry(screen, textvariable = user_inform_pharm, bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14))
		pharmacy_entered_name.place(x = 330, y = 50)
		Button(screen, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "20", font = ("Helvetica", 14),command = self._check_entered_name_pharm).place(x = 600, y = 50)
	
	def _check_entered_name_pharm(self): 
		entered_name_pharm = user_inform_pharm.get()
		if  entered_name_pharm == "":
			self.error("Field must be fulled")
			pharmacy_entered_name.delete(0, END)
		else:
			self._set_id_pharm(entered_name_pharm)


	def _set_id_pharm(self, entered_name_pharm):
		flag = False
		global entered_id_pharm
		for inform_pharm in data_of_pharm["pharmacy"]: 
				if entered_name_pharm == inform_pharm.get("name"): 
					entered_id_pharm = inform_pharm.get("ID pharmacy") #ID pharmacy
					flag = True
					if flag_delete:
						self._full_name_pills(screen_delete_pills)
					else:
						self.id_pharm = entered_id_pharm
						self._set_id_pills()   
		if flag == False:
			self.error("The pharmacy hasn't been found")
			pharmacy_entered_name.delete(0, END)
	
	def error(self, line):
		global screen_error
		screen_error = Toplevel()
		screen_error.title("Warning")
		screen_error.geometry("900x250")
		Label(screen_error, text = line, bg ="#F0FFF0" , fg ="#FF0000", width = "65", font = ("Helvetica", 14)).place(x = 105, y = 35)
		Label(screen_error, text = "Please, try again", bg ="#F0FFF0" , fg ="#B22222", width = "15", font = ("Helvetica", 14)).place(x = 370, y = 85)
		Button(screen_error, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "20", font = ("Helvetica", 14), command = screen_error.destroy).place(x = 345, y = 130)	
	
	def _set_id_pills(self):
		self.id_pills = self._check_ID("ID pills")
		self._full_name_pills(screen_add_pills) #call the function for fulling name pills
	
	def _check_ID(self,key):
		id_value = self._random_ID()
		for inform_pills in data_of_pills_pharm["pills"]: 
			while id_value == inform_pills.get(key): 
				id_value = self._random_ID()
		return id_value

	def _random_ID(self):
		buff_ID = random.choice(list('123456789abcdefghijklmnopqrstuvwxyz-'))
		for x in range(35):
			buff_ID = buff_ID + random.choice(list('123456789abcdefghijklmnopqrstuvwxyz-'))
		return buff_ID

	def _full_name_pills(self, screen):
		global user_name_pills
		user_name_pills = StringVar()
		global entered_name_pills
		Label(screen, text = "Enter name of pills", bg ="#F0FFF0" , fg ="#0000CD", width = "20", font = ("Helvetica", 14)).place(x = 30, y = 130)
		entered_name_pills = Entry(screen, textvariable = user_name_pills, bg ="#F0FFF0" , fg ="#0000CD", width = "20", font = ("Helvetica", 14))
		entered_name_pills.place(x = 330, y = 130)
		Button(screen, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "20", font = ("Helvetica", 14),command = self._set_entered_name_pills ).place(x = 600, y = 130)

	
	def _set_entered_name_pills(self):
		global buff_user_name #pills' names
		buff_user_name = user_name_pills.get()
		if  buff_user_name == "":
			self.error("Field must be fulled")
			entered_name_pills.delete(0, END)
		elif flag_delete:
			self._full_size_pills(screen_delete_pills)
		else:
			self.name = buff_user_name #full name tablets
			self._full_size_pills(screen_add_pills)

		
		
	def _full_size_pills(self, screen):
		global user_size_pills
		user_size_pills = StringVar()
		global entered_size_pills
		Label(screen, text = "Enter size of pills", bg ="#F0FFF0" , fg ="#4169E1", width = "20", font = ("Helvetica", 14)).place(x = 30, y = 210)
		entered_size_pills = Entry(screen, textvariable = user_size_pills, bg ="#F0FFF0" , fg ="#4169E1", width = "20", font = ("Helvetica", 14))
		entered_size_pills.place(x = 330, y = 210)
		Button(screen, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "20", font = ("Helvetica", 14),command = self._set_entered_size_pills).place(x = 600, y = 210)
		
			
	def _set_entered_size_pills(self):
		flag = True
		buff_user_size = user_size_pills.get()
		try:
			buff_user_size = int(buff_user_size)
		except:
			flag = False
			self.error("Entered symbols must be numbers")
			entered_size_pills.delete(0, END)
		if flag:
			if flag_delete:
				pharmacy.check_pills_in_pharm_delete(buff_user_size)
			else:
				self.size = buff_user_size 
				self._full_price_pills()

	def _full_price_pills(self):
			global user_price_pills
			user_price_pills = StringVar()
			global entered_price_pills
			Label(screen_add_pills, text = "Enter price of pills", bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14)).place(x = 30, y = 290)
			entered_price_pills = Entry(screen_add_pills, textvariable = user_price_pills, bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14))
			entered_price_pills.place(x = 330, y = 290)
			Button(screen_add_pills, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "20", font = ("Helvetica", 14),command = self._set_entered_price_pills).place(x = 600, y = 290)		

	def _set_entered_price_pills(self):
		flag = True
		buff_user_price = user_price_pills.get()
		try:
			buff_user_price = int(buff_user_price)
		except:
			flag = False
			self.error("Entered symbols must be numbers")
			entered_price_pills.delete(0, END)
		if flag:
			self.price = buff_user_price #fulling price of pills
			self._full_expiration_date_pills()

	def _full_expiration_date_pills(self):
		global user_date_pills
		user_date_pills = StringVar()
		global entered_date_pills
		Label(screen_add_pills, text = "Enter expiration of pills", bg ="#F0FFF0" , fg ="#00008B", width = "20", font = ("Helvetica", 14)).place(x = 370, y = 350)
		Label(screen_add_pills, text = "Enter date", bg ="#F0FFF0" , fg ="#4682B4", width = "20", font = ("Helvetica", 14)).place(x = 30, y = 410)
		entered_date_pills = Entry(screen_add_pills, textvariable = user_date_pills, bg ="#F0FFF0" , fg ="#4682B4", width = "20", font = ("Helvetica", 14))
		entered_date_pills.place(x = 330, y = 410)
		Button(screen_add_pills, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "20", font = ("Helvetica", 14),command = self._check_entered_date_pills ).place(x = 600, y = 410)	


	def _check_entered_date_pills(self):
		flag = True
		global buff_user_date 
		buff_user_date = user_date_pills.get()
		try:
			buff_user_date = int(buff_user_date)
			if buff_user_date < 1 or buff_user_date > 31:
				flag = False
		except:
			flag = False
		if flag == False:
			self.error("Entered symbols must be numbers (since 1 to 31)")
			entered_date_pills.delete(0, END)
		if flag:
			self._full_expiration_month_pills()
	
	def _full_expiration_month_pills(self):
		global user_month_pills
		user_month_pills = StringVar()
		global entered_month_pills
		Label(screen_add_pills, text = "Enter month", bg ="#F0FFF0" , fg ="#6B8E23", width = "20", font = ("Helvetica", 14)).place(x = 30, y = 490)
		entered_month_pills = Entry(screen_add_pills, textvariable = user_month_pills, bg ="#F0FFF0" , fg ="#6B8E23", width = "20", font = ("Helvetica", 14))
		entered_month_pills.place(x = 330, y = 490)
		Button(screen_add_pills, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "20", font = ("Helvetica", 14),command = self._check_entered_month_pills ).place(x = 600, y = 490)	

	def _check_entered_month_pills(self):
		flag = True
		global buff_user_month
		buff_user_month = user_month_pills.get()
		try:
			buff_user_month = int(buff_user_month)
			if buff_user_month <1 or buff_user_month > 12:
				flag = False
		except:
			flag = False
		if flag == False:
			self.error("Entered symbols must be numbers (since 1 to 12)")
			entered_month_pills.delete(0, END)
		if flag:
			self._full_expiration_year_pills()

	def _full_expiration_year_pills(self):
		global user_year_pills
		user_year_pills = StringVar()
		global entered_year_pills
		Label(screen_add_pills, text = "Enter year", bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14)).place(x = 30, y = 570)
		entered_year_pills = Entry(screen_add_pills, textvariable = user_year_pills, bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14))
		entered_year_pills.place(x = 330, y = 570)
		Button(screen_add_pills, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "20", font = ("Helvetica", 14),command = self._set_expiration ).place(x = 600, y = 570)	

	def _set_expiration(self):
		flag = True
		global buff_user_year
		buff_user_year = user_year_pills.get()
		try:
			buff_user_year = int(buff_user_year)
			if buff_user_year < 2000:
				flag = False
		except:
			flag = False
		if flag == False:
			self.error("Your entered symbols are unpropriated for value of year. They must be numbers.")
			entered_year_pills.delete(0, END)
		if flag:
			self.expiration = str(buff_user_date)+ "."+ str(buff_user_month) + "." + str(buff_user_year)
			self._full_quantuty_pills()

	def _full_quantuty_pills(self):
		global user_quantity_pills
		user_quantity_pills = StringVar()
		global entered_quantity_pills
		Label(screen_add_pills, text = "Enter quantity", bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14)).place(x = 30, y = 650)
		entered_quantity_pills = Entry(screen_add_pills, textvariable = user_quantity_pills, bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14))
		entered_quantity_pills.place(x = 330, y = 650)
		Button(screen_add_pills, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "20", font = ("Helvetica", 14),command = self._set_entered_quantity_pills ).place(x = 600, y = 650)	

	def _set_entered_quantity_pills(self):
		flag = True
		buff_user_quantity = user_quantity_pills.get()
		try:
			buff_user_quantity = int(buff_user_quantity)
		except:
			flag = False
			self.error("Entered symbols must be numbers")
			entered_quantity_pills.delete(0, END)
		if flag:
			self.quantity = buff_user_quantity
			Button(screen_add_pills, text = "Add to file", bg ="#00FF7F" , fg ="#006400", width = "20", font = ("Helvetica", 14),command = self.add_to_file ).place(x = 900, y = 430)
			Button(screen_add_pills, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_add_pills.destroy).place(x = 900, y = 480)

	def add_to_file(self):
		data_of_pills_pharm["pills"].append(self._template_with_data())
		self.write_to_file("pills_in_pharmacies.json", "w", json.dumps(data_of_pills_pharm))
		self.success(screen_add_pills)

	def success(self, screen):
		global screen_success
		screen_success = Toplevel()
		screen_success.title("Successful action")
		screen_success.geometry("450x200")
		Label(screen_success, text = "The action has been successful", bg ="#F0FFF0" , fg ="#008000", width = "25", font = ("Helvetica", 14) ).place(x = 85, y = 40)
		Button(screen_success, text = "Back", bg ="#F0FFF0" , fg ="#008000", width = "15", font = ("Helvetica", 14),command = lambda: (screen_success.destroy(), screen.destroy())).place(x = 127, y = 85)
		


class Pharmacy:

	def __init__(self, pharmacy, pills):
		self.pharmacy = pharmacy
		self.pills = pills

	def print_pharmacies(self):
		for el_pharmacy in self.pharmacy:
			Label(screen_inform_pharm, text = el_pharmacy.get('name'),  fg ="#008B8B", width = "20", font = ("Helvetica", 12)).pack()
			Label(screen_inform_pharm, text = "").pack()
		Button(screen_inform_pharm, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_inform_pharm.destroy).pack()
			

	def print_pills(self):
		dic_pills={} # key - name of pills, value - size 
		z = 75
		for el_pills in self.pills:
			if el_pills.get("name") in dic_pills and el_pills.get("size") == dic_pills.get(el_pills.get("name")):
				continue
			dic_pills[el_pills.get("name")] = el_pills.get("size")
			
			Label(screen_inform_pills, text = el_pills.get("name"),  fg ="#008B8B", width = "20", font = ("Helvetica", 12)).place(x = 34, y = z )
			Label(screen_inform_pills, text = el_pills.get('size'),  fg ="#008B8B", width = "20", font = ("Helvetica", 12)).place(x =200 , y = z)
			z = z + 50
		Button(screen_inform_pills, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_inform_pills.destroy).place(x = 160, y = z)
			

	def pills_in_pharm(self):
		k = 35
		for pharmacy in self.pharmacy:
			Label(screen_inform_pills_in_pharm, text = pharmacy.get("name"), bg ="#F0FFF0" , fg ="#00FF00", width = "10", font = ("Helvetica", 11)).place(x = 34, y = k)
			for pills in self.pills:
				if pharmacy.get("ID pharmacy") == pills.get("ID pharmacy"):
					Label(screen_inform_pills_in_pharm, text = pills.get("name"), bg ="#F0FFF0" , fg ="#006400", width = "10", font = ("Helvetica", 11)).place(x = 150, y = k)
					Label(screen_inform_pills_in_pharm, text = pills.get("size"), bg ="#F0FFF0" , fg ="#006400", width = "10", font = ("Helvetica", 11)).place(x = 250, y = k)
		
					k = k + 25
			k = k + 25
		Button(screen_inform_pills_in_pharm, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_inform_pills_in_pharm.destroy).place(x = 200, y = k)

	def _get_expired_pills(self, pills):
		buff_list_exp = pills.get("expiration").split(".")
		date = int(buff_list_exp[0])
		month = int(buff_list_exp[1])
		year = int(buff_list_exp[2])
		if (cur_year > year) or (cur_year == year and cur_month > month) or (cur_year == year and cur_month == month and cur_date > date):
			return False # pills is expired
		else:
			return True

	def print_expir_pills_in_pharm(self, selection):
		z = 35
		for pharmacy in self.pharmacy:
			without_expiration = True
			if selection == pharmacy.get("name"):
				Label(screen_inf_exp_pills, text = selection, bg ="#F0FFF0" , fg ="#008000", width = "15", font = ("Helvetica", 11)).place(x = 20, y = z)
				for pills in self.pills:
					if pharmacy.get("ID pharmacy") == pills.get("ID pharmacy"):
						if self._get_expired_pills(pills):
							continue #hasn't found expired pills
						without_expiration = False
						Label(screen_inf_exp_pills, text = pills.get("name"), bg ="#F0FFF0" , fg ="#008000", width = "15", font = ("Helvetica", 11)).place(x = 170, y = z)
						Label(screen_inf_exp_pills, text = pills.get("size"), bg ="#F0FFF0" , fg ="#008000", width = "7", font = ("Helvetica", 11)).place(x = 320, y = z)
						Label(screen_inf_exp_pills, text = pills.get("price"), bg ="#F0FFF0" , fg ="#008000", width = "7", font = ("Helvetica", 11)).place(x = 400, y = z)
						Label(screen_inf_exp_pills, text = pills.get("expiration"), bg ="#F0FFF0" , fg ="#008000", width = "15", font = ("Helvetica", 11)).place(x = 480, y = z)
						Label(screen_inf_exp_pills, text = pills.get("quantity"), bg ="#F0FFF0" , fg ="#008000", width = "7", font = ("Helvetica", 11)).place(x = 630, y = z)
						z = z + 30
				if without_expiration:
					Label(screen_inf_exp_pills, text = "There aren't expired pills", bg ="#F0FFF0" , fg ="#00CED1", width = "20", font = ("Helvetica", 11)).place(x = 170, y = z)
					z = z + 30
		Button(screen_inf_exp_pills, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_inf_exp_pills.destroy).place(x = 400, y = z)
	
	def get_amount_of_money(self, pharm):
		sum = 0
		Label(screen_money_pharm, text = pharm, bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 20, y = 40)
		for pharmacy in self.pharmacy:
			if pharmacy.get("name") == pharm:
				for pills in self.pills:
					if pills.get("ID pharmacy") == pharmacy.get("ID pharmacy"):
						sum = sum + pills.get("price") * pills.get("quantity")
		Label(screen_money_pharm, text = sum, bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 180, y = 40)
		Button(screen_money_pharm, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_money_pharm.destroy).place(x = 140, y = 80)
	
	
	def check_pills_in_pharm_delete(self, buff_user_size):
		flag = False
		for el_pills in self.pills:
			if (el_pills.get("name") == buff_user_name) and (el_pills.get("size") == buff_user_size):
				if el_pills.get("ID pharmacy") == entered_id_pharm:
					flag = True
					global id_pills_delete 
					id_pills_delete = el_pills.get("ID pills")
		if flag:
			Button(screen_delete_pills, text = "Delete", bg ="#f0fff0" , fg ="#008080", width = "20", font = ("helvetica", 14), command = self._deleting).place(x = 330, y = 290)
			Button(screen_delete_pills, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_delete_pills.destroy).place(x = 387, y = 350)
		else:
			pills.error("In this pharmacy hasn't been found the pills. Please, try again.")
			entered_name_pills.delete(0, END)
			entered_size_pills.delete(0, END)

	def _deleting(self):
		for el_pills in self.pills:
			if el_pills.get("ID pills") == id_pills_delete:
				self.pills.pop(self.pills.index(el_pills))

				pills.write_to_file('pills_in_pharmacies.json', "w", json.dumps(data_of_pills_pharm))
				pills.success(screen_delete_pills)


class Provider:
	def __init__(self, provider, pills_prov):
		self.provider = provider
		self.pills_prov = pills_prov

	def print_provider(self):
		for el_provider in self.provider:
			Label(screen_inform_prov, text = el_provider.get('name'),  fg ="#008B8B", width = "20", font = ("Helvetica", 12)).pack()
			Label(screen_inform_prov, text = "").pack()
		Button(screen_inform_prov, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_inform_prov.destroy).pack()
			

	def get_pills_prov(self, selection):
		z = 35
		for el_prov in self.provider:
			if selection == el_prov.get("name"):
				Label(screen_inf_prov_pills, text = selection, bg ="#F0FFF0" , fg ="#008000", width = "15", font = ("Helvetica", 11)).place(x = 20, y = z)
				for el_pills_prov in self.pills_prov:
					if el_prov.get("ID provider") == el_pills_prov.get("ID provider"):
						Label(screen_inf_prov_pills, text = el_pills_prov.get("name"), bg ="#F0FFF0" , fg ="#008000", width = "15", font = ("Helvetica", 11)).place(x = 170, y = z)
						Label(screen_inf_prov_pills, text = el_pills_prov.get("size"), bg ="#F0FFF0" , fg ="#008000", width = "7", font = ("Helvetica", 11)).place(x = 320, y = z)
						Label(screen_inf_prov_pills, text = el_pills_prov.get("price"), bg ="#F0FFF0" , fg ="#008000", width = "7", font = ("Helvetica", 11)).place(x = 400, y = z)
						Label(screen_inf_prov_pills, text = el_pills_prov.get("expiration"), bg ="#F0FFF0" , fg ="#008000", width = "15", font = ("Helvetica", 11)).place(x = 480, y = z)
						Label(screen_inf_prov_pills, text = el_pills_prov.get("quantity"), bg ="#F0FFF0" , fg ="#008000", width = "7", font = ("Helvetica", 11)).place(x = 630, y = z)
						z = z + 30
		Button(screen_inf_prov_pills, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_inf_prov_pills.destroy).place(x = 340, y = z)


	def full_dic_prov_have_pills_size(self, medicine, size):
		dic_medic_size={}
		for el_pills_prov in self.pills_prov:
			if el_pills_prov.get("name")== medicine and el_pills_prov.get("size") == size:
				dic_medic_size[el_pills_prov.get("ID pills_prov")] = el_pills_prov.get("price")
				flag = True			
									
		self._print_prov_pills_size(self._sort_dic_pills_size(dic_medic_size))


	def _sort_dic_pills_size(self, dic_medic_size):
		sorted_dic_medic_size = sorted(dic_medic_size.items(), key = lambda x: x[1], reverse = False)
		return dict(sorted_dic_medic_size)

	def _print_prov_pills_size(self, id_pills_price):
		i = 1
		z = 35
		for buff_ID in id_pills_price: 
			for el_pills_prov in self.pills_prov:
				if el_pills_prov.get("ID pills_prov") == buff_ID:
					for el_prov in self.provider:
						if el_prov.get("ID provider") == el_pills_prov.get("ID provider"):
							Label(screen_prov_pills_size, text = i, bg ="#F0FFF0" , fg ="#008080", width = "22", font = ("Helvetica", 11)).place(x = 20, y = z)
							Label(screen_prov_pills_size, text = el_prov.get("name"), bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 240, y = z)
							Label(screen_prov_pills_size, text = el_pills_prov.get("name"), bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 400, y = z)
							Label(screen_prov_pills_size, text = el_pills_prov.get("size"), bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 550, y = z)
							Label(screen_prov_pills_size, text = el_pills_prov.get("price"), bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 630, y = z)
							Label(screen_prov_pills_size, text = el_pills_prov.get("expiration"), bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 710, y = z)
							Label(screen_prov_pills_size, text = el_pills_prov.get("quantity"), bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 860, y = z)
							z = z + 30
			i = i + 1
		Button(screen_prov_pills_size, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_prov_pills_size.destroy).place(x = 430, y = z)

	def get_prov_pills(self, medicine):
		z = 35
		for el_pills_prov in self.pills_prov:
			if el_pills_prov.get("name") == medicine:
				for el_prov in self.provider:
					if el_prov.get("ID provider") == el_pills_prov.get("ID provider"):
						Label(screen_prov_have_pills, text = el_prov.get("name"), bg ="#F0FFF0" , fg ="#008000", width = "15", font = ("Helvetica", 11)).place(x = 20, y = z)
						Label(screen_prov_have_pills, text = medicine, bg ="#F0FFF0" , fg ="#008000", width = "15", font = ("Helvetica", 11)).place(x = 170, y = z)
						Label(screen_prov_have_pills, text = el_pills_prov.get("size"), bg ="#F0FFF0" , fg ="#008000", width = "7", font = ("Helvetica", 11)).place(x = 320, y = z)
						Label(screen_prov_have_pills, text = el_pills_prov.get("price"), bg ="#F0FFF0" , fg ="#008000", width = "7", font = ("Helvetica", 11)).place(x = 400, y = z)
						Label(screen_prov_have_pills, text = el_pills_prov.get("expiration"), bg ="#F0FFF0" , fg ="#008000", width = "15", font = ("Helvetica", 11)).place(x = 480, y = z)
						Label(screen_prov_have_pills, text = el_pills_prov.get("quantity"), bg ="#F0FFF0" , fg ="#008000", width = "7", font = ("Helvetica", 11)).place(x = 630, y = z)
						z = z + 30
		Button(screen_prov_have_pills, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_prov_have_pills.destroy).place(x = 340, y = z)


class Graphical_interface:
	def main_menu(self):
		global pharmacy
		global provider
		global pills
		pharmacy = Pharmacy(data_of_pharm["pharmacy"], data_of_pills_pharm["pills"])
		provider = Provider(data_of_provider["provider"],data_of_pills_prov["pills_provider"])
		pills = Pills()
		global main_screen
		main_screen = Tk()
		main_screen.title("Main Menu")
		main_screen.geometry("500x500")
		Label(main_screen, text = "Main menu", bg ="#F0FFF0" , fg ="#008000", width = "20", font = ("Helvetica", 14)).place(x = 120, y = 45)
	
		Button(main_screen, text = "Display information", height = "3",width = "40", font = ("Helvetica", 12), bg ="#F0FFF0" , fg ="#4682B4", command = self.display_inform).place(x = 50, y = 100)
		Button(main_screen, text = "Add information", height = "3",width = "40" , font = ("Helvetica", 12), bg ="#F0F8FF" , fg ="#008080", command = self.add_info).place(x = 50, y = 190)
		Button(main_screen, text = "Delete information", height = "3",width = "40",  bg ="#F0FFF0" , fg ="#556B2F", font = ("Helvetica", 12), command = self.delete_info).place(x = 50, y = 280)
		Button(main_screen, text = "Exit", height = "3",width = "40",  bg ="#F0FFF0" , fg ="#008B8B", font = ("Helvetica", 12), command = main_screen.destroy ).place(x = 50, y = 370)
		main_screen.mainloop()
		
	def display_inform(self):
		global screen_disp_inf
		screen_disp_inf = Toplevel()
		screen_disp_inf.title("Display information")
		screen_disp_inf.geometry("500x600")
		Label(screen_disp_inf, text = "Choose information", bg ="#F0FFF0" , fg ="#00FF00", width = "20", font = ("Helvetica", 14)).place(x = 120, y = 10)
		Button(screen_disp_inf, text = "Information about pharmacies", height = "2",width = "40", font = ("Helvetica", 12), bg ="#F0FFF0" , fg ="#4682B4", command = self.display_inform_pharmacies).place(x = 50, y = 60)
		Button(screen_disp_inf, text = "Information about pills", height = "2",width = "40", font = ("Helvetica", 12), bg ="#F0FFF0" , fg ="#4682B4", command = self.display_inform_pills).place(x = 50, y = 100)
		Button(screen_disp_inf, text = "Information about providers", height = "2",width = "40", font = ("Helvetica", 12), bg ="#F0FFF0" , fg ="#4682B4", command = self.display_inform_provider).place(x = 50, y = 140)
		Button(screen_disp_inf, text = "Information about pills are in definite pharmacies", height = "2",width = "40", font = ("Helvetica", 12), bg ="#F0FFF0" , fg ="#4682B4", command = self.display_pills_in_pharm).place(x = 50, y = 180)
		Button(screen_disp_inf, text = "Information about expired pills ", height = "2",width = "40", font = ("Helvetica", 12), bg ="#F0FFF0" , fg ="#4682B4", command = self.display_exp_pills).place(x = 50, y = 220)
		Button(screen_disp_inf, text = "What pills providers have ", height = "2",width = "40", font = ("Helvetica", 12), bg ="#F0FFF0" , fg ="#4682B4", command = self.display_prov_pills).place(x = 50, y = 260)
		Button(screen_disp_inf, text = "Amount of money in the pharmacy ", height = "2",width = "40", font = ("Helvetica", 12), bg ="#F0FFF0" , fg ="#4682B4", command = self.display_pharm).place(x = 50, y = 300)
		Button(screen_disp_inf, text = "Who has definite pills ", height = "2",width = "40", font = ("Helvetica", 12), bg ="#F0FFF0" , fg ="#4682B4", command = self.display_pills).place(x = 50, y = 340)
		Button(screen_disp_inf, text = "Who has definite pills with definite size ", height = "2",width = "40", font = ("Helvetica", 12), bg ="#F0FFF0" , fg ="#4682B4", command = self.display_pills_with_size).place(x = 50, y = 380)
		Button(screen_disp_inf, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_disp_inf.destroy).place(x = 190, y = 500)

	@staticmethod
	def display_inform_pharmacies():
		global screen_inform_pharm
		screen_inform_pharm = Toplevel()
		screen_inform_pharm.title("Information about pharmacies")
		screen_inform_pharm.geometry("500x500")
		Label(screen_inform_pharm, text = "Names of pharmacies:", bg ="#F0FFF0" , fg ="#00FF00", width = "20", font = ("Helvetica", 14)).pack()
		pharmacy.print_pharmacies()


	@staticmethod
	def display_inform_pills():
		global screen_inform_pills
		screen_inform_pills = Toplevel()
		screen_inform_pills.title("Information about pills")
		screen_inform_pills.geometry("500x700")
		Label(screen_inform_pills, text = "Name of pills:", bg ="#F0FFF0" , fg ="#00FF00", width = "20", font = ("Helvetica", 14)).place(x = 34, y = 25)
		Label(screen_inform_pills, text = "Size of pills:", bg ="#F0FFF0" , fg ="#00FF00", width = "20", font = ("Helvetica", 14)).place(x = 200, y = 25)
		pharmacy.print_pills()
		

	@staticmethod
	def display_inform_provider():
		global screen_inform_prov
		screen_inform_prov = Toplevel()
		screen_inform_prov.title("Information about providers")
		screen_inform_prov.geometry("500x400")
		Label(screen_inform_prov, text = "Names of providers:", bg ="#F0FFF0" , fg ="#00FF00", width = "20", font = ("Helvetica", 14)).pack()
		provider.print_provider()
		
	@staticmethod
	def display_pills_in_pharm():
		global screen_inform_pills_in_pharm
		screen_inform_pills_in_pharm = Toplevel()
		screen_inform_pills_in_pharm.title("Pills are in definite pharmacies")
		screen_inform_pills_in_pharm.geometry("500x1000")
		Label(screen_inform_pills_in_pharm, text = "Pharmacy:", bg ="#F0FFF0" , fg ="#008080", width = "10", font = ("Helvetica", 11)).place(x = 34, y = 5)
		Label(screen_inform_pills_in_pharm, text = "Pills:", bg ="#F0FFF0" , fg ="#008080", width = "10", font = ("Helvetica", 11)).place(x = 150, y = 5)
		Label(screen_inform_pills_in_pharm, text = "Size:", bg ="#F0FFF0" , fg ="#008080", width = "10", font = ("Helvetica", 11)).place(x = 250, y = 5)
		pharmacy.pills_in_pharm()
		
		
	def display_exp_pills(self):
		global screen_choose_pharm
		screen_choose_pharm = Toplevel()
		screen_choose_pharm.title("Pharmacy")
		screen_choose_pharm.geometry("500x500")
		Label(screen_choose_pharm, text = "Choose pharmacy", bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14)).place(x = 120, y = 10)
		global listbox_pharmacy
		listbox_pharmacy = Listbox(screen_choose_pharm, selectmode = SINGLE, bg ="#F0FFF0" , fg ="#7B68EE", font = ("Helvetica", 14))
		for el_pharmacy in data_of_pharm["pharmacy"]:
			listbox_pharmacy.insert(END, el_pharmacy.get('name'))
		listbox_pharmacy.place(x = 120, y = 67) 
		selection = listbox_pharmacy.curselection()
		Button(screen_choose_pharm, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "10", font = ("Helvetica", 14), command = self.selection_pharmacy_exp_pills). place(x = 120, y = 330)	
		Button(screen_choose_pharm, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_choose_pharm.destroy).place(x = 120, y = 400)


	@staticmethod
	def selection_pharmacy_exp_pills():
		
		selection = listbox_pharmacy.curselection()
		if selection:
			global screen_inf_exp_pills
			screen_inf_exp_pills = Toplevel()
			screen_inf_exp_pills.title("Explored pills")
			screen_inf_exp_pills.geometry("1000x500")
			Label(screen_inf_exp_pills, text = "Pharmacy", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 20, y = 5)
			Label(screen_inf_exp_pills, text = "Pills", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 170, y = 5)
			Label(screen_inf_exp_pills, text = "Size", bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 320, y = 5)
			Label(screen_inf_exp_pills, text = "Price", bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 400, y = 5)
			Label(screen_inf_exp_pills, text = "Expiration", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 480, y = 5)
			Label(screen_inf_exp_pills, text = "Quantity", bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 630, y = 5)
			pharmacy.print_expir_pills_in_pharm(listbox_pharmacy.get(selection))

		else:
			pills.error("Nothing has been chosen")


	def display_prov_pills(self):
		global screen_choose_prov
		screen_choose_prov = Toplevel()
		screen_choose_prov.title("Providers")
		screen_choose_prov.geometry("500x500")
		Label(screen_choose_prov, text = "Choose a provider", bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14)).place(x = 120, y = 10)
		global listbox_prov
		listbox_prov = Listbox(screen_choose_prov, selectmode = SINGLE, bg ="#F0FFF0" , fg ="#7B68EE", font = ("Helvetica", 14))
		for el_prov in data_of_provider["provider"]:
			listbox_prov.insert(END, el_prov.get('name'))
		listbox_prov.place(x = 120, y = 67) 
		Button(screen_choose_prov, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "10", font = ("Helvetica", 14), command = self.selection_prov). place(x = 120, y = 320)	
		Button(screen_choose_prov, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_choose_prov.destroy).place(x = 120, y = 370)
	
	@staticmethod
	def selection_prov():
		
		selection = listbox_prov.curselection()
		if selection:
			global screen_inf_prov_pills
			screen_inf_prov_pills = Toplevel()
			screen_inf_prov_pills.title("Provider's pills")
			screen_inf_prov_pills.geometry("800x500")
			Label(screen_inf_prov_pills, text = "Provider", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 20, y = 5)
			Label(screen_inf_prov_pills, text = "Pills", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 170, y = 5)
			Label(screen_inf_prov_pills, text = "Size", bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 320, y = 5)
			Label(screen_inf_prov_pills, text = "Price", bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 400, y = 5)
			Label(screen_inf_prov_pills, text = "Expiration", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 480, y = 5)
			Label(screen_inf_prov_pills, text = "Quantity", bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 630, y = 5)
			provider.get_pills_prov(listbox_prov.get(selection))
		else:
			pills.error("Nothing has been chosen")
	
		
	def display_pharm(self):
		global screen_choose_pharm
		screen_choose_pharm = Toplevel()
		screen_choose_pharm.title("Choice a pharmacy")
		screen_choose_pharm.geometry("500x500")
		Label(screen_choose_pharm, text = "Choose a pharmacy", bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14)).place(x = 120, y = 10)
		global listbox_pharm
		listbox_pharm = Listbox(screen_choose_pharm, selectmode = SINGLE, bg ="#F0FFF0" , fg ="#7B68EE", font = ("Helvetica", 14))
		for el_pharm in data_of_pharm["pharmacy"]:
			listbox_pharm.insert(END, el_pharm.get('name'))
		listbox_pharm.place(x = 120, y = 67) 
		Button(screen_choose_pharm, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "10", font = ("Helvetica", 14), command = self.selection_pharm). place(x = 120, y = 320)
		Button(screen_choose_pharm, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_choose_pharm.destroy).place(x = 120, y = 370)
		

	@staticmethod	
	def selection_pharm():
		
		selection = listbox_pharm.curselection()
		if selection:
			global screen_money_pharm
			screen_money_pharm = Toplevel()
			screen_money_pharm.title("Amount of money")
			screen_money_pharm.geometry("350x200")
			Label(screen_money_pharm, text = "Pharmacy", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 20, y = 5)
			Label(screen_money_pharm, text = "Amount of money", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 180, y = 5)
			pharmacy.get_amount_of_money(listbox_pharm.get(selection))
		else:
			pills.error("Nothing has been chosen")
			
			
	def display_pills(self):
		global screen_choose_pills
		screen_choose_pills = Toplevel()
		screen_choose_pills.title("Pills")
		screen_choose_pills.geometry("500x500")
		Label(screen_choose_pills, text = "Choose pills", bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14)).place(x = 120, y = 10)
		global listbox_pills
		listbox_pills = Listbox(screen_choose_pills, selectmode = SINGLE, bg ="#F0FFF0" , fg ="#7B68EE", font = ("Helvetica", 14))
		x = 0
		for el_pills in data_of_pills_prov["pills_provider"]:
			if el_pills.get("name") in listbox_pills.get(0, x):
				continue
			listbox_pills.insert(END, el_pills.get('name'))
			x = x + 1
		listbox_pills.place(x = 120, y = 67) 
		Button(screen_choose_pills, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "10", font = ("Helvetica", 14), command = self.selection_pills). place(x = 120, y = 320)
		Button(screen_choose_pills, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_choose_pills.destroy).place(x = 120, y = 370)


	@staticmethod
	def selection_pills():
		
		selection = listbox_pills.curselection()
		if selection:
			global screen_prov_have_pills
			screen_prov_have_pills = Toplevel()
			screen_prov_have_pills.title("Providers have definite pills")
			screen_prov_have_pills.geometry("800x300")
			Label(screen_prov_have_pills, text = "Provider's name", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 20, y = 5)
			Label(screen_prov_have_pills, text = "Pills", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 170, y = 5)
			Label(screen_prov_have_pills, text = "Size", bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 320, y = 5)
			Label(screen_prov_have_pills, text = "Price", bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 400, y = 5)
			Label(screen_prov_have_pills, text = "Expiration", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 480, y = 5)
			Label(screen_prov_have_pills, text = "Quantity", bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 630, y = 5)
			provider.get_prov_pills(listbox_pills.get(selection))
		else:
			pills.error("Nothing has been chosen")
			
			
			
	def display_pills_with_size(self):
		global screen_choose_pills_size
		screen_choose_pills_size = Toplevel()
		screen_choose_pills_size.title("Pills")
		screen_choose_pills_size.geometry("1000x500")
		Label(screen_choose_pills_size, text = "Choose pills", bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14)).place(x = 120, y = 10)
		global listbox_pills_prov
		listbox_pills_prov = Listbox(screen_choose_pills_size, selectmode = SINGLE, bg ="#F0FFF0" , fg ="#7B68EE", font = ("Helvetica", 14))
		x = 0
		for el_pills in data_of_pills_prov["pills_provider"]:
			if el_pills.get("name") in listbox_pills_prov.get(0, x):
				continue
			listbox_pills_prov.insert(END, el_pills.get('name'))
			x = x + 1
		listbox_pills_prov.place(x = 120, y = 67) 
		Button(screen_choose_pills_size, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "10", font = ("Helvetica", 14), command = self.selection_size). place(x = 120, y = 320)
		Button(screen_choose_pills_size, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_choose_pills_size.destroy).place(x = 120, y = 380)
		
	def selection_size(self):
		global selection_pills
		selection_pills = listbox_pills_prov.curselection()
		if selection_pills:
			Label(screen_choose_pills_size, text = "Choose size", bg ="#F0FFF0" , fg ="#008080", width = "20", font = ("Helvetica", 14)).place(x = 450, y = 10)
			global listbox_size_prov
			listbox_size_prov = Listbox(screen_choose_pills_size, selectmode = SINGLE, bg ="#F0FFF0" , fg ="#7B68EE", font = ("Helvetica", 14))
			x = 0
			for el_pills in data_of_pills_prov["pills_provider"]:
				if el_pills.get("name") == listbox_pills_prov.get(selection_pills):
					if el_pills.get("size") in listbox_size_prov.get(0, x):
						continue
					listbox_size_prov.insert(END, el_pills.get('size'))
					x = x + 1
			listbox_size_prov.place(x = 450, y = 67) 
			Button(screen_choose_pills_size, text = "OK", bg ="#F0FFF0" , fg ="#006400", width = "10", font = ("Helvetica", 14), command = self.selection_pills_size). place(x = 450, y = 320)
			Button(screen_choose_pills_size, text = "Back", height = "2",width = "10", font = ("Helvetica", 12), bg ="#B0E0E6" , fg ="#00008B", command = screen_choose_pills_size.destroy).place(x = 450, y = 380)
		else:
			pills.error("Nothing has been chosen")
			
			
	@staticmethod		
	def selection_pills_size():
		selection = listbox_size_prov.curselection()
		if selection:
			global screen_prov_pills_size
			screen_prov_pills_size = Toplevel()
			screen_prov_pills_size.title("Providers have definite pills with definite size")
			screen_prov_pills_size.geometry("1000x300")
			Label(screen_prov_pills_size, text = "Value of provider's advantage", bg ="#F0FFF0" , fg ="#008080", width = "22", font = ("Helvetica", 11)).place(x = 20, y = 5)
			Label(screen_prov_pills_size, text = "Provider's name", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 240, y = 5)
			Label(screen_prov_pills_size, text = "Pills", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 400, y = 5)
			Label(screen_prov_pills_size, text = "Size", bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 550, y = 5)
			Label(screen_prov_pills_size, text = "Price", bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 630, y = 5)
			Label(screen_prov_pills_size, text = "Expiration", bg ="#F0FFF0" , fg ="#008080", width = "15", font = ("Helvetica", 11)).place(x = 710, y = 5)
			Label(screen_prov_pills_size, text = "Quantity", bg ="#F0FFF0" , fg ="#008080", width = "7", font = ("Helvetica", 11)).place(x = 860, y = 5)
			provider.full_dic_prov_have_pills_size(listbox_pills_prov.get(selection_pills), listbox_size_prov.get(selection))
		else:
			pills.error("Nothing has been chosen")
			
	@staticmethod	
	def add_info():
		global screen_add_pills
		global flag_delete
		screen_add_pills = Toplevel()
		screen_add_pills.title("Add information")
		screen_add_pills.geometry("1300x1000")
		Label(screen_add_pills, text = "Add pills in pharmacy", bg ="#F0FFF0" , fg ="#32CD32", width = "20", font = ("Helvetica", 14)).place(x = 370, y = 10)
		flag_delete = False
		pills.enter_name_pharm(screen_add_pills)
		
	@staticmethod
	def delete_info():
		global screen_delete_pills
		global flag_delete
		screen_delete_pills = Toplevel()
		screen_delete_pills.title("Delete information")
		screen_delete_pills.geometry("900x500")
		Label(screen_delete_pills, text = "Delete pills in pharmacy", bg ="#F0FFF0" , fg ="#00CED1", width = "20", font = ("Helvetica", 14)).place(x = 330, y = 10)
		flag_delete = True
		pills.enter_name_pharm(screen_delete_pills)

current_datatime = datetime.now()
global cur_year
cur_year = current_datatime.year
global cur_month
cur_month = current_datatime.month
global cur_day
cur_day = current_datatime.day
interface = Graphical_interface()
interface.main_menu()
