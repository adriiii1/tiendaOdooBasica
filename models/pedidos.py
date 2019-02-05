from odoo import models,fields,api

class Pedidos(models.Model):
    _name = 'tiendaodoo.pedidos'
    cliente = fields.Many2one('tiendaodoo.clientes', 'Clientes')
    articulo = fields.Many2one('tiendaodoo.articulos', 'Articulos')
    total = fields.Integer('Total', required=True)

    @api.one
    def limpiar(self):
        self.nombre = ""
        return True

    @api.multi
    def limpia_todo(self):
        done_recs = self.search([('nombre', '=', 'fender')])
        done_recs.write({'nombre': 'Fender'})
        return True
