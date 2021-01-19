from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

'''
sklearn.neighbors.KNeighborsClassifier(n_neighbors=5,algorithm='auto')
n_neighbors：int,可选（默认= 5），k_neighbors查询默认使用的邻居数
algorithm：{‘auto’，‘ball_tree’，‘kd_tree’，‘brute’}
auto:默认参数，可以理解为算法自己决定合适的搜索算法
brute:是蛮力搜索，也就是线性扫描，当训练集很大时，计算非常耗时。
kd_tree:数据维度 20 以下时效率最好,构造kd树存储数据以便对其进行快速检索的树形数据结构，kd树也就是数据结构中的二叉树。以中值切分构造的树，每个结点是一个超矩形。
ball tree:是为了克服kd树高维失效而发明的，其构造过程是以质心C和半径r分割样本空间，每个节点是一个超球体。
'''

# 1.获取数据集
iris = load_iris()

# 2.数据基本处理
x_train, x_test, y_train, y_test \
    = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)

# 3、特征工程：标准化,注意,对训练集用fit_transform,测试集用transform
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)


# 4、机器学习(模型训练)
estimator = KNeighborsClassifier(n_neighbors=9)
estimator.fit(x_train, y_train)
# 5、模型评估
# 方法1：比对真实值和预测值
y_predict = estimator.predict(x_test)
print("预测结果为:\n", y_predict)
print("比对真实值和预测值：\n", y_predict == y_test)
# 方法2：直接计算准确率
score = estimator.score(x_test, y_test)
print("准确率为：\n", score)

