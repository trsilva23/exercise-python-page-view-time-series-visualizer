import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

# Necessário para que o matplotlib use corretamente as datas no eixo X
register_matplotlib_converters()

def import_and_clean_data():
    # Lê o arquivo CSV
    df = pd.read_csv(
        'fcc-forum-pageviews.csv',
        parse_dates=['date'], # Converte a coluna 'date' para datetime já na leitura
        index_col='date'     # Define 'date' como índice do DataFrame
    )

    # Limpeza de dados: Filtra os 2.5% menores e maiores valores de page views
    # Usamos loc para selecionar apenas as linhas que estão dentro do intervalo percentil
    df = df.loc[
        (df['value'] >= df['value'].quantile(0.025)) & 
        (df['value'] <= df['value'].quantile(0.975))
    ]
    return df

def draw_line_plot():
    # Usa os dados limpos
    df = import_and_clean_data()
    df = df.copy() # Cria uma cópia para evitar SettingWithCopyWarning em alguns ambientes

    # Configura a figura e eixos do Matplotlib
    fig, ax = plt.subplots(figsize=(15, 6))
    
    # Plota a linha usando o índice (data) no eixo X e 'value' (page views) no eixo Y
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    
    # Define os títulos e rótulos
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Retorna o objeto figure
    return fig

def draw_bar_chart():
    # Usa os dados limpos
    df = import_and_clean_data()
    df_bar = df.copy() # Cria uma cópia para trabalhar

    # Adiciona colunas de ano e mês para agrupar
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    # Agrupa por ano e mês e calcula a média (mean) de page views
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    # Converte a série agrupada de volta para um DataFrame para facilitar o plot
    df_bar = df_bar.unstack(level='month')

    # Define a ordem correta dos meses para o plot
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                    'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar[months_order]

    # Desenha o gráfico de barras
    fig = df_bar.plot(kind='bar', figsize=(10, 8)).get_figure()
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    
    # Retorna o objeto figure
    return fig

def draw_box_plot():
    # Usa os dados limpos
    df = import_and_clean_data()
    df_box = df.copy() # Cria cópia

    # Prepara os dados adicionando colunas para ano e meses curtos
    df_box['year'] = [d.year for d in df_box.index]
    df_box['month'] = [d.strftime('%b') for d in df_box.index] # Formato curto (Jan, Feb, etc)

    # Cria uma figura com dois subplots lado a lado
    fig, axes = plt.subplots(1, 2, figsize=(20, 8))

    # Box plot Anual (esquerda)
    sns.boxplot(ax=axes[0], x='year', y='value', data=df_box)
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Box plot Mensal (direita)
    # Define a ordem correta para os meses curtos
    month_order_short = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(ax=axes[1], x='month', y='value', data=df_box, order=month_order_short)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    # Retorna o objeto figure
    return fig
