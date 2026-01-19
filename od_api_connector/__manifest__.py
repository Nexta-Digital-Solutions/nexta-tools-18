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

{
    'name': 'Odoo API Connector',
    'version': '18.0.0.1',
    'summary': 'Base module for Odoo Dynamic API & Webhook Manager',
    'decscription': """
        This module is base module for provides a dynamic API request handler for Odoo, allowing you to manage API requests and responses dynamically.
        It is designed to work with the Odoo Dynamic API & Webhook Manager module, enabling seamless integration with external systems.
        You must have Odoo Dynamic API & Webhook Manager module to manage below features!
        - Manage Odoo system through API requests without any customization. 
        - You can create, update, search, copy and delete records in Odoo using secure API requests.
        - The module supports dynamic API request handling, allowing you to define and manage API endpoints and their responses.
        - It provides a user-friendly interface to configure API handlers and their associated responses.
        - You can also run the Server Action using the API request handler to process the request and return the response.
    """,
    'category': 'Base',
    'author': 'OdriTech Solutions',
    'company': 'OdriTech Solutions',
    'website': 'https://odritech.com/',
    'depends': [
        'base', 'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/api_connector.xml',
        'views/api_logger.xml',
    ],
    'license': 'OPL-1',
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'live_test_url': 'https://www.youtube.com/playlist?list=PLFWwGZArKfBs6nwCaRGd5z_Gax8OSwwBO',
}
