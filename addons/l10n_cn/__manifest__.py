# -*- coding: utf-8 -*-
# Part of Cnmx. See LICENSE file for full copyright and licensing details.

{
    'name': 'China - Accounting',
    'version': '1.8',
    'category': 'Localization',
    'author': 'Cnmx Ltd.',
    'maintainer': 'dean@cnmx.com',
    'website': 'https://www.cnmx.com',
    'description': """
Includes the following data for the Chinese localization
========================================================

Account Type/科目类型

State Data/省份数据

    """,
    'depends': ['base', 'account', 'l10n_multilang', 'base_address_city'],
    'data': [
        'data/account_tax_group_data.xml',
        'data/res_country_data.xml',
        'data/res_city_data.xml',
    ],
}
