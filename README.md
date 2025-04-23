# 🌎 Mapa do Índice de Gini por Município Brasileiro

Este projeto tem como objetivo visualizar a distribuição da desigualdade social no Brasil através do Índice de Gini por município, utilizando dados do Censo 2010 e as bibliotecas GeoPandas, Matplotlib e Pandas.

---

## 📌 Sobre o Projeto

Neste repositório, você encontrará:

- Processamento de dados geoespaciais dos municípios brasileiros  
- Visualização cartográfica do Índice de Gini  
- Customização de legendas e elementos visuais  
- Análise da distribuição da desigualdade por região  

---

## 🗂️ Estrutura dos Dados

A base de dados contém:

- `Município`: nome e código IBGE dos municípios brasileiros  
- `2010`: Valores do Índice de Gini calculado para o Censo de 2010  
- `codigo_ibge`: código numérico utilizado para o merge com os dados geográficos  

O shapefile contém informações geoespaciais como:

- `CD_MUN`: código do IBGE dos municípios  
- `NM_MUN`: nome do município  
- Geometrias de polígonos representando os limites municipais  

---

## 🗺️ Visualização

O mapa utiliza uma escala de cores **"coolwarm"**, onde:

- **Tons mais quentes (vermelhos)** representam maior desigualdade  
- **Tons mais frios (azuis)** representam menor desigualdade  
- Municípios **sem dados disponíveis** são exibidos em **cinza claro** com padrão hachurado  

---

## 📊 Tecnologias e Bibliotecas Utilizadas

- Pandas    
- GeoPandas  
- Matplotlib  

---

## 🧠 Insights

Através da visualização espacial do Índice de Gini, é possível identificar padrões regionais de desigualdade no Brasil. Estados das regiões Norte e Nordeste tendem a apresentar maiores índices, enquanto algumas áreas do Sul e Sudeste demonstram menor desigualdade relativa.

---

## 👤 Autor

**João Daniel Temporin**  
📍 Analista de Dados  
📬 [LinkedIn](https://www.linkedin.com/in/joao-temporin/)

---

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, estudar e modificar!
