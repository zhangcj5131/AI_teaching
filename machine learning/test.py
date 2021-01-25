# coding: utf-8

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, RidgeCV
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib






def linear_model_ridge():
    boston = load_boston()
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=42)

    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    try:

        model =joblib.load('../model/test.pkl')
        print('the model is successfully restored')
    except:
        print('the model does not exist, we have to train a new one')
        model = Ridge(alpha=0.1)

        model.fit(x_train, y_train)
        joblib.dump(model, '../model/test.pkl')



    print('偏置', model.intercept_)
    print('系数', model.coef_)

    y_pred = model.predict(x_test)
    error = mean_squared_error(y_test, y_pred)
    print('square error:', error)





linear_model_ridge()