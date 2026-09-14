# -*- coding: utf-8 -*-

from odoo import fields, models


class StockPickingDecaDocument(models.Model):
    _name = 'stock.picking.deca.document'
    _description = 'Documento DeCA de entrega'
    _order = 'version desc, id desc'

    name = fields.Char(required=True, readonly=True)
    picking_id = fields.Many2one(
        'stock.picking',
        string='Entrega',
        required=True,
        readonly=True,
        ondelete='cascade',
    )
    version = fields.Integer(required=True, readonly=True)
    state = fields.Selection(
        [('draft', 'Borrador'), ('final', 'Final')],
        required=True,
        default='draft',
        readonly=True,
    )
    attachment_id = fields.Many2one(
        'ir.attachment',
        string='PDF',
        readonly=True,
        ondelete='restrict',
    )
    access_url = fields.Char(string='URL', readonly=True)
    generated_at = fields.Datetime(string='Generado el', readonly=True)

    _sql_constraints = [
        (
            'picking_version_unique',
            'unique(picking_id, version)',
            'La versión DeCA debe ser única por entrega.',
        ),
    ]

    def action_open_document(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url': self.access_url,
            'target': 'self',
        }
