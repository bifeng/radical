path = "C:\\Users\\kiss\\radical\\rule\\"

with open(path + 'tdlr_tag_word_guess.txt',encoding='utf-8') as f1:
    tag_files = f1.readlines()
tag_dict = {}
last_keys = None
for each in tag_files:
    each_ = each.strip()
    if each_:
        if each_.startswith('t_') and each_ not in tag_dict.keys():
            tag_dict[each_] = []
            last_keys = each_
        else:
            tag_dict[last_keys].append(each_)

tag_dict_freq={}
for key,value in tag_dict.items():
    new_value = []
    for v in value:
        new_value.append(v + ' ' + str(10**len(v)))
    tag_dict_freq[key] = new_value

dict_for_jieba =[leaf for branch in list(tag_dict_freq.values()) for leaf in branch]
ftag = open(path + 'tag_dict.txt','w')
ftag.write('\n'.join(dict_for_jieba))
ftag.close()

# DAG - 有向无环图
import jieba
jieba.set_dictionary(dictionary_path='.\\rule\\tag_dict.txt')
jieba.get_dict_file()
sentence='两个人上下摞起来是什么字'
jieba.get_DAG(sentence)
list(jieba.cut(sentence, cut_all=False, HMM=False))
['两个', '人', '上', '下', '摞起来', '是', '什么字']
list(jieba.cut(sentence, cut_all=False, HMM=True))
['两个', '人上', '下', '摞起来', '是', '什么字']
list(jieba.cut(sentence, cut_all=True, HMM=False))
['两个', '人', '上', '下', '摞起来', '是', '什么字']


# 最大匹配方法


# 最小切分


