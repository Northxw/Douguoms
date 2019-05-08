## 豆果美食APP菜谱

&emsp; 抓取豆果美食APP菜谱分类数据（参考：某课网app抓取实战）



## 抓取流程

1. 进入豆果美食菜谱分类，抓取所有分类
2. 进入细分的分类菜谱，抓取"做过最多"的菜谱。例如"热门 -> 热门食材 -> 小龙虾 -> 做过最多"。
3. 进入详情页，抓取tips，cookstep，填充至菜谱字典并插入到数据库



## 环境依赖

```python
pip3 install -r requirements.txt
```



## 运行

```python
python main.py
```

