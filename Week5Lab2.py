#!/usr/bin/env python3

from pexpect import pxssh

#On the WEB and DB servers: Create a user named egoad w/a password of RubberDuck!
def CreateUser(IP,username,password):
    session = pxssh.pxssh()
    session.login(IP,username,password)
    print("SSH Login: successful")
    session.sendline('sudo useradd egoad')
    session.prompt()
    session.sendline('Password01')
    session.prompt()
    session.sendline('sudo passwd egoad')
    session.prompt()
    session.sendline('RubberDuck!')
    session.prompt()
    session.sendline('RubberDuck!')
    session.prompt()
    print("User creation successful")
    session.logout()

#WEB servers: Install Apache (apache2), Start Apache,Configure Apache to auto-start at system boot
def InstallApache(IP,username,password):
    session = pxssh.pxssh()
    session.login(IP,username,password)
    session.sendline('sudo apt update')
    session.prompt()
    session.sendline('Password01')
    print("Updated successfully")
    session.prompt()
    session.sendline('sudo apt-get -y install apache2')
    session.prompt()
    print("Installed Apache2 successfully")
    session.sendline('sudo systemctl start apache2')
    session.prompt()
    session.sendline('sudo systemctl enable apache2')
    session.prompt()
    print("Enabled Apache2 @boot successfully")
    session.logout()


def InstallMySQL(IP, username,password):
    session = pxssh.pxssh()
    session.login(IP,username,password)
    session.sendline('sudo apt update') #very necessary!
    session.prompt()
    session.sendline('Password01')
    print("Updated successfully")
    session.prompt()
    session.sendline('sudo apt-get -y install mysql-client')
    session.prompt()
    session.sendline('sudo apt-get -y install mysql-server')
    session.promt()
    session.sendline('sudo systemctl start mysql')
    session.promt()
    session.sendline('sudo systemctl enable mysql') #auto start @boot
    print("MySQL installed successfully")
    session.logout()

#create users on Web & DB servers:
CreateUser('192.168.0.111','justincase','Password01')
CreateUser('192.168.0.112','justincase','Password01')
CreateUser('192.168.0.121','justincase','Password01')
CreateUser('192.168.0.122','justincase','Password01')

InstallApache('192.168.0.111','justincase','Password01')
InstallApache('192.168.0.112','justincase','Password01')

#Install MySQL on DB servers:
InstallMySQL('192.168.0.121','justincase','Password01')
InstallMySQL('192.168.0.122','justincase','Password01')

print("Entire Script was successful!")