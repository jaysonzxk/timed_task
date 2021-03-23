"""
author： mask
filename: main.py
datetime： 2021/3/23 16:31 
ide： PyCharm
"""
from apscheduler.schedulers.blocking import BlockingScheduler
from timed_task.recharge_task import Recharge
from timed_task.review_task import Review


def job_Recharge():
    """
    充值job
    :return:
    """
    Recharge().recharge_money()


def job_review():
    """
    审核job
    :return:
    """
    Review().review_money()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(job_Recharge, 'date', run_date='2021-03-23 23:55:00')
    scheduler.add_job(job_review, 'date', run_date='2021-03-24 00:10:00')
    scheduler.start()
