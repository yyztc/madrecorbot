from itoptop import Itop
import config

itop = Itop('http://{}/itop/webservices/rest.php', '1.3', '{}', '').format(config.server, config.ItopUser, config.ItopPss)

#UNIDADE INTERNAÇÃO ENFERMARIA
#ENFERMAGEM PRONTO ATENDIMENTO

def createItopUser(name, user, organization):

    '''
    Criar usuário no ITOP\n
    params:
        @name - Nome completo da pessoa para criar o acesso
        @organization - Organização para fazer busca no ITOP
        @user - Usuário da pessoa para criar no ITOP
    '''

    name = str.upper(name)
    name = name.split(' ')
    n = name[0]
    name.remove(name[0])
    name = ' '.join(name)

    org = itop.schema('Organization').find({'name': organization})
    madre = itop.schema('Organization').find({'name': 'HOSPITAL MADRECOR'})
    guy = itop.schema('Person').insert({'name': name, 'first_name': n, 'org_id': org['id'], 'email': user+'@madrecor.com.br'})
    profile = itop.schema('URP_Profiles').find({'name': 'Portal user'})
    
    user = {
        'contactid': guy['id'],
        'login': user,
        'password': 'Madre19@@',
        'language': 'PT BR',
        'status': 'enabled',
        'profile_list': [
            {
                'profileid': profile['id']
            }
        ],
        'allowed_org_list': [
            {
                'allowed_org_id': madre['id']
            }
        ]
    }

    guyuser = itop.schema('UserLocal').insert(user)

def checkItopUser(name, organization):

    '''
    Fazer busca se existe usuário ativo no ITOP\n
    params:
        @name - Nome completo da pessoa para criar o acesso
    '''

    org = itop.schema('Organization').find({'name': organization})
    user = itop.schema('Person').find({'name': name})
    if type(user) == dict:
        return True
    else:
        return False

def updatePss(usuario):

    '''
    Faz a troca da senha do usuario no ITOP\n
    params:
        @usuario - Usuario para alterar senha do ITOP
    '''

    itop.schema('User').update({'login': usuario}, {'password': 'Madre19@@'}, {'status': 'enabled'})



def deleteUser(usuario):

    '''
    Deletar usuário do ITOP\n
    params:
        @usuario - Usuario para deletar do ITOP
    '''

    itop.schema('User').remove({'login': usuario})

def createItopEquip(name, organization, serial, desc, fabricante, modelo):

    '''
    Criar equipamento no ITOP\n
    params:
        @name - Nome do equipamento
        @organization - Organização
        @serial - Serial do equipamento
        @desc - Descrição para o equipamento
        @fabricante - Fabricante do equipamento
        @modelo - Modelo do equipamento
    '''
    
    fab = itop.schema('Brand').find({'name': fabricante})
    eqType = itop.schema('EquipamentType').find({'name': modelo})

    if type(fab) != dict:
        fab = itop.schema('Brand').insert({'name': fabricante})
        eqType = itop.schema('EquipamentType').insert(
                {
                    'name': modelo, 
                }
            )
    elif type(eqType) != dict:
        eqType = itop.schema('EquipamentType').insert(
                {
                    'name': modelo, 
                }
            )
    org = itop.schema('Organization').find({'name': organization})
    equip = itop.schema('Equipament').insert(
            {
                "name": name,
                "description": desc,
                "org_id": org['id'],
                "serialnumber": serial,
                "brand_id": fab['id'],
                "equipamenttype_id": eqType['id'],
                "finalclass": "Equipament",
            }
        )

def deleteItopEquip(name):
    itop.schema('Equipament').remove({'name': name})

def disableUser(usuario):
    itop.schema('User').update({'login': usuario}, {'status': 'disabled'})

