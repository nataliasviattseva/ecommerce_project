


# Installing Ansible
sudo apt update
sudo apt install ansible
# Setting Up the Inventory File
sudo nano /etc/ansible/hosts

EOF
[servers]
server1 ansible_host=203.0.113.111
server2 ansible_host=203.0.113.112
server3 ansible_host=203.0.113.113

[all:vars]
ansible_python_interpreter=/usr/bin/python3

# Testing Connection
ansible all -m ping -u root