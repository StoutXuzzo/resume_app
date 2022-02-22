# -*- coding: utf-8 -*-

from odoo import models, fields, api
# DO THIS IMPORT
from odoo.exceptions import ValidationError

# CHANGE THE CLASS NAME
class UserModel(models.Model):
# CHANGE THE NAME FOR THE MODEL NAME
    _name = 'resume_app.user_model'
# CHANGE THE DESCRIPTION
    _description = 'User Model'

# SQL CONSTRAIN     ACUERDATE DE LA ULTIMA COMA, QUE SINO NO FUNCIONA
    _sql_constraints = [('user_unique_username', 'UNIQUE(username)', 'The username is already on use.'),
    ('user_unique_id', 'UNIQUE(id)', 'This ID already exist.'),]

# ID ASIGNADA MANUALMENTE
    # CREADION DEL CAMPO CONTENEDOR DE LA ID
    id = fields.Integer("ID: ", default = lambda self: self.getId())

    # METODO DE LA ID
    def getId(self):
        if len(self.env["resume_app.user_model"].search([])) > 0:
            return self.env["resume_app.user_model"].search([])[-1].id + 1
        return 1

# CAMPO STATE
    # CREACION DEL CAMPO SELECTION CON UN VALOR POR DEFECTO
    state = fields.Selection(string="State: ", selection=[('c', 'Confirmed'), ('u', 'Unconfirmed')], default='u')

    # METODO REFERENCIADO EN LA VISTA PARA CONFIRMAR USUARIOS
    def confirm(self):
        password = self.password
        if len(password) > 16 or len(password) < 4:
            raise ValidationError('The password can\'t be longer than 16 or shorter than 4.')
        self.state = 'c'
        

# CAMPO CON CONSTRAIN
    # CREACION NORMAL DEL CAMPO
    username = fields.Char("Username: ", required=True, index=True, help="Username")

    #CREACION DEL METODO QUE VA A CONTROLAR SU CONTENIDO
    @api.constrains('username')
    def valUsername(self):
        user = self.username
        if len(user) > 16 or len(user) < 4:
            raise ValidationError('The username can\'t be longer than 16 or shorter than 4.')

    password = fields.Char("Password: ", required=True)

# CAMPO CALCULADO
    # CREACION DEL CAMPO CALCULADO
    name = fields.Char("DataBase name: ", compute="setName", store=True)

    # METODO DEL CAMPO CALCULADO
    @api.depends('username', 'password')
    def setName(self):
        if self.username != False and self.password != False:
            self.name = str(self.username) + "#" + str(self.password)
            return True
    
    photo =  fields.Binary("Photo: ", help="User photo.")
    age = fields.Integer("Age: ", default = 16)
    date = fields.Date("Important date: ", required=True, help="The most important date for the user.")
    gender = fields.Selection(string = "Gender: ", selection=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], required=True)
    phone = fields.Char("Phone number: ")
    email = fields.Char("Email address: ")

# RELACIONES
    manyToOne_id = fields.Many2one('resume_app.manytoone_model', "ManyToOne: ")
    oneToMany_ids = fields.One2many('resume_app.onetomany_model', 'user_id', "OneToMany: ")
    manyToMany_ids = fields.Many2many('resume_app.manytomany_model', string="ManyToMany: ")

