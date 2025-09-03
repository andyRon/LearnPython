[PyQt编程快速上手](https://book.douban.com/subject/36337901/)
---

PyQt是一个创建GUI应用程序的工具包，是Python编程语言和Qt库的成功融合。





## 1 PyQt基础

### 1.1 安装



```
pip3 install pyqt5==5.15.4

pip3 install pyqt5==5.15.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
```



安装预编译的 PyQt5 轮子：

```
pip3 install pyqt5 -i https://pypi.tuna.tsinghua.edu.cn/simple --only-binary :all:
```





### 1.2 设计一个简单的PyQt窗口



### 1.3 布局管理

#### 1.3.1 使用move()方法布局





#### 1.3.2 垂直布局管理器QVBoxLayout





#### 1.3.3 水平布局管理器QHBoxLayout





#### 1.3.4 表单布局管理器QFormLayout



#### 1.3.5 网格布局管理器QGridLayout



### 1.4 信号和槽

信号和槽机制是PyQt中各个对象之间的通信基础。

#### 1.4.1 理解信号和槽机制

红灯信号发射后，行人就会停下；当绿灯信号发射后，行人就会前进。我们用red和green来表示信号，用stop()和go()函数来表示行人的动作，这两个函数也被称为槽函数。也就是说，当red信号发射后，stop()槽函数就会被调用；当green信号发射后，go()槽函数会被调用。不过信号和槽只有在连接之后才可以起作用，连接方式如图1-21所示。

在图1-21中，widget就是PyQt中的控件对象，signal就是控件对象拥有的信号，connect()方法用于连接信号和槽，而slot是槽函数名称。我们参考上面的红绿灯例子，了解代码中的连接方式：

```python
traffic_light.red.connect(stop)
traffic_light.green.connect(go)
```

![](images/image-20250903193312143.png)

red信号和stop()槽函数进行连接，green信号和go()槽函数进行连接，只有这样连接后，发射的信号才可以调用相应的槽函数。总结起来就一句话：连接后，信号发射，槽函数“启动”。

> 在connect()方法中传入的是函数名。

#### 1.4.2 一个信号连接一个槽



#### 1.4.3 一个信号连接多个槽



#### 1.4.4 多个信号连接一个槽



#### 1.4.5 信号与信号连接



#### 1.4.6 自定义信号



### 1.5 学会使用文档

