# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, api, exceptions, fields, models, tools, registry, SUPERUSER_ID, Command


class AccountMove(models.AbstractModel):
    _inherit = 'account.move'

    def _notify_get_recipients(self, message, msg_vals, **kwargs):
        """
        Odoo 18 hook:
        Evita emails cuando se asigna user_id en facturas.
        """
        recipients_data = super(AccountMove, self)._notify_get_recipients(message, msg_vals, **kwargs)

        if message.model == "account.move" and message.subtype_id and \
           message.subtype_id.internal:
            return {}

        return recipients_data
