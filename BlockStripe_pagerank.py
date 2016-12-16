# -*- coding: utf-8 -*-

import numpy as np
import time
from memory_profiler import profile

#分块的pagerank，每次只对edge的source和destination对应的r进行更新，不考虑等于0的边
@profile
def BlockStripe_pagerank(Parameter,threshold):
    r_old=r
    edge_num=len(edges)
    while(1):
        r_new=np.zeros(size)
        for edge in edges:
            r_new[edge[1]]=r_new[edge[1]]+r_old[edge[0]]*Parameter/out[edge[0]]
            
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
    
    edges=np.zeros(data.shape)
    out=np.zeros(size)
    i=0
    #将每条边对应到映射数组中，在block_stripe算法中使用
    for num in data:
        edges[i]=[index[num[0]],index[num[1]]]
        out[index[num[0]]]=out[index[num[0]]]+1
        i=i+1
    #测时间和内存
    start=time.clock()
    BlockStripe_pagerank(0.85,1e-8)
    end=time.clock()
    print('time2:%ss'%(end-start))
    
