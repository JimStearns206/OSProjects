# Modify PYTHONPATH appropriately to find pandas development version.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

print("pandas version = {}, from={}".format(pd.__version__, pd.__file__))
print("python version = {}".format(sys.version))

def is_grid_on(axes):
    """
    From pandas/tests/plotting/common.py._check_grid_settings._is_grid_on

    :return: True if plot has grid on else False
    """
    xoff = all(not g.gridOn
               for g in axes.xaxis.get_major_ticks())
    yoff = all(not g.gridOn
               for g in axes.yaxis.get_major_ticks())
    return not (xoff and yoff)

dataset = np.random.rand(10,5)
df = pd.DataFrame(dataset, columns=['A', 'B', 'C', 'D', 'E'])
figsize=(3,2)

# Matplotlib boxplot
fig = plt.figure(1, figsize=figsize)
ax = fig.add_subplot(111)
bp = ax.boxplot(dataset)
print(f"Figure size (inches) = {fig.figsize}, dpi={fig.dpi}.")
result_plt_boxplot = plt.boxplot(dataset)
fig.savefig('plt_boxplot.png')
plt.show()
assert not is_grid_on(ax)

# Pandas plot(kind='box)
#df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])

result_plot_kind_box = df.plot(kind='box', figsize=figsize)
plt.show()
result_plot_kind_box.get_figure().savefig('pd_plot_kind_box.png')
assert not is_grid_on(result_plot_kind_box.axes)

# Pandas boxplot
result_boxplot = df.boxplot(return_type='axes', figsize=figsize)
plt.show()
result_boxplot.get_figure().savefig('pd_boxplot.png')
assert not is_grid_on(result_boxplot.axes)
