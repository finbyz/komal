import frappe

from erpnext.controllers.accounts_controller import AccountsController

def set_discount_in_quotation(self , method):
	if frappe.session.user == "Administrator":
		frappe.msgprint("KOMAL")
	if self.discount:
		for row in self.items:
			row.discount_amount = (row.price_list_rate * self.discount)/100
			frappe.db.set_value(row.doctype , row.name , "discount_amount" , row.discount_amount)
			row.discount_percentage = self.discount
			if(self.discount == 0):
				row.discount_percentage = 0
				row.discount_amount = 0	
	else:
		for row in self.items:
			frappe.db.set_value(row.doctype , row.name , "discount_amount" , 0)
			row.discount_percentage = 0
			row.discount_amount = 0	
	AccountsController.set_missing_item_details(self)
	AccountsController.calculate_taxes_and_totals(self)
