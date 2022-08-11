import time

# 📚锁预计收到的veKEN计算公式：
# ①预计收到=锁定数量*(实际锁定时间/(1460*24*3600))
# ②解锁时间=(Floor[(timestamp+实际锁定时间)/锁周期]*锁周期)
from math import floor

from debugpy.common import timestamp

locksycle = input("Enter a lock")
un_lock_time = (floor[(timestamp +locksycle)])
