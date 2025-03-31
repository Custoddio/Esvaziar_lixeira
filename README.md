Gerenciador de Login com Automação 🖥️✨


Bem-vindo ao Gerenciador de Login com Automação! 😎 Este repositório contém um script Python simples que utiliza as bibliotecas PySimpleGUI e pyautogui para criar uma interface gráfica que simula um processo de login. Após a autenticação bem-sucedida, o script realiza ações automatizadas no sistema, como esvaziar a lixeira do Windows 🗑️.


Funcionalidades 🎯
Interface gráfica de login com campos para nome de usuário e senha. 👨‍💻

Validação de login com credenciais fixas:

Usuário: admin

Senha: 0123

Após o login bem-sucedido, o script realiza as seguintes automações:

Exibe alertas de confirmação 💬.

Busca e clica na "Lixeira" do Windows 🧹.

Seleciona todos os itens na lixeira e os deleta ⚡.

Exibe alertas de sucesso após a exclusão da lixeira 🎉.

Tecnologias Utilizadas 🚀
PySimpleGUI: Biblioteca para criar interfaces gráficas simples e intuitivas. 🖥️

pyautogui: Biblioteca para automação de interações com a interface gráfica do sistema (como cliques, digitação e teclas de atalho). ⌨️

time: Biblioteca para gerenciar intervalos de tempo entre ações no script ⏳.

Como Usar 📋
1. Instalação 🛠️
Primeiro, certifique-se de ter o Python 3.x instalado em sua máquina. Para instalar as dependências necessárias, execute o seguinte comando no terminal:

bash
Copiar
pip install PySimpleGUI pyautogui
2. Executando o Script 🎬
Após instalar as dependências, basta executar o script Python no seu ambiente local:

bash
Copiar
python gerenciador_login.py
3. Passos para Uso 🏃‍♂️
Abra o aplicativo: Uma interface gráfica aparecerá pedindo para você fazer o login.

Insira as credenciais:

Usuário: admin

Senha: 0123

Clique em "Entrar": Se as credenciais estiverem corretas, o script realizará as automações para você. 🎉

4. Explicação das Ações de Automação 🧠
Após o login bem-sucedido, o script vai:

Exibir um alerta com o texto: "Clique em OK para começarmos!" 📲

Clicar na lixeira do sistema (localizada nas coordenadas (641, 442) da tela). 🖱️

Escrever "lixeira" na busca do sistema e pressionar Enter ⌨️.

Selecionar todos os itens da lixeira usando o atalho de teclado Ctrl + A. 🗂️

Exibir um alerta dizendo que a lixeira será esvaziada em 30 segundos. ⏳

Deletar os itens da lixeira e pressionar Enter para confirmar a exclusão. 🔥

Exibir um alerta final indicando que a lixeira foi esvaziada com sucesso! 🎉

5. Segurança 🔒
Este script usa credenciais fixas e simples ("admin" e "0123") para fins de demonstração. Não é recomendado utilizar este código em ambientes de produção ou com dados sensíveis. Use-o apenas para fins de aprendizado e automação de tarefas simples. 😉



Exemplo de Execução 🎥
Inicie o aplicativo.

Preencha os campos de login com o nome de usuário admin e a senha 0123.

Clique em "Entrar": Se tudo estiver certo, o script vai automaticamente esvaziar a lixeira para você!
