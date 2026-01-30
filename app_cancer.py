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

# --- FUNÇÃO: CARREGAR O GUIA DIDÁTICO (VERSÃO 4.0 - COMPLETA) ---
def mostrar_guia_didatico():
    st.title("📚 Guia Didático e Base Científica")
    st.markdown("---")
    
    # Adicionamos novas abas para o conteúdo técnico PAAF e Estatísticas
    aba1, aba2, aba3, aba4, aba5 = st.tabs([
        "💉 O Exame (PAAF)",
        "📊 Estatísticas (IA)",
        "🧬 Tipos Moleculares", 
        "💊 Tratamentos",
        "❓ Glossário de Termos"
    ])

    # --- ABA 1: EXPLICANDO A TÉCNICA (PAAF) ---
    with aba1:
        st.header("A Origem dos Dados: PAAF de Mama")
        
        col_paaf1, col_paaf2 = st.columns([2, 1])
        with col_paaf1:
            st.markdown("""
            **PAAF (Punção Aspirativa por Agulha Fina)** é o procedimento padrão-ouro para coleta inicial.
            
            * **O que é:** Uma técnica minimamente invasiva onde uma agulha fina é inserida no nódulo para aspirar células.
            * **Como funciona:** Guiada por ultrassom, permite visualizar a agulha dentro da lesão, garantindo que a amostra venha do lugar certo, mesmo em nódulos pequenos.
            * **O Resultado:** O material coletado é colocado em uma lâmina de vidro, corado e analisado ao microscópio. É dessa lâmina que a IA extrai os dados matemáticos.
            """)
            st.info("💡 **Curiosidade:** O dataset deste projeto (Wisconsin) foi criado digitalizando essas lâminas de PAAF e calculando a geometria dos núcleos celulares.")
        
        with col_paaf2:
            # Imagem ilustrativa da PAAF 
           st.image("paaf.jpg", caption="Ilustração da técnica PAAF", use_column_width=True)
                   

    # --- ABA 2: A INTELIGÊNCIA DA MÁQUINA (ESTATÍSTICAS) ---
    with aba2:
        st.header("Como a IA diferencia Benigno de Maligno?")
        st.write("A IA não 'chuta'. Ela analisa padrões estatísticos robustos. Veja a comparação real dos dados:")

        # Tabela Comparativa (Baseada nos dados reais do WDBC)
        st.markdown("### ⚖️ Comparação Numérica (Médias)")
        
        col_stat1, col_stat2 = st.columns(2)
        
        with col_stat1:
            st.success("🟢 **Padrão Benigno**")
            st.markdown("""
            * **Raio Médio:** ~12.15
            * **Textura:** ~17.91 (Mais uniforme)
            * **Perímetro:** ~78.08
            * **Área:** ~462.8
            * **Concavidade:** ~0.046 (Núcleo redondinho)
            """)
        
        with col_stat2:
            st.error("🔴 **Padrão Maligno**")
            st.markdown("""
            * **Raio Médio:** ~17.46 (Núcleos grandes)
            * **Textura:** ~21.60 (Manchado/Irregular)
            * **Perímetro:** ~115.4
            * **Área:** ~978.4 (Quase o dobro!)
            * **Concavidade:** ~0.161 (Bordas dentadas)
            """)

        st.markdown("---")
        st.caption("Fonte dos dados: Wisconsin Breast Cancer Diagnostic Dataset (WDBC).")
        st.info("🧠 **Interpretação:** Note que a ÁREA e a CONCAVIDADE nos tumores malignos são drasticamente maiores. O algoritmo aprende essas diferenças.")

    # --- ABA 3: TIPOS MOLECULARES ---
    with aba3:
        st.header("Classificação Molecular")
        st.write("O tratamento depende da 'personalidade' biológica do tumor.")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.info("### 1. Hormônio Positivo (ER/PR+)")
            st.markdown("""
            *📌 É o tipo mais comum e geralmente com melhor prognóstico.*
            * **Tratamento:** Hormonioterapia por 5–10 anos.
            * ✅ **Responde bem a tratamento**
            """)
            
            st.error("### 3. Triplo Negativo")
            st.markdown("""
            *📌 O mais desafiador (sem receptores).*
            * **Tratamento:** Quimioterapia é essencial.
            * ⚠️ **Crescimento rápido**
            """)

        with col_b:
            st.warning("### 2. HER2 Positivo")
            st.markdown("""
            *📌 Mais agressivo, mas hoje muito tratável.*
            * **Tratamento:** Quimioterapia + Terapia Alvo (Anti-HER2).
            * 🎯 **Tratamento específico**
            """)
            try:
                st.image("anatomia.png", caption="Ilustração: Estágios", width=250)
            except:
                st.caption("Imagem anatomia.png não carregada.")

    # --- ABA 4: TRATAMENTOS E EFEITOS ---
    with aba4:
        st.header("Tratamentos e Efeitos Colaterais")
        
        with st.expander("🔪 Cirurgia e Linfedema"):
            st.markdown("**Linfedema:** Inchaço no braço após esvaziamento axilar.")
            try:
                st.image("linfedema.jpg", caption="Exemplo de Linfedema", width=200)
            except:
                st.caption("Imagem linfedema.jpg não carregada.")

        with st.expander("☢️ Radioterapia"):
            col_r1, col_r2 = st.columns([1, 2])
            with col_r1:
                try:
                    st.image("radioterapia.png", caption="Esquema")
                except:
                    st.caption("Imagem radioterapia.png não carregada.")
            with col_r2:
                st.write("**Efeitos:** Vermelhidão na pele, fadiga e fibrose tardia.")

    # --- ABA 5: GLOSSÁRIO TÉCNICO ---
    with aba5:
        st.header("🔍 Glossário: Entendendo os Parâmetros")
        st.markdown("""
        Se você sempre teve dúvida do que significam os números que a IA analisa:
        
        * **📏 Raio Médio:** Distância do centro do núcleo até a borda. (Câncer = Núcleos gigantes).
        * **🧵 Textura:** Variação da cor cinza. (Câncer = Aparência "suja" ou heterogênea).
        * **📐 Perímetro:** O tamanho do contorno. (Câncer = Contorno grande e irregular).
        * **🌊 Suavidade:** Quão lisa é a borda. (Câncer = Bordas ásperas/denteadas).
        * **🕳️ Concavidade:** "Buracos" ou reentrâncias na borda. (Câncer = Muitas invaginações).
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













