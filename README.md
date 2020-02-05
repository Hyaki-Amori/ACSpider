# ACSpider
动画漫画爬虫API,数据源为漫画堆和樱花动漫,应用了python3.5+requests+selenium+phantomjs+flask

这是我为了做一个动漫搜索网站而写的爬虫API。(现已废弃)

7.29 更改获取动画地址的方式

7.28  添加动画爬虫,数据来源于樱花动漫


## 文件作用

### spider.py
爬虫类，可获取搜索页、详情页和章节页的必要数据

### api.py
API类，为爬虫类创建API

### spiderInDB.py
存储类，可将漫画堆的所有漫画的可用数据存入mysql数据库(除了漫画具体章节的图片，因为如果加了会使爬取时间变得非常长)

### comic_info.sql
存储类用到的数据表结构

## 存在的问题
小问题应该很多，这里只提下我认为比较大的问题
### Phantomjs 内存占用
Phantomjs在持续爬取的过程中内存占用会越来越大，使服务器崩掉。模拟浏览器关开标签或窗口、清除cookie、改用headless + Chrome都没太大作用，最后还是用了一个笨方法：爬到一定量网页就重启Phantomjs。不过还有问题，重启会阻塞数据的返回，我觉得可以把重启的代码放入新线程里，但是我不太会操作
### selenium 重试 
(7.21 已解决)
我不知道selenium有没有内置方法设置重试次数，所以在api.py中写了while来重试，但是好像不起作用，selenium的等待时间设短了就会直接报错
