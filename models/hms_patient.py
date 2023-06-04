from odoo import models,fields,api
from odoo.exceptions import ValidationError,UserError

class HmsPatient(models.Model):
    _name="hms.patient"
    _rec_name="first_name"
    first_name=fields.Char()
    last_name=fields.Char()
    birthdate=fields.Date()
    history=fields.Html()
    cr_ratio=fields.Float()
    blood_type=fields.Selection(
        [('Blood_type_A','A'), 
        ('Blood_type_B','B'),
        ('Blood_type_O','O'),
        ('Blood_type_AB','AB')]
    )
    pcr=fields.Boolean()
    image=fields.Binary()
    address=fields.Text()
    age=fields.Integer()
    state=fields.Selection([("Undetermined","Undetermined"),("Good","Good"),("Fair","Fair"),("Serious","Serious")])
    doctor_id=fields.Many2many("hms.doctors")
    department_id=fields.Many2one("hms.department")
    department_capacity=fields.Integer(related='department_id.capacity')
    department_status=fields.Boolean(related='department_id.is_opened')
