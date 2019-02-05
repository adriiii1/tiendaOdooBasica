from odoo import models,fields,api

class Clientes(models.Model):
    _name = 'tiendaodoo.clientes'
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    edad = fields.Date('Edad')
    telefono = fields.Integer('Telefono', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

    class Pedidos(models.Model):
        _name = 'tiendaodoo.pedidos'
        total = fields.Integer('Total', required=True)

        def name_get(self):
            res = []
            for record in self:
                name = record.pedidos
                res.append((record.id, name))
            return res

    @api.one
    def limpiar(self):
        self.nombre = ""
        return True

    @api.multi
    def limpia_todo(self):
        done_recs = self.search([('nombre', '=', 'fender')])
        done_recs.write({'nombre': 'Fender'})
        return True
