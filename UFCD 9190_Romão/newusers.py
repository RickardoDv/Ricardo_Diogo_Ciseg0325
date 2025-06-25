#Conexao com o servidor de AD

from ldap3 import Server, Connection, ALL, NTLM, MODIFY_REPLACE
from ldap3.core.exceptions import LDAPException

#configuration
DOMAIN_NAME = "ciseg.internal"
DOMAIN_CONTROLLER="Dc01.ciseg.internal"
ADMIN_USERNAME="ciseg\\Administrator"
ADMIN_PASSWORD="Formacao2025"
BASE_DN="DC=ciseg,DC=internal"
NEW_USER="ricardo.diogo"
NEW_USER_DN=f"CN={NEW_USER},CN=Users,{BASE_DN}"
NEW_USER_PASSWORD="P+sswordCyber2025"

try:
    #conexão ao DC
    server=Server(DOMAIN_CONTROLLER,get_info=ALL)
    conn=Connection(server, user=ADMIN_USERNAME, password=ADMIN_PASSWORD, authentication=NTLM, auto_bind=True)



except:
    pass