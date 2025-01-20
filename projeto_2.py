import streamlit as st
import pandas as pd
import plotly.express as px

# Configurações da página
st.set_page_config(page_title="Bem-vindo ao Projeto", page_icon=":bar_chart:", layout="wide")

# Função para exibir a página de boas-vindas
def pagina_boas_vindas():
    st.image("https://keystoneacademic-res.cloudinary.com/image/upload/element/97/97189_thumb.png", width=200)  # Adicionando a logo

    st.title("Bem-vindo ao Projeto de Previsão de Renda!")
    
    st.markdown("""
    ## Este projeto explora o perfil financeiro de diversos clientes, permitindo análises de tendências de renda com base em múltiplas variáveis.
    Siga os passos abaixo para começar:
    1. Baixe a base de dados fornecida.
    2. Clique no botão **Iniciar**.
    3. Faça o upload da base baixada para gerar os gráficos interativos.
    """)
    
    # Botão para download da base
    with open("previsao_de_renda.csv", "rb") as file:
        st.download_button(
            label="Baixar Base de Dados",
            data=file,
            file_name="previsao_de_renda.csv",
            mime="text/csv"
        )
    
    # Botão para iniciar a análise
    if st.button("Iniciar"):
        st.session_state.pagina_inicial = False

# Função para exibir a página principal do app
def pagina_principal():
    st.title("Análise Exploratória da Previsão de Renda")

    # Upload da base pelo usuário
    uploaded_file = st.file_uploader("Faça o upload da base de dados baixada (previsao_de_renda.csv):", type=["csv"])

    if uploaded_file is not None:
        renda = pd.read_csv(uploaded_file)
        st.success("Arquivo carregado com sucesso!")
        st.write("Visualização dos primeiros registros da base:")
        st.dataframe(renda.head())

        # Layout com duas colunas
        col1, col2 = st.columns(2)

        with col1:
            with st.expander("Gráfico: Posse de Imóvel vs Renda", expanded=True):
                fig1 = px.bar(renda, x='posse_de_imovel', y='renda', title='Posse de Imóvel vs Renda',
                              color='posse_de_imovel', color_discrete_sequence=px.colors.qualitative.Prism)
                st.plotly_chart(fig1, use_container_width=True)

            with st.expander("Gráfico: Quantidade de Filhos vs Renda", expanded=True):
                fig2 = px.bar(renda, x='qtd_filhos', y='renda', title='Quantidade de Filhos vs Renda',
                              color='qtd_filhos', color_discrete_sequence=px.colors.qualitative.Bold)
                st.plotly_chart(fig2, use_container_width=True)

        with col2:
            with st.expander("Gráfico: Tipo de Renda vs Renda", expanded=True):
                fig3 = px.bar(renda, x='tipo_renda', y='renda', title='Tipo de Renda vs Renda',
                              color='tipo_renda', color_discrete_sequence=px.colors.qualitative.Vivid)
                st.plotly_chart(fig3, use_container_width=True)

            with st.expander("Gráfico: Educação vs Renda", expanded=True):
                fig4 = px.bar(renda, x='educacao', y='renda', title='Educação vs Renda',
                              color='educacao', color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig4, use_container_width=True)
    else:
        st.warning("Por favor, faça o upload da base de dados para continuar.")

# Controle de navegação entre páginas
if "pagina_inicial" not in st.session_state:
    st.session_state.pagina_inicial = True

if st.session_state.pagina_inicial:
    pagina_boas_vindas()
else:
    pagina_principal()
