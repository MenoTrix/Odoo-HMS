from odoo import fields,models


class HmsDoctors(models.Model):
    _name="hms.doctors"
    # usually rec_name value is name but we can sit it to the field name so it can show this field if we didn't put it we will see model name
    _rec_name="first_name" 
    first_name=fields.Char()
    last_name=fields.Char()
    image=fields.Binary()
    department_id=fields.Many2one("hms.department")
    patient_id=fields.Many2many("hms.patient")
    