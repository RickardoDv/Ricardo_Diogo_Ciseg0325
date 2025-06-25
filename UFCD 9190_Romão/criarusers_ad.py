# Conexao com o servidor de Active Directory

from ldap3 import Server, Connection, ALL, NTLM, MODIFY_REPLACE
from ldap3.core.exceptions import LDAPException

# Configuration
DOMAIN_NAME = "ciseg.internal"
DOMAIN_CONTROLLER = "Dc01.ciseg.internal"
ADMIN_USERNAME = "ciseg\\Administrator"
ADMIN_PASSWORD = "Formacao2025"
BASE_DN = "DC=ciseg,DC=internal"
NEW_USER = "joao.fuzeta"
NEW_USER_DN = f"CN={NEW_USER},CN=Users,{BASE_DN}"
NEW_USER_PASSWORD = "P+sswordCyber2025"

try:
    # Connexao ao DC
    server = Server(DOMAIN_CONTROLLER, get_info=ALL)
    conn = Connection(server, user=ADMIN_USERNAME, password=ADMIN_PASSWORD, authentication=NTLM, auto_bind=True)

    conn.add(
        dn=NEW_USER_DN,
        object_class=['top', 'person', 'organizationalPerson', 'user'],
        attributes={
                'cn': NEW_USER,
                'givenName': 'Joao',
                'sn': 'Fuzeta',
                'displayName': 'Joao Fuzeta',
                'userPrincipalName': f'{NEW_USER}@{DOMAIN_NAME}',
                'samAccountName': NEW_USER,
                'userAccountControl': 544
        }
    )

    if conn.result['result'] == 0:
        print("Usuário criado com sucesso")

        # Estipular a password
        conn.extend.microsoft.modify_password( NEW_USER_DN , NEW_USER_PASSWORD  )

        conn.modify( NEW_USER_DN ,  { 'pwdLastSet':  [( MODIFY_REPLACE, ['0']  )  ]   }   )

        print("Password foi alterada, por default")
        
    else:
        print("Deu bide a criar o user.")

    conn.unbind()        

except:
    print("Deu bide")
    pass




