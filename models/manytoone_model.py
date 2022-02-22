# -*- coding: utf-8 -*-
from odoo import models, fields, api
# DO THIS IMPORT
from odoo.exceptions import ValidationError

# CHANGE THE CLASS NAME
class ManyToOneModel(models.Model):
# CHANGE THE NAME FOR THE MODEL NAME
    _name = 'resume_app.manytoone_model'
# CHANGE THE DESCRIPTION
    _description = 'ManyToOne Model'

    text = fields.Char("Text: ", default="AAAAAAAAAAAAAAAAAAAAAAA")
    user_ids = fields.One2many('resume_app.user_model', 'manyToOne_id', "Users: ")



