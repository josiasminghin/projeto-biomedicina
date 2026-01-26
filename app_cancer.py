import streamlit as st
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="BioOnco System", page_icon="🧬")

st.title("🧬 Sistema de Apoio ao Diagnóstico (SAD)")
st.write("""
Este sistema utiliza **Inteligência Artificial** para analisar parâmetros morfométricos 
de células mamárias e sugerir investigação citogenética.
""")

# 2. CARREGAR E TREINAR A IA (Roda em segundo plano)
@st.cache_resource # Isso faz a IA não precisar treinar toda vez que você clica
def treinar_modelo():
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    
    # Para a aula, vamos usar só os 4 principais fatores de risco para ficar visual
    features = ['mean radius', 'mean texture', 'mean smoothness', 'worst concave points']
    X = df[features]
    y = df['target']
    
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X, y)
    return modelo

modelo = treinar_modelo()

# 3. BARRA LATERAL (O "Microscópio Virtual")
st.sidebar.header("🔬 Parâmetros da Amostra")
st.sidebar.write("Ajuste as medidas conforme a lâmina:")

# Sliders para o usuário brincar
raio = st.sidebar.slider("Raio Médio do Núcleo", 6.0, 30.0, 14.0)
textura = st.sidebar.slider("Textura (Desvio Padrão)", 9.0, 40.0, 19.0)
suavidade = st.sidebar.slider("Suavidade (Smoothness)", 0.05, 0.2, 0.09)
concavidade = st.sidebar.slider("Pontos Côncavos (Irregularidade)", 0.0, 0.3, 0.04)

# Botão para analisar
if st.button("Analisar Lâmina"):
    
    # Criar o dataframe com os dados que o usuário escolheu
    dados_paciente = pd.DataFrame([[raio, textura, suavidade, concavidade]], 
                                  columns=['mean radius', 'mean texture', 'mean smoothness', 'worst concave points'])
    
    # A IA faz a previsão
    resultado = modelo.predict(dados_paciente)[0]
    probabilidade = modelo.predict_proba(dados_paciente)
    
    st.markdown("---") # Linha divisória
    
    # 4. EXIBIÇÃO DOS RESULTADOS
    if resultado == 1: # Benigno
        st.success("✅ DIAGNÓSTICO: NEGATIVO (Benigno)")
        st.write(f"Probabilidade de ser benigno: **{probabilidade[0][1]*100:.2f}%**")
        st.info("Conduta sugerida: Acompanhamento clínico de rotina.")
        
    else: # Maligno
        st.error("⚠️ DIAGNÓSTICO: POSITIVO (Maligno)")
        st.write(f"Certeza da IA: **{probabilidade[0][0]*100:.2f}%**")
        
        st.warning("🧬 ALERTA DE CITOGENÉTICA")
        st.write("Baseado na morfologia, o sistema sugere investigação dos seguintes alvos:")
        
        # Lógica do Cromossomo (A mesma que criamos antes)
        if raio > 20 or concavidade > 0.15:
            st.markdown("- **Gene BRCA1** (Cromossomo 17q21)")
            st.markdown("- **Gene TP53** (Cromossomo 17p13)")
            st.caption("Perfil de Alta Agressividade")
        else:
            st.markdown("- **Gene BRCA2** (Cromossomo 13q12)")
            st.markdown("- **Gene CHEK2** (Cromossomo 22)")
            st.caption("Perfil Moderado")

# Rodapé
st.markdown("---")
st.caption("Desenvolvido para a disciplina de Biomedicina - 1º Ano")