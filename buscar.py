import streamlit as st
import re
import os
import time
from google import genai
from google.genai.errors import APIError

# =========================================================================
# CONFIGURAÇÃO E FUNÇÕES DA API (IA)
# =========================================================================

def configurar_api():
    """
    Configura a chave da API Gemini.
    A chave deve ser definida como um 'Secret' no Streamlit Cloud.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        st.error(
            "🚨 ERRO DE CONFIGURAÇÃO: A chave 'GEMINI_API_KEY' não foi encontrada. "
            "Por favor, configure-a nos Streamlit Secrets para usar a função de IA."
        )
        return None
    try:
        return genai.Client(api_key=api_key)
    except Exception as e:
        st.error(f"Erro ao inicializar o cliente Gemini: {e}")
        return None


def gerar_explicacao_ia(client, artigo_completo):
    """
    Chama a API Gemini para gerar uma explicação simplificada do artigo.
    O 'system_prompt' foi incorporado ao 'user_prompt' para contornar o erro de SDK.
    """
    # System Instruction incorporada ao prompt para garantir a compatibilidade com o SDK
    system_instruction = (
        "INSTRUÇÃO DE ROLEPLAY: Você é um tutor jurídico prestativo. Sua tarefa é simplificar textos legais "
        "complexos (artigos de lei) para que sejam compreendidos por leigos. "
        "Sua resposta deve ser escrita em linguagem clara, acessível e objetiva, "
        "evitando jargões desnecessários, mantendo a fidelidade ao sentido legal."
    )
