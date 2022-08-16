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
    # print(num, rewardsOutput)


# 📚Minimum received
#   最小收到=预计收到*(1-容忍的滑点)
def get_minimum_received(ex_received, percentage):
    minimum_received = ex_received * (1 - percentage)
    return minimum_received


# 📚Price impact （价格影响率计算公式）（即滑点）
#  x 兑换 y
# 价格影响率 = (预计收到价值y - 输入价值x）/ 输入价值x * 100%
# 示例：假设币种A价格为$1，币种B价格为$1，用2个A 换到 1个B，则：
# 价格影响率 = (1*1 - 2*1) / 2*1 * 100% = -50%

def get_price_impact(tokens_sold_num, tokens_sold_pri, tokens_bought_num, tokens_bought_pri):
    bought = tokens_bought_num * tokens_bought_pri
    sold = tokens_sold_num * tokens_sold_pri
    price_impact = (bought - sold) / sold
    return price_impact


if __name__ == '__main__':
    minimum_received = get_minimum_received(15.3745, 0.005)
    print("最小收到", minimum_received)
    price_impact = get_price_impact(100, 1.33, 15.3745, 21.14)
    print("价格影响率", "{:.2%}".format(price_impact))
