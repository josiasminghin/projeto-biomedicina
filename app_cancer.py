import streamlit as st
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import base64
# Configuração da Página
st.set_page_config(
    page_title="SAD - BioOnco",
    page_icon="🏥",
    layout="wide"
)
import streamlit as st
import base64

# --- FUNÇÃO: ESTILO COMPLETO (VERSÃO INFALÍVEL PARA CELULAR) ---
def adicionar_fundo_local(imagem_arquivo):
    url_fundo_principal = "https://raw.githubusercontent.com/josiasminghin/projeto-biomedicina/main/fundo.jpg"
    
    st.markdown(
    f"""
    <style>
    /* 1. CONFIGURAÇÃO DO FUNDO PRINCIPAL */
    .stApp {{
        background-image: url("{url_fundo_principal}");
        background-attachment: fixed;
        background-size: cover;
        background-color: rgba(255,255,255,0.90);
        background-blend-mode: overlay;
    }}

    /* 2. CONFIGURAÇÃO DA BARRA LATERAL (MENU) */
    section[data-testid="stSidebar"] {{
        background-color: #f0f4f8 !important;
        border-right: 1px solid #d1d5db;
    }}

    /* 3. CORREÇÃO DE TEXTO GERAL */
    h1, h2, h3, h4, h5, h6, p, li, div, span, label {{
        color: #000000 !important;
    }}
    
    /* 4. AJUSTE PARA TEXTO DA BARRA LATERAL */
    [data-testid="stSidebar"] * {{
        color: #1a1a1a !important;
    }}

    /* 5. AJUSTE PARA CELULAR (Fundo) */
    @media only screen and (max-width: 600px) {{
        .stApp {{
            background-attachment: scroll;
            background-size: cover; 
        }}
    }}

    /* 6. LIMPEZA VISUAL (Rodapé e Botão Deploy) */
    footer {{visibility: hidden;}}
    .stDeployButton {{display:none;}}

    /* 7. CABEÇALHO (ESTRATÉGIA: TRANSPARÊNCIA, NÃO REMOÇÃO) */
    
    /* A barra superior continua existindo, mas fica invisível (transparente) */
    header[data-testid="stHeader"] {{
        background: transparent !important;
        z-index: 1 !important; /* Garante que fique acima do fundo */
    }}

    /* Removemos a linha colorida do topo (decoração) */
    [data-testid="stDecoration"] {{
        display: none !important;
    }}

    /* Escondemos APENAS os ícones da direita (Github, Menu, Deploy) */
    [data-testid="stToolbar"] {{
        display: none !important;
    }}
    
    /* Garantimos que o botão do menu (esquerda) tenha cor preta forte */
    /* E forçamos ele a ser visível */
    button[kind="header"] {{
        color: #000000 !important; /* Cor do ícone */
        background-color: transparent !important;
    }}
    
    [data-testid="baseButton-header"] {{
        color: #000000 !important;
    }}

    /* 8. CONTORNO PARA CAIXAS DE SELEÇÃO */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {{
        border: 1px solid #4b5563 !important;
        background-color: #ffffff !important;
        border-radius: 6px;
    }}
    
    </style>
    """,
    unsafe_allow_html=True
    )
# --- COMO USAR ---
# Tente carregar o fundo. Se não achar, ele avisa mas não quebra o site.
try:
    adicionar_fundo_local("fundo.jpg") 
except:
    pass # Se não tiver a imagem, fica com o fundo branco padrão
# --- FUNÇÃO: CARREGAR O GUIA DIDÁTICO (VERSÃO 5.0 - COMPLETA E CORRIGIDA) ---
def mostrar_guia_didatico():
    st.title("📚 Guia Didático e Base Científica")
    st.markdown("---")
    
   # AGORA SÃO 7 ABAS (Adicionamos "Sobre o Projeto")
    aba1, aba2, aba3, aba4, aba5, aba6, aba7 = st.tabs([
        "💉 O Exame (PAAF)",
        "📊 Estatísticas (IA)",
        "🔬 Tipos Histológicos",
        "🧬 Tipos Moleculares", 
        "💊 Tratamentos",
        "❓ Glossário",
        "📘 Sobre o Projeto"  # <--- NOVA ABA
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

    # --- ABA 3: ATLAS DE LÂMINAS (TIPOS HISTOLÓGICOS) ---
    with aba3:
        st.header("🔬 Atlas de Patologia: Tipos Histológicos")
        st.write("Visualização das diferenças morfológicas entre os principais tipos de câncer de mama..")
        
        # Seletor para escolher a lâmina
        tipo_cancer = st.selectbox(
            "Escolha o Tipo Histológico para ver a lâmina.:",
            ["Carcinoma Ductal In Situ (CDIS)", 
             "Carcinoma Lobular Invasivo", 
             "Carcinoma Inflamatório", 
             "Tecido Normal/Benigno"]
        )

        col_img, col_desc = st.columns([1, 1])

        with col_img:
            # Lógica para mostrar a imagem correta (lembre de subir os arquivos!)
            if tipo_cancer == "Carcinoma Ductal In Situ (CDIS)":
                try: st.image("ductal.jpg", caption="Microscopia: CDIS", use_column_width=True)
                except: st.warning("⚠️ Adicione a foto 'ductal.jpg' no GitHub.")
            
            elif tipo_cancer == "Carcinoma Lobular Invasivo":
                try: st.image("lobular.jpg", caption="Microscopia: Lobular Invasivo", use_column_width=True)
                except: st.warning("⚠️ Adicione a foto 'lobular.jpg' no GitHub.")

            elif tipo_cancer == "Carcinoma Inflamatório":
                try: st.image("inflamatorio.jpg", caption="Microscopia: Carcinoma Inflamatório", use_column_width=True)
                except: st.warning("⚠️ Adicione a foto 'inflamatorio.jpg' no GitHub.")
            
            else:
                try: st.image("Benigno.jpg", caption="Microscopia: Tecido Normal", use_container_width=True)
                except: st.warning("⚠️ Adicione a foto 'normal.jpg' no GitHub.")

        with col_desc:
            if tipo_cancer == "Carcinoma Ductal In Situ (CDIS)":
                st.subheader("Características")
                st.info("Cerca de 80% dos casos.")
                st.markdown("""
                * **Origem:** Revestimento dos ductos de leite.
                * **Comportamento:** Não invadiu o tecido adiposo ou vasos (ainda).
                * **Prognóstico:** Excelente se tratado cedo.
                * **Receptores:** Geralmente RE+ e RP+.
                """)
            
            elif tipo_cancer == "Carcinoma Lobular Invasivo":
                st.subheader("Características")
                st.warning("Cerca de 10-15% dos casos.")
                st.markdown("""
                * **Origem:** Lobos produtores de leite.
                * **Morfologia:** Células pequenas, redondas, em 'fila indiana' (crescimento linear).
                * **Dificuldade:** Mais difícil de ver na mamografia pois não forma um 'caroço' denso, mas sim um espessamento.
                """)

            elif tipo_cancer == "Carcinoma Inflamatório":
                st.subheader("Características")
                st.error("Raro (1-5%) e Agressivo.")
                st.markdown("""
                * **Sinais Clínicos:** Mama vermelha, inchada e quente (parece mastite).
                * **Morfologia:** Células tumorais bloqueiam os vasos linfáticos da pele (daí o inchaço).
                * **Classificação:** Todo inflamatório é considerado, no mínimo, Estágio III.
                """)
            
            else:
                st.success("Tecido Saudável / Benigno")
                st.markdown("""
                * Estruturas ductais e lobulares preservadas.
                * Membrana basal intacta.
                * Ausência de atipias nucleares (núcleos uniformes).
                """)
        
        st.markdown("---")
        with st.expander("📚 Aula: Como surge o Câncer (Oncogênese)"):
            st.markdown("""
            **1. A Mutação:** Células normais sofrem alterações no DNA devido a fatores hereditários ou ambientais (tabagismo, radiação, idade).
            
            **2. Perda de Controle:** Elas perdem a capacidade de parar de crescer (apoptose) e começam a se multiplicar desenfreadamente.
            
            **3. Angiogênese:** O tumor cria novos vasos sanguíneos para se "alimentar".
            
            **4. Invasão:** Elas produzem enzimas que destroem tecidos vizinhos e enganam o sistema imune.
            """)

    # --- ABA 4: GENÉTICA E BIOLOGIA MOLECULAR (ATUALIZADA) ---
    with aba4:
        st.header("🧬 Genética e Biologia Molecular")
        st.write("Mapeamento detalhado dos genes, cromossomos e vias de resistência.")

        # 1. OS GENES E CROMOSSOMOS (O CORAÇÃO DO PROJETO)
        st.subheader("🔍 Os Guardiões do DNA (Genes Supressores)")
        st.info("Clique nos cartões abaixo para entender a função e localização cromossômica.")

        col_g1, col_g2 = st.columns(2)

        with col_g1:
            # BRCA1
            with st.expander("🧬 BRCA1 (O Reparador Principal)"):
                st.error("📍 Localização: Cromossomo 17q21")
                st.markdown("""
                * **Função:** Repara danos no DNA (fita dupla).
                * **Risco:** Mutações aqui aumentam drasticamente o risco de câncer de mama (especialmente triplo-negativo) e ovário.
                * **Herança:** Autossômica dominante (basta um pai passar o gene).
                """)
            
            # TP53
            with st.expander("🛡️ TP53 (O Guardião do Genoma)"):
                st.error("📍 Localização: Cromossomo 17p13")
                st.markdown("""
                * **Função:** Sensor de estresse. Se o DNA quebra, ele para a célula para consertar ou manda ela se destruir (apoptose).
                * **O Perigo:** É o gene mais mutado em cânceres (>50%). Sem ele, a célula vira um "zumbi" imortal.
                * **Síndrome:** Li-Fraumeni.
                """)

        with col_g2:
            # BRCA2
            with st.expander("🧬 BRCA2 (O Consertador)"):
                st.warning("📍 Localização: Cromossomo 13q12")
                st.markdown("""
                * **Função:** Atua na recombinação homóloga junto com a proteína RAD51.
                * **Diferencial:** Fortemente ligado ao câncer de mama **masculino**, próstata e pâncreas.
                * **Importância:** Pacientes com essa mutação respondem bem a inibidores de PARP.
                """)

            # CHEK2
            with st.expander("👮 CHEK2 (O Inspetor de Segurança)"):
                st.info("📍 Localização: Cromossomo 22q12")
                st.markdown("""
                * **Função:** "Inspetor". Ele pausa a divisão celular se achar erros.
                * **Risco:** Moderado (aumenta 1.5x a 5x o risco).
                * **Variante Comum:** c.1100delC (comum no norte europeu).
                """)

        st.markdown("---")

        # 2. BIOMARCADORES E VIAS DE RESISTÊNCIA
        st.subheader("🔬 Biomarcadores e Vias de Resistência")
        
        tab_bio1, tab_bio2 = st.tabs(["Os 3 Pilares (RE/HER2/Ki67)", "A Via PI3K/AKT/mTOR"])
        
        with tab_bio1:
            st.markdown("""
            * **Receptor Hormonal (RH+):** A "fechadura" que usa estrogênio como combustível. (70% dos casos).
            * **HER2 (ERBB2):** O "acelerador" na membrana. Se positivo (3+), o tumor cresce rápido.
            * **Ki-67:** O velocímetro. Indica a taxa de proliferação celular.
            """)
        
        with tab_bio2:
            st.warning("⚠️ O Caminho da Resistência ao Tratamento")
            st.markdown("""
            **O Problema:** Mesmo tratando com hormonioterapia, o tumor pode "aprender" a sobreviver.
            
            **A Via PI3K / AKT / mTOR:**
            É uma via de sinalização intracelular que, quando **hiperativada**, funciona como um "plano B" para o tumor crescer mesmo sem hormônios.
            
            * **Mutações PIK3CA:** Ocorrem em ~40% dos casos RH+.
            * **Consequência:** O tumor ignora o bloqueio hormonal.
            * **Solução:** Usar inibidores específicos dessa via junto com o tratamento hormonal.
            """)
            
            # --- IMAGEM GERAL ---
            st.markdown("### 🖼️ Esquema da Via de Sinalização")
            try:
                st.image("imagem3.jpg", caption="Interação entre Via AKT e Ciclo Celular", use_column_width=True)
            except:
                st.warning("⚠️ Faltando arquivo: imagem3.jpg")
            
            # --- DETALHES E NOVA EXPLICAÇÃO ---
            with st.expander("🔎 Detalhes da Hiperativação e Consequências", expanded=True):
                
                # Colunas para Imagem 4 e 5
                col_v1, col_v2 = st.columns(2)
                with col_v1:
                    st.markdown("**1. Ativação da Cascata**")
                    try:
                        st.image("imagem4.jpg", use_column_width=True)
                    except:
                        st.warning("⚠️ Faltando: imagem4.jpg")
                        
                with col_v2:
                    st.markdown("**2. Proliferação Resultante**")
                    try:
                        st.image("imagem5.jpg", use_column_width=True)
                        st.caption("👀 **Obs:** As vias e sinais ilustrados em **roxo** representam a hiperativação.")
                    except:
                        st.warning("⚠️ Faltando: imagem5.jpg")

                st.markdown("---")
                
                # --- O TEXTO NOVO QUE VOCÊ PEDIU ---
                st.subheader("💥 Impactos da Hiperativação do AKT")
                
                st.write("""
                Uma vez que ocorre a hiperativação, a Via do AKT promove o **crescimento celular descontrolado** e a **sobrevivência celular**. 
                Esses processos permitem que as células cancerígenas evitem os mecanismos normais que levariam à sua morte (apoptose), resultando na progressão da doença.
                """)

                col_lista, col_impacto = st.columns(2)
                
                with col_lista:
                    st.markdown("##### 📉 Efeitos Posteriores")
                    st.markdown("""
                    A hiperativação amplifica a sinalização de muitos efeitos associados à resistência:
                    * 🔴 **Proliferação celular** aumentada.
                    * 🔄 **Progressão desregulada** do ciclo celular.
                    * ⬆️ Aumento do nível de **expressão do ER**.
                    * 📢 **Amplificação da sinalização** do ER.
                    """)
                
                with col_impacto:
                    st.info("""
                    **💡 Ponto Crítico:**
                    O impacto da hiperativação pode ser **independente do Receptor de Estrogênio (ER)**. 
                    
                    Isso significa que, mesmo bloqueando o estrogênio com remédios, a célula tumoral continua se dividindo através dessa via alternativa.
                    """)
   # --- ABA 5: TRATAMENTOS E MECANISMOS ---
    with aba5:
        st.header("💊 Tratamentos e Mecanismos de Ação")
        st.write("Da quimioterapia clássica à medicina de precisão.")

        # Explicação Didática: PARP e Letalidade Sintética
        st.subheader("🎯 Terapia Alvo e Mecanismo PARP")
        
        col_t1, col_t2 = st.columns([1, 2])
        
        with col_t1:
            st.info("**Conceito: Letalidade Sintética**")
            st.caption("Como matar o câncer usando a própria falha dele.")
        
        with col_t2:
            st.markdown("""
            **1. O Cenário:** Células com mutação BRCA já não consertam bem o DNA (falha na recombinação homóloga). Elas dependem de uma "muleta" chamada enzima **PARP** para sobreviver.
            
            **2. O Golpe (Inibidor de PARP):** O remédio (como Olaparibe) "chuta" essa muleta.
            
            **3. Resultado:** Sem BRCA (quebrado geneticamente) e sem PARP (bloqueado pelo remédio), o DNA da célula tumoral colapsa e ela morre. Células saudáveis sobrevivem porque ainda têm o BRCA funcionando.
            """)
            
            # --- ADICIONANDO AS IMAGENS DA PARP ---
            st.markdown("---")
            
            # Imagem 1
            try:
                st.image("parp_mecanismo.jpg", caption="Como a PARP repara o DNA normalmente", use_column_width=True)
            except:
                st.warning("⚠️ Imagem 'parp_mecanismo.jpg' não encontrada.")

            # Imagem 2
            try:
                st.image("parp_inibidor.jpg", caption="Ação do medicamento levando à morte celular", use_column_width=True)
            except:
                st.warning("⚠️ Imagem 'parp_inibidor.jpg' não encontrada.")

        # --- AQUI É O PULO DO GATO: VOLTAMOS A MARGEM DA ESQUERDA (FORA DA COLUNA) ---
        st.markdown("---")

        # Tabela Comparativa de Tratamentos
        st.subheader("⚖️ Comparativo de Terapias")
        
        st.markdown("""
        | Terapia | O que faz? | Exemplo |
        | :--- | :--- | :--- |
        | **Quimioterapia** | Mata tudo que cresce rápido (Bomba Atômica). | Doxorrubicina, Taxol. |
        | **Hormonioterapia** | Bloqueia o "combustível" (estrogênio). | Tamoxifeno, Anastrozol. |
        | **Terapia Alvo** | Ataca uma molécula específica (Tiro de Elite). | Trastuzumabe (Anti-HER2). |
        | **Imunoterapia** | Treina o sistema imune para atacar. | Pembrolizumabe. |
        | **Inibidor CDK4/6** | Trava o ciclo celular na fase G1. | Ribociclibe, Palbociclibe. |
        """)
           
   # --- ABA 6: GLOSSÁRIO ---
    with aba6:
        st.header("🔍 Glossário Técnico")
        st.markdown("""
        * **📏 Raio:** Tamanho do núcleo.
        * **🧵 Textura:** Variação de cor (sujeira).
        * **📐 Perímetro:** Contorno.
        * **🕳️ Concavidade:** Irregularidade da borda (amora).
        * **💪 Linfedema:** Inchaço crônico, geralmente no braço, por acúmulo de líquido.
        """)
     # --- ABA 7: METODOLOGIA (SOBRE O PROJETO) ---
    with aba7:
        st.header("📘 Metodologia Científica")
        st.write("A transparência é fundamental na ciência. Entenda a diferença entre o que a IA aprendeu sozinha e as regras médicas inseridas.")        
        st.markdown("---")
        col_met1, col_met2 = st.columns(2)
        
        with col_met1:
            st.info("### 🤖 1. Machine Learning (A IA)")
            st.markdown("""
            **O que ela faz:** Distingue Benigno de Maligno.            
            **Fonte de Dados:** *Breast Cancer Wisconsin (Diagnostic) Data Set*.            
            **Como funciona:**
            * Este banco de dados contém **apenas geometria** (números).
            * Ele **não** tem dados de DNA ou Genes.
            * A IA analisou milhares de casos reais e aprendeu padrões matemáticos, ex: *"Quando a área é grande (>800) e a concavidade é alta, 99% das vezes é Maligno".*
            
            ✅ **Nisso, ela é especialista.**
            """)

        with col_met2:
            st.warning("### ⚕️ 2. Conhecimento Médico (Regras)")
            st.markdown("""
            **O que ele faz:** Sugere Genes (BRCA1, BRCA2, TP53).            
            **Fonte de Dados:** Literatura Médica e Regras de Negócio.            
            **Como funciona:**
            * A sugestão dos genes **não veio do dataset**.
            * Foi uma **lógica biomédica** inserida no código (`if raio > 16...`).
            * **A Lógica:** Tumores com morfologia agressiva (núcleos gigantes/deformados) estatisticamente têm maior correlação com mutações severas (BRCA1/TP53). Tumores menores sugerem perfil Luminal/BRCA2.            
            ⚠️ **Isso é uma inferência clínica, não um teste genético.**
            """)
        
        st.markdown("---")
        st.success("### 🎯 Resumo da Metodologia")
        st.markdown("""
        O sistema combina duas inteligências:
        1.  **Artificial:** Para ler a geometria e dar o diagnóstico visual.
        2.  **Humana (Biomédica):** Para correlacionar essa geometria com prováveis mutações genéticas baseadas na agressividade do fenótipo.
        """)
        # --- AQUI COMEÇA A NOVA PARTE DO AUTOR (Linha 369 em diante) ---
        st.markdown("---")  # Linha divisória
        
        st.header("👤 Sobre o Autor")
        
        col_autor_img, col_autor_info = st.columns([1, 3])
        
        with col_autor_img:
            # Foto de Perfil (lembre de subir perfil.jpg no GitHub)
            url_perfil = "https://raw.githubusercontent.com/josiasminghin/projeto-biomedicina/main/perfil.jpg"
            st.image(url_perfil, width=180, caption="Josias Minghin")
            
        with col_autor_info:
            st.markdown("""
            ### Josias Minghin
            **🎓 Estudante de Biomedicina**
            
            **🏛️ UNIP - Universidade Paulista (EAD Flex)** *2º Semestre | São José do Rio Preto - SP*
            
            ---
            
            **🎯 Objetivo do Projeto:**
            Este sistema foi desenvolvido como portfólio acadêmico, integrando **Patologia Digital**, **Genética Molecular** (BRCA1/2) e **Inteligência Artificial** para auxiliar no estudo e diagnóstico do Câncer de Mama.
            """)
            
            # Botão de contato
            st.link_button("✉️ Entre em Contato (Email)", "mailto:josiasmarques@gmail.com")
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
    st.sidebar.caption("Ajuste os valores com precisão ou deslize:")

    # --- FUNÇÃO MÁGICA DE SINCRONIZAÇÃO (CORRIGIDA) ---
    def criar_controle(label, min_v, max_v, default_v, key_base, step_v, help_txt=None):
        # 1. Cria a memória inicial se não existir
        if f'{key_base}_val' not in st.session_state:
            st.session_state[f'{key_base}_val'] = default_v

        # 2. Callback: Quando muda o NÚMERO, força o SLIDER a mudar
        def update_from_num():
            new_val = st.session_state[f'{key_base}_num']
            st.session_state[f'{key_base}_val'] = new_val
            st.session_state[f'{key_base}_slide'] = new_val # <--- FORÇA O SLIDER

        # 3. Callback: Quando muda o SLIDER, força o NÚMERO a mudar
        def update_from_slider():
            new_val = st.session_state[f'{key_base}_slide']
            st.session_state[f'{key_base}_val'] = new_val
            st.session_state[f'{key_base}_num'] = new_val # <--- FORÇA O NÚMERO

        # 4. Renderiza a CAIXINHA (Input)
        val = st.sidebar.number_input(
            label, 
            min_value=float(min_v), 
            max_value=float(max_v), 
            value=float(st.session_state[f'{key_base}_val']),
            step=step_v,
            key=f'{key_base}_num',
            on_change=update_from_num, # Chama a função que atualiza tudo
            help=help_txt
        )

        # 5. Renderiza a BARRINHA (Slider)
        st.sidebar.slider(
            "Ajuste Visual",
            min_value=float(min_v), 
            max_value=float(max_v), 
            value=float(st.session_state[f'{key_base}_val']),
            key=f'{key_base}_slide', 
            on_change=update_from_slider, # Chama a função que atualiza tudo
            label_visibility="collapsed"
        )
        
        return val

    # --- CRIAÇÃO DOS CONTROLES ---
    raio_medio = criar_controle("📏 Raio Médio", 6.0, 30.0, 14.0, "raio", 0.1, "Média Benigno: ~12.1 | Maligno: ~17.4")
    textura_media = criar_controle("🧶 Textura (Desvio)", 9.0, 40.0, 19.0, "textura", 0.1)
    perimetro_medio = criar_controle("⭕ Perímetro", 40.0, 190.0, 90.0, "perimetro", 0.5)
    area_media = criar_controle("🔵 Área Nuclear", 140.0, 2500.0, 600.0, "area", 10.0)
    smoothness = criar_controle("💧 Suavidade", 0.05, 0.25, 0.09, "suavidade", 0.001)
    concavidade = criar_controle("🕳️ Concavidade", 0.0, 0.5, 0.04, "concavidade", 0.001)

    # --- CÁLCULOS ESSENCIAIS (NÃO REMOVER) ---
    area_calculada = area_media
    if raio_medio > 15.0 and area_media < 700:
        area_calculada = 3.1415 * (raio_medio ** 2)

    compactness = concavidade
    concave_points = concavidade
    fractal_dimension = 0.06
    symmetry = 0.18

    # --- PREVISÃO ---
    input_data = [
        raio_medio, textura_media, perimetro_medio, area_calculada, smoothness,
        compactness, concavidade, concave_points, symmetry, fractal_dimension,
        0.5, 1.0, 3.0, 40.0, 0.005, 
        0.02, 0.02, 0.01, 0.02, 0.004,
        raio_medio * 1.2, textura_media, perimetro_medio * 1.2, area_calculada * 1.2, smoothness,
        compactness, concavidade, concave_points, symmetry, fractal_dimension
    ]

    prediction = model.predict([input_data])[0]
    probability = model.predict_proba([input_data])[0]

    # --- EXIBIÇÃO ---
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

   # ... (o resto do código continua igual) ...

    # ... (o resto do código continua igual) ...

    with col2:
        st.markdown("### Resumo")
        st.metric(label="Classificação", value="Maligno" if prediction == 0 else "Benigno")
        
        # Barra de progresso (Malignidade)
        prob_maligno = int(probability[0]*100)
        st.progress(prob_maligno)
        st.caption(f"Prob. Malignidade: {prob_maligno}%")
        
        st.markdown("---")

        # --- GERAÇÃO DO LAUDO (COM FUSO HORÁRIO CORRIGIDO) ---
        from datetime import datetime, timedelta
        
        # 1. Ajuste de Fuso Horário (UTC para Brasília)
        # O servidor está em UTC (+0), o Brasil está em UTC (-3)
        fuso_brasil = timedelta(hours=3)
        data_hora_atual = datetime.now() - fuso_brasil
        data_formatada = data_hora_atual.strftime("%d/%m/%Y às %H:%M")
        
        # 2. Definir o texto do resultado
        resultado_texto = "MALIGNO" if prediction == 0 else "BENIGNO"
        
        # 3. Criar o conteúdo do arquivo de texto
        laudo_texto = f"""
🏥 SAD - BioOnco | Relatório de Análise Computacional
=====================================================
Data da Emissão: {data_formatada}
Responsável Técnico: Josias Minghin (Acad. Biomedicina)

🔬 PARÂMETROS DA AMOSTRA (MICROSCOPIA):
-----------------------------------------------------
- Raio Médio:       {raio_medio:.2f}
- Textura (Desvio): {textura_media:.2f}
- Perímetro:        {perimetro_medio:.2f}
- Área Nuclear:     {area_media:.2f}
- Suavidade:        {smoothness:.3f}
- Concavidade:      {concavidade:.3f}

🧠 ANÁLISE DE INTELIGÊNCIA ARTIFICIAL:
-----------------------------------------------------
>> CLASSIFICAÇÃO:   {resultado_texto}
>> PROBABILIDADE:   {probability[0 if prediction == 0 else 1]*100:.1f}% de certeza

📋 NOTA TÉCNICA:
Este relatório é gerado por algoritmos de Machine Learning 
(Random Forest) baseado no Dataset Wisconsin. 
Não substitui o diagnóstico clínico ou histopatológico.
=====================================================
"""
        # 4. Botão de Download
        st.download_button(
            label="📄 Baixar Laudo Completo",
            data=laudo_texto,
            file_name=f"Laudo_BioOnco_{data_hora_atual.strftime('%Y%m%d_%H%M')}.txt",
            mime="text/plain"
        )
# --- CONTROLE DE NAVEGAÇÃO (COLE ISTO NO FINAL DO ARQUIVO) ---
# Aqui criamos o menu lateral que troca as telas
st.sidebar.markdown("---") # Uma linha separadora antes do menu
st.sidebar.title("Menu Principal")
navegacao = st.sidebar.radio("Ir para:", ["🤖 Sistema Diagnóstico (IA)", "📚 Guia Didático: Tipos e Tratamentos"])

if navegacao == "🤖 Sistema Diagnóstico (IA)":
    mostrar_diagnostico_ia()
else:
    mostrar_guia_didatico()

# Rodapé
st.sidebar.markdown("---")
st.sidebar.info("Desenvolvido por Josias Minghin\nBiomedicina 1º Ano")









































































