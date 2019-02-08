from odoo import models, fields, api, _


class Ventas(models.Model):
    _name = 'tienda.ventas'
    cod = fields.Char('COD', required=True)
    fechaventa = fields.Date('Fecha Venta', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    cliente = fields.Many2one('tienda.clientes', 'Clientes', required=True)
    articulo = fields.Many2one('tienda.articulos', 'Articulos', required=True)
    precio = fields.Integer()
    cantidad = fields.Integer('Cantidad', required=True)
    total = fields.Float(string='Total', compute='_total')

    def name_get(self):
        res = []
        for record in self:
            name = record.cod
            res.append((record.id, name))
        return res

    @api.one
    @api.depends('cantidad')
    def _total(self):
        self.precio = self.articulo.precio
        self.total = self.articulo.precio * self.cantidad
