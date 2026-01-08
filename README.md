# Page View Time Series Visualizer (Visualizador de Séries Temporais de Visualizações de Página)


## Sobre
Este é um projeto desenvolvido como parte do curso "Data Analysis with Python" da [freeCodeCamp](www.freecodecamp.org).

O objetivo é usar Pandas, Matplotlib e Seaborn para limpar, analisar e visualizar dados de visualizações de páginas diárias do fórum freeCodeCamp.

## Estrutura

*   **Pré-processamento de Dados:** Limpeza de outliers (2.5% menores e maiores).
*   **Gráfico de Linha:** Exibe as visualizações diárias ao longo do tempo.
*   **Gráfico de Barras:** Mostra a média mensal de visualizações agrupadas por ano.
*   **Box Plots (Gráficos de Caixa):** Visualiza a distribuição anual e mensal das visualizações de página.

 ## Instrução

1.  Clone este repositório (e certifique-se de ter o arquivo `fcc-forum-pageviews.csv` no mesmo diretório):
    ```bash
    git clone github.com
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd page-view-time-series-visualizer
    ```
3.  Instale as bibliotecas necessárias: pandas, matplotlib e seaborn:
    ```bash
    pip install pandas matplotlib seaborn numpy
    ```
4.  Execute o arquivo `main.py` para rodar a análise e gerar os gráficos:
    ```bash
    python3 main.py
    ```


## Arquivos no Projeto

*   `time_series_visualizer.py`: Contém as funções de análise e plotagem (`draw_line_plot`, `draw_bar_chart`, `draw_box_plot`).
*   `main.py`: Arquivo de exemplo para testar as funções e salvar as imagens geradas.
*   `fcc-forum-pageviews.csv`: O conjunto de dados utilizado na análise.


## Licença e Créditos

Licença MIT. Disponível para modificação e distribuição livre, desde que atribua os créditos ao autor original.

## Autor
- **GitHub:** [trsilva23]
- **E-mail:** [trsilva23.contato@gmail.com] 

