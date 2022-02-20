# 哆啦A梦番剧下载链接获取
![](https://github.com/HuangRunHua/Doraemon-Video-Download/blob/main/cover.png)
本项目用于哆啦A梦番剧视频下载链接的获取，使用Python实现该功能。

## 网页文件获取
在使用本程序获取视频下载链接之前，需要先获取哆啦A梦番剧视频所在的网页文件，通常为`.php`文件。获取方式可以利用Chrome浏览器。在Chrome浏览器上打开[哆啦A梦新番在线合集](https://www.dora-family.com/index.php?title=Resource:TV&variant=zh)显示并下载网页源代码，将源代码文件保存至`Doraemon Video Download`文件夹下。
![](https://github.com/HuangRunHua/Doraemon-Video-Download/blob/main/phpfile.png)

## 程序的使用方式
在`Get_Link.py`文件的最末尾，修改`get_all_links`函数里的参数名称，该函数三个参数意义分别表示如下：
```python
def get_all_links(path, save_link_file_name, save_name_link_file_name):
```

- path: `.php`文件所在的位置，mac下为该文件的名称
- save_link_file_name: 保存txt文件的路径，该文件只保存下载地址，并不保存每一集的名字
```
https://cdn3.dora-video.cn/0b2emuaaiaaaa4anekfmqrqvazodarsqabaa.f0.mp4
https://cdn3.dora-video.cn/0bc3r4abeaaasyabm2nkqnqvbd6dckhqaeqa.f0.mp4
http://cdn3.dora-video.cn/0bc3gaaakaaac4adypm2kzqvamgdauyaabia.f0.mp4
https://cdn2.dora-video.cn/5K
https://cdn2.dora-video.cn/5G
```
- save_name_link_file_name: 保存txt文件的路径，该文件同时保存每一集的名字与下载地址，按空格隔开。
```
683_哆啦A梦与帕门_大预言·地球的毁灭之日 https://cdn3.dora-video.cn/0b2emuaaiaaaa4anekfmqrqvazodarsqabaa.f0.mp4
682_广阔的日本_重建破旧旅馆 https://cdn3.dora-video.cn/0bc3r4abeaaasyabm2nkqnqvbd6dckhqaeqa.f0.mp4
681_大雄与大雄_谎话成真扩音器 http://cdn3.dora-video.cn/0bc3gaaakaaac4adypm2kzqvamgdauyaabia.f0.mp4
680_无人境饮料_叶子侦探大雄 https://cdn2.dora-video.cn/5K
679_持续喷雾_训练棒球吧！ https://cdn2.dora-video.cn/5G
678_真实的日本一周特快列车大富翁游戏_静香SOS https://cdn2.dora-video.cn/5F
677_骨川大师的手工DIY_主角嵌入机 https://cdn2.dora-video.cn/5D
```

## 注意⚠️
本代码爬取的链接并非均能成功下载视频，只有部分链接可以下载。同时本代码为本人个人使用并非商用，任何形式的盈利手段均为非法的，还望周知。
