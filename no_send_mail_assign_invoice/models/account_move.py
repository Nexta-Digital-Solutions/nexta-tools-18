# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, api, exceptions, fields, models, tools, registry, SUPERUSER_ID, Command


class AccountMove(models.AbstractModel):
    _inherit = 'account.move'

    def _notify_get_recipients(self, message, recipients_data):
        """
        Odoo 18 hook:
        Evita emails cuando se asigna user_id en facturas.
        """
        recipients_data = super()._notify_get_recipients(message, recipients_data)

        if message.model == "account.move" and message.subtype_id and \
           message.subtype_id.internal:
            for partner_id, data in recipients_data.items():
                # Forzar notificación interna (inbox)
                data["notification_type"] = "inbox"

        return recipients_data
