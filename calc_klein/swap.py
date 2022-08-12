from contract.boost import totalAllocPoint
from contract.swap_mining import *


poolInfo = get_poolinfo()
# print(poolInfo)

# Rewards output 该池子的日产出计算
# =交易挖矿的TRA块日产出总量 * 池权重系数
# =(TRA单块产量*28800 )*（该池子权重 / 所有池子权重 ）
rewardsOutput = (0.1 * 28800) * (poolInfo[1][2]/totalAllocPoint)
print(rewardsOutput)