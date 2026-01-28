import streamlit as st
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Configuração da Página
st.set_page_config(
    page_title="SAD - BioOnco",
    page_icon="🏥",
    layout="wide"
)

# --- FUNÇÃO: CARREGAR O GUIA DIDÁTICO (VERSÃO CORRIGIDA - IMAGENS LOCAIS) ---
def mostrar_guia_didatico():
    st.title("📚 Guia de Tipos Moleculares e Tratamentos")
    st.markdown("---")
    
    # Criamos abas para organizar o conteúdo extenso
    aba1, aba2, aba3, aba4 = st.tabs([
        "🧬 Tipos Moleculares", 
        "🔬 Tipos Histológicos", 
        "💊 Tratamentos e Efeitos", 
        "🧠 Fatores de Risco"
    ])

    with aba1:
        st.header("Classificação Molecular")
        st.write("O tratamento depende da 'personalidade' biológica do tumor.")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.info("### 1. Hormônio Positivo (ER/PR+)")
            st.markdown("""
            *📌 É o tipo mais comum e geralmente com melhor prognóstico.*
            
            **Tratamento Típico:**
            * Cirurgia
            * Radioterapia (maioria dos casos)
            * **Hormonioterapia** por 5–10 anos
            * Quimioterapia: 👉 nem sempre necessária
            
            ✅ **Responde bem a tratamento**
            """)
            
            st.error("### 3. Triplo Negativo")
            st.markdown("""
            *📌 O mais desafiador (sem receptores).*
            
            **Tratamento Típico:**
            * Cirurgia + Radioterapia
            * **Quimioterapia é essencial**
            * Imunoterapia (casos selecionados)
            
            ⚠️ **Crescimento rápido**
            """)

        with col_b:
            st.warning("### 2. HER2 Positivo")
            st.markdown("""
            *📌 Mais agressivo, mas hoje muito tratável.*
            
            **Tratamento Típico:**
            * Cirurgia + Radioterapia
            * Quimioterapia + **Terapia Alvo Anti-HER2**
            
            🎯 **Tratamento específico** (~1 ano)
            """)
            
            # Tenta carregar a imagem local, se não tiver, avisa
            try:
                st.image("imagens/anatomia.png", caption="Ilustração: Estágios e Anatomia", width=300)
            except:
                st.caption("Imagem 'anatomia.png' não encontrada na pasta 'imagens'.")

    with aba2:
        st.header("Diferenças por Tipo Histológico")
        
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Carcinoma Ductal In Situ (CDIS)")
            st.success("Estágio 0 (Pré-invasivo)")
            st.markdown("""
            * Cirurgia (conservadora)
            * Radioterapia
            * ❌ **Não precisa quimioterapia**
            """)
            
            st.subheader("Carcinoma Lobular Invasivo")
            st.markdown("""
            * Geralmente é **Hormônio Positivo**
            * Menos sensível à quimioterapia clássica
            """)
            try:
                st.image("imagens/lobular.jpg", caption="Microscopia: Carcinoma Lobular", width=300)
            except:
                st.caption("Imagem 'lobular.jpg' não encontrada.")

        with c2:
            st.subheader("Câncer Inflamatório")
            st.error("⚠️ Raro e Agressivo")
            st.markdown("""
            * **Tratamento Combinado:**
            * 1. Quimioterapia Inicial
            * 2. Cirurgia
            * 3. Radioterapia
            """)

    with aba3:
        st.header("Efeitos Colaterais")
        
        with st.expander("🔪 Cirurgia e Linfedema"):
            st.markdown("**Linfedema:** Inchaço no braço após esvaziamento axilar.")
            try:
                st.image("imagens/linfedema.jpg", caption="Exemplo de Linfedema", width=250)
            except:
                st.caption("Imagem 'linfedema.jpg' não encontrada.")

        with st.expander("☢️ Radioterapia"):
            col_r1, col_r2 = st.columns([1, 2])
            with col_r1:
                try:
                    st.image("imagens/radioterapia.png", caption="Esquema de Radioterapia")
                except:
                    st.caption("Imagem 'radioterapia.png' não encontrada.")
            with col_r2:
                st.write("**Efeitos:** Vermelhidão na pele, fadiga e fibrose tardia.")
        
        with st.expander("💊 Quimioterapia"):
            st.markdown("""
            * **Quimio:** Náuseas, queda de cabelo, baixa imunidade.
            * **Hormonioterapia:** Sintomas de menopausa, dores articulares.
            """)

    with aba4:
        st.header("Fatores de Decisão Médica")
        st.markdown("""
        1. **Estágio** (Tamanho e metástase)
        2. **Linfonodos** (Axila comprometida?)
        3. **Idade e Saúde** da paciente
        4. **Genética** (Mutações BRCA1/2)
        """)

# --- LÓGICA DO APP ORIGINAL (DIAGNÓSTICO) ---
def mostrar_diagnostico_ia():
    # Cache para não treinar toda hora
    @st.cache_resource
    def treinar_modelo():
        data = load_breast_cancer()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['target'] = data.target
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(df.drop('target', axis=1), df['target'])
        return model, data.feature_names

    model, feature_names = treinar_modelo()

    # Barra Lateral de Parâmetros
    st.sidebar.markdown("---")
    st.sidebar.header("🔬 Parâmetros da Amostra")
    st.sidebar.caption("Ajuste conforme a microscopia:")

    raio_medio = st.sidebar.slider("Raio Médio", 6.0, 30.0, 14.0, help="Média Benigno: ~12.1 | Maligno: ~17.4")
    textura_media = st.sidebar.slider("Textura (Desvio)", 9.0, 40.0, 19.0)
    perimetro_medio = st.sidebar.slider("Perímetro", 40.0, 190.0, 90.0)
    area_media = st.sidebar.slider("Área Nuclear", 140.0, 2500.0, 600.0)
    smoothness = st.sidebar.slider("Suavidade", 0.05, 0.25, 0.09)
    concavidade = st.sidebar.slider("Concavidade", 0.0, 0.5, 0.04)

    # Lógica de preenchimento inteligente
    compactness = concavidade
    concave_points = concavidade
    fractal_dimension = 0.06
    symmetry = 0.18

    input_data = [
        raio_medio, textura_media, perimetro_medio, area_media, smoothness,
        compactness, concavidade, concave_points, symmetry, fractal_dimension,
        0.5, 1.0, 3.0, 40.0, 0.005, 
        0.02, 0.02, 0.01, 0.02, 0.004,
        raio_medio * 1.2, textura_media, perimetro_medio * 1.2, area_media * 1.2, smoothness,
        compactness, concavidade, concave_points, symmetry, fractal_dimension
    ]

    prediction = model.predict([input_data])[0]
    probability = model.predict_proba([input_data])[0]

    st.title("🧬 Sistema de Apoio ao Diagnóstico (SAD)")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Laudo Preliminar (IA)")
        
        if prediction == 0: # Maligno
            st.error("⚠️ ALERTA: PADRÃO COMPATÍVEL COM MALIGNIDADE")
            st.markdown(f"**Probabilidade Estimada:** {probability[0]*100:.1f}%")
            
            st.markdown("---")
            st.subheader("🧬 Investigação Citogenética Direcionada")
            
            if raio_medio > 16.0 or concavidade > 0.14:
                st.markdown("##### 🚨 Perfil de Alta Agressividade (High Grade)")
                st.info("""
                    **Fenótipo sugere instabilidade genômica severa.**
                    Investigar painel para:
                    * **Gene TP53** (Cromossomo 17p13)
                    * **Gene BRCA1** (Cromossomo 17q21)
                """)
            else:
                st.markdown("##### ⚠️ Perfil Moderado / Luminal")
                st.warning("""
                    **Fenótipo sugere progressão intermediária.**
                    Investigar painel para:
                    * **Gene BRCA2** (Cromossomo 13q12)
                    * **Gene CHEK2** (Cromossomo 22)
                """)
        else: # Benigno
            st.success("✅ RESULTADO: PADRÃO MORFOLÓGICO BENIGNO")
            st.markdown(f"**Probabilidade de Benignidade:** {probability[1]*100:.1f}%")
            st.info("""
                **Conduta:**
                * Características dentro da normalidade.
                * Manter rotina de rastreamento.
            """)

    with col2:
        st.markdown("### Resumo")
        st.metric(label="Classificação", value="Maligno" if prediction == 0 else "Benigno")
        st.progress(int(probability[0]*100))
        st.caption(f"Raio: {raio_medio} µm | Concavidade: {concavidade}")

# --- CONTROLE DE NAVEGAÇÃO ---
# Aqui criamos o menu lateral que troca as telas
st.sidebar.title("Menu Principal")
navegacao = st.sidebar.radio("Ir para:", ["🤖 Sistema Diagnóstico (IA)", "📚 Guia Didático: Tipos e Tratamentos"])

if navegacao == "🤖 Sistema Diagnóstico (IA)":
    mostrar_diagnostico_ia()
else:
    mostrar_guia_didatico()

# Rodapé
st.sidebar.markdown("---")
st.sidebar.info("Desenvolvido por Josias Minghin\nBiomedicina 1º Ano")








