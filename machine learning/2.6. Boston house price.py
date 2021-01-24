# coding: utf-8

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, RidgeCV
from sklearn.metrics import mean_squared_error

'''
1.获得数据
2.数据预处理
    2.1. 分割数据
3.特征工程,标准化
4.机器学习
5.模型评估
'''

def linear_model_equation():
    '''
    线性回归,正规方程的方法
    :return:
    '''
    print('正规方程')
    #1.获得数据
    boston = load_boston()
    #2.数据预处理
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=42)
    #3.特征工程,标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    #4.机器学习
    model = LinearRegression()
    model.fit(x_train, y_train)
    print('偏置:', model.intercept_)
    print('系数:', model.coef_)
    #5.模型评估
    y_pred = model.predict(x_test)
    mean_square = mean_squared_error(y_test, y_pred)
    print('square:', mean_square)


def linear_model_sgd():
    '''
    线性回归,随机梯度下降
    :return:
    '''
    #1.获得数据
    print('随机梯度下降')
    boston = load_boston()
    #2.数据预处理
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=42)
    #3.特征工程,标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    #4.机器学习
    #model = SGDRegressor(max_iter=1000, learning_rate="constant", eta0=0.01)
    model = SGDRegressor(max_iter=1000)
    model.fit(x_train, y_train)
    print('偏置:', model.intercept_)
    print('系数:', model.coef_)
    #5.模型评估
    y_pred = model.predict(x_test)
    mean_square = mean_squared_error(y_test, y_pred)
    print('square:', mean_square)


def linear_model_ridge():
    """
    线性回归:岭回归
    :return:
    """
    # 1.获取数据
    data = load_boston()

    # 2.数据集划分
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, random_state=22)

    # 3.特征工程-标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    # 4.机器学习-线性回归(岭回归)
    model = Ridge(alpha=1)
    # model = RidgeCV(alphas=(0.1, 1, 10))
    model.fit(x_train, y_train)

    # 5.模型评估
    # 5.1 获取系数等值
    y_predict = model.predict(x_test)
    # print("预测值为:\n", y_predict)
    print("模型中的系数为:\n", model.coef_)
    print("模型中的偏置为:\n", model.intercept_)

    # 5.2 评价
    # 均方误差
    error = mean_squared_error(y_test, y_predict)
    print("误差为:\n", error)

linear_model_equation()
print('*'*20)
linear_model_sgd()
print('*'*20)
linear_model_ridge()








