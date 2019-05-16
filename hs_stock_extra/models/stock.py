# -*- coding: utf-8 -*-
from odoo import api, fields, models

class StockDeliveryOrderInherit1(models.Model):
	_inherit = "stock.picking"
	hs_display = fields.Boolean("Display Managment", compute="_compute_display_mangment", store=False)
	hs_managment = fields.Char('Administrador', compute="_compute_managment", store=False)


	@api.one
	@api.depends('name', 'origin')
	def _compute_managment(self):
		if self.env["sale.order"].search_count([("name", "=", self.origin)]) > 0:
			env = self.env["sale.order"].search([("name", "=", self.origin)], limit=1)
			self.hs_managment = env.user_id.name
		elif self.env["purchase.order"].search_count([("name", "=", self.origin)]) > 0:
			env = self.env["purchase.order"].search([("name", "=", self.origin)], limit=1)
			self.hs_managment = env.user_id.name
		else:
			self.hs_managment = ""


	@api.one
	@api.depends('name', 'origin')
	def _compute_display_mangment(self):
		self.hs_display = True


"""
class StockPickingInherit(models.Model):
	_inherit = "stock.picking"
	#hs_category = fields.Char(related='picking_type_id.name', string="Operation Type", store=False)
	hs_state = fields.Selection(selection='_get_selection_content', store=False)


	@api.depends('picking_type_id')
	def _get_selection_content(self):
		if self.picking_type_id.name == "Delivery Orders":
			return [
					('draft', 'Draft'),
					('waiting', 'Waiting Another Operation'),
					('confirmed', 'Waiting'),
					('assigned', 'Ready'),
					('done', 'Bodega EMSA'),
					('cancel', 'Cancelled'),
			]
		elif self.picking_type_id.name == "Recepciones":
			return [
					('draft', 'Draft'),
					('waiting', 'Waiting Another Operation'),
					('confirmed', 'Waiting'),
					('assigned', 'Ready'),
					('done', 'Entregado'),
					('cancel', 'Cancelled'),
			]
		else:
			return [
					('draft', 'Draft'),
					('waiting', 'Waiting Another Operation'),
					('confirmed', 'Waiting'),
					('assigned', 'Ready'),
					('done', 'Completado'),
					('cancel', 'Cancelled'),
			]
"""