from pyad import *
import datetime
import ItopAutomacao
import connection
from rmConnection import *

config = {
    'AgenciaTransfusional': {
        'OU': 'OU=Users,OU=Agencia Transfusional,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['AgenciaTransfusional', 'enf_age_tra_web'],
        'ITOP': 'AGENCIA TRANSFUSIONAL'
        },
    'Apartamento': {
        'OU': 'OU=Users,OU=Unidade Internação Apartamentos,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['enf_apa_web', 'Enfermagem Apartamento'],
        'ITOP': 'UNIDADE INTERNAÇÃO APARTAMENTOS'
    },
    'Almoxarifado': {
        'OU': 'OU=Users,OU=Almoxarifado,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['alm_web', 'Usuario Caf'],
        'ITOP': 'ALMOXARIFADO'
    },
    'Ambulatorio': {
        'OU': 'OU=Ambulatorio,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['aten_amb_web', 'Usuario Recepção Ambulatorio'],
        'ITOP': 'AMBULATORIO'
    },
    'Auditoria': {
        'OU': 'OU=Users,OU=Auditoria Contas Medicas,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['aud_web', 'Usuario Auditoria'],
        'ITOP': 'AUDITORIA CONTAS MEDICAS'
    },
    'Bercario': {
        'OU': 'OU=Users,OU=Bercario,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['enf_ber_web', 'Enfermagem Berçário'],
        'ITOP': 'BERCARIO'
    },
    'Callcenter': {
        'OU': 'OU=Users,OU=CallCenter,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['callcenter'],
        'ITOP': 'CALLCENTER'
    },
    'CCIH': {
        'OU': 'OU=Users,OU=CCIH/Educação Continuada,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['enf_scih_web', 'Enfermagem CCIH'],
        'ITOP': 'CCIH/EDUCAÇÃO CONTINUADA'
    },
    'CentroCirurgico': {
        'OU': 'OU=Users,OU=Centro Cirurgico,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['enf_cc_web', 'Enfermagem CC'],
        'ITOP': 'CENTRO CIRURGICO'
    },
    'Vacinas':{
        'OU': 'OU=Users,OU=Clinica de Vacinas,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['ClinicaVacina', 'cli_vac_web'],
        'ITOP': 'CLINICA DE VACINAS'
    },
    'CME': {
        'OU': 'OU=Users,OU=CME - Central Mat. Esterilizado,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['Enfermagem CME', 'enf_cme_web'],
        'ITOP': 'CME - CENTRAL MAT. ESTERILIZADO'
    },
    'Comercial': {
        'OU': 'OU=Users,OU=Comercial,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['Comercial', 'com_web'],
        'ITOP': 'COMERCIAL'
    },
    'Compras': {
        'OU': 'OU=Users,OU=Compras/Suprimentos,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['Compras', 'sup_web', 'Usuarios Suprimentos'],
        'ITOP': 'COMPRAS/SUPRIMENTOS'
    },
    'Contabilidade': {
        'OU': 'OU=Users,OU=Contabilidade,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['cont_web','Contabilidade'],
        'ITOP': 'CONTABILIDADE'
    },
    'Controladoria': {
        'OU': 'OU=Users,OU=Controladoria,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['contr_web'],
        'ITOP': 'CONTROLADORIA'
    },
    'CoordenacaoHotelaria': {
        'OU': 'OU=Users,OU=Coordenação Hotelaria,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['hot_web','Coordenador de Hotelaria'],
        'ITOP': 'COORDENAÇÃO HOTELARIA'
    },
    'EnfermagemEndoscopia': {
        'OU': 'OU=Users,OU=Enfermagem Endoscopia,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['enf_end_web','Endoscopia'],
        'ITOP': 'ENFERMAGEM ENDOSCOPIA'
    },
    'ProntoAtendimento': {
        'OU': 'OU=Users,OU=Enfermagem PA,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['ProntoSocorro','Enfermagem PA', 'enf_pa_web'],
        'ITOP': 'ENFERMAGEM PRONTO ATENDIMENTO'
    },
    'EnfermagemImacor': {
        'OU': 'OU=Users,OU=Enfermagem/IMACOR,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['Enfermagem Imacor','enf_ima_web'],
        'ITOP': 'ENFERMAGEM IMACOR'
    },
    'EnfermagemImagem': {
        'OU': 'OU=Users,OU=Enfermagem/IMAGEM,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['Enfermagem Imagem','enf_img_web'],
        'ITOP': 'ENFERMAGEM IMAGEM'
    },
    'FarmaciaCentral': {
        'OU': 'OU=Users,OU=Farmacia Central,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['Usuario Farmacia','far_cen_web'],
        'ITOP': 'FARMACIA CENTRAL'
    },
    'FarmaciaCentroCirurgico': {
        'OU': 'OU=Users,OU=Farmacia Satelite Centro Cirurgico,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['Usuario Farmacia CC','far_cc_web'],
        'ITOP': 'FARMACIA SATELITE CENTRO CIRURGICO'
    },
    'Portarias': {
        'OU': 'OU=Portarias,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['Assistencia Portaria', 'Usuarios Portaria', 'por_web'],
        'ITOP': 'SESMT'
    },
    'SND': {
        'OU': 'OU=Users,OU=SND - Serviço de Nutrição e Dietetica,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['snd_web', 'SND'],
        'ITOP': 'SND - SERVIÇO DE NUTRIÇÃO E DIETETICA'
    },
    'Enfermaria': {
        'OU': 'OU=Users,OU=Unidade Internação Enfermaria,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['enf_enf_web', 'Enfermagem Enfermaria'],
        'ITOP': 'UNIDADE INTERNAÇÃO ENFERMARIA'
    },
    'UTINeo': {
        'OU': 'OU=Users,OU=UTI Neonatal,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['enf_neo_web', 'Enfermagem UTINEO'],
        'ITOP': 'UTI NEONATAL'
    },
    'OPME': {
        'OU': 'OU=Users,OU=OPME,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['opm_web', 'Usuarios OPME'],
        'ITOP': 'OPME'
    },
    'UCE': {
        'OU': 'OU=Users,OU=UCE - Unidade Cuidades Especiais,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['Enfermagem UCE', 'enf_uce_web'],
        'ITOP': 'UCE - UNIDADE DE CUIDADOS ESPECIAIS'
    },
    'UCO': {
        'OU': 'OU=Users,OU=UCO - Unidade Coronariana,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['Usuarios Enf Coronariana', 'enf_cor_web'],
        'ITOP': 'UCO - UNIDADE CORONARIANA'
    },
    'UTIAdulto': {
        'OU': 'OU=Users,OU=UTI Adulto,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['enf_uti_web', 'Usuarios Enf Uti Geral'],
        'ITOP': 'UTI ADULTO'
    },
    'Faturamento': {
        'OU': 'OU=Users,OU=Faturamento,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['Usuario Faturamento', 'Simpro', 'fat_web'],
        'ITOP': 'FATURAMENTO'
    },
    'Engenharia': {
        'OU': 'OU=Users,OU=Engenharia Clinica,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['eng_cli_web', 'Tecnico Eletronico'],
        'ITOP': 'ENGENHARIA CLINICA'
    },
    'Higienizacao': {
        'OU': 'OU=Users,OU=Higiene e Limpeza,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['Supervisor Higienização'],
        'ITOP': 'HIGIENIZACAO'
    },
    'Fisioterapia': {
        'OU': 'OU=Users,OU=Fisioterapia,OU=Departamentos,OU=Sociedade Hospitalar de Uberlandia,DC=madre,DC=com,DC=br',
        'grupos': ['fis_web', 'Fisioterapia'],
        'ITOP': 'FISIOTERAPIA'
    }
}

tt = datetime.datetime.now()
log = open('\\\\192.168.0.5\\Scanner\\Tecnologia\\Automacao\\log.txt', 'a+')
log.write('Feita conexão na data '+datetime.datetime.strftime(tt, '%d/%m/%Y %H:%M:%S')+'\n')

def setMemberInGroup(user, sector):
    '''
    Adicionar usuários em um grupo\n
    params:
        @user - Usuário Ex: pyad.from_cn("Raphael Miranda Rezende")
        @sector - grupo único ou lista de grupos
    '''
    for groups in config[sector]['grupos']:
        group = pyad.adgroup.ADGroup.from_cn(groups)
        group.add_members([pyad.from_cn(user)]) #adicionar membro em grupo existente

def createUser():
    '''
    Criar usuário novo no Active Directory\n
    params:
        @name - Nome completo do Usuário
        @sector - OU para criação do usuário
        @user - Usuário para fazer login
    '''
    print(name, user, sector)
    ou = pyad.adcontainer.ADContainer.from_dn(config[sector]['OU'])
    pyad.aduser.ADUser.create(name, ou, password="Madre19@@") #Criar usuário no Active Directory
    pyad.from_cn(name).update_attribute('sAMAccountName', user)
    mail = user+'@madre.com.br'
    pyad.from_cn(name).update_attribute('userPrincipalName', mail)
    setMemberInGroup(name, sector) #Setar usuários no grupo
    ItopAutomacao.createItopUser(name, user, config[sector]['ITOP']) #Criar usuário no ITOP
    #log.write(f'Usuário {name} criado ás '+datetime.datetime.strftime(tt, '%d/%m/%Y %H:%M:%S')+'\n')

def checkIfUserExists(name):
    '''
    Checar se tem usuário existente no Active Directory\n
    params:
        @name - Nome completo para a busca
    return: bool
    '''
    if pyad.from_cn(name) == None:
        return print(False)
    else:
        return print(True)
    #print(pyad.aduser.ADUser.from_cn(name).get_attribute('sAMAccountName')[0])

def deleteUser(name):
    '''
    Deletar usuário no Active Directory\n
    params:
        @name - Nome completo do usuário
    '''
    user = pyad.aduser.ADUser.from_cn(name).get_attribute('sAMAccountName')
    print(user)
    pyad.aduser.ADUser.from_cn(name).delete()
    ItopAutomacao.disableUser(user[0])
    #log.write(f'Usuário {name} deletado ás '+datetime.datetime.strftime(tt, '%d/%m/%Y %H:%M:%S')+'\n')

def lastPasswordChanged(name):
    '''
    Verificar última vez que foi alterada a senha do usuário\n
    params:
        @name - Nome completo do usuário
    '''
    pss = pyad.aduser.ADUser.from_cn(name).get_password_last_set()
    return pss

def forcePasswordChange(name):
    '''
    Verificar última vez que foi alterada a senha do usuário\n
    params:
        @name - Nome completo do usuário
    '''
    pyad.aduser.ADUser.from_cn(name).force_pwd_change_on_login()

def setPasswordExpiration(name, day):
    '''
    Verificar última vez que foi alterada a senha do usuário\n
    params:
        @name - Nome completo do usuário
    '''
    pyad.aduser.ADUser.from_cn(name).set_expiration(day)

def setPassword(name):
    '''
    Verificar última vez que foi alterada a senha do usuário\n
    params:
        @name - Nome completo do usuário
    '''
    pyad.aduser.ADUser.from_cn(name).set_password('Madre19@@')
    user = pyad.aduser.ADUser.from_cn(name).get_attribute('sAMAccountName')
    ItopAutomacao.updatePss(user)

def createUsersFromFile():
    '''
    Criar vários usuários a partir de um arquivo\n
    '''
    fTeste = '\\\\192.168.0.5\\Scanner\\Tecnologia\\Automacao\\Criar_Users.txt'
    with open(fTeste, 'r') as reader:
        readLines = reader.readlines()
        for lines in readLines:
            lines = lines.split(',')
            lines[2] = lines[2].replace('\n','')
            #print(lines[0], lines[1], lines[2])
            createUser(lines[0], lines[1], lines[2])

def deleteUsersFromFile():
    '''
    Deletar vários usuários a partir de um arquivo\n
    '''
    fTeste = '\\\\192.168.0.5\\Scanner\\Tecnologia\\Automacao\\Deletar_Users.txt'
    with open(fTeste, 'r') as reader:
        readLines = reader.readlines()
        for lines in readLines:
            lines = lines.split(',')
            lines[0] = lines[0].replace('\n','')
            #print(lines[0], lines[1], lines[2])
            deleteUser(lines[0], lines[1])

def enableUser(name):
    '''
    Habilitar usuário
    param:
        name - Nome do usuário no Active Directory 
    '''
    pyad.from_cn(name).enable()
    setPassword(name)

def userDeBusca(name):
    '''
    param:
        name - 
    '''
    print(pyad.from_cn(name))


'''rm = rmConnection(user='gabriela.ribeiro').getAllSchema()
createUser(rm[1], rm[0], 'Fisioterapia')'''



'''

q = pyad.adquery.ADQuery()
q.execute_query(attributes = ["distinguishedName", "description"], where_clause = "objectClass = '*'")
for row in q.get_results():
    print(row['description'])

'''

