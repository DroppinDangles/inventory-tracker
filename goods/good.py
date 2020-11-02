#import packages
import aiy.voice.tts
from goods.shoppinglist import ShoppingList

class Good():
	def __init__(self, id_num, good_name, quant, quant_units, min_quant, s_tier, p_date):
		self.id = id_num
		self.good_name = good_name
		self.quant = quant
		self.quant_units = quant_units
		self.min_quant
		self.s_tier = s_tier
		self.p_date = p_date

	def checkQuant(self):
		if self.quant <= self.min_quant:
			return True
		else:
			return False

	def useGood(self, use_quant):
		self.quant -= use_quant

		#check if restock is necessary
		restock = checkQuant()
		if restock == True:
			addToList()

	def addToList(self, listId):
		if self.s_tier = "t1":
			return #finish method

	def askRestock(self):
		pass