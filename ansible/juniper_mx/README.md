# Juniper Get Down Ports with Transceiver Inventory Info by Telnet

This Ansible playbook automates the process of retrieving information about down ports and associated transceiver inventory from Juniper devices using telnet.

## Prerequisites

0. Install Python modules from `requirements.txt`.

   ```bash
   pip install -r requirements.txt

1. Copy inventory_example.ini to inventory.ini.

2. Enter your telnet credentials and add Juniper device hosts in the inventory.ini file.

3. Run the playbook on the configured inventory.