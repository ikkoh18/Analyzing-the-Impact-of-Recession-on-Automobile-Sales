# 📉 Analyzing the Impact of Recession on Automobile Sales

### *Final Project – Data Visualization & Dashboarding*

Este projeto foi desenvolvido como parte da análise de dados da empresa **XYZAutomotives**, com o objetivo de entender como períodos de recessão impactaram as vendas de automóveis ao longo dos anos.
O projeto utiliza **Python**, **Pandas**, **Matplotlib**, **Seaborn**, **Folium**, **Plotly** e **Dash** para criar visualizações e dashboards interativos.

---

## 🧠 Objetivo Geral

Analisar o comportamento das vendas de automóveis da XYZAutomotives durante diferentes períodos históricos de recessão e comunicar os achados por meio de gráficos e dashboards interativos.

O projeto é dividido em duas partes:

### ✔️ **Part 1 – Data Visualization**

Criar visualizações usando Pandas, Matplotlib, Seaborn e Folium.

### ✔️ **Part 2 – Dash & Plotly Dashboard**

Construir um dashboard interativo para permitir que diretores explorem os dados por ano, categoria e cenários de recessão.

---

# 📂 Dataset

O dataset utilizado é sintético e inclui:

* **Date**
* **Recession** (0 = normal, 1 = recessão)
* **Automobile_Sales**
* **GDP**
* **Unemployment_Rate**
* **Consumer_Confidence**
* **Seasonality_Weight**
* **Price**
* **Advertising_Expenditure**
* **Vehicle_Type**
* **Competition**
* **Month, Year**

### 🕒 Períodos de Recessão (dados do projeto)

* 1980
* 1981–1982
* 1991
* 2000–2001
* 2007–2009
* 2020 (Fev–Abr – COVID-19)

---

# 🧩 Part 1 – Tasks & Visualizations

### **TASK 1.1 – Line Chart:**

Mostrar variação anual das vendas de automóveis.

### **TASK 1.2 – Line Chart por Vehicle Type:**

Comparar tendências e detectar diferenças durante recessões.

### **TASK 1.3 – Seaborn Visualization:**

Comparar vendas por tipo de veículo entre períodos de recessão e não recessão.

### **TASK 1.4 – Subplots (GDP):**

Comparar variações de GDP em períodos de recessão vs. períodos normais.

### **TASK 1.5 – Bubble Plot:**

Impacto da sazonalidade nas vendas.

### **TASK 1.6 – Scatter Plot:**

Relação entre preço médio e volume de vendas durante recessões.

### **TASK 1.7 – Pie Chart:**

Distribuição dos gastos com publicidade em recessão vs. não recessão.

### **TASK 1.8 – Pie Chart por Vehicle Type:**

Gasto total com publicidade por tipo de veículo durante recessões.

### **TASK 1.9 – Line Plot:**

Efeito da taxa de desemprego nas vendas durante recessões.

---

# 📊 Part 2 – Dash & Plotly Dashboard

### **TASK 2.1 – Criar aplicação Dash**

Título e estrutura inicial.

### **TASK 2.2 – Dropdowns interativos**

Filtro por:

* Ano
* Estatística
* Período (Recession / Non-Recession)
* Vehicle Type

### **TASK 2.3 – Divs para saída**

Estrutura para os gráficos e mensagens.

### **TASK 2.4 – Callbacks**

Funções para atualizar gráficos dinamicamente.

### **TASK 2.5 – Recession Report Dashboard**

Gráficos como:

* Sales
* GDP
* Unemployment
* Advertising

### **TASK 2.6 – Yearly Statistics Dashboard**

Vendas por ano, comparações e métricas exploráveis.

---

# ▶️ Como Executar o Projeto

### **1. Instale as dependências**

```bash
pip install -r requirements.txt
```

### **2. Abra o notebook da Parte 1**

```bash
jupyter notebook DV0101EN-Final-Assign-Part1.ipynb
```

### **3. Execute o Dashboard (Parte 2)**

```bash
python app.py
```

Acesse no navegador:

```
http://127.0.0.1:8050/
```

---

# 📈 Resultados Esperados

✔️ Entendimento profundo de como recessões impactam vendas
✔️ Comparação entre tipos de veículos
✔️ Métricas econômicas correlacionadas às vendas
✔️ Dashboard interativo para análise exploratória
✔️ Visualizações salvas para submissão no curso



