import streamlit as st
import requests
from deep_translator import PonsTranslator


st.set_page_config(page_title="Celebridades", page_icon="🌟")
st.title("🌟 Buscador de Celebridades 🌟")

nome = st.text_input("Digite o nome de uma celebridade:")



if st.button("Buscar"):
    if nome:
        url = f"https://api.api-ninjas.com/v1/celebrity?name={nome}"
        headers = {"X-Api-Key": st.secrets["api_key"]} 

        resposta = requests.get(url, headers=headers)

        if resposta.status_code == 200:
            dados = resposta.json()
            if dados:
                celebridade = dados[0]
                st.subheader("Resultado:")
                st.write(f"**Nome:** {celebridade.get('name', 'Desconhecido')}")
                st.write(f"**Idade:** {celebridade.get('age', 'Desconhecida')}")
                ocupacoes = celebridade.get('occupation', [])
                if ocupacoes:
                    st.write("**Ocupações:**")
                   
                    for ocupacao in ocupacoes:
                        try:
                            traducao = PonsTranslator(source="english",target="portuguese").translate(ocupacao)
                            st.write(f"- {traducao}")
                        except:
                            pass
                else:
                    st.write("**Ocupações:** Não encontradas")
            else:
                st.warning("Nenhuma celebridade encontrada.")
        else:
            st.error("Erro ao acessar a API.")
    else:
        st.warning("Digite um nome para buscar.")
