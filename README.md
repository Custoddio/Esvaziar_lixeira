Gerenciador de Login e Automação
Este projeto é uma aplicação simples desenvolvida em Python que utiliza as bibliotecas PySimpleGUI e PyAutoGUI para criar uma interface gráfica de login e realizar ações automatizadas no sistema operacional, como abrir a lixeira e esvaziá-la.

Descrição
O programa apresenta uma interface gráfica onde o usuário pode inserir um nome de usuário e senha. Após o login bem-sucedido, o programa realiza as seguintes ações automaticamente:

Abre a lixeira do sistema.
Seleciona todos os itens na lixeira.
Exibe alertas para o usuário antes de esvaziar a lixeira.
Esvazia a lixeira e exibe uma mensagem de sucesso.
Pré-requisitos
Antes de executar o programa, certifique-se de que os seguintes itens estão instalados no seu ambiente:

Python 3.6 ou superior
Bibliotecas Python:
PySimpleGUI: Para criar a interface gráfica.
PyAutoGUI: Para automação de ações no sistema operacional.
Instale as bibliotecas necessárias:
Como usar
Execute o programa:

Salve o código em um arquivo chamado gerenciador.py (ou outro nome de sua escolha).
Execute o programa no terminal:
Insira as credenciais:

Nome de usuário: admin
Senha: 0123
Clique em "Entrar":

Após o login bem-sucedido, o programa iniciará as ações automatizadas.
Ações automatizadas:

O programa abrirá a lixeira, selecionará todos os itens, exibirá alertas e esvaziará a lixeira.
Fluxo do Programa
Interface Gráfica:

Criada com PySimpleGUI, a interface contém:
Campos para nome e senha.
Botões "Entrar" e "Cancelar".
Uma opção para salvar o login (não funcional no código atual).
Validação de Login:

O programa verifica se o nome de usuário e a senha inseridos correspondem aos valores pré-definidos:
Nome: admin
Senha: 0123
Automação com PyAutoGUI:

Após o login, o programa utiliza PyAutoGUI para:
Abrir o menu iniciar.
Pesquisar e abrir a lixeira.
Selecionar todos os itens na lixeira.
Exibir alertas antes de esvaziar a lixeira.
Esvaziar a lixeira.
Personalização
Credenciais:

Você pode alterar o nome de usuário e senha no trecho:
Coordenadas do mouse:

As coordenadas usadas para cliques na lixeira (x=641, y=442, etc.) podem variar dependendo da resolução e configuração do monitor. Ajuste as coordenadas conforme necessário.
Atenção
Automação:
Certifique-se de que o sistema operacional está configurado corretamente para que as ações automatizadas funcionem.
Teste o programa em um ambiente seguro antes de usá-lo em produção
