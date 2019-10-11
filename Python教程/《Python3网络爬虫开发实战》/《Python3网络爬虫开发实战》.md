《Python3网络爬虫开发实战》笔记
--------------

网络爬虫与反爬措施

https://github.com/Python3WebSpider

## 1开发环境配置

### 1.1 Python3安装

### 1.2 请求库安装

#### requests
`sudo pip3 install requests`

#### selenium
`sudo pip3 install selenium`      selenium 是自动化测试工具，需要浏览器配合使用


##### Mac 中python3的两个库地址问题
/usr/local/lib/python3.7/site-packages
/Library/Python/3.7/site-packages


`python3 -m pip install -U selenium` 安装在前者
`sudo pip3 install selenium` 安装在后者

#### PhantomJS

PhantomJS是一个无界面的、可脚本编程的WebKit浏览器引擎，它原生支持多种Web标准：DOM操作、CSS选择、JSON、Canvas以及SVG。
？？

#### aiohttp 

aiohttp是相对于 requests库的一个异步Web服务端的库

`python3 -m pip install -U aiohttp`

`python3 -m pip install -U cchardet aiodns`
cchardet是字符编码检测库，aiodns是加速DNS的解析库

