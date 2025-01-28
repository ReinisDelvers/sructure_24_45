import pandas as pd # Failu apstrāde
import matplotlib.pyplot as plt # vizualizācija grafiki
import seaborn as sb # vizualizācijas

sb.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (15,10)

def heat_map(file):
    data_file = pd.read_csv(file).select_dtypes("number")
    sb.heatmap(data_file.corr(), annot=True, cmap="magma")
    plt.show()
    return

def distribution(file, colomn):
    data_file = pd.read_csv(file)
    sb.histplot(data_file[colomn], color="r")
    plt.show()


heat_map("masinmacisanas/data/auto_imports.csv")