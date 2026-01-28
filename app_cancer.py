import streamlit as st
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Configuração da Página (Título e ícone)
st.set_page_config(
    page_title="Sistema BioOnco - Diagnóstico Inteligente",
    page_icon="🧬",
    layout="wide"
)

# --- 1. TREINAMENTO DA IA (O Cérebro) ---
@st.cache_resource
def treinar_modelo():
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(df.drop('target', axis=1), df['target'])
    return model, data.feature_names

model, feature_names = treinar_modelo()

# --- 2. INTERFACE (Barra Lateral) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3004/3004458.png", width=100)
st.sidebar.title("🔬 Parâmetros da Amostra")
st.sidebar.write("Ajuste as medidas da citometria:")

# Sliders (Controles)
# Usamos valores padrão que geram 'Benigno' para começar
raio_medio = st.sidebar.slider("Raio Médio do Núcleo", 6.0, 30.0, 14.0)
textura_media = st.sidebar.slider("Textura (Desvio Padrão)", 9.0, 40.0, 19.0)
perimetro_medio = st.sidebar.slider("Perímetro Nuclear", 40.0, 190.0, 90.0)
area_media = st.sidebar.slider("Área Nuclear", 140.0, 2500.0, 600.0)
smoothness = st.sidebar.slider("Suavidade (Smoothness)", 0.05, 0.25, 0.09)
concavidade = st.sidebar.slider("Concavidade", 0.0, 0.5, 0.04)

# --- 3. PREDIÇÃO (O Cálculo) ---
# Criamos um paciente "fictício" com médias gerais para preencher o que falta
# E substituímos pelos valores que o usuário escolheu nos sliders
input_data = [
    raio_medio, textura_media, perimetro_medio, area_media, smoothness,
    0.0, concavidade, 0.0, 0.0, 0.0, # Preenchemos o resto com zeros ou médias
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    raio_medio, textura_media, perimetro_medio, area_media, smoothness,
    0.0, concavidade, 0.0, 0.0, 0.0
]

# A IA calcula a probabilidade
prediction = model.predict([input_data])[0]
probability = model.predict_proba([input_data])[0]

# --- 4. TELA PRINCIPAL (Resultados) ---

st.title("🧬 Sistema de Apoio ao Diagnóstico (SAD)")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Resultado da Análise Morfométrica")
    
    if prediction == 0: # Maligno
        st.error("🚨 RESULTADO: ALTA PROBABILIDADE DE MALIGNIDADE")
        st.write(f"Confiança da IA: **{probability[0]*100:.1f}%**")
        
        st.markdown("### 🧬 Sugestão de Investigação Genética")
        st.warning(
            """
            **Protocolo Sugerido:**
            1. Realizar Biópsia Confirmatória.
            2. **Painel NGS (Sequenciamento):** Investigar mutações nos genes **BRCA1** (Cromossomo 17) e **BRCA2** (Cromossomo 13).
            3. Avaliar expressão de HER2.
            """
        )
        
    else: # Benigno
        st.success("✅ RESULTADO: PADRÃO BENIGNO DETECTADO")
        st.write(f"Probabilidade de ser benigno: **{probability[1]*100:.1f}%**")
        st.balloons()
        st.info("Monitoramento clínico anual recomendado. Nenhuma alteração citogenética visualizada.")

with col2:
    st.metric(label="Classificação", value="Maligno" if prediction == 0 else "Benigno")
    st.metric(label="Risco Calculado", value=f"{probability[0]*100:.1f}%")
    
    st.markdown("---")
    st.write("**Dados Técnicos:**")
    st.caption(f"Raio: {raio_medio} | Textura: {textura_media}")
    st.caption("Modelo: Random Forest (Scikit-Learn)")

# Rodapé
st.markdown("---")
st.caption("Desenvolvido por Josias M.M.Minghin para disciplina de Biomedicina e TICs ")
