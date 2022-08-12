import math
import time


# 📚锁预计收到的veKEN计算公式：
# ①预计收到=锁定数量*(实际锁定时间/(1460*24*3600))
# ②解锁时间=(Floor[(timestamp+实际锁定时间)/锁周期]*锁周期)
# 锁周期:合约设定的最小周期(秒)
# lock_number = input("请输入ken的数量：")
def locktime():
    timelist()
    lock_number = int(input("请输入ken的数量："))
    lock_time = int(input("请输入锁定时间："))
    unlock_time = math.floor((time.time() + lock_time) / 3600) * 3600
    expect_receive = lock_number * (unlock_time - time.time()) / (1460 * 24 * 3600)
    return unlock_time, expect_receive


def timelist():
    print("1小时：3600     1周：604800")
    print("1个月：2628000  3个月：7884000")
    print("6个月：15768000 1年：31536000")
    print("4年：126144000")
    print("当前时间：", int(time.time()))
    print("")


if __name__ == '__main__':
    unlock_time, expect_receive = locktime()
    print("解锁时间", unlock_time)
    print("预计收到的veKEN", expect_receive)
