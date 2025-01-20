import streamlit as st
import pandas as pd
import plotly.express as px

# Configurações da página
st.set_page_config(page_title="Bem-vindo ao Projeto", page_icon=":bar_chart:", layout="wide")

# Função para exibir a página de boas-vindas
def pagina_boas_vindas():
    st.image("https://keystoneacademic-res.cloudinary.com/image/upload/element/97/97189_thumb.png", width=200)  # Adicionando a logo

    st.title("Bem-vindo ao Projeto de Previsão de Renda!")
    
    # Mensagem de boas-vindas
    st.markdown("""
        
       ## Este projeto explora o perfil financeiro de diversos clientes, permitindo análises de tendências de renda com base em múltiplas variáveis.
        Sinta-se à vontade para navegar pelos gráficos interativos e descobrir insights valiosos.
                
        by Aluno Jonathan Gustavo
    """)

    # Botão para iniciar a análise
    if st.button("Iniciar"):
        st.session_state.pagina_inicial = False  # Muda o estado para mostrar a página de análise

# Função para exibir a página principal do app
def pagina_principal():
    st.title("Análise Exploratória da Previsão de Renda")

    # Carregar o dataset
    renda = pd.read_csv('previsao_de_renda.csv')

    # Layout com duas colunas
    col1, col2 = st.columns(2)

    # Adicionando gráficos em expander com Plotly
    with col1:
        with st.expander("Gráfico: Posse de Imóvel vs Renda", expanded=True):
            fig8 = px.bar(renda, x='posse_de_imovel', y='renda', title='Posse de Imóvel vs Renda',
                          color='posse_de_imovel', color_discrete_sequence=px.colors.qualitative.Prism)
            st.plotly_chart(fig8, use_container_width=True)

        with st.expander("Gráfico: Posse de Veículo vs Renda", expanded=True):
            fig9 = px.bar(renda, x='posse_de_veiculo', y='renda', title='Posse de Veículo vs Renda',
                          color='posse_de_veiculo', color_discrete_sequence=px.colors.qualitative.Set1)
            st.plotly_chart(fig9, use_container_width=True)

        with st.expander("Gráfico: Quantidade de Filhos vs Renda", expanded=True):
            fig10 = px.bar(renda, x='qtd_filhos', y='renda', title='Quantidade de Filhos vs Renda',
                           color='qtd_filhos', color_discrete_sequence=px.colors.qualitative.Bold)
            st.plotly_chart(fig10, use_container_width=True)

    with col2:
        with st.expander("Gráfico: Tipo de Renda vs Renda", expanded=True):
            fig11 = px.bar(renda, x='tipo_renda', y='renda', title='Tipo de Renda vs Renda',
                           color='tipo_renda', color_discrete_sequence=px.colors.qualitative.Vivid)
            st.plotly_chart(fig11, use_container_width=True)

        with st.expander("Gráfico: Educação vs Renda", expanded=True):
            fig12 = px.bar(renda, x='educacao', y='renda', title='Educação vs Renda',
                           color='educacao', color_discrete_sequence=px.colors.qualitative.Pastel)
            st.plotly_chart(fig12, use_container_width=True)

        with st.expander("Gráfico: Estado Civil vs Renda", expanded=True):
            fig13 = px.bar(renda, x='estado_civil', y='renda', title='Estado Civil vs Renda',
                           color='estado_civil', color_discrete_sequence=px.colors.qualitative.Set2)
            st.plotly_chart(fig13, use_container_width=True)

        with st.expander("Gráfico: Tipo de Residência vs Renda", expanded=True):
            fig14 = px.bar(renda, x='tipo_residencia', y='renda', title='Tipo de Residência vs Renda',
                           color='tipo_residencia', color_discrete_sequence=px.colors.qualitative.Safe)
            st.plotly_chart(fig14, use_container_width=True)

# Controle para determinar se estamos na página inicial ou na principal
if "pagina_inicial" not in st.session_state:
    st.session_state.pagina_inicial = True

# Exibir página de boas-vindas ou página principal com base no estado
if st.session_state.pagina_inicial:
    pagina_boas_vindas()
else:
    pagina_principal()
