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

# --- FUNÇÃO: CARREGAR O GUIA DIDÁTICO (VERSÃO 5.0 - COMPLETA E CORRIGIDA) ---
def mostrar_guia_didatico():
    st.title("📚 Guia Didático e Base Científica")
    st.markdown("---")
    
    # AGORA SÃO 6 ABAS (Trouxemos a Histologia de volta)
    aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
        "💉 O Exame (PAAF)",
        "📊 Estatísticas (IA)",
        "🔬 Tipos Histológicos", # <-- ELA VOLTOU!
        "🧬 Tipos Moleculares", 
        "💊 Tratamentos",
        "❓ Glossário"
    ])

    # --- ABA 1: O EXAME PAAF ---
    with aba1:
        st.header("A Origem dos Dados: PAAF de Mama")
        col_paaf1, col_paaf2 = st.columns([2, 1])
        with col_paaf1:
            st.markdown("""
            **PAAF (Punção Aspirativa por Agulha Fina)** é o procedimento padrão-ouro.
            * **O que é:** Agulha fina inserida no nódulo para aspirar células.
            * **Como funciona:** Guiada por ultrassom, garante precisão.
            * **O Resultado:** Lâmina de vidro analisada ao microscópio (origem dos dados da IA).
            """)
            st.info("💡 **Curiosidade:** O dataset Wisconsin foi criado digitalizando essas lâminas.")
        with col_paaf2:
            st.image("paaf.jpg", caption="Ilustração da técnica PAAF", use_column_width=True)

    # --- ABA 2: ESTATÍSTICAS (IA) ---
    with aba2:
        st.header("Como a IA diferencia Benigno de Maligno?")
        st.write("Comparação real dos dados do Dataset Wisconsin:")
        st.markdown("### ⚖️ Comparação Numérica (Médias)")
        
        col_stat1, col_stat2 = st.columns(2)
        with col_stat1:
            st.success("🟢 **Padrão Benigno**")
            st.markdown("""
            * **Raio Médio:** ~12.15
            * **Textura:** ~17.91 (Uniforme)
            * **Perímetro:** ~78.08
            * **Área:** ~462.8
            * **Concavidade:** ~0.046 (Redondo)
            """)
        with col_stat2:
            st.error("🔴 **Padrão Maligno**")
            st.markdown("""
            * **Raio Médio:** ~17.46 (Grande)
            * **Textura:** ~21.60 (Irregular)
            * **Perímetro:** ~115.4
            * **Área:** ~978.4 (Dobro!)
            * **Concavidade:** ~0.161 (Dentado)
            """)
        st.info("🧠 **Interpretação:** ÁREA e CONCAVIDADE são os maiores delatores do câncer.")

    # --- ABA 3: TIPOS HISTOLÓGICOS (RECUPERADA COM A FOTO!) ---
    with aba3:
        st.header("Diferenças por Tipo Histológico")
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Carcinoma Ductal In Situ (CDIS)")
            st.success("Estágio 0 (Pré-invasivo)")
            st.write("* Cirurgia + Radio. Não precisa quimio.")
            
            st.markdown("---")
            st.subheader("Carcinoma Lobular Invasivo")
            st.markdown("""
            * Geralmente **Hormônio Positivo**.
            * Menos sensível à quimioterapia clássica.
            """)
            # AQUI ESTÁ A SUA FOTO DO LOBULAR
            st.image("lobular.jpg", caption="Microscopia: Carcinoma Lobular", use_column_width=True)

        with c2:
            st.subheader("Câncer Inflamatório")
            st.error("⚠️ Raro e Agressivo")
            st.write("* Tratamento Combinado (Quimio + Cirurgia + Radio).")

    # --- ABA 4: TIPOS MOLECULARES ---
    with aba4:
        st.header("Classificação Molecular")
        col_a, col_b = st.columns(2)
        with col_a:
            st.info("### 1. Hormônio Positivo")
            st.write("Crescimento lento. Tratamento: Hormonioterapia.")
            st.error("### 3. Triplo Negativo")
            st.write("Agressivo. Tratamento: Quimioterapia essencial.")
        with col_b:
            st.warning("### 2. HER2 Positivo")
            st.write("Tratamento: Terapia Alvo (Anti-HER2).")
            # Foto da Anatomia
            st.image("anatomia.png", caption="Anatomia da Mama", width=250)

    # --- ABA 5: TRATAMENTOS ---
    with aba5:
        st.header("Tratamentos e Efeitos")
        with st.expander("🔪 Cirurgia e Linfedema"):
            st.write("Risco de inchaço no braço.")
          st.image("linfedema.jpg", caption="Ilustração do Linfedema", use_column_width=True)           
        with st.expander("☢️ Radioterapia"):
            st.write("Vermelhidão e fadiga.")
            st.image("radioterapia.png", caption="Ilustração da técnica Radioterapia", use_column_width=True)
           
    # --- ABA 6: GLOSSÁRIO ---
    with aba6:
        st.header("🔍 Glossário Técnico")
        st.markdown("""
        * **📏 Raio:** Tamanho do núcleo.
        * **🧵 Textura:** Variação de cor (sujeira).
        * **📐 Perímetro:** Contorno.
        * **🕳️ Concavidade:** Irregularidade da borda (amora).
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















