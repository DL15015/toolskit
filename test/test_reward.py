import app
import contract.boost as boost
import contract.gauge as gauge
from decimal import *
from app import get_block_number

# 当前块
blockNumber = app.get_block_number()
get_for = boost.get_for()
pool_Info = boost.get_pool_Info(0)
tokenPerBlock = boost.get_tokenPerBlock()
userInfo = gauge.get_userInfo("0x182d8bE296CA371Ba2e314967Ea142F4d7c0820A")
totalSupply = gauge.get_totalSupply()
totalAllocPoint = boost.get_totalAllocPoint()
votes =boost.get_votes(25,"0xB92524021c43f663F78dbD56Ed5007E110F94998")
weights = boost.get_weights("0xB92524021c43f663F78dbD56Ed5007E110F94998")


# Current boots计算
def get_piece_of_output():
    # 块产出
    piece_of_output = 0.4 * (blockNumber - pool_Info[2])
    return piece_of_output

def get_normal_reward():
    # 正常reward
    normal_reward = (userInfo[0] / totalSupply) * piece_of_output * (pool_Info[1] / totalAllocPoint)
    return normal_reward

def get_base_reward():

    # BaseReward
    base_reward = normal_reward * (3 / 10)
    return base_reward


def get_speed_reward():
    # SpeedReward
    # 加速的时候使用Decimal这行公式运行，Deciml代表很多位小数值的计算
    return Decimal(votes) * Decimal(totalSupply) * Decimal.from_float(0.7) / Decimal(weights)
    # 未加速时使用SpeedReard这行公式
    # speed_reward = (votes / weights) * totalSupply * 0.7
    # return speed_reward


def get_min():
    # 取最小加速奖励
    speed_reward = get_speed_reward()
    print(speed_reward)
    min_speed_reward = min(normal_reward * 0.7, speed_reward)
    # print("normalreward",normalreward*0.7)
    # print("SpeedReward", speed_reward.__str__())
    return min_speed_reward


def get_Speed():
    # Current boots总结果
    speed = (base_reward + min_speed_reward) / base_reward
    print(speed)
    return speed


if __name__ == '__main__':
    piece_of_output = get_piece_of_output()
    print("块产出", piece_of_output)
    normal_reward = get_normal_reward()
    print("正常Reward",normal_reward)
    base_reward = get_base_reward()
    print("BaseReward",base_reward)
    speed_reward = get_speed_reward()
    print("SpeedReward",speed_reward.__str__())
    min_speed_reward = get_min()
    print("取最小加速奖励",min_speed_reward)
    speed = get_Speed()
    print("Current boots总结果",speed)
