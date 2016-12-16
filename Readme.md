Web大数据第一次大作业

Task: Compute the PageRank scores on the Wikipedia dataset.
Dataset: WikiData.txt (can be downloaded from cc.nankai.edu.cn)

The format of the lines in the file is as follow:
FromNodeID   ToNodeID

In this project, you need to report the Top 100 NodeID with their PageRank scores. You can choose different parameters, such as the teleport parameter, to compare different results. One result you must report is that when setting the teleport parameter is set to 0.85.

In addition to the basic PageRank algorithm, you need to implement the Block-Stripe Update algorithm (see pages 53-59 in the ppt of class 5: Link Analysis).
