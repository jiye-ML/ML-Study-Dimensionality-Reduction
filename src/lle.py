# -*- coding: utf-8 -*-
"""
   LLE 降维算法， 局部线性嵌入： 试图保持领域内样本之间的线性关系。
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import   datasets,manifold

def load_data():
    '''
    加载用于降维的数据

    :return: 一个元组，依次为训练样本集和样本集的标记
    '''
    iris=datasets.load_iris()# 使用 scikit-learn 自带的 iris 数据集
    return  iris.data,iris.target

def test_LocallyLinearEmbedding(*data):
    '''
    测试 LocallyLinearEmbedding 的用法
    '''
    X,y=data
    for n in [4,3,2,1]:# 依次考察降维目标为 4维、3维、2维、1维
        lle=manifold.LocallyLinearEmbedding(n_components=n)
        lle.fit(X)
        print('reconstruction_error(n_components=%d) : %s'% (n, lle.reconstruction_error_))

def plot_LocallyLinearEmbedding_k(*data):
    '''
    测试 LocallyLinearEmbedding 中 n_neighbors 参数的影响，其中降维至 2维
    '''
    X,y=data
    Ks=[1,5,25,y.size-1]# n_neighbors参数的候选值的集合

    fig=plt.figure()
    for i, k in enumerate(Ks):
        lle=manifold.LocallyLinearEmbedding(n_components=2,n_neighbors=k)
        X_r=lle.fit_transform(X)#原始数据集转换到二维

        ax=fig.add_subplot(2,2,i+1)## 两行两列，每个单元显示不同 n_neighbors 参数的 LocallyLinearEmbedding 的效果图
        colors=((1,0,0),(0,1,0),(0,0,1),(0.5,0.5,0),(0,0.5,0.5),(0.5,0,0.5),
            (0.4,0.6,0),(0.6,0.4,0),(0,0.6,0.4),(0.5,0.3,0.2),)# 颜色集合，不同标记的样本染不同的颜色
        for label ,color in zip( np.unique(y),colors):
            position=y==label
            ax.scatter(X_r[position,0],X_r[position,1],label="target= %d"
            %label,color=color)

        ax.set_xlabel("X[0]")
        ax.set_ylabel("X[1]")
        ax.legend(loc="best")
        ax.set_title("k=%d"%k)
    plt.suptitle("LocallyLinearEmbedding")
    plt.show()

def plot_LocallyLinearEmbedding_k_d1(*data):
    '''
    测试 LocallyLinearEmbedding 中 n_neighbors 参数的影响，其中降维至 1维
    '''
    X,y=data
    Ks=[1,5,25,y.size-1]# n_neighbors参数的候选值的集合

    fig=plt.figure()
    for i, k in enumerate(Ks):
        lle=manifold.LocallyLinearEmbedding(n_components=1,n_neighbors=k)
        X_r=lle.fit_transform(X)#原始数据集转换到 1 维

        ax=fig.add_subplot(2,2,i+1)## 两行两列，每个单元显示不同 n_neighbors 参数的 LocallyLinearEmbedding 的效果图
        colors=((1,0,0),(0,1,0),(0,0,1),(0.5,0.5,0),(0,0.5,0.5),(0.5,0,0.5),
            (0.4,0.6,0),(0.6,0.4,0),(0,0.6,0.4),(0.5,0.3,0.2),)# 颜色集合，不同标记的样本染不同的颜色
        for label ,color in zip( np.unique(y),colors):
            position=y==label
            ax.scatter(X_r[position],np.zeros_like(X_r[position]),
            label="target= %d"%label,color=color)

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend(loc="best")
        ax.set_title("k=%d"%k)
    plt.suptitle("LocallyLinearEmbedding")
    plt.show()


if __name__=='__main__':
    X,y=load_data() # 产生用于降维的数据集
    test_LocallyLinearEmbedding(X,y)   # 调用 test_LocallyLinearEmbedding
    #plot_LocallyLinearEmbedding_k(X,y)   # 调用 plot_LocallyLinearEmbedding_k
    #plot_LocallyLinearEmbedding_k_d1(X,y)   # 调用 plot_LocallyLinearEmbedding_k_d1