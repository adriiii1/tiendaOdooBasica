from odoo import models, fields, api, _


class Articulos(models.Model):
    _name = 'tienda.articulos'
    cod = fields.Char('COD', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    proveedor = fields.Many2one('tienda.proveedores', 'Proveedores')
    precio = fields.Float('Precio', required=True)
    cantidad = fields.Integer('Cantidad', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.cod + ' - ' + record.descripcion
            res.append((record.id, name))
        return res
