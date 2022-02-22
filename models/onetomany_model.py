# -*- coding: utf-8 -*-

from odoo import models, fields, api
# DO THIS IMPORT
from odoo.exceptions import ValidationError

# CHANGE THE CLASS NAME
class OneToManyModel(models.Model):
# CHANGE THE NAME FOR THE MODEL NAME
    _name = 'resume_app.onetomany_model'
# CHANGE THE DESCRIPTION
    _description = 'OneToMany Model'

    text = fields.Char("Text: ", default="AAAAAAAAAAAAAAAAAAAAAAA")
    user_id = fields.Many2one('resume_app.user_model', "Users: ")



