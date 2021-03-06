# cs231n学习记录
## 2017
在ubuntu中配置cs231n所需要的环境（Jupyter notebook etc.）
学习版本控制git，push作业到github
看完cs231n视频和notes

## 2018.1.30
完成assignment1中knn.ipynb（交叉验证技巧 numpy操作）

## 2018.2.1
完成assignment1中svm.ipynb（numpy向量化操作 svm损失函数实践  SGD实践）（判断准确率为39%）

## 2018.2.1
完成assignment1中softmax.ipynb（类比svm的实现 交叉验证超参数 softmax损失函数实践）（判断准确率为37%）

## 2018.2.3
完成assignment1中2-layers-network.ipynb（Relu 前向传播 反向传播（配合维度相容原则快速判断）softmax作为loss function 超参数调优) (判断准确率为52%）
**ps: 双层神经网络可以逼近任何连续函数（强大之处）**

## 2018.2.3
完成assignment1中的feature.ipynb（特征工程可有效提高模型的准确率：线性svm准确率达到42%， 两层神经网络准确率达到58%）

## 2018.2.4
完成assignment2中的fullyconnectednet.ipynb（模块化编程 参数矩阵预生成 参数最优化方法：动量方法 学习率退火 RMSProp Adam）

## 2018.2.6
完成assignment2中的batchnorm.ipynb，给全连接神经网络添加BN层（batchnorm可有效提高收敛速和模型的泛化能力）

## 2018.2.6
完成assignment2中dropout.ipynb，给全连接神经网络激活层后添加dropout处理，提高了模型的泛化能力，在测试集上准确率提升。

## 2018.2.8
完成assignment2中convolutionalnetworks.ipynb（卷积神经网络Python完成 类似fcnet）

## 2018.2.9
配置tensorflow-GPU（配置cuda9-0, 默认cuda9.1不支持tensorflow，需降版本  添加环境变量 cudnn7-0-5 anaconda中配置tensorflow）
学习tensorflow document, stanford cs20

## 2018.2.10
完成assignment2中tensorflow.ipynb（用gpu并行计算conv-relu-bn-pool-affine-relu-dropout-affine-softmax架构， 准确率达到70.6%，且具备良好的泛化能力）
