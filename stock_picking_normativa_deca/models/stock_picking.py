# -*- coding: utf-8 -*-

from odoo import _, fields, models
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    deca_effective_carrier_id = fields.Many2one(
        'res.partner',
        string='Transportista efectivo',
    )
    deca_goods_nature = fields.Text(
        string='Naturaleza de la mercancía',
    )
    deca_alternative_magnitude = fields.Char(
        string='Otra magnitud',
        help='Indicarla únicamente cuando no sea posible determinar el peso exacto.',
    )
    deca_special_authorization = fields.Char(
        string='Autorización especial',
    )
    deca_vehicle_plate = fields.Char(
        string='Matrícula del vehículo tractor',
    )
    deca_trailer_plate = fields.Char(
        string='Matrícula del remolque o semirremolque',
    )
    deca_observations = fields.Text(
        string='Observaciones o reservas',
    )
    deca_document_ids = fields.One2many(
        'stock.picking.deca.document',
        'picking_id',
        string='Documentos DeCA',
    )

    def action_generate_deca_document(self):
        self.ensure_one()
        if self.picking_type_code != 'outgoing':
            raise UserError(_('El documento DeCA sólo se puede generar para entregas.'))

        version = max(self.deca_document_ids.mapped('version'), default=0) + 1
        document = self.env['stock.picking.deca.document'].create({
            'name': _('%(picking)s - DeCA v%(version)s', picking=self.name, version=version),
            'picking_id': self.id,
            'version': version,
            'generated_at': fields.Datetime.now(),
        })
        filename = '%s_DeCA_v%s.pdf' % (self.name.replace('/', '_'), version)
        attachment = self.env['ir.attachment'].create({
            'name': filename,
            'type': 'binary',
            'mimetype': 'application/pdf',
            'res_model': document._name,
            'res_id': document.id,
            'public': False,
        })
        token = attachment.generate_access_token()[0]
        access_url = '%s/web/content/%s?access_token=%s&download=1' % (
            self.get_base_url().rstrip('/'),
            attachment.id,
            token,
        )
        document.write({
            'attachment_id': attachment.id,
            'access_url': access_url,
        })

        report = self.env.ref('stock_picking_normativa_deca.action_report_delivery_deca')
        pdf_content = report._render_qweb_pdf(
            report,
            self.ids,
            data={'deca_document': document},
        )[0]
        attachment.raw = pdf_content
        document.write({
            'state': 'final',
        })
        return document.action_open_document()
