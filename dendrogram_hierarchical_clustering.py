import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch

dataset = pd.read_excel('Car Inventory.xlsx', sheet_name='Car Inventory') 
df = dataset.iloc[:, [4, 5]].values


dendrogram = sch.dendrogram(sch.linkage(df, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()