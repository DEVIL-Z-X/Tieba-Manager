# Tieba-Manager

[![gitee](https://img.shields.io/badge/mirror-gitee-red)](https://gitee.com/Starry-OvO/Tieba-Manager)
[![release](https://img.shields.io/github/release/Starry-OvO/Tieba-Manager?color=blue&logo=github)](https://github.com/Starry-OvO/Tieba-Manager/releases)
[![license](https://img.shields.io/github/license/Starry-OvO/Tieba-Manager?color=blue&logo=github)](https://github.com/Starry-OvO/Tieba-Manager/blob/master/LICENSE)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Starry-OvO/Tieba-Manager?logo=lgtm)](https://lgtm.com/projects/g/Starry-OvO/Tieba-Manager/context:python)

## 功能概览

+ 按回复时间/发布时间/热门序获取贴吧主题帖/精华帖列表。支持获取带转发/投票/转发嵌套投票/各种卡片的主题帖信息
+ 获取带图片链接/小尾巴内容/点赞情况/用户信息（用户名/user_id/portrait/等级/性别/是否锁回复）/每条回复的前排楼中楼（支持按或不按点赞数排序）的回复列表
+ 获取带所有前述用户信息的楼中楼列表
+ 根据`用户名` `昵称` `portrait` `user_id`中的任一项反查其他用户信息
+ 使用小吧主、语音小编的`BDUSS`删帖/屏蔽/封禁任意用户3天或10天
+ 使用已被大吧主分配解封/恢复/处理申诉权限的吧务`BDUSS`解封/恢复/处理申诉。支持一键拒绝所有解封申诉
+ 使用大吧主`BDUSS`推荐帖子到首页/移动帖子到指定分区/加精/撤精/置顶/撤置顶/添加黑名单/查看黑名单/取消黑名单
+ 获取用户主页信息/关注贴吧列表/关注用户列表/粉丝列表/发帖历史/回复历史
+ 获取贴吧最新关注用户列表/等级排行榜/吧务列表/吧详情
+ 使用`BDUSS`关注贴吧/取关贴吧/关注用户/取关用户/移除粉丝/签到/水帖/发送私信

## 入门使用

+ 确保你的[`Python`](https://www.python.org/downloads/)版本在`3.9`及以上

+ 拉取代码并安装依赖

```bash
git clone https://github.com/Starry-OvO/Tieba-Manager.git
cd ./Tieba-Manager
pip install -r requirements.txt
```

+ 依序运行教程脚本`tutorial-*.py`，参考注释学习用法

## 若要开启云审查功能

+ 参考`config/config_full_example.yaml`中的注释完成对`database`字段的配置，你需要一个`MySQL`数据库用来缓存通过检测的内容id以及记录用户权限级别（黑、白名单）。配置完成的`config/config.yaml`如下所示

```yaml
BDUSS:
  starry: ABCDEFGai2LdUd5TTVHblhFeXoxdGyOVURGUE1OYzNqVXVRaWF-HnpGckRCNFJnRVFBQUFBJCQAAAAAAAAAAAEAAADiglQb0f3Osqmv0rbJ2QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMN6XGDDelxgc

database:
  host: 127.0.0.1
  port: 3306
  user: root
  password: 123456
```

+ 使用函数`Database.init_database()`一键建库，如下例所示

```python
import asyncio

import aiotieba as tb


async def main():
    async with tb.Reviewer() as brow:
        await brow.database.init_database(["贴吧名1", "贴吧名2"])

asyncio.run(main())
```

+ 自定义审查行为：请参照我给出的例子自己编程修改[`cloud_review_hanime.py`](https://github.com/Starry-OvO/Tieba-Manager/blob/master/cloud_review_hanime.py)，这是被实际应用于[宫漫吧](https://tieba.baidu.com/f?ie=utf-8&kw=%E5%AE%AB%E6%BC%AB)的云审查工具
+ 运行`cloud_review_yours.py`。对`Windows`平台，建议使用`pythonw.exe`无窗口运行，对`Linux`平台，建议使用如下的`nohup`指令在后台运行

```bash
nohup python cloud_review_yours.py >/dev/null 2>&1 &
```

## 友情链接

+ [指令管理器wiki](https://github.com/Starry-OvO/Tieba-Manager/wiki/%E6%8C%87%E4%BB%A4%E7%AE%A1%E7%90%86%E5%99%A8%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E%E4%B9%A6)
+ [另一个仍在活跃更新的贴吧管理器（有用户界面）](https://github.com/dog194/TiebaManager)
+ [用户反馈（我的个人吧）](https://tieba.baidu.com/f?ie=utf-8&kw=starry)

## 用户名单

云审查工具&指令管理器已在以下贴吧应用（2022.06.21更新，按启用时间先后排序）

|      吧名      | 关注用户数 | 最近29天日均访问量 | 日均主题帖数 | 日均回复数 |
| :------------: | :--------: | :----------------: | :----------: | :--------: |
| vtuber自由讨论 |   16,358   |       3,299        |      3       |     75     |
|     asoul      |  159,984   |      150,910       |    1,461     |   18,114   |
|      嘉然      |   54,218   |       32,692       |     283      |   4,477    |
|      宫漫      | 1,248,996  |       48,395       |     292      |   3,397    |
|    lol半价     | 1,937,015  |      140,253       |     530      |   8,236    |
|     孙笑川     | 1,945,177  |      506,735       |    5,767     |  144,181   |
|    新孙笑川    |  225,184   |       40,095       |     396      |   12,213   |
|      向晚      |   27,550   |       29,137       |     309      |   3,944    |
|      贝拉      |   21,206   |       18,006       |      85      |   1,724    |
|    王力口乐    |   12,548   |       42,922       |     442      |   5,877    |
|      乃琳      |   16,570   |       9,406        |      64      |   1,043    |
| asoul一个魂儿  |   15,127   |       5,039        |      68      |    932     |
|     贝贝珈     |   1,660    |       1,373        |      9       |    117     |
