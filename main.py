import streamlit as st
from spellchecker import SpellChecker


def corrigir_ortografia(texto):
    """
    Corrige a ortografia do texto fornecido.
    """
    spell = SpellChecker(language='pt')  # Define o idioma para português
    linhas = texto.splitlines()

    linhas_corrigidas = []
    for linha in linhas:
        palavras = linha.split()
        palavras_corrigidas = [spell.correction(palavra) for palavra in palavras]
        linhas_corrigidas.append(" ".join(palavras_corrigidas))

    return "\n".join(linhas_corrigidas)


def converter_maiusculo(texto):
    """
    Converte o texto fornecido para letras maiúsculas.
    """
    linhas = texto.splitlines()
    return "\n".join([linha.upper() for linha in linhas if linha.strip()])


def corrigir_e_converter(texto):
    """
    Corrige a ortografia e converte o texto para letras maiúsculas.
    """
    texto_corrigido = corrigir_ortografia(texto)
    return converter_maiusculo(texto_corrigido)


# Configuração da interface Streamlit
st.title("Conversor de Texto com Correção Ortográfica")

entrada_usuario = st.text_area("Insira o texto ou palavra")

col1, col2, col3 = st.columns(3)

if col1.button("Corrigir e Converter"):
    if entrada_usuario:
        texto_convertido = corrigir_e_converter(entrada_usuario)
        st.text_area("Texto Convertido:", value=texto_convertido, height=300)
    else:
        st.warning("Por favor, insira algum texto na caixa acima.")

if col2.button("Corrigir Ortografia"):
    if entrada_usuario:
        texto_corrigido = corrigir_ortografia(entrada_usuario)
        st.text_area("Texto Corrigido:", value=texto_corrigido, height=300)
    else:
        st.warning("Por favor, insira algum texto na caixa acima.")

if col3.button("Converter para Maiúsculas"):
    if entrada_usuario:
        texto_maiusculo = converter_maiusculo(entrada_usuario)
        st.text_area("Texto em Maiúsculas:", value=texto_maiusculo, height=300)
    else:
        st.warning("Por favor, insira algum texto na caixa acima.")
