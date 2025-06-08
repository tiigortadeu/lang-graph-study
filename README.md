# 🔗 LangGraph Study - Projetos de Exemplo

Uma coleção abrangente de mini-projetos demonstrando as capacidades do **LangGraph**, desde conceitos básicos até implementações avançadas de agentes de IA, sistemas de reflexão e assistentes pessoais completos.

## 📁 Estrutura do Projeto

```
lgraph/
├── 1_introduction/           # 🚀 Introdução ao LangGraph
├── 2_basic_reflection_system/ # 🪞 Sistema de Reflexão Básico
├── 3_test/                   # 🤖 Assistente Pessoal Completo
├── streamlit_app.py          # 🎯 Interface Principal Streamlit
└── README.md                 # 📖 Este arquivo
```

## 🎯 Mini-Projetos Incluídos

### 1️⃣ **Introduction** - Primeiros Passos com LangGraph
**Pasta:** `1_introduction/`

Projetos introdutórios que demonstram os conceitos fundamentais do LangGraph:

#### **🔍 Real-time Agent** (`lg_real.py`)
- **Tecnologias:** LangGraph, Google Gemini 2.0 Flash, Tavily Search
- **Funcionalidades:**
  - Agente ReAct com capacidade de busca em tempo real
  - Integração com Tavily para pesquisas atualizadas
  - Ferramenta de data/hora do sistema
  - Exemplo prático: consultar próximos jogos do Corinthians

#### **⚡ Basic ReAct Agent** (`reac_agent_basic.py`)
- **Tecnologias:** LangGraph, Agentes ReAct
- **Funcionalidades:**
  - Implementação básica de agente ReAct
  - Estrutura fundamental para tomada de decisão

**Como usar:**
```bash
cd 1_introduction
python lg_real.py
```

### 2️⃣ **Basic Reflection System** - Sistema de Auto-Reflexão
**Pasta:** `2_basic_reflection_system/`

Sistema avançado que implementa um mecanismo de reflexão e melhoria iterativa:

#### **🪞 Reflection Workflow** (`basic.py`)
- **Tecnologias:** LangGraph, MessageGraph, Google Gemini
- **Funcionalidades:**
  - Nós de Geração e Reflexão
  - Fluxo condicional baseado no número de iterações
  - Chains customizadas para geração e reflexão
  - Visualização do grafo em ASCII e Mermaid

#### **⛓️ Custom Chains** (`chains.py`)
- **Tecnologias:** LangChain, Prompt Templates
- **Funcionalidades:**
  - Chains especializadas para geração de conteúdo
  - Chains de reflexão para análise crítica
  - Templates de prompt otimizados

**Como usar:**
```bash
cd 2_basic_reflection_system
python basic.py
```

**Ou via Streamlit:**
```bash
streamlit run streamlit_app.py
```

### 3️⃣ **Personal Assistant** - Assistente Completo com Gmail
**Pasta:** `3_test/`

Assistente pessoal completo com integração total ao Gmail e interface Streamlit:

#### **🤖 Gmail-Integrated Chatbot** (`app.py`, `chatbot.py`)
- **Tecnologias:** LangGraph, Google Gemini 2.0, Gmail API, Streamlit
- **Funcionalidades:**
  - **5 Ferramentas Gmail:**
    - 📤 Enviar emails
    - 📝 Criar rascunhos
    - 🔍 Pesquisar emails
    - 📨 Ler mensagens
    - 🧵 Gerenciar threads
  - Interface web moderna com Streamlit
  - Autenticação OAuth2 segura
  - Histórico de conversação
  - Status de ferramentas em tempo real

**Como usar:**
```bash
cd 3_test
pip install -r requirements.txt
streamlit run app.py
```

**Setup necessário:**
1. Configure a API do Gmail no Google Cloud Console
2. Baixe `credentials.json`
3. Configure variáveis de ambiente
4. Execute a autenticação OAuth na primeira vez

## 🚀 Instalação Rápida

### Pré-requisitos
- Python 3.8+
- Conta Google (para Gmail API)
- Chaves API: Google AI Studio, Tavily

### Setup Básico
```bash
# Clone o repositório
git clone https://github.com/tiigortadeu/lang-graph-study.git
cd lang-graph-study

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale dependências gerais
pip install langchain langgraph python-dotenv streamlit
pip install langchain-google-genai langchain-community

# Para o projeto 3 (Gmail Assistant)
cd 3_test
pip install -r requirements.txt
```

### Configuração de Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto:

```env
# APIs necessárias
GOOGLE_API_KEY=sua_chave_google_ai_studio
TAVILY_API_KEY=sua_chave_tavily

# Apenas para desenvolvimento local
OPENAI_API_KEY=sua_chave_openai_opcional
```

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso | Projetos |
|------------|-----|----------|
| **LangGraph** | Framework principal para workflows de IA | Todos |
| **Google Gemini 2.0** | Modelo de linguagem principal | Todos |
| **Streamlit** | Interface web interativa | 2, 3 |
| **Gmail API** | Integração completa com email | 3 |
| **Tavily Search** | Pesquisas em tempo real | 1 |
| **LangChain** | Ferramentas e chains | Todos |
| **OAuth2** | Autenticação segura | 3 |

## 📊 Recursos de Aprendizado

### **🎯 Interface Principal Streamlit**
Execute `streamlit run streamlit_app.py` para acessar:
- Demonstração interativa do sistema de reflexão
- Visualização de grafos em tempo real
- Execução controlada dos workflows
- Análise detalhada dos resultados

### **📈 Progressão Sugerida**
1. **Projeto 1:** Entenda agentes básicos e ferramentas
2. **Projeto 2:** Explore sistemas de reflexão e workflows complexos
3. **Projeto 3:** Implemente assistente completo com APIs reais

### **🔍 Conceitos Demonstrados**
- **Agentes ReAct:** Raciocínio, Ação e Observação
- **Message Graphs:** Grafos baseados em mensagens
- **Conditional Edges:** Roteamento condicional
- **Tool Calling:** Integração com APIs externas
- **State Management:** Gerenciamento de estado persistente
- **OAuth Integration:** Autenticação segura

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. **Adicionar novos mini-projetos** em pastas numeradas
2. **Melhorar documentação** existente
3. **Corrigir bugs** ou otimizar código
4. **Sugerir novas funcionalidades**

### Estrutura para Novos Projetos
```
4_novo_projeto/
├── README.md          # Documentação específica
├── main.py           # Arquivo principal
├── requirements.txt  # Dependências específicas
└── utils/            # Módulos auxiliares
```

## 📞 Suporte

- **Issues:** [GitHub Issues](https://github.com/tiigortadeu/lang-graph-study/issues)
- **Documentação:** README individual em cada pasta
- **Exemplos:** Código comentado em todos os arquivos

## 📄 Licença

Este projeto é open source e está disponível sob a [MIT License](LICENSE).

## 🎓 Sobre LangGraph

LangGraph é uma biblioteca para construção de aplicações com múltiplos agentes de IA usando grafos. É especialmente útil para:

- **Workflows Complexos:** Coordenação de múltiplos agentes
- **Estados Persistentes:** Manutenção de contexto entre interações
- **Roteamento Condicional:** Decisões baseadas em estado
- **Integração de Ferramentas:** Conexão com APIs externas

---

**📚 Explore, aprenda e construa com LangGraph!** 

*Desenvolvido por [Tiago Tadeu](https://github.com/tiigortadeu) para aprendizado e demonstração das capacidades do LangGraph.* 