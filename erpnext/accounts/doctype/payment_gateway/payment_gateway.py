# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PaymentGateway(Document):
	def validate(self):
		self.update_default_payment_gateway()
	
	def update_default_payment_gateway(self):
		frappe.db.sql("""update `tabPayment Gateway` set is_default = 0
			where is_default = 1 """)
		
		
