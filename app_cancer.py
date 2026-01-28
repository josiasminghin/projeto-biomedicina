import streamlit as st
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Configuração da Página com tom profissional
st.set_page_config(
    page_title="SAD - BioOnco",
    page_icon="🏥",
    layout="wide"
)

# --- 1. TREINAMENTO DA IA ---
@st.cache_resource
def treinar_modelo():
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(df.drop('target', axis=1), df['target'])
    return model, data.feature_names

model, feature_names = treinar_modelo()

# --- 2. BARRA LATERAL (Entrada de Dados) ---
st.sidebar.header("🔬 Parâmetros Morfométricos")
st.sidebar.markdown("Insira os dados da análise citológica:")

# Sliders ajustados para cobrir as médias reais
raio_medio = st.sidebar.slider("Raio Médio", 6.0, 30.0, 14.0, help="Média Benigno: ~12.1 | Maligno: ~17.4")
textura_media = st.sidebar.slider("Textura (Desvio Padrão)", 9.0, 40.0, 19.0, help="Média Benigno: ~17.9 | Maligno: ~21.6")
perimetro_medio = st.sidebar.slider("Perímetro", 40.0, 190.0, 90.0, help="Média Benigno: ~78.0 | Maligno: ~115.3")
area_media = st.sidebar.slider("Área Nuclear", 140.0, 2500.0, 600.0, help="Média Benigno: ~462.0 | Maligno: ~978.0")
smoothness = st.sidebar.slider("Suavidade (Smoothness)", 0.05, 0.25, 0.09)
concavidade = st.sidebar.slider("Concavidade", 0.0, 0.5, 0.04, help="Ponto chave para malignidade")

# --- 3. PREDIÇÃO (O Cálculo Inteligente) ---

# Ajuste Fino: Para a IA não ficar confusa com os valores zerados,
# vamos vincular os campos invisíveis aos que você mexe nos sliders.

# Estimativa baseada em correlação biológica:
compactness = concavity       # Compactação geralmente acompanha a concavidade
concave_points = concavity    # Pontos côncavos acompanham a concavidade
fractal_dimension = 0.06      # Valor médio padrão
symmetry = 0.18               # Valor médio padrão

input_data = [
    # Média (Mean)
    raio_medio, textura_media, perimetro_medio, area_media, smoothness,
    compactness, concavity, concave_points, symmetry, fractal_dimension,
    
    # Erro Padrão (Standard Error) - Valores baixos padrão
    0.5, 1.0, 3.0, 40.0, 0.005, 
    0.02, 0.02, 0.01, 0.02, 0.004,
    
    # Pior Caso (Worst) - Assumimos que o "Pior" é igual ou um pouco maior que a média
    raio_medio * 1.2, textura_media, perimetro_medio * 1.2, area_media * 1.2, smoothness,
    compactness, concavity, concave_points, symmetry, fractal_dimension
]

prediction = model.predict([input_data])[0]
probability = model.predict_proba([input_data])[0]

# --- 4. TELA PRINCIPAL (Laudo) ---

st.title("🧬 Sistema de Apoio ao Diagnóstico (SAD)")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Laudo Preliminar (IA)")
    
    if prediction == 0: # Maligno
        st.error("⚠️ ALERTA: PADRÃO COMPATÍVEL COM MALIGNIDADE")
        st.markdown(f"**Probabilidade Estimada:** {probability[0]*100:.1f}%")
        
        st.markdown("### 🧬 Protocolo de Investigação Sugerido")
        st.warning(
            """
            A morfometria nuclear indica alta atipia.
            
            **Próximos Passos:**
            1. **Confirmação Histopatológica:** Biópsia obrigatória.
            2. **Investigação Citogenética:** * Sequenciamento do gene **BRCA1** (Locus: 17q21).
               * Sequenciamento do gene **BRCA2** (Locus: 13q12).
            """
        )
        
    else: # Benigno
        st.success("✅ RESULTADO: PADRÃO MORFOLÓGICO BENIGNO")
        st.markdown(f"**Probabilidade de Benignidade:** {probability[1]*100:.1f}%")
        
        # AQUI MUDOU: Texto sério em vez de balões
        st.info(
            """
            **Conduta:**
            * As características nucleares estão dentro dos limites da normalidade.
            * Manter rotina de rastreamento conforme diretrizes clínicas.
            * Resultado sujeito a revisão médica.
            """
        )

with col2:
    # Painel lateral direito com resumo
    st.markdown("### Resumo da Análise")
    st.metric(label="Classificação", value="Maligno" if prediction == 0 else "Benigno")
    
    # Indicador visual de risco (Barra de progresso)
    st.write("Nível de Risco:")
    st.progress(int(probability[0]*100))
    
    st.markdown("---")
    st.caption(f"Raio Nuclear: {raio_medio} µm")
    st.caption(f"Concavidade: {concavidade}")
    st.caption("Algoritmo: Random Forest")

st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>Sistema desenvolvido para fins acadêmicos - Biomedicina </div>", unsafe_allow_html=True)

