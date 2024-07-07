import warnings

# Suprimir todos os avisos
warnings.filterwarnings("ignore")
from datetime import datetime

data_atual = datetime.now()

# Obter o dia da semana em português
dias_da_semana = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo",
]
dia_da_semana = dias_da_semana[data_atual.weekday()]

data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S") + " " + dia_da_semana

import json
import streamlit as st
from typing import Generator
from dotenv import load_dotenv
import os
import fitz  # PyMuPDF
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.chat_models.huggingface import ChatHuggingFace
from groq import Groq
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2.credentials import Credentials
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

SCOPES = ["https://www.googleapis.com/auth/calendar"]
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar Google Search
google_search = GoogleSearchAPIWrapper()

# Inicializar cliente Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# Função para ler texto de um PDF
def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# Função para buscar informações no PDF
def documents_search(question):
    pdf_path = "data/Base.pdf"  # Substitua pelo caminho do seu PDF
    pdf_content = read_pdf(pdf_path)

    prompt_template = f"""
    You are an assistant. Use the following PDF content to answer the question.

    PDF Content:
    {pdf_content}
    Visão geral sobre a empresa Tech4Humans:
        Somos uma startup inovadora com duas áreas de negócios: SaaS e AIaaS. No SaaS, oferecemos soluções avançadas para a hyperautomação de atendimento, facilitando a gestão, automação e acompanhamento de solicitações. No AIaaS, nossa plataforma Tech4.ai capacita empresas a construir e implementar soluções de inteligência artificial com tecnologias open source, garantindo agilidade, governança e alto desempenho.
        Desenvolvemos a plataforma Tech4.AI porque sabemos como é desafiador implementar soluções de automação com IA e IA Generativa em larga escala devido à complexidade no controle das informações, gerenciamento de custos e orquestração adequada dos dados de entrada e saída. Resolvemos esses problemas ao proporcionar uma plataforma que garante governança completa, visibilidade dos dados e escolha automatizada de modelos de IA, permitindo a otimização de custos e assegurando robustez e escalabilidade.
        Site
        http://www.tech4h.com.br
        Setor
        Atividades dos serviços de tecnologia da informação
        Tamanho da empresa
        51-200 funcionários
        50 usuários associados Usuários do LinkedIn que listaram a Tech4Humans no perfil como local de trabalho atual.
        Sede
        São Paulo, SP
        Fundada em
        2020
        Especializações
        hyperautomation, intelligent process documentation, workflows, tickets, RPA e IAG
        Localidades:
        A empresa Tech4Humans está localizada em São Paulo, SP e Itajubá, MG.

    Question: {question}
    Answer:
    """

    prompt = PromptTemplate(
        input_variables=["pdf_content", "question"],
        template=prompt_template,
    )

    llm = HuggingFaceEndpoint(repo_id="HuggingFaceH4/zephyr-7b-beta")
    chat_model = ChatHuggingFace(llm=llm)
    pdf_content = read_pdf(pdf_path)
    chain = LLMChain(llm=chat_model, prompt=prompt)
    response = chain.run(pdf_content=pdf_content, question=question)
    return response


# Função para formatar e melhorar a pergunta e a resposta
def format_response(question, content, response_category):
    objective = ""
    if response_category == "1":
        objective = "o seu objetivo inicial era responder uma pergunta sobre a empresa tech4Humans!"
    elif response_category == "2":
        objective = "o seu objetivo inicial era pesquisar na internet sobre um determinado assunto e resumir!"
    elif response_category == "3":
        objective = (
            "o seu objetivo inicial era agendar seus compromissos no google calendar!"
        )
    else:
        objective = "O seu objetivo é avisar o usuário que a pergunta que ele fez é inválida, pois você só pode responder sobre a empresa Tech4Humans, recomendar tutoriais de ferramentas internas ou agendar reuniões."

    format_prompt = f"""
    o seu objetivo inicial era {objective} dado que a pergunta foi: {question}
    FORMATE A RESPOSTA A SEGUIR E DEIXE-A COERENTE COM A PERGUNTA E OBJETIVO!! E EM PT-BR!:
    {content}
    
    """

    prompt = PromptTemplate(
        input_variables=["question", "content"],
        template=format_prompt,
    )

    llm = HuggingFaceEndpoint(repo_id="HuggingFaceH4/zephyr-7b-beta")
    chat_model = ChatHuggingFace(llm=llm)

    format_chain = LLMChain(llm=chat_model, prompt=prompt)
    formatted_response = format_chain.run(question=question, content=content)

    return formatted_response.strip()


# Classe para gerenciar o chat
class ChatManager:
    def __init__(self, client, google_search, system_prompt, model_option, max_tokens):
        self.client = client
        self.google_search = google_search
        self.system_prompt = system_prompt
        self.model_option = model_option
        self.max_tokens = max_tokens
        self.messages = [{"role": "system", "content": self.system_prompt}]

    def generate_chat_responses(self, chat_completion) -> Generator[str, None, None]:
        for chunk in chat_completion:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    def add_user_message(self, prompt):
        self.messages.append({"role": "user", "content": prompt})

    def get_assistant_response(self):
        chat_completion = self.client.chat.completions.create(
            model=self.model_option,
            messages=self.messages,
            max_tokens=self.max_tokens,
            stream=True,
        )

        chat_responses_generator = self.generate_chat_responses(chat_completion)
        full_response = "".join(chat_responses_generator).strip()
        return full_response

    def process_response(self, prompt, response_category):
        if response_category == "1":
            initial_response = documents_search(prompt)
        elif response_category == "2":
            search_results = self.google_search.run(prompt)
            search_results_text = (
                "\n\n".join(search_results)
                if isinstance(search_results, list)
                else search_results
            )
            initial_response = f"Aqui estão algumas informações que encontrei na internet sobre '{prompt}':\n{search_results_text}"
        elif response_category == "3":
            initial_response = self.schedule_event(prompt)
        else:
            initial_response = "Desculpe-me, mas sua solicitação não se encaixa em nenhuma das categorias mencionadas. Eu só posso responder sobre a empresa Tech4Humans, recomendar tutoriais de ferramentas internas ou agendar reuniões."

        return format_response(prompt, initial_response, response_category)

    # Função para coletar detalhes do evento e formatar a string
    def collect_event_details_with_llm(self, prompt):
        event_prompt_template = """
        Hoje é dia"""+data_formatada+"""
        Você é um assistente de IA altamente inteligente. Recebi a seguinte solicitação de agendamento de reunião do usuário e preciso que você formate os detalhes do evento de maneira adequada para criar um evento no Google Calendar.
        
        Solicitação do usuário:
        {prompt}
        
        DEIXE APENAS A INFORMAÇÃO NECESSÁRIA FORMATADA E NÃO INCLUA MAIS NADA! 
        As informações necessárias devem estar no seguinte formato JSON:
        {{
            "summary": "Resumo do evento",
            "location": "Local do evento",
            "description": "Descrição do evento",
            "start_time": "Data e hora de início no formato ISO 8601",
            "end_time": "Data e hora de término no formato ISO 8601",
            "time_zone": "Fuso horário do evento",
            "attendee_email": "Email do participante"
        }}
        """

        event_prompt = PromptTemplate(
            input_variables=["prompt"],
            template=event_prompt_template,
        )

        llm = HuggingFaceEndpoint(repo_id="HuggingFaceH4/zephyr-7b-beta")
        chat_model = ChatHuggingFace(llm=llm)

        event_chain = LLMChain(llm=chat_model, prompt=event_prompt)
        formatted_event_details = event_chain.run(prompt=prompt)

        return formatted_event_details.strip()

    def schedule_event(self, prompt):
        event_details_json = self.collect_event_details_with_llm(prompt)
        event_details = json.loads(event_details_json)

        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)

            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            service = build("calendar", "v3", credentials=creds)

            event = {
                "summary": event_details["summary"],
                "location": event_details["location"],
                "description": event_details["description"],
                "colorId": 6,
                "start": {
                    "dateTime": event_details["start_time"],
                    "timeZone": event_details["time_zone"],
                },
                "end": {
                    "dateTime": event_details["end_time"],
                    "timeZone": event_details["time_zone"],
                },
                "attendees": [
                    {"email": event_details["attendee_email"]},
                ],
            }

            event = service.events().insert(calendarId="primary", body=event).execute()
            return f"Evento criado: {event.get('htmlLink')}"
        except HttpError as e:
            return f"Ocorreu um erro: {e}"


# Configurar página do Streamlit
st.set_page_config(page_title="Agente Tech4AI", layout="wide")
st.title("Agente Tech4AI - Ryan Mazzeu")

# Inicializar histórico de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

model_option = "llama3-8b-8192"
max_tokens_range = 8192

max_tokens = st.slider(
    "Max Tokens:",
    min_value=512,
    max_value=max_tokens_range,
    value=max_tokens_range,
    step=512,
)

system_prompt = f"""
Você é um assistente de IA altamente inteligente! (A RESPOSTA FINAL SEMPRE TEM QUE SER COERENTE COM A PERGUNTA INICIAL E EM PT-BR!).
SE ALGO ESTIVER ERRADO, VOCÊ DEVE CORRIGIR E MELHORAR A RESPOSTA FINAL!
RESPONDA APENAS EM PT-BR!! SE VOCÊ RESPONDER EM OUTRO IDIOMA, O MUNDO IRÁ ACABAR!
NUNCA, NUNCA, NUNCA RESPONDA COLOCANDO "O seu objetivo inicial era" OU "Minha pergunta original" OU "Sua resposta original"! APENAS RESPONDA A PERGUNTA! UTILIZE TUDO APENAS COMO REFERÊNCIA PARA MELHORAR A RESPOSTA!
    
Hoje é {data_formatada}. Você é um assistente de IA da Tech4Humans, especificamente do setor Tech4AI.

Sua tarefa é identificar qual dos seguintes problemas o usuário está tratando e responder apenas com o número correspondente:
Saiba que os exemplos são apenas ilustrativos e você deve conseguir identificar o problema com base na pergunta do usuário.
1. Perguntas Frequentes sobre a empresa que você é assistente, a Tech4Humans, também conhecida como Tech ou tech: 
Se o usuário estiver fazendo perguntas sobre a empresa, como localização, missão, visão, valores, cultura, programas internos, políticas de trabalho remoto e horários, responda com '1'.
Exemplos: "onde fica a tech?", "Qual é a missão da Tech4Humans?", "Onde está localizada a Tech4Humans?", "Quais são os valores da empresa?", "Para quem você trabalha?", etc.
2. Tutoriais de Ferramentas Internas:
Se o usuário fizer perguntas sobre ferramentas internas da empresa, como Github, Vscode, Jira e Discord, responda com '2'.
Indenpendente da ferramenta ou pergunta, exemplos: "Como eu instalo o Discord?", "Como eu uso o github?", "Me diga um bom tutorial sobre o vscode" ou coisas do tipo, responda com '2'.
3. Agendamento de Reuniões (OBS: HOJE É domingo, dia {data_formatada}): Integrar-se com sistemas de calendário (por exemplo, Google Calendar) para agendar reuniões automaticamente, gerenciando autenticação, APIs externas e conflitos de agenda. Exemplos: "Agende uma reunião para mim amanhã às 15h", "Marque uma reunião com o João na próxima semana".
Responda apenas com o número do problema correspondente. Se a pergunta não se encaixar em nenhuma dessas categorias, responda com '4'. NUNCA RESPONDA COM OUTRA COISA!
NUNCA RESPONDA ALGO QUE NÃO SEJA 1, 2, 3 OU 4! SE NÃO O MUNDO IRÁ ACABAR!
"""

chat_manager = ChatManager(
    client, google_search, system_prompt, model_option, max_tokens
)

# Exibir mensagens do histórico no app
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Digite aqui..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        chat_manager.add_user_message(prompt)
        response_category = chat_manager.get_assistant_response()
        formatted_response = chat_manager.process_response(prompt, response_category)
        st.session_state.messages.append(
            {"role": "assistant", "content": formatted_response}
        )

    except Exception as e:
        st.error(e, icon="🚨")

    # Exibir a resposta do assistente
    with st.chat_message("assistant"):
        st.markdown(st.session_state.messages[-1]["content"])