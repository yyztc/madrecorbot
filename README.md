## Madrecorbot ##

 - Bot para criação de usuários

# Cria/altera/deleta usuários no Active Directory e ITOP (Sistema de chamados)
  * Faz verificação no banco de dados do RM (TOTVS erp), para consultar o usuário que foi criado. (Necessário pois o usuário é criado por outra equipe e para deixar padronizado).
  * Busca no setor que foi informado para verificar os grupos no Active Diretory e atribuir para o novo usuário.
  * Envia e-mail assim que é criado o usuário.
  * Cria assinatura de e-mail.

# Necessário 02 máquinas.
  * Caso queira deixar em apenas 01 máquina apenas seguir os passos abaixo, porém pode acabar consumindo muito processo.

- Executar ADServer em uma máquina com o Active Directory instalado (https://www.technipages.com/windows-install-active-directory-users-and-computers) ou executar no servidor.
- Executar connection na máquina local para inserir usuários no banco de dados.

# Exemplo de dado a ser passado.

* No arquivo connection.py é necessário passar 02 argumentos para criar o usuário.
  * Raphael Miranda Rezende, TI
  * Teste de Automacao, CCIH
 
# A fazer
 * Criar match dos setores - Ex: TI = tecnologia = ti
 *                               CCIH = ccih = educacao
 
 * Criar usuários no RM
 * Criar e-mail no outlook
