import app
import contract.boost as boost
import contract.gauge as gauge
from app import get_block_number

# 当前块
blockNumber = app.get_block_number()
pool_Info = boost.get_pool_Info()
tokenPerBlock = boost.get_tokenPerBlock()
userInfo = gauge.get_userInfo("0x182d8bE296CA371Ba2e314967Ea142F4d7c0820A")
totalSupply = gauge.get_totalSupply()
totalAllocPoint = boost.get_totalAllocPoint()
votes = boost.get_votes(50, "0xB92524021c43f663F78dbD56Ed5007E110F94998")
weights = boost.get_weights("0xB92524021c43f663F78dbD56Ed5007E110F94998")


# Current boots计算
def get_pieceofoutput():
    # 块产出
    pieceofoutput = (tokenPerBlock / 10 ** 18) * (blockNumber - pool_Info[2])
    return pieceofoutput


def get_normalreward():
    # 正常reward
    normalreward = (userInfo[0] / totalSupply) * pieceofoutput * (pool_Info[1] / totalAllocPoint)
    return normalreward


def get_BaseReward():
    # BaseReward
    BaseReward = normalreward * (3 / 10)
    return BaseReward


def get_SpeedReward():
    # SpeedReward
    SpeedReward = (votes / weights) * totalSupply * 0.7
    return SpeedReward


def get_min():
    # 取最小加速奖励
    minspeedreward = min(normalreward * (7 / 10), SpeedReward)
    return minspeedreward


def get_Speed():
    # Current boots总结果
    Speed = (BaseReward + SpeedReward) / BaseReward
    return Speed


if __name__ == '__main__':
    pieceofoutput = get_pieceofoutput()
    print("块产出", pieceofoutput)
    normalreward = get_normalreward()
    print("正常Reward", normalreward)
    BaseReward = get_BaseReward()
    print("BaseReward", BaseReward)
    SpeedReward = get_SpeedReward()
    print("SpeedReward", SpeedReward)
    minspeedreward = get_min()
    print("取最小加速奖励", minspeedreward)
    Speed = get_Speed()
    print("Current boots总结果", Speed)
