# -- coding: utf-8 --
###############################################################################
#
#    Odritech Solutions
#
#    Copyright (C) 2025 Odritech Solutions (<https://odritech.com/>)
#    Author: Odritech Solutions (odritechsolutions@gmail.com)
#
#    This program is under the terms of the Odoo Proprietary License v1.0 (OPL-1)
#    It is forbidden to publish, distribute, sublicense, or sell copies of the
#    Software or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL
#    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
###############################################################################

from odoo import models, fields, api, Command, _
from odoo.exceptions import UserError


class ApiHandlerResponse(models.Model):
    _name = 'api.handler.response'
    _description = 'Dynamic response for API Handler requests'

    name = fields.Char(string='Response Field Name', required=True, copy=False, compute='_compute_response_field', readonly=False, store=True)
    api_handler_id = fields.Many2one('api.handler', 'API Handler', required=True, ondelete='cascade', index=True, help='API Handler to which this field belongs.')
    field_id = fields.Many2one(
        comodel_name='ir.model.fields',
        domain="[('model_id', '=', parent.model_id)]",
        store=True
    )

    @api.depends('field_id')
    def _compute_response_field(self):
        for line in self:
            line.name = line.field_id.field_description or line.field_id.name or ''
