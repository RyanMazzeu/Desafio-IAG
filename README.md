# PROJETO TECHLAB AGENTES

## Descrição

Este README documenta o projeto TechLab Agentes, desenvolvido para criar um agente conversacional que facilite a integração de novos funcionários na Tech4ai. O projeto foi realizado durante o período de 25/06 a 07/07, com apresentações nos dias 10 e 11 de julho.


## Índice

* [Descrição](#descrição)
* [Funcionalidades](#funcionalidades)
* [Demonstração](#demonstração)
* [Instalação e Uso](#instalação-e-uso)
* [Contribuição](#contribuição)
* [Licença](#licença)
* [Contato](#contato)

## Funcionalidades

* Respostas a perguntas frequentes: O agente responde a perguntas comuns sobre a empresa, como missão, visão, valores, cultura, programas internos, políticas de trabalho remoto e horários.
* Tutoriais sobre ferramentas internas: O agente fornece tutoriais detalhados sobre como usar as ferramentas internas da empresa, como Github, Vscode, Jira e Discord.
* Agendamento de reuniões: O agente se integra com sistemas de calendário, como Google Calendar, para agendar reuniões automaticamente.


## Demonstração

* **Imagens:** Inclua imagens que mostrem as funcionalidades do seu projeto em ação.
* **GIFs:** Utilize GIFs para animações curtas e demonstrativas.
* **Vídeos:** Crie vídeos tutoriais ou demonstrações mais completas.

## Instalação e Uso

### Instalação de Dependências

#### Criar e Ativar Ambiente Virtual
1. Crie um ambiente virtual para isolar as dependências do projeto:
   ```bash
   python -m venv venv
2. Ative o ambiente virtual:
* No windows:
    ```bash
    venv\Scripts\activate
* No macOS/Linux:
    ```bash
    source venv/bin/activate

#### Instalar as Dependências Necessárias
Instale todas as bibliotecas e ferramentas mencionadas no código:

    pip install streamlit python-dotenv google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client langchain pymupdf huggingface_hub groq

### Configuração de Variáveis de Ambiente

#### Criar um Arquivo '.env'
Crie um arquivo chamado .env na raiz do seu projeto com as seguintes chaves (será ensinado em seguida como requisitá-las):

    GROQ_API_KEY = "SUA CHAVE GROQ"
    GOOGLE_API_KEY=SUA CHAVE DE API DA GOOGLE
    GOOGLE_CSE_ID=SUA CHAVE DA FERRAMENTA DE BUSCA GOOGLE
    HUGGINGFACEHUB_API_TOKEN=SEU TOKEN DE API DO HUGGINGFACE

Como consegui-las:

* https://console.groq.com/keys
* https://console.cloud.google.com/apis/credentials?authuser=1&project=tech4humans&supportedpurview=project
* https://programmablesearchengine.google.com/
* https://huggingface.co/settings/tokens

#### Obter Credenciais do Google Calendar

Vá para o Google Cloud Console:
* https://console.cloud.google.com/apis/api/customsearch.googleapis.com/overview?project=tech4humans

Crie um novo projeto ou selecione um projeto existente.
Habilite a API do Google Calendar.
Crie credenciais de OAuth 2.0 e baixe o arquivo credentials.json.
Coloque o arquivo credentials.json na raiz do seu projeto.

### Estrutura do Projeto

Garanta que a estrutura do seu projeto seja semelhante a esta: 

### Código Fonte
 Código!

### Executar o Projeto

Após garantir que todas as etapas anteriores foram concluídas com sucesso, execute o comando abaixo no prompt de comando dentro da pasta principal do projeto para iniciar a aplicação Streamlit:

    
    streamlit run main.py

Isso deve abrir uma nova janela no seu navegador padrão com a interface da aplicação TechLab-Agentes, onde você pode interagir com o assistente.

Caso tenha mais perguntas ou precise de assistência adicional, estou aqui para ajudar!

## Licença

* Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato:


 seu-usuario
* Email: ryanmazzeu111@gmail.com
* GitHub: https://github.com/RyanMazzeu

## Observações

* Obs 1
* Utilize linguagem clara, concisa e profissional.
* Apresente uma formatação visual atraente e organizada.
* Inclua exemplos e casos de uso para demonstrar o valor do seu projeto.
* Utilize ferramentas e recursos para facilitar a criação e atualização do README.


## Uso/Exemplos

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```


## Stack utilizada

**Front-end:** React, Redux, TailwindCSS

**Back-end:** Node, Express


## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  npm run test
```


## Outras seções comuns em perfis do GitHub
👩‍💻 Trabalho atualmente na/no...

🧠 Estou aprendendo...

👯‍♀️ Procuro colaborar em...

🤔 Procuro ajuda com...

💬 Me pergunte sobre...

📫 Como entrar em contato comigo...

😄 Pronomes...

⚡️ Fatos engraçados...


## 🚀 Sobre mim
Eu sou uma pessoa desenvolvedora full-stack...

