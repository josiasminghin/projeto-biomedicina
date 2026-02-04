import streamlit as st
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import base64
from datetime import datetime, timedelta

# --- 1. CONFIGURAÇÃO DA PÁGINA (Deve ser a primeira linha) ---
st.set_page_config(
    page_title="SAD - BioOnco",
    page_icon="🏥",
    layout="wide"
)

# --- 2. CSS "MARTELO" (ESTILO BLINDADO PARA MENU E REMOÇÃO DE BOTÕES) ---
def adicionar_estilo_css():
    url_fundo_principal = "https://raw.githubusercontent.com/josiasminghin/projeto-biomedicina/main/fundo.jpg"
    
    st.markdown(f"""
    <style>
    /* A. FUNDO PRINCIPAL */
    .stApp {{
        background-image: url("{url_fundo_principal}");
        background-attachment: fixed;
        background-size: cover;
        background-color: rgba(255,255,255,0.92);
        background-blend-mode: overlay;
    }}

    /* B. MENU LATERAL (Sidebar) */
    section[data-testid="stSidebar"] {{
        background-color: #f0f4f8 !important;
        border-right: 1px solid #d1d5db;
    }}

    /* C. TEXTOS (Forçar Preto para Leitura) */
    h1, h2, h3, h4, h5, h6, p, li, div, span, label, b, strong {{
        color: #000000 !important;
    }}
    [data-testid="stSidebar"] * {{
        color: #1a1a1a !important;
    }}

    /* D. CONTORNO PARA INPUTS (Caixinhas) */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {{
        border: 1px solid #4b5563 !important;
        background-color: #ffffff !important;
        border-radius: 6px;
    }}

    /* --- E. AQUI ESTÁ A SOLUÇÃO DO MENU (CSS DE ALTO CONTRASTE) --- */
    
    /* 1. O Cabeçalho fica transparente, mas EXISTE (para não quebrar o celular) */
    header[data-testid="stHeader"] {{
        background: transparent !important;
        z-index: 100 !important;
    }}

    /* 2. Esconder Decoração e Ícones da Direita (Github, etc) */
    [data-testid="stDecoration"], [data-testid="stToolbar"] {{
        display: none !important;
        visibility: hidden !important;
    }}

    /* 3. FORÇAR O BOTÃO DE MENU A APARECER (BRANCO C/ ÍCONE PRETO) */
    button[kind="header"] {{
        display: block !important;
        visibility: visible !important;
        background-color: #FFFFFF !important; /* Fundo BRANCO Puro */
        border: 1px solid #999999 !important; /* Borda Cinza */
        border-radius: 8px !important;
        width: 44px !important;
        height: 44px !important;
        opacity: 1 !important;
        z-index: 99999 !important;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.2) !important;
    }}

    /* 4. TINTA PRETA PARA O ÍCONE (SVG) - Vence o Modo Noturno */
    button[kind="header"] > svg {{
        fill: #000000 !important;
        color: #000000 !important;
    }}
    
    /* Garante que a área clicável esteja ativa */
    [data-testid="stSidebarCollapsedControl"] {{
        display: block !important;
        visibility: visible !important;
    }}

    /* --- F. REMOÇÃO DE "MANAGE APP" E RODAPÉ --- */
    footer {{visibility: hidden;}}
    .stDeployButton {{display: none !important;}}
    
    /* Ocultar o Widget de Status (Manage App) */
    div[data-testid="stStatusWidget"] {{
        visibility: hidden !important;
        display: none !important;
        height: 0px !important;
        width: 0px !important;
    }}

    /* Ajuste Mobile */
    @media only screen and (max-width: 600px) {{
        .stApp {{ background-attachment: scroll; }}
    }}
    </style>
    """, unsafe_allow_html=True)

# Aplica o CSS
try:
    adicionar_estilo_css()
except:
    pass

# --- 3. GUIA DIDÁTICO (ABAS E CONTEÚDO) ---
def mostrar_guia_didatico():
    st.title("📚 Guia Didático e Base Científica")
    st.markdown("---")
    
    aba1, aba2, aba3, aba4, aba5, aba6, aba7 = st.tabs([
        "💉 O Exame (PAAF)", "📊 Estatísticas (IA)", "🔬 Tipos Histológicos",
        "🧬 Tipos Moleculares", "💊 Tratamentos", "❓ Glossário", "📘 Sobre o Projeto"
    ])

    with aba1:
        st.header("A Origem dos Dados: PAAF de Mama")
        col_paaf1, col_paaf2 = st.columns([2, 1])
        with col_paaf1:
            st.markdown("""
            **PAAF (Punção Aspirativa por Agulha Fina)** é o procedimento padrão-ouro.
            * **O que é:** Agulha fina inserida no nódulo para aspirar células.
            * **Como funciona:** Guiada por ultrassom, garante precisão.
            * **O Resultado:** Lâmina de vidro analisada ao microscópio.
            """)
        with col_paaf2:
            st.image("paaf.jpg", caption="Ilustração PAAF", use_container_width=True)

    with aba2:
        st.header("Como a IA diferencia Benigno de Maligno?")
        col_stat1, col_stat2 = st.columns(2)
        with col_stat1:
            st.success("🟢 **Padrão Benigno**")
            st.markdown("* **Raio:** ~12.15 | **Área:** ~462.8 | **Concavidade:** ~0.046")
        with col_stat2:
            st.error("🔴 **Padrão Maligno**")
            st.markdown("* **Raio:** ~17.46 | **Área:** ~978.4 | **Concavidade:** ~0.161")

    with aba3:
        st.header("🔬 Atlas de Patologia")
        tipo_cancer = st.selectbox("Escolha o Tipo Histológico:", 
            ["Carcinoma Ductal In Situ (CDIS)", "Carcinoma Lobular Invasivo", 
             "Carcinoma Inflamatório", "Tecido Normal/Benigno"])
        
        col_img, col_desc = st.columns([1, 1])
        with col_img:
            if tipo_cancer == "Carcinoma Ductal In Situ (CDIS)":
                st.image("ductal.jpg", caption="CDIS", use_container_width=True)
            elif tipo_cancer == "Carcinoma Lobular Invasivo":
                st.image("lobular.jpg", caption="Lobular", use_container_width=True)
            elif tipo_cancer == "Carcinoma Inflamatório":
                st.image("inflamatorio.jpg", caption="Inflamatório", use_container_width=True)
            else:
                st.image("Benigno.jpg", caption="Normal", use_container_width=True)
        
        with col_desc:
            if tipo_cancer == "Carcinoma Ductal In Situ (CDIS)":
                st.info("Cerca de 80% dos casos. Origem nos ductos.")
            elif tipo_cancer == "Carcinoma Lobular Invasivo":
                st.warning("10-15% dos casos. Células em fila indiana.")
            elif tipo_cancer == "Carcinoma Inflamatório":
                st.error("Raro e agressivo. Bloqueia vasos linfáticos.")
            else:
                st.success("Estruturas preservadas e sem atipias.")

    with aba4:
        st.header("🧬 Genética e Biologia Molecular")
        st.subheader("🔍 Os Guardiões do DNA")
        c1, c2 = st.columns(2)
        with c1:
            with st.expander("🧬 BRCA1"): st.error("Cromossomo 17q21. Reparo de DNA.")
            with st.expander("🛡️ TP53"): st.error("Cromossomo 17p13. Guardião do Genoma.")
        with c2:
            with st.expander("🧬 BRCA2"): st.warning("Cromossomo 13q12. Câncer masculino.")
            with st.expander("👮 CHEK2"): st.info("Cromossomo 22q12. Inspetor.")
        
        st.markdown("---")
        tab_b1, tab_b2 = st.tabs(["Biomarcadores", "Via PI3K/AKT"])
        with tab_b1:
            st.markdown("* **RH+:** Receptor Hormonal.\n* **HER2:** Acelerador.\n* **Ki-67:** Velocidade.")
        with tab_b2:
            st.warning("⚠️ Resistência ao Tratamento")
            st.markdown("A Via PI3K/AKT atua como 'Plano B' para o tumor.")
            try: st.image("Imagem3.jpg", caption="Via AKT", use_container_width=True)
            except: st.warning("Falta Imagem3.jpg")
            
            with st.expander("🔎 Detalhes da Hiperativação", expanded=True):
                cv1, cv2 = st.columns(2)
                with cv1: 
                    try: st.image("Imagem4.jpg", use_container_width=True) 
                    except: pass
                with cv2: 
                    try: st.image("Imagem5.jpg", caption="Obs: Roxo = Hiperativação", use_container_width=True)
                    except: pass
                st.subheader("💥 Impactos")
                st.write("Crescimento descontrolado e sobrevivência celular independente do estrogênio.")

    with aba5:
        st.header("💊 Tratamentos e Mecanismos")
        st.subheader("🎯 Mecanismo PARP e Letalidade Sintética")
        ct1, ct2 = st.columns([1,2])
        with ct1: st.info("Matar o câncer usando a falha dele.")
        with ct2:
            st.markdown("Sem BRCA (quebrado) e sem PARP (bloqueado), a célula morre.")
            st.markdown("---")
            try: st.image("parp_mecanismo.jpg", caption="Reparo Normal", use_container_width=True)
            except: pass
            try: st.image("parp_inibidor.jpg", caption="Ação do Medicamento", use_container_width=True)
            except: pass

    with aba6:
        st.header("🔍 Glossário")
        st.markdown("* **Raio:** Tamanho.\n* **Textura:** Variação.\n* **Concavidade:** Irregularidade.")

    with aba7:
        st.header("📘 Sobre o Projeto")
        c_aut1, c_aut2 = st.columns([1,3])
        with c_aut1:
            st.image("https://raw.githubusercontent.com/josiasminghin/projeto-biomedicina/main/perfil.jpg", width=150)
        with c_aut2:
            st.markdown("### Josias Minghin\n**Acadêmico de Biomedicina - UNIP**\n\nEste sistema integra Patologia Digital, Genética e IA.")

# --- 4. SISTEMA DE DIAGNÓSTICO (COM LÓGICA DE SINCRONIZAÇÃO) ---
def mostrar_diagnostico_ia():
    @st.cache_resource
    def treinar_modelo():
        data = load_breast_cancer()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['target'] = data.target
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(df.drop('target', axis=1), df['target'])
        return model
    
    model = treinar_modelo()

    st.sidebar.markdown("---")
    st.sidebar.header("🔬 Parâmetros da Amostra")

    # Função Mágica para Sincronizar Caixa e Slider
    def criar_controle(label, min_v, max_v, default_v, key_base, step_v):
        if f'{key_base}_val' not in st.session_state:
            st.session_state[f'{key_base}_val'] = default_v

        def update_from_num():
            new_val = st.session_state[f'{key_base}_num']
            st.session_state[f'{key_base}_val'] = new_val
            st.session_state[f'{key_base}_slide'] = new_val

        def update_from_slider():
            new_val = st.session_state[f'{key_base}_slide']
            st.session_state[f'{key_base}_val'] = new_val
            st.session_state[f'{key_base}_num'] = new_val

        val = st.sidebar.number_input(label, min_value=float(min_v), max_value=float(max_v),
            value=float(st.session_state[f'{key_base}_val']), step=step_v, key=f'{key_base}_num', on_change=update_from_num)
        
        st.sidebar.slider("Ajuste Visual", min_value=float(min_v), max_value=float(max_v),
            value=float(st.session_state[f'{key_base}_val']), key=f'{key_base}_slide', on_change=update_from_slider, label_visibility="collapsed")
        return val

    raio_medio = criar_controle("📏 Raio Médio", 6.0, 30.0, 14.0, "raio", 0.1)
    textura_media = criar_controle("🧶 Textura (Desvio)", 9.0, 40.0, 19.0, "textura", 0.1)
    perimetro_medio = criar_controle("⭕ Perímetro", 40.0, 190.0, 90.0, "perimetro", 0.5)
    area_media = criar_controle("🔵 Área Nuclear", 140.0, 2500.0, 600.0, "area", 10.0)
    smoothness = criar_controle("💧 Suavidade", 0.05, 0.25, 0.09, "suavidade", 0.001)
    concavidade = criar_controle("🕳️ Concavidade", 0.0, 0.5, 0.04, "concavidade", 0.001)

    # Cálculos Auxiliares
    area_calculada = area_media
    if raio_medio > 15.0 and area_media < 700:
        area_calculada = 3.1415 * (raio_medio ** 2)
    compactness = concavidade
    concave_points = concavidade
    fractal_dimension = 0.06
    symmetry = 0.18

    # Previsão
    input_data = [
        raio_medio, textura_media, perimetro_medio, area_calculada, smoothness,
        compactness, concavidade, concave_points, symmetry, fractal_dimension,
        0.5, 1.0, 3.0, 40.0, 0.005, 0.02, 0.02, 0.01, 0.02, 0.004,
        raio_medio * 1.2, textura_media, perimetro_medio * 1.2, area_calculada * 1.2, smoothness,
        compactness, concavidade, concave_points, symmetry, fractal_dimension
    ]
    prediction = model.predict([input_data])[0]
    probability = model.predict_proba([input_data])[0]

    # Exibição
    st.title("🧬 Sistema de Apoio ao Diagnóstico (SAD)")
    st.markdown("---")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Laudo Preliminar (IA)")
        if prediction == 0:
            st.error("⚠️ ALERTA: PADRÃO COMPATÍVEL COM MALIGNIDADE")
            st.markdown(f"**Probabilidade Estimada:** {probability[0]*100:.1f}%")
            st.markdown("---")
            if raio_medio > 16.0 or concavidade > 0.14:
                st.info("🚨 **High Grade:** Investigar TP53 e BRCA1.")
            else:
                st.warning("⚠️ **Luminal:** Investigar BRCA2 e CHEK2.")
        else:
            st.success("✅ PADRÃO BENIGNO")
            st.markdown(f"**Probabilidade:** {probability[1]*100:.1f}%")

    with col2:
        st.markdown("### Resumo")
        st.metric("Classificação", "Maligno" if prediction == 0 else "Benigno")
        st.progress(int(probability[0]*100))
        st.markdown("---")
        
        # --- LAUDO COM HORA CORRETA ---
        fuso_brasil = timedelta(hours=3)
        data_hora_atual = datetime.now() - fuso_brasil
        laudo_texto = f"""
🏥 SAD - BioOnco | Relatório Técnico
Data: {data_hora_atual.strftime("%d/%m/%Y às %H:%M")}
Responsável: Josias Minghin

MICROSCOPIA:
- Raio: {raio_medio} | Textura: {textura_media} | Concavidade: {concavidade}

RESULTADO IA: {"MALIGNO" if prediction == 0 else "BENIGNO"}
PROBABILIDADE: {probability[0 if prediction == 0 else 1]*100:.1f}%
        """
        st.download_button("📄 Baixar Laudo", data=laudo_texto, 
                           file_name=f"Laudo_{data_hora_atual.strftime('%H%M')}.txt")

# --- 5. MENU PRINCIPAL (RODAPÉ E NAVEGAÇÃO) ---
st.sidebar.markdown("---")
st.sidebar.title("Menu Principal")
navegacao = st.sidebar.radio("Ir para:", ["🤖 Sistema Diagnóstico (IA)", "📚 Guia Didático"])

if navegacao == "🤖 Sistema Diagnóstico (IA)":
    mostrar_diagnostico_ia()
else:
    mostrar_guia_didatico()

st.sidebar.markdown("---")
st.sidebar.info("Desenvolvido por Josias Minghin\nBiomedicina 1º Ano")
















































































