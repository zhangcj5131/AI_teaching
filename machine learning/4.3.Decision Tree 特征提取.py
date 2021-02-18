from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import jieba
def dict_demo():
    """
    对字典类型的数据进行特征抽取
    :return: None
    """
    data = [{'city': '北京','temperature':100}, {'city': '上海','temperature':60}, {'city': '深圳','temperature':30}]
    # 1、实例化一个转换器类
    transfer = DictVectorizer(sparse=True)
    # 2、调用fit_transform
    data = transfer.fit_transform(data)
    print("返回的结果:\n", data)
    # 打印特征名字
    print("特征名字：\n", transfer.get_feature_names())

    return None


def english_count_demo():
    data = ["Lucky is a cat, he is my pet", "Lucky is a lovely cat, he dislike fish"]
    transfer = CountVectorizer(stop_words=['is'])
    data = transfer.fit_transform(data)
    print("文本特征抽取的结果,toarray：\n", data.toarray())
    # print("文本特征抽取的结果：\n", data)
    print("返回特征名字：\n", transfer.get_feature_names())

def cut_word(text):
    return " ".join(jieba.cut(text))

def chinese_count_demo(data):
    text_list = []
    for sent in data:
        text_list.append(cut_word(sent))
    print(text_list)
    transfer = CountVectorizer()
    # 2、调用fit_transform
    data = transfer.fit_transform(text_list)
    print("文本特征抽取的结果：\n", data.toarray())
    print("返回特征名字：\n", transfer.get_feature_names())



if __name__ == '__main__':
    # dict_demo()
    # english_count_demo()
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]

    chinese_count_demo(data)