# main.py para testar as funções de visualização localmente
from time_series_visualizer import draw_line_plot, draw_bar_chart, draw_box_plot
import matplotlib.pyplot as plt

# Gera o gráfico de linha e salva
fig_line = draw_line_plot()
fig_line.savefig('line_plot.png')
print("line_plot.png salvo.")

# Gera o gráfico de barras e salva
fig_bar = draw_bar_chart()
fig_bar.savefig('bar_chart.png')
print("bar_chart.png salvo.")

# Gera os box plots e salva
fig_box = draw_box_plot()
fig_box.savefig('box_plot.png')
print("box_plot.png salvo.")

# plt.show() # Descomente para visualizar as janelas dos gráficos localmente
