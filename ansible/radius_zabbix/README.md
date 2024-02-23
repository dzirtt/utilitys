# Ansible Playbook for Zabbix Agent Deployment

This Ansible playbook automates the configuration of Zabbix agents on different hosts. The playbook includes tasks such as adding Debian squeeze repositories, updating aptitude, installing required packages, and configuring Zabbix agent settings. Also include old zabbix agent deb files.

## Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
2. Update Inventory

   Rename the inventory_example.ini to inventory.ini, fill use user\passwords

3. RUN
   ```bash
   ansible-playbook -i inventory.ini zabbix-agent-playbook.yml