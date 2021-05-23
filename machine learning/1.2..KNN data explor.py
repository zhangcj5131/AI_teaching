# coding:utf-8
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris, fetch_20newsgroups
from sklearn.model_selection import train_test_split

'''
获取鸢尾花数据集
datasets.load_*(),获取小规模数据集，数据包含在datasets里

load和fetch返回的数据类型datasets.base.Bunch(字典格式)
    data：特征数据数组，是 [n_samples * n_features] 的二维 numpy.ndarray 数组
    target：标签数组，是 n_samples 的一维 numpy.ndarray 数组
    DESCR：数据描述
    feature_names：特征名,新闻数据，手写数字、回归数据集没有
    target_names：标签名
'''
iris = load_iris()
# print("鸢尾花数据集的返回值：\n", iris)
# print("鸢尾花的特征值:\n", iris["data"])
# print("鸢尾花的目标值：\n", iris.target)
# print("鸢尾花特征的名字：\n", iris.feature_names)
# print("鸢尾花目标值的名字：\n", iris.target_names)
# print("鸢尾花的描述：\n", iris.DESCR)

'''
datasets.fetch_*(data_home=None)
获取大规模数据集，需要从网络上下载，
data_home:表示数据集下载的目录,默认是 ~/scikit_learn_data/

sklearn.datasets.fetch_20newsgroups(data_home=None,subset=‘train’)
subset：'train'或者'test'，'all'，可选，选择要加载的数据集。
训练集的“训练”，测试集的“测试”，两者的“全部”
'''
news = fetch_20newsgroups(data_home='../data',subset='all', shuffle=True, random_state = 42)
print(type(news.data))
# print(news.target)

# 3.数据可视化
'''
seaborn.lmplot() 是一个非常有用的方法，它会在绘制二维散点图时，自动完成回归拟合
sns.lmplot() 里的 x, y 分别代表横纵坐标的列名,
data= 是关联到数据集,需要是 dataframe 类型
hue=*代表按照 species即花的类别分类显示,
fit_reg=是否进行线性拟合,默认是 False。
'''
def iris_plot(data, col1, col2):
    sns.lmplot(x=col1, y=col2, data=data, hue="target", fit_reg=True)
    plt.title("data explor")
    plt.show()


iris_db = pd.DataFrame(data=iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
iris_db["target"] = iris.target
print(iris_db.head())

#画图
iris_plot(iris_db, 'Sepal_Width', 'Petal_Length')

# 4.数据集的划分
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
# print("训练集的特征值是:\n", x_train)
# print("训练集的目标值是:\n", y_train)
# print("测试集的特征值是:\n", x_test)
# print("测试集的目标值是:\n", y_test)
#
# print("训练集的目标值的形状是:\n", y_train.shape)
# print("测试集的目标值的形状是:\n", y_test.shape)
