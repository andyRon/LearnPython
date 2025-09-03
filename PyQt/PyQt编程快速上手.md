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



## 2 PyQt的基础控件

### 2.1 标签控件QLabel

#### 2.1.1 显示文本



#### 2.1.2 显示图片



#### 2.1.3 显示动图





### 2.2 消息框控件QMessageBox

#### 2.2.1 各种类型的消息框

![](images/image-20250903200209860.png)



#### 2.2.2 与消息框交互



#### 2.2.3 编写带中文按钮的消息框



### 2.3 文本框控件

#### 2.3.1 单行文本框控件QLineEdit



#### 2.3.2 文本编辑框控件QTextEdit



#### 2.3.3 文本浏览框控件QTextBrowser



### 2.4 各种按钮控件

#### 2.4.1 普通按钮控件QPushButton



#### 2.4.2 工具按钮控件QToolButton



#### 2.4.3 单选框按钮控件QRadioButton



#### 2.4.4 复选框按钮控件QCheckBox



#### 2.4.5 下拉框按钮控件QComboBox





### 2.5 与数字相关的控件

#### 2.5.1 液晶数字控件QLCDNumber



#### 2.5.2 数字调节框控件QSpinBox和QDoubleSpinBox



#### 2.5.3 滑动条控件QSlider



#### 2.5.4 仪表盘控件QDial





### 2.6 与日期相关的控件

#### 2.6.1 日历控件QCalendarWidget



#### 2.6.2 日期时间控件QDateTimeEdit



### 2.7 定时器控件和进度条控件

#### 2.7.1 定时器控件QTimer



#### 2.7.2 进度条控件QProgressBar



## 3 PyQt的高级控件

之所以称它们为高级控件，是因为它们在用法上更有难度，通常需要联系到其他模块，开发者要注意的点也会更多。

### 3.1 组合框控件和工具箱控件

#### 3.1.1 分组框控件QGroupBox



#### 3.1.2 工具箱控件QToolBox



### 3.2 滚动区域控件和滚动条控件

#### 3.2.1 滚动区域控件QScrollArea



#### 3.2.2 滚动条控件QScrollBar



### 3.3 更多容器控件

#### 3.3.1 拆分窗口控件QSplitter



#### 3.3.2 标签页控件QTabWidget



#### 3.3.3 堆栈控件QStackedWidget





#### 3.3.4 多文档区域控件QMdiArea



### 3.4 列表视图控件、树形视图控件、表格视图控件

#### 3.4.1 列表视图控件QListView





#### 3.4.2 树形视图控件QTreeView





#### 3.4.3 表格视图控件QTableView





### 3.5 简化版的列表、树形、表格视图控件

#### 3.5.1 简化版列表视图控件QListWidget





#### 3.5.2 简化版树形视图控件QTreeWidget





#### 3.5.3 简化版表格视图控件QTableWidget







### 3.6 各种对话框控件

#### 3.6.1 颜色对话框控件QColorDialog



#### 3.6.2 字体对话框控件QFontDialog



#### 3.6.3 输入对话框控件QInputDialog



#### 3.6.4 文件对话框控件QFileDialog





## 4 深入窗口





## 5 Qt Designer



## 6 PyQt高级应用



## 7 图形视图框架



## 8 打包



## 9 可视化爬虫



## 10 贪吃蛇

