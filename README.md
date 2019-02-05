Module
=========

This role allows to manage Odoo modules automatically and configure them depending of our need.
The following actions can be made:

* **install**: install a list of Odoo modules on a lastest version available on the host (look at the `modules_to_install` variable)

* **update_list**: enable us to update the app like we make in UI after update addons source code. This action is run every time instal or upgrade actions are called

* **upgrade**: upgrade et list of Odoo modules based on a provided list (look at the `modules_to_upgrade` variable)

* **uninstall**: uninstall Odoo modules base on a list (look at the `modules_to_uninstall` variable)

* **configure_pos**: this action were add because is't very common and frequently made, so we will use that when we need to configure our Odoo Point Of Sale (look at the `pos_to_configure` variable))

* **configure_company**: we use it to update information about the company created in Odoo (look at the `company_to_configure` variable)

* **configure_custome_module**: we use it to configure odoo custom module installed in Odoo (look at the `custom_modules_to_configure` variable)

* **configure_product**: we use it to create and configure  odoo product, category and subcategoryo (look at the `product_to_configure` variable)

`NB`: To easily use this role, every single action are tasks with the corresponding tags (tags: install, update_list ...)

Odoo version tested
-------------------
-> 10.0

Requirements
------------

You need to install python dependancies on odoo host : xmlrpclib, odoorpc

Role Variables
--------------

There are a lot of variables, so to see all of them plase check the `default/main.yml` where i present variable with description and cautions

Dependencies
------------

.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      user: root
      become: yes
      gather_facts: false

      pre_tasks:
        - block:
            - name: "Check connectivity"
             ping: ~
          rescue:
            - debug:
                msg: "Module ping: error"
            - raw: bash -c "test -f /usr/bin/python || (apt-get update && apt-get install python python3 -yqq) || (yum -y install python)"
              register: output
          always:
            - setup: ~

      roles:
        - { role: module, tags: ['install', 'configure_pos'] }

License
-------

BSD

Author Information
------------------

- Dirane TAFEN (diranetafen@yahoo.com)
