import sys
import odoorpc

odoo = odoorpc.ODOO('127.0.0.1', port=80)
timeout_backup = odoo.config['timeout']
odoo.config['timeout'] = 240
odoo.db.create('admin', 'test_db' , 'False', 'fr_FR', 'password')
odoo.config['timeout'] = timeout_backup
