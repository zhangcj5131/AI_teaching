# coding: utf-8

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, RidgeCV
from sklearn.metrics import mean_squared_error
# from sklearn.externals import joblib
import joblib
'''
- from sklearn.externals import joblib
    - 保存：joblib.dump(estimator, 'test.pkl')
    - 加载：estimator = joblib.load('test.pkl')
    - 1.保存文件，后缀名是**.pkl
    - 2.加载模型是需要通过一个变量进行承接
'''


def load_dump_demo():
    """
    模型保存和加载
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
    try:
        # 4.3 模型加载
        estimator = joblib.load("../model/2.10.pkl")
    except:
        # 4.1 模型训练
        estimator = Ridge(alpha=1)
        estimator.fit(x_train, y_train)

        # 4.2 模型保存
        joblib.dump(estimator, "../model/2.10.pkl")

    # 5.模型评估
    # 5.1 获取系数等值
    y_predict = estimator.predict(x_test)
    # print("预测值为:\n", y_predict)
    print("模型中的系数为:\n", estimator.coef_)
    print("模型中的偏置为:\n", estimator.intercept_)

    # 5.2 评价
    # 均方误差
    error = mean_squared_error(y_test, y_predict)
    print("误差为:\n", error)


load_dump_demo()