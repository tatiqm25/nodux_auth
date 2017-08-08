# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
__version__ = '0.0.1'

@frappe.whitelist(allow_guest=True)
def authenticate(user, password):
    print "Esta ingresando", password, frappe.db.sql("""select company_name from `tabCompany` where company_name = 'Nodux'""", as_dict=1)
    print "Mal ", frappe.db.sql("""select company_name from `tabCompany` where pass_auth = %s""", password, as_dict=1)
    company = frappe.db.sql("""select company_name from `tabCompany` where pass_auth = %s""", password, as_dict=1)
    c = 0
    a = None
    print "company", company
    if company != []:
        flag = '1'
        flag_c = '0'
        flag_a = '0'
        c = company.formato
        a = company.date_active
    else:
        print "Pasa 1.1"
        flag = '0'
        flag_c = '0'
        flag_a = '0'

    print "Pasa 1"
    if c == 1:
        flag_c = '1'
    else:
        flag_c = '0'
    print "Pasa 2"
    if a != None:
        date= datetime.now()
        limit= (date-a).days
        if limit > 5:
            flag_a = '1'
        else:
            flag_a = '0'
    return flag, flag_c, flag_a
    #return flag, flag_c, flag_a
