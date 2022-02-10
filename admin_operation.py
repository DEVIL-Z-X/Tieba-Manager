# -*- coding:utf-8 -*-
import argparse
import os

import tiebaBrowser as tb
from tiebaBrowser.data_structure import BasicUserInfo

PATH = os.path.split(os.path.realpath(__file__))[0]


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='ADMIN OPERATION', allow_abbrev=False)

    parser.add_argument('tieba_name',
                        type=str,
                        help='需要执行操作的目标贴吧吧名')
    parser.add_argument('--BDUSS_key', '-key',
                        type=str,
                        default='default',
                        help='用于获取BDUSS')

    parser.add_argument('--id', '-i',
                        type=str,
                        help='用户id（user_name或nick_name或portrait）')
    parser.add_argument('--user_id', '-uid',
                        type=int,
                        help='用户user_id')
    parser.add_argument('--tid', '-t',
                        type=int,
                        default=0,
                        help='帖子tid')
    parser.add_argument('--pid', '-p',
                        type=int,
                        default=0,
                        help='帖子pid')

    parser.add_argument('--block', '-b',
                        action='store_true',
                        help='将用户封10天')
    parser.add_argument('--unblock', '-u',
                        action='store_true',
                        help='将用户解封')
    parser.add_argument('--blacklist_add', '-ba',
                        action='store_true',
                        help='将用户加入黑名单')
    parser.add_argument('--blacklist_cancel', '-bc',
                        action='store_true',
                        help='将用户解除黑名单')

    parser.add_argument('--delete', '-d',
                        action='store_true',
                        help='删除帖子')
    parser.add_argument('--recover', '-r',
                        action='store_true',
                        help='恢复帖子')
    parser.add_argument('--hide',
                        action='store_true',
                        help='屏蔽帖子')
    parser.add_argument('--unhide',
                        action='store_true',
                        help='解除屏蔽帖子')
    parser.add_argument('--recommend', '-rc',
                        action='store_true',
                        help='推荐帖子')

    parser.add_argument('--refuse_appeals', '-ra',
                        action='store_true',
                        help='一键拒绝所有解封申诉')

    args = parser.parse_args()
    tieba_name = args.tieba_name
    brow = tb.Browser(args.BDUSS_key)

    if args.id:
        user = brow.get_userinfo(BasicUserInfo(args.id))
        print(user)

        if args.user_id:
            user = brow.get_userinfo_weak(BasicUserInfo(args.user_id))
        if user.portrait:
            if args.block:
                brow.block(tieba_name, user, day=10)
            if args.unblock:
                brow.unblock(tieba_name, user)
            if args.blacklist_add:
                brow.blacklist_add(tieba_name, user)
            if args.blacklist_cancel:
                brow.blacklist_cancel(tieba_name, user)

    tid = args.tid
    pid = args.pid
    if tid or pid:
        if args.recover:
            brow.recover(tieba_name, tid, pid)
        if tid:
            if args.delete:
                brow.del_post(tieba_name, tid, pid)
            if args.hide:
                brow.del_thread(tieba_name, tid, is_frs_mask=True)
            if args.unhide:
                brow.recover(tieba_name, tid, is_frs_mask=True)
            if args.recommend:
                brow.recommend(tieba_name, tid)

    if args.refuse_appeals:
        brow.refuse_appeals(tieba_name)

    brow.close()
