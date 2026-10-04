import streamlit as st
from paginas.login import pagina_login
from paginas.listar_usuarios import pagina_listar

st.set_page_config(page_title="Palete-Caixa",
                   page_icon="📦",
                   layout="centered")



if "usuario" not in st.session_state:
    st.session_state.usuario = None

print(st.session_state.usuario)

if st.session_state.usuario is None:
    pagina_login()

else:
    usuario = st.session_state.usuario
    is_admin = usuario.get("tipo") == "admin"
    with st.sidebar:
        tipo_badge = ":crown: Admin" if is_admin else \
                        ":bust_in_silhouette: Regular"
        st.markdown(f"**Olá {usuario['razao_social']}**")
        st.caption(f"Usuario'{usuario['nome_usuario']}' - {tipo_badge}")

        st.divider()
        opcoes_menu = (
            ["Modelo Palete-Caixa", "Listar Usuários",
             "Criar Usuarios", "Alterar Status", "Alterar Senha", 
             "Deletar Usuario"]
            if is_admin else ["Moddelo Palete-Caixa", "Alterar Senha"]
        )

        pagina = st.radio("Menu", opcoes_menu, index=0,
                           label_visibility="collapsed")
        st.divider()

        if st.button(":door: Sair"):
            st.session_state.usuario = None
            st.rerun()
    
    if pagina == "Listar Usuários":
       pagina_listar()

