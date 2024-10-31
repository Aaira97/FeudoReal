from frappe import _
import frappe

@frappe.whitelist(allow_guest=True) 
def formulario_de_contacto():
    request_args = frappe.form_dict  
    doc = frappe.new_doc("Formulario Contacto")
    doc.fecha = request_args.get("fecha")
    doc.comensales = int(request_args.get("comensales", 0))
    doc.email = request_args.get("email")
    doc.cliente = request_args.get("cliente")
    doc.telefono = request_args.get("telefono")
    doc.mensaje = request_args.get("mensaje")
    doc.insert(ignore_permissions=True)
    frappe.response["message"] = doc