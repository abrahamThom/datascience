import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris=pd.read_csv("iris.csv")
sns.displot(iris['sepal.length'],kde=True,rug=True)
plt.title("Distribution of Sepal length")
plt.show()
sns.histplot(iris['petal.width'],kde=True,bins=20)
plt.title("Histogram of Petal width")
plt.show()
sns.relplot(x="sepal.length",y="sepal.width",data=iris,hue="variety",style="variety")
plt.title("Sepal Length v/s Sepal Width")
plt.show()
