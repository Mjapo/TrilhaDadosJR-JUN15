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

        # Análise temporal
        st.subheader('Análise Temporal')
        if 'Data' in cursos.columns:
            cursos['Data'] = pd.to_datetime(cursos['Data'])
            cursos.set_index('Data', inplace=True)
            st.line_chart(cursos)
        else:
            st.write("A coluna 'Data' não foi encontrada nos dados.")

        # Matriz de correlação
        st.subheader('Matriz de Correlação')
        numerical_columns = cursos.select_dtypes(include=['float64', 'int64']).columns
        correlation_matrix = cursos[numerical_columns].corr()
        st.write(correlation_matrix)
        fig, ax = plt.subplots()
        sns.heatmap(correlation_matrix, ax=ax, annot=True, cmap='coolwarm')
        st.pyplot(fig)

        # Outros gráficos
        st.subheader('Distribuição de Frequências')
        for column in numerical_columns:
            fig, ax = plt.subplots()
            sns.histplot(cursos[column], kde=True, ax=ax)
            ax.set_title(f'Distribuição de {column}')
            st.pyplot(fig)

if __name__ == '__main__':
    main()

