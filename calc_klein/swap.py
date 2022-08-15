from contract.swap_mining import *

poolInfo = get_poolinfo()
totalAllocPoint = get_totalAllocPoint()
print("所有池子权重", totalAllocPoint)
print("池子lp/Zap地址", "查询该池子的总交易量", "池子权重", "该池子累计的奖励", "上次池子更新的块",
      "Daily Output")  # 日产出有3分钟延迟
for num in poolInfo:
    totalAllocPoint = get_totalAllocPoint()
    rewardsOutput = (28800 * 0.1) * num[2] / totalAllocPoint
    # Rewards output 该池子的日产出计算
    # =交易挖矿的TRA块日产出总量 * 池权重系数
    # =(TRA单块产量*28800 )*（该池子权重 / 所有池子权重 ）
    print(num, rewardsOutput)

