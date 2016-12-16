# -*- coding: utf-8 -*-

import numpy as np
import time
from memory_profiler import profile

#basic_pagerank，用转移矩阵运算
@profile
def basic_pagerank(Parameter,threshold):
    r_old=r
    while(1):
        r_new=np.dot(r_old,M)*Parameter
        r_sum=sum(r_new)
        r_sub=np.ones(size)*(1-r_sum)/size
        r_now=r_new+r_sub
        s=np.sqrt(sum((r_now-r_old)**2))
        if(s<=threshold):
            r_old=r_now
            break
        else:
            r_old=r_now
    print_result(r_old)
    
def print_result(r_now):
    r_index=r_now.argsort()[::-1][:100]
    r_now.sort()
    r_now=r_now[::-1][:100]
    top_index=np.zeros(100)
    for i in range(100):
        top_index[i]=ind[r_index[i]]
        print top_index[i],r_now[i]

if __name__=='__main__':

    #读取文件
    data = np.loadtxt('WikiData.txt')
    #获取数据大小
    row,col=data.shape
    ind=list(data.flatten())
    #找出所有点
    ind=np.unique(ind)
    dead_ends=list(set(data[:,1]).difference(set(data[:,0])))
    ind=[int(i) for i in ind]
    #找出最大点的下标
    Max=max(ind)
    index=np.zeros(Max+1)
    node_num=len(ind)
    for i in range(len(ind)):
        index[ind[i]]=i
    ind.sort()
    #初始化所有r的值为1.0/size
    size=len(ind)
    graph=np.zeros((size,size))
    r=np.ones(size)*1.0/size
    r=r.T
    
    #邻接矩阵
    for i in range(row):
        m=data[i][0]
        n=data[i][1]
        m_ind=index[m]
        n_ind=index[n]
        graph[m_ind][n_ind]=graph[m_ind][n_ind]+1

    graph_sum=np.sum(graph,axis=1)
    #计算M，在basic算法中使用
    M=np.zeros((size,size))
    for i in range(size):
        if graph_sum[i]!=0:
            M[i]=np.true_divide(graph[i],graph_sum[i])
    #测时间和内存
    start=time.clock()
    basic_pagerank(0.85,1e-8)
    end=time.clock()
    print('time1:%ss'%(end-start))
    

    
