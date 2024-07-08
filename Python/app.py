import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title('Análise de Cursos')

    # Carregar o arquivo CSV com a codificação correta
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
    if uploaded_file is not None:
        # Especificar a codificação correta ao ler o arquivo
        cursos = pd.read_csv(uploaded_file, encoding='ISO-8859-1')

        # Mostrar os dados na tabela
        st.subheader('Dados dos Cursos')
        st.dataframe(cursos)

        # Gráfico 1: Histograma para Quantidade de Vendas
        st.subheader('Distribuição da Quantidade de Vendas')
        fig, ax = plt.subplots()
        ax.hist(cursos['Quantidade de Vendas'], bins=10, color='skyblue', edgecolor='black')
        ax.set_title('Distribuição da Quantidade de Vendas')
        ax.set_xlabel('Quantidade de Vendas')
        ax.set_ylabel('Frequência')
        st.pyplot(fig)

        # Gráfico 2: Histograma para Preço Unitário
        st.subheader('Distribuição do Preço Unitário')
        fig, ax = plt.subplots()
        ax.hist(cursos['Preço Unitário'], bins=10, color='lightgreen', edgecolor='black')
        ax.set_title('Distribuição do Preço Unitário')
        ax.set_xlabel('Preço Unitário')
        ax.set_ylabel('Frequência')
        st.pyplot(fig)

        # Convertendo a coluna 'Data' para o tipo datetime, se necessário
        cursos['Data'] = pd.to_datetime(cursos['Data'])

        # Ordenando os dados pela data
        cursos = cursos.sort_values(by='Data')

        # Gráfico 3: Análise temporal da quantidade de vendas
        st.subheader('Distribuição das Vendas ao Longo do Tempo')
        fig, ax = plt.subplots()
        ax.plot(cursos['Data'], cursos['Quantidade de Vendas'], marker='o', linestyle='-', color='b')
        ax.set_title('Distribuição das Vendas ao Longo do Tempo')
        ax.set_xlabel('Data')
        ax.set_ylabel('Quantidade de Vendas')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Selecionando apenas colunas numéricas para a matriz de correlação
        numeric_cols = cursos.select_dtypes(include=['number'])

        # Gráfico 4: Matriz de Correlação
        st.subheader('Matriz de Correlação')
        correlation_matrix = numeric_cols.corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
        ax.set_title('Matriz de Correlação')
        st.pyplot(fig)

if __name__ == '__main__':
    main()
