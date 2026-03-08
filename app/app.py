import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# 1. Configuration de la page Web
st.set_page_config(page_title="Uber Insights AI", page_icon="🚖", layout="centered")
st.title("🚖 Uber Sentiment AI")
st.markdown("Posez vos questions à l'IA basée sur l'analyse de **12 000 avis clients**.")

# 2. Chargement du "Cerveau" en cache 
# (@st.cache_resource évite de recharger la base de données à chaque message)
@st.cache_resource
def load_rag_system():
    load_dotenv()
    # On pointe vers le dossier où tu as sauvegardé la base de données (Ajuste le chemin si besoin)
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(persist_directory="../db_uber", embedding_function=embeddings)
    
    llm = ChatOpenAI(model_name="gpt-5.2", temperature=0)
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 5})
    )
    return qa_chain

qa_chain = load_rag_system()

# 3. Gestion de l'historique de la conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Bonjour CEO ! Que souhaitez-vous savoir sur les retours de nos utilisateurs aujourd'hui ?"}
    ]

# 4. Affichage des anciens messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. La barre de saisie pour l'utilisateur
if user_query := st.chat_input("Ex: Quels sont les problèmes de facturation à Paris ?"):
    
    # Afficher la question de l'utilisateur
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Faire réfléchir l'IA (avec un petit spinner d'attente)
    with st.chat_message("assistant"):
        with st.spinner("Analyse des 12 000 avis en cours..."):
            try:
                # Appel au système RAG
                response = qa_chain.invoke({"query": user_query})
                ai_answer = response['result']
                
                # Affichage de la réponse
                st.markdown(ai_answer)
                
                # Sauvegarde dans l'historique
                st.session_state.messages.append({"role": "assistant", "content": ai_answer})
            except Exception as e:
                st.error(f"Une erreur s'est produite : {e}")
