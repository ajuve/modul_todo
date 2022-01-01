{
    'name': "Modul Todo",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': 'Artur Juvé Vidal',
	'license': "AGPL-3", 	
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '11.0.1.0',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': ['security/ir.model.access.csv','views/views.xml'],
	
	#'demo': ['demo.xml'], 
}
