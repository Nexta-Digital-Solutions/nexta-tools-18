# -*- coding: utf-8 -*-

from odoo import api, models


class IrActions(models.Model):
    _inherit = 'ir.actions.actions'

    @api.model
    def get_bindings(self, model_name):
        bindings = super().get_bindings(model_name)
        if model_name != 'stock.picking' or not bindings.get('report'):
            return bindings

        delivery_id = self.env.ref('stock.action_report_delivery').id
        deca_id = self.env.ref(
            'stock_picking_normativa_deca.action_generate_delivery_deca'
        ).id
        reports = bindings['report']
        deca_report = next((report for report in reports if report['id'] == deca_id), None)
        if deca_report:
            reports.remove(deca_report)
            delivery_index = next(
                (index for index, report in enumerate(reports) if report['id'] == delivery_id),
                len(reports) - 1,
            )
            reports.insert(delivery_index + 1, deca_report)
        return bindings
