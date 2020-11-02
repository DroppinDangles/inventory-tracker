#import packages
from goods.good import Good
import datetime

class Food(Good):
	def __init__(self, exp_date):
		self.exp_date = exp_date