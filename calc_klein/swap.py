from contract.swap_mining import *
from contract.pool3 import *

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


blockNumber = get_block_number()
calc_token_amount = get_calc_token_amount(10, 0, 0)
userInfo = get_userInfo(5, "0xdf4e614dc3e91b4D8aaB7CA1622A8771d29C7923")
rewardPoolInfo = get_rewardPoolInfo(0, "0xdf4e614dc3e91b4D8aaB7CA1622A8771d29C7923")


def get_trading_rewards(tokenamount1, tokenamount2, tokenamount3):
    # blockNumber 当前块
    diff_block = blockNumber - num[4]
    cur_diff_reward = (0.1 * diff_block * 100) / totalAllocPoint
    fut_poolinfo_trans_volume = poolinfo[0][1] + calc_token_amount
    fut_userinfo_trans_volume = userInfo[0] + calc_token_amount
    fut_pools_unclaimed_rewards = rewardPoolInfo + cur_diff_reward
    fut_rewards = fut_pools_unclaimed_rewards * fut_userinfo_trans_volume / fut_poolinfo_trans_volume
    now_rewards = rewardPoolInfo * 0 / 100


# 📚Trading rewards
# 计算公式：
# 当前块-上次更新的块=差值块
# 当前差值奖励=(每个块产出奖励 x 差值块 x 池子的权重) / 总权重
# calc_token_amount计算用户输入后未来交易量
# 未来的poolinfo交易量=当前池子交易量+calc_token_amount
# 未来的userinfo交易量=当前用户个人交易量+calc_token_amount
# 未来池子未领取的奖励=池子未领取的奖励+当前差值奖励
# 未来的奖励=未来池子未领取的奖励 X 未来的userinfo交易量 / 未来的poolinfo交易量
# 当前的奖励=池子未领取的奖励 X 用户当前的个人奖励 / 池子交易量
# 用户当前可获得奖励=getboost （当前的奖励数，用户的权重，池子的总权重，用户交易量）
# getboost 当前的奖励数 用户的权重 池子的总权重 用户交易量
# 基础奖励：当前的奖励数*0.3
# 加速奖励：用户交易量*用户权重/池子总权重 x 0.7
# 最小奖励数=（基础奖励+加速奖励）VS 当前的奖励数 取最小值
# 用户将来可获得奖励= getboost （未来奖励数，用户的权重，池子的总权重，未来用户交易量）
# 预计收益奖励 = 将来 - 当前


if __name__ == '__main__':
    minimum_received = get_minimum_received(15.3745, 0.005)
    print("最小收到", minimum_received)
    price_impact = get_price_impact(100, 1.33, 15.3745, 21.14)
    print("价格影响率", "{:.2%}".format(price_impact))
    # blockNumber = get_block_number()
    # print("当前块", blockNumber)
