# Importação das bibliotecas
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Carregar os dados de Gini
gini_por_municipio = pd.read_excel('ginibr.xlsx')

# Extrai os códigos da coluna "Município", insere em uma nova coluna "codigo_ibge" e transforma no tipo Int
gini_por_municipio['codigo_ibge'] = gini_por_municipio['Município'].str[:6]
gini_por_municipio['codigo_ibge'] = gini_por_municipio['codigo_ibge'].astype(int)

# Carregar o shapefile dos municípios do Brasil
shapefile_path = './BR_Municipios_2023.shp'
gdf = gpd.read_file(shapefile_path)

# Extrai os 6 primeiros dígitos da coluna "CD_MUN"
gdf["CD_MUN"] = gdf["CD_MUN"].str[:6]
gdf['CD_MUN'] = gdf['CD_MUN'].astype(int)

# Unir o DataFrame com o GeoDataFrame usando o código do IBGE
gdf = gdf.merge(gini_por_municipio, left_on='CD_MUN', right_on='codigo_ibge', how='outer')

# Cria a figure e o axis onde será inserido o mapa
fig, ax = plt.subplots(1, 1, figsize=(15, 15))

# Posicionando a legenda mais à esquerda
cax = fig.add_axes([0.01, 0.3, 0.02, 0.4]) 

# Plotando o mapa
gdf.plot(
    column=2010,  # Coluna do índice de Gini
    ax=ax,
    legend=True,
    legend_kwds={
        'orientation': "vertical",
        'cax': cax
    },
    cmap='coolwarm',
    linewidth=0.1,
    edgecolor='gray',
    missing_kwds={
        "color": "lightgray",
        "edgecolor": "gray",
        "hatch": "///",
        "label": "Sem dado de Gini"
    }
)

# Remove as linhas dos eixos
ax.set_axis_off()

# Insere o título 
ax.set_title('Mapa do Índice de Gini por Município Brasileiro (2010)', font='Poppins', fontsize=20)

# Insere a Fonte
fig.text(0.03, 0.03, 'Fonte: Índice de Gini da renda domiciliar per capita segundo Município - Censo IBGE 2010', font='Poppins', fontsize=10, ha='left')

# Ajuste para garantir que o tight_layout não afete a posição da legenda
plt.tight_layout(rect=[0.03, 0, 1, 1])

plt.show()
