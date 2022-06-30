import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
i=0
G=list()
for i in range(0,10000):
    x = list()
    x.append(np.random.normal(0,1,10))
    a=np.max(x)
    b=np.mean(x)
    c=np.std(x)
    G.append((a-b)/c)
    i +=1

def get_quartiles(result_list, quartile_numer):
    '''
    result_list：是待计算的分位数的数列，用list表示
    quartile_numer：是要计算的分位数的比例
    '''
    result_list = sorted(result_list)
    num = len(result_list)
    ly = (num + 1) * quartile_numer
    ly_int, ly_decimal = int(ly), ly - int(ly)
    # 使用插入法调整相应的数字，百分位数的值，可能就不在原来的序列中了
    return result_list[ly_int - 1] + (result_list[ly_int] - result_list[ly_int - 1]) * ly_decimal
print(get_quartiles(G, 0.95))

sns.distplot(G, hist=False, kde=False, fit=stats.norm, fit_kws={'color':'blue','label':'u=2,s=3','linestyle':'-'})
plt.show()


#2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
i=0
G=list()
for i in range(0,10000):   #随机模拟数为10000次
    x = list()
    x.append(np.random.normal(0,1,10))   #模拟标准正太分布抽样10次
    a=np.max(x)
    b=np.mean(x)
    c=np.std(x)
    G.append((a-b)/c)    #计算G
    i +=1
#计算G的P=0.95分位数
def get_quartiles(result_list, quartile_numer):
#是待计算的分位数的数列，用list表示
#quartile_numer：是要计算的分位数的比例
    result_list = sorted(result_list)
    num = len(result_list)
    ly = (num + 1) * quartile_numer
    ly_int, ly_decimal = int(ly), ly - int(ly)
    return result_list[ly_int - 1] + (result_list[ly_int] - result_list[ly_int - 1]) * ly_decimal
print(get_quartiles(G, 0.95))
#显示直方图与核密度图
sns.distplot(G)
plt.show()







