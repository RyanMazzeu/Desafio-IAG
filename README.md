# PROJETO TECHLAB AGENTES

## Descrição

Este README documenta o projeto TechLab Agentes, desenvolvido para criar um agente conversacional que facilite a integração de novos funcionários na Tech4ai. O projeto foi realizado durante o período de 25/06 a 07/07, com apresentações nos dias 10 e 11 de julho.


## Índice

* [Descrição](#descrição)
* [Funcionalidades](#funcionalidades)
* [Demonstração](#demonstração)
* [Instalação e Uso](#instalação-e-uso)
* [Licença](#licença)
* [Contato](#contato)

## Funcionalidades

* Respostas a perguntas frequentes: O agente responde a perguntas comuns sobre a empresa, como missão, visão, valores, cultura, programas internos, políticas de trabalho remoto e horários.
* Tutoriais sobre ferramentas internas: O agente fornece tutoriais detalhados sobre como usar as ferramentas internas da empresa, como Github, Vscode, Jira e Discord.
* Agendamento de reuniões: O agente se integra com sistemas de calendário, como Google Calendar, para agendar reuniões automaticamente.


## Demonstração
O projeto consiste em um chat-bot que simula um funcionário da empresa Tech4humans, portanto eu não me preocupei tanto com o visual (utilizei apenas a interface padrão fornecida pela biblioteca streamlit)

![image](https://github.com/RyanMazzeu/Desafio-IAG/assets/104333277/9a5f8464-b6fd-49ac-8f16-4d914caf7ef2)
OBS: Não me preocupei em deixar o bot online. Portanto, esse tutorial apenas sobe o bot com um URL Local (roda apenas no próprio pc) e um Network URL (roda em todos os dispositivos conectados na mesma rede)

Exemplos de cada funcionalidade:

Mensagens adversas que fogem do escopo do bot:
![image](https://github.com/RyanMazzeu/Desafio-IAG/assets/104333277/dc5b4059-ce42-4b47-8108-0306550b9a2f)
![image](https://github.com/RyanMazzeu/Desafio-IAG/assets/104333277/30d3cf74-8bc7-4bfb-8062-19b427888f7c)

Perguntas sobre a empresa (PDF):
![image](https://github.com/RyanMazzeu/Desafio-IAG/assets/104333277/ae886f63-fa34-47f3-ba3d-36bec69cb390)
![image](https://github.com/RyanMazzeu/Desafio-IAG/assets/104333277/2bc5fd11-2a69-4c1d-bcfb-b99d0700a31d)
![image](https://github.com/RyanMazzeu/Desafio-IAG/assets/104333277/31ed7cee-b524-4e45-a97e-00606030fdb4)

Tutoriais sobre ferramentas internas (A partir de acesso à internet):
![image](https://github.com/RyanMazzeu/Desafio-IAG/assets/104333277/b308d98d-b041-4530-bc86-3aea3062634c)
![image](https://github.com/RyanMazzeu/Desafio-IAG/assets/104333277/00aaf75c-b19c-4407-bc6e-39b777672aa9)

Agendamento de reuniões
![image](https://github.com/RyanMazzeu/Desafio-IAG/assets/104333277/ffe8dec8-a576-43e3-b3d6-08c6476dcece)
![image](https://github.com/RyanMazzeu/Desafio-IAG/assets/104333277/de09ab7c-5018-405b-811a-1b446c36d03a)
![image](https://github.com/RyanMazzeu/Desafio-IAG/assets/104333277/80b1f3d2-cd51-4309-9fad-f58f404bb413)
![image](https://github.com/RyanMazzeu/Desafio-IAG/assets/104333277/e8063e7b-44dc-4220-b97f-5d6bdea2f77a)


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

    pip install streamlit python-dotenv google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pymupdf huggingface_hub groq langchain langchain_community streamlit transformers

### Configuração de Variáveis de Ambiente

#### Criar um Arquivo '.env'
Crie um arquivo chamado .env na raiz do seu projeto com as seguintes chaves (será ensinado em seguida como requisitá-las):

    GROQ_API_KEY = "SUA CHAVE GROQ"
    GOOGLE_API_KEY=SUA CHAVE DE API DA GOOGLE
    GOOGLE_CSE_ID=SUA CHAVE DA FERRAMENTA DE BUSCA GOOGLE
    HUGGINGFACEHUB_API_TOKEN=SEU TOKEN DE API DO HUGGINGFACE

Como consegui-las:

* https://console.groq.com/keys
* https://console.cloud.google.com/apis/credentials
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

![image](https://github.com/RyanMazzeu/Desafio-IAG/assets/104333277/4b294eb8-ef1c-43fc-9058-2171f1b47568)


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

* O bot não é perfeito! Devido a data e prazo estabelecidos, que coincidiram com o final de semestre na faculdade, não tive muito tempo para ficar aperfeiçoando os prompts.
* As respostas sobre a empresa são fracas, pois o documento pdf divulgado também é. Por isso acrescentei algumas informações da internet no próprio prompt.

## Erros/Defeitos encontrados

* Dependendo de como a pergunta sobre a empresa é feita a ia responde aleatóriamente!
* O agendamento, se mal explicado na requisição, dá erro!
* As pesquisas de tutoriais na internet não estão nem perto de serem perfeitas, uma vez que dependendo do que o bot retorna, a ia não consegue extrair informações o suficiente para formar uma resposta descente.
  
