# -*- coding: utf-8 -*-
# Part of Cnmx. See LICENSE file for full copyright and licensing details.

{
    'name': 'Indonesian - Accounting',
    'version': '1.0',
    'category': 'Localization',
    'description': """
This is the latest Indonesian Cnmx localisation necessary to run Cnmx accounting for SMEs with:
=================================================================================================
    - generic Indonesian chart of accounts
    - tax structure""",
    'author': 'vitraining.com',
    'website': 'http://www.vitraining.com',
    'depends': ['account', 'base_iban', 'base_vat'],
    'data': [
        'data/account_chart_template_data.xml',
        'data/account.account.template.csv',
        'data/account_chart_template_post_data.xml',
        'data/account_tax_template_data.xml',
        'data/account_chart_template_configuration_data.xml',
        'views/account_reconcile_model_views.xml',
    ],
}
