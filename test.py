# coding: utf-8
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, fetch_20newsgroups
from sklearn.model_selection import train_test_split

iris = load_iris()
# print("鸢尾花数据集的返回值：\n", iris)
# print("鸢尾花的特征值:\n", iris["data"])
# print("鸢尾花的目标值：\n", iris.target)
# print("鸢尾花特征的名字：\n", iris.feature_names)
# print("鸢尾花目标值的名字：\n", iris.target_names)
# print("鸢尾花的描述：\n", iris.DESCR)


news = fetch_20newsgroups(data_home='./data', subset='all', shuffle=True, random_state = 42)

def iris_plot(data, col_name1, col_name2):
    sns.lmplot(x=col_name1, y=col_name2, data=data, hue='target', fit_reg=True)
    plt.title('data explore')
    plt.show()

iris_db = pd.DataFrame(data=iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
iris_db['target'] = iris.target
print(iris_db.head())

iris_plot(iris_db, 'Sepal_Width', 'Petal_Length')

x_train, x_test, y_train, y_test = train_test_split(iris_db.iloc[:,:-1], iris_db.iloc[:,-1], random_state=42, test_size=0.2)
print(x_train)