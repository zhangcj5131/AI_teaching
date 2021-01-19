import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

'''
sklearn.preprocessing.MinMaxScaler (feature_range=(0,1)… )
    MinMaxScalar.fit_transform(X)
    X:numpy array格式的数据[n_samples,n_features]
    feature_range: 期待转换后数据的分布范围,默认是(mi=0,mx=1)
返回值：转换后的形状相同的array
x'=(x-min)/(max-min)
x'' = x'*(mx-mi)+mi
'''
def minmax_demo():
    """
    归一化演示
    :return: None
    """
    data = pd.read_csv("../data/dating.txt")
    print(data)
    # 1、实例化一个转换器类
    transfer = MinMaxScaler(feature_range=(2, 3))
    # 2、调用fit_transform
    data = transfer.fit_transform(data[['milage','Liters','Consumtime']])
    print("最小值最大值归一化处理的结果：\n", data)

    return None


"""
sklearn.preprocessing.StandardScaler( )
    处理之后每列来说所有数据都聚集在均值0附近标准差差为1
    StandardScaler.fit_transform(X)
    X:numpy array格式的数据[n_samples,n_features]
    返回值：转换后的形状相同的array
"""
def stand_demo():
    """
    标准化演示
    :return: None
    """
    data = pd.read_csv("../data/dating.txt")
    print(data)
    # 1、实例化一个转换器类
    transfer = StandardScaler()
    # 2、调用fit_transform
    data = transfer.fit_transform(data[['milage','Liters','Consumtime']])
    print("标准化的结果:\n", data)
    print("每一列特征的平均值：\n", transfer.mean_)
    print("每一列特征的方差：\n", transfer.var_)

    return None


# minmax_demo()
stand_demo()