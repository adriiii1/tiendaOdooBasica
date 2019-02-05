from odoo import models,fields,api

class Proveedores(models.Model):
    _name = 'tiendaodoo.proveedores'
    cif = fields.Char('Cif', required=True)
    nombre = fields.Char('Nombre', required=True)
    telefono = fields.Integer('Telefono', required=True)
    calle = fields.Char('Calle', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res



class Articulos(models.Model):
    _name = 'tiendaodoo.articulos'
    marca = fields.Char('Marca', required=True)
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    precio = fields.Integer('Precio', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.articulos
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
