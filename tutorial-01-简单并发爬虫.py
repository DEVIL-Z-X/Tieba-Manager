"""
本例中，你将学会使用aiotieba库和asyncio.gather并发地完成两个网络请求
请认真阅读注释
"""

import asyncio

import aiotieba as tb


async def main():
    # 使用键名"default"对应的BDUSS创建客户端
    async with tb.Client("default") as brow:
        # 下面这行语句会同时请求用户个人信息和图拉丁吧首页前30帖
        # asyncio.gather会自动创建任务来同时运行两个协程brow.get_self_info和brow.get_threads
        # 使用await等待协程asyncio.gather执行完毕
        # 返回的数据会被分别装入变量user和threads
        # 参考https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.gather
        user, threads = await asyncio.gather(brow.get_self_info(), brow.get_threads('图拉丁'))

    # 将获取的信息打印到日志
    tb.LOG.info(f"当前用户信息: {user}")
    for thread in threads:
        tb.LOG.info(f"tid: {thread.tid} 最后回复时间戳: {thread.last_time} 标题: {thread.title}")


# 执行协程main
# 参考https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.run
asyncio.run(main())
