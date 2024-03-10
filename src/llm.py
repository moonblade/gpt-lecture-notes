from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain_openai import ChatOpenAI


from src.constants import CREATE_NOTE_PROMPT
from src.utils import getNotes, getTranscription

def getText(aiMessage):
    return aiMessage.content

def getLLM(temperature=0.1):
    with open("secrets/openai-apikey", "r") as f:
        openai_api_key = f.read().strip()
    with open("secrets/openai-orgId", "r") as f:
        openai_orgId = f.read().strip()
    return ChatOpenAI(openai_api_key=openai_api_key,
            openai_organization=openai_orgId,
            temperature=temperature,
            model="gpt-3.5-turbo")

def createNotes(fileName):
    prompt = ChatPromptTemplate.from_messages([
        ("system", CREATE_NOTE_PROMPT),
        ("user", "{lecture_transcription}")
    ])
    transcriptionFile = getTranscription(fileName)
    with open(transcriptionFile, "r") as f:
        transcriptionContent = f.read().strip()

    chain = prompt | getLLM() | getText
    notes = chain.invoke({"lecture_transcription": transcriptionContent})
    notesFile = getNotes(fileName)
    with open(notesFile, "w") as f:
        f.write(notes)



