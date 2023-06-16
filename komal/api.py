import frappe

from erpnext.controllers.accounts_controller import AccountsController

def set_discount_in_quotation(self , method):
	if self.discount:
		for row in self.items:
			row.discount_percentage = self.discount
			row.discount_amount = (row.price_list_rate * self.discount)/100
			if(self.discount == 0):
				row.discount_percentage = 0
				row.discount_amount = 0	
	else:
		for row in self.items:
			row.discount_percentage = 0
			row.discount_amount = 0	
	AccountsController.calculate_taxes_and_totals(self)
	AccountsController.set_missing_item_details(self)
