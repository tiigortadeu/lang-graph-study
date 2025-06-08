import streamlit as st
import sys
import os
from io import StringIO
import contextlib

# Adicionar o diretório do basic.py ao path
sys.path.append(os.path.join(os.getcwd(), '2_basic_reflection_system'))

st.title("🤖 LangGraph Reflection System Demo")
st.write("Visualizando o resultado do sistema de reflexão básico")

if st.button("Executar Sistema de Reflexão"):
    with st.spinner("Executando o sistema..."):
        # Capturar a saída do print
        f = StringIO()
        with contextlib.redirect_stdout(f):
            try:
                # Importar e executar o basic.py
                from basic import app, HumanMessage
                
                # Executar o app
                response = app.invoke(HumanMessage(content="AI Agent taking over content creation"))
                
                # Mostrar o gráfico
                st.subheader("📊 Estrutura do Grafo")
                mermaid_graph = app.get_graph().draw_mermaid()
                st.code(mermaid_graph, language="mermaid")
                
                # Mostrar ASCII do grafo
                st.subheader("🔤 Representação ASCII do Grafo")
                ascii_graph = f.getvalue()
                if ascii_graph:
                    st.text(ascii_graph)
                
                # Mostrar as mensagens resultantes
                st.subheader("💬 Resultado da Execução")
                st.write(f"**Total de mensagens:** {len(response)}")
                
                for i, message in enumerate(response):
                    with st.expander(f"Mensagem {i+1} - {type(message).__name__}"):
                        st.write(f"**Tipo:** {type(message).__name__}")
                        st.write(f"**Conteúdo:**")
                        st.write(message.content)
                        if hasattr(message, 'additional_kwargs') and message.additional_kwargs:
                            st.write(f"**Kwargs adicionais:** {message.additional_kwargs}")
                        if hasattr(message, 'response_metadata') and message.response_metadata:
                            st.write(f"**Metadata:** {message.response_metadata}")
                
            except Exception as e:
                st.error(f"Erro ao executar: {str(e)}")
                st.exception(e)

st.sidebar.header("ℹ️ Informações")
st.sidebar.write("""
Este sistema demonstra um grafo de reflexão básico usando LangGraph:

- **Generate Node**: Gera conteúdo inicial
- **Reflect Node**: Reflete sobre o conteúdo gerado
- **Conditional Edge**: Decide se deve continuar refletindo ou parar

O sistema executa até atingir mais de 2 mensagens no estado.
""")

# Mostrar informações sobre o arquivo
st.sidebar.subheader("📁 Arquivo Fonte")
st.sidebar.code("2_basic_reflection_system/basic.py") 