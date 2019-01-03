[详细介绍：https://blog.csdn.net/l598465252/article/details/81100127](https://blog.csdn.net/l598465252/article/details/81100127)

## 使用方法
将该项目下载到本地，本地需要使用`Linux`操作系统，直接放服务器上也可以。
下载完之后先删除`.git`文件夹
```bash
git clone git@github.com:YES-Lee/git_painter.git && cd git_painter && rm -rf .git // 可以直接下载zip在解压

```
重新初始化git
```bash
git init
git add .
git commit -m 'init'

```

然后执行loop脚本刷记录，等待结束
```bash
python loop.py

```

GitHub，将该项目推上去，然后就可以到GitHub上看效果啦
```bash
git remote add origin {仓库地址}
git push -u origin master

```

在服务器部署自动commit
```bash
crontab -e
#  输入以下代码，前两个参数分别是分钟和小时，该任务为每天12:00定时执行
# 00 12 * * * cd /home/git_heart && git pull && /usr/bin/python main.py

```

## 参数说明
`main.py`用于在服务端执行定时任务的脚本，`loop.py`用来刷之前的记录
```python
#  loop.py
#  自定义图形
PATTEN = [  # 图形矩阵，可以通过修改该变量来设置不同的图形，行建议最多不超过7行
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
]


# 修改提交次数，次数越多颜色越深，耗时也越长
def commit(flag):
    if flag:
        for n in range(39):
            with open('./record.txt', 'a') as record:
                record.write('.~^~')
                record.close()
                os.system('git commit -a -m \"HeartBeat\"')
...

# 开始日期，在GitHub主页查看左上角日期
START_DATE = '2017-7-16'  # 开始日期, 码云和git显示不一样, 建议从最左上角开始
...

```

## 才过的坑
* GitHub将项目删除后记录也会随之消失，但是码云不会（码云已经被我弄的一团糟）
* GitHub从上到下是周日到周六，码云是周一到周日，两个要分别重选时间`commit`

## 图形展示
* 小心心❤️
```json
[
  [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
  [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
]
```
![heart](./static/heart.png)

* X(原谅鄙人想象力不够丰富)
```json
[
  [0, 0, 0, 0, 0],
  [1, 0, 0, 0, 1],
  [0, 1, 0, 1, 0],
  [0, 0, 1, 0, 0],
  [0, 1, 0, 1, 0],
  [1, 0, 0, 0, 1],
  [0, 0, 0, 0, 0]
]
```
![heart](./static/x.png)

> **此项目始于无聊，终于装逼，仅供娱乐，请勿用于其他操作**
