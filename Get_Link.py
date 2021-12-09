import numpy as np
from sympy import *
from bs4 import BeautifulSoup
np.seterr(divide='ignore', invalid='ignore')

def text_save(filename, data):
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'  #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

def get_all_links(path, save_link_file_name, save_name_link_file_name):
    # 用于连接每期集数与每期的名字
    join_str = '_'
    # 存放所有标题与链接的字典
    all_episodes = {}
    # 存放所有链接的列表
    links_list = []
    # 存放名称与链接的列表
    episodes_name_lin_list = []

    # 打开并读取php文件
    phpFile = open(path, 'r', encoding='utf-8')
    phpHandle = phpFile.read()

    soup = BeautifulSoup(phpHandle, 'lxml')

    for dt in soup.select('dt'):
        # 获取本周标题下的第一个链接用于下载
        for sibling in dt.next_siblings:
            if sibling != "\n":
                if sibling.has_attr('data-src'):
                    link = sibling['data-src']
                    break
        
        # 获取当前周的标题与集数
        episode_number = dt.find('span', attrs={'class':'textBold'}).text
        episodes_name = dt.select('div')
        for episode in episodes_name:
            episode = episode.get_text(strip=True, separator='\n').splitlines()
            # 使用下划线连接当前集数的所有名称
            episode_name = episode_number + '_' + join_str.join(episode)
    
        # 添加集数标题与链接到字典中
        all_episodes[episode_name] = link
        
    # 添加链接到列表中
    for name in all_episodes:
        # 将链接单独保存在一个列表中
        links_list.append(all_episodes[name])
        # 将标题与链接按空格隔开放在一个列表中
        current_episode = name + ' ' + all_episodes[name]
        episodes_name_lin_list.append(current_episode)

    # 保存链接到txt文件里
    text_save(save_link_file_name, links_list)
    # 同时保存标题与链接到txt文件里
    text_save(save_name_link_file_name, episodes_name_lin_list)

# 主程序
get_all_links('index.php','2021_All_Episodes_Links.txt', '2021_All_Episodes.txt')