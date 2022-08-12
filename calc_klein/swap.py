
from contract.swap_mining import *


poolInfo = get_poolinfo()
# print("池子{}".format(i+1), poolInfo)

totalAllocPoint=get_totalAllocPoint()

# print(poolInfo)
# Rewards output 该池子的日产出计算
for i in poolInfo:
    # =交易挖矿的TRA块日产出总量 * 池权重系数
    # =(TRA单块产量*28800 )*（该池子权重 / 所有池子权重 ）
    # poolInfo = swap_mining.functions.poolInfo(i).call()
    # rewardsOutput = poolInfo

    rewardsOutput = (28800*0.1)* i[2]/totalAllocPoint

    print(rewardsOutput)