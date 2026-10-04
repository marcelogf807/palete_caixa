import streamlit as st
from banco_dados.db import (criar_usuario, listar_tipos_status, listar_tipos_usuario)

def pagina_criar():
    st.header(":heavy_plus_sign: Criar Usuario")

    opcoes_tipos_usuarios = listar_tipos_usuario()

    with st.form("form_criar"):
        col1, col2 = st.columns(2)
        cnpj = col1.text_input("CNPJ (14 dígitos, sem pontuação)", placeholder="12345678000144")
        razao_social = col2.text_input("CNPJ (razão Social)")
        nome_fantasia = col1.text_input("Nome Fantasia)", placeholder="***")
        nome_contato = col2.text_input("Nome do contato)")
        telefone = col1.text_input("telefone", autocomplete="tel")
        email = col2.text_input("E-mail")

        st.divider()
        col1, col2 = st.columns(2)

        nome_usuario = col1.text_input("Nome de usuário")
        tipo = col2.selectbox("Tipo do Usuário", opcoes_tipos_usuarios)
        senha = col1.text_input("Senha", type="password", placeholder="Pelo menos 6 caracteres")
        Confirmar = col2.text_input("Confrmar senha", type="password")

        criar = st.form_submit_button("Criar Usuário")

    if criar:
        erros = []
        if not cnpj or len(cnpj) != 14 or not cnpj.isdigit():
            erros.append("CNPJ deve ter exatamente 14 digitos " \
                         "numéricos")

        if not razao_social:
            erros.append("Razão social é obrigatoria")

        if not nome_usuario:
            erros.append("Nome de usuário é obrigatório")

        if not senha:
            erros.append("Senha é obrigatória")
        elif len(senha) < 6:
            erros.append("Senha deve ter pelo menos 6 caracteres")
        elif senha != Confirmar:
            erros.append("Senhas não conferem")

        if erros:
            for e in erros:
                st.warning(f":warning: {e}")
                return

        dados = {
            "cnpj": cnpj,
            "razao_social": razao_social,
            "nome_fantasia": nome_fantasia,
            "nome_contato": nome_contato,
            "telefone_contato": telefone,
            "nome_usuario": nome_usuario,
            "status": "ativo",
            "tipo": tipo,
        }
        erro = criar_usuario(dados, senha)
        if erro:
            st.error(erro)
        else:
            st.success(f"Usuário **{nome_usuario}** criado com sucesso!")