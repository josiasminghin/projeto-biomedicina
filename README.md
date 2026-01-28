# 🧬 BioOnco - Sistema de Apoio ao Diagnóstico (SAD)

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://projeto-biomedicina-ew7lwpouxmvuayqxndlu24.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Nota:** Este projeto foi desenvolvido para fins acadêmicos na disciplina de Biomedicina e TICs.

## 🏥 Sobre o Projeto
O **BioOnco** é uma ferramenta de **Patologia Digital** que utiliza Inteligência Artificial (Machine Learning) para auxiliar na classificação citológica de células mamárias. O sistema analisa parâmetros morfométricos nucleares para estimar a probabilidade de malignidade e sugerir protocolos de investigação genética (ex: mutações em *BRCA1* e *BRCA2*).

### 🎯 Funcionalidades
* **Diagnóstico Preditivo:** Classificação binária (Benigno/Maligno) em tempo real.
* **Análise Biométrica:** Processamento de dados como Raio, Textura, Perímetro e Concavidade Nuclear.
* **Correlação Genética:** Sugestão automática de exames citogenéticos baseada no fenótipo celular.
* **Laudo Inteligente:** Geração de relatórios com condutas médicas sugeridas baseadas em diretrizes clínicas.

---

## 🧠 Tecnologia e IA
O "cérebro" do sistema utiliza o algoritmo **Random Forest Classifier** da biblioteca Scikit-Learn.
* **Dataset Utilizado:** [Breast Cancer Wisconsin (Diagnostic) Data Set](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)).
* **Acurácia do Modelo:** ~96% (nos testes de validação).
* **Inputs:** O modelo recebe 30 parâmetros vetoriais, sendo 6 controláveis pelo usuário via interface.

---

## 🚀 Como Executar Localmente

### Pré-requisitos
* Python 3.8 ou superior
* Git

### Passo a Passo
1. Clone o repositório:
   ```bash
   git clone [https://github.com/josiasminghin/projeto-biomedicina.git](https://github.com/josiasminghin/projeto-biomedicina.git)
