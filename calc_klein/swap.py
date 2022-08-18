from contract.swap_mining import *
from contract.pool4 import *

poolInfos = get_poolinfos()
totalAllocPoint = get_totalAllocPoint()
print("totalAllocPoint", totalAllocPoint)
print("lp/Zap_address", "quantity", "allocPoint", "allocSwapTokenAmount", "lastRewardBlock",
      "Daily Output")  # 日产出有3分钟延迟
for num in poolInfos:
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
def get_price_impact(tokens_sold_num, tokens_sold_pri, tokens_bought_num, tokens_bought_pri):
    """
    x 兑换 y
    价格影响率 = (预计收到价值y - 输入价值x）/ 输入价值x * 100%
    示例：假设币种A价格为$1，币种B价格为$1，用2个A 换到 1个B，则：
    价格影响率 = (1*1 - 2*1) / 2*1 * 100% = -50%
    :param tokens_sold_num:
    :param tokens_sold_pri:
    :param tokens_bought_num:
    :param tokens_bought_pri:
    :return:
    """
    bought = tokens_bought_num * tokens_bought_pri
    sold = tokens_sold_num * tokens_sold_pri
    price_impact = (bought - sold) / sold
    return price_impact


# 当前块
def get_block_number():
    blockNumber = web3.eth.blockNumber
    return blockNumber


# calc_token_amount 计算用户输入后未来交易量ken # False交易的交易量
# 需要输入的池子输入交易数量，其他输入0
def get_calc_token_amount(token1, token2, token3, token4):
    calc_token_amount = pool4.functions.calc_token_amount(
        [token1 * 10 ** 17, token2, token3, token4], False).call()
    return calc_token_amount


# userInfo 用户信息 参数0：uint256 输入池子id  参数1：address 输入一个钱包账户
def get_userInfo(id, address):
    userInfo = swap_mining.functions.userInfo(id, address).call()
    return userInfo


# votes：用户交易池子加速在池子的权重 参数0：uint256 输入一个tokenid 参数1: address 输入一个池子lp地址
def get_votes(token_id, address):
    votes = swap_mining.functions.votes(token_id, address).call()
    return votes


blockNumber = get_block_number()
calc_token_amount = get_calc_token_amount(1, 0, 0, 0)
userInfo = get_userInfo(0, "0xdf4e614dc3e91b4D8aaB7CA1622A8771d29C7923")
votes = get_votes(38, "0x471831942aE446CfB1B6A4156e6660968c2f9924")


# def get_poolinfo(pool_id):
#     poolinfo = swap_mining.functions.poolInfo(pool_id).call()
#     return poolinfo
#
#
# poolinfo = get_poolinfo(2)
# print(poolinfo)

def get_trading_rewards():
    # 差值块=当前块-上次更新的块(poolinfo.lastRewardBlock)
    diff_block = blockNumber - num[4]

    # 当前差值奖励 = (每个块产出奖励 x 差值块 x 池子的权重(poolinfo.allocPoint)) / 总权重(total_allocPoint)
    cur_diff_reward = (1*10**17 * diff_block * poolInfos[4][2]) / totalAllocPoint

    # 未来的poolinfo交易量 = 当前池子交易量(poolinfo.quantity) + calc_token_amount
    fut_poolinfo_trans_volume = poolInfos[4][1] + calc_token_amount

    # 未来的userinfo交易量 = 当前用户个人交易量(userinfo.quantity) + calc_token_amount
    fut_userinfo_trans_volume = userInfo[0] + calc_token_amount

    # 未来池子未领取的奖励 = 池子未领取的奖励(poolinfo.allocSwapTokenAmount) + 当前差值奖励
    fut_pools_unclaimed_rewards = poolInfos[4][3] + cur_diff_reward

    # 未来的奖励 = 未来池子未领取的奖励X未来的userinfo交易量 / 未来的poolinfo交易量
    fut_rewards = fut_pools_unclaimed_rewards * fut_userinfo_trans_volume / fut_poolinfo_trans_volume

    # 当前的奖励=池子未领取的奖励(poolinfo.allocSwapTokenAmount ) X 用户当前的个人交易量(userinfo.quantity) / 池子交易量
    now_rewards = poolInfos[4][3] * userInfo[0] / poolInfos[4][1]

    # 用户当前可获得奖励
    # 基础奖励：当前的奖励数 * 0.3
    now_base_rewards = now_rewards * 0.3

    # 加速奖励：用户交易量 * 用户权重 / 池子总权重 x 0.7
    now_acc_rewards = userInfo[0] * votes / poolInfos[4][2] * 0.7

    # 最小奖励数 =（基础奖励 + 加速奖励）VS 当前的奖励数 取最小值
    cur_receive_rewards = min((now_base_rewards + now_acc_rewards), now_rewards)

    # 用户将来可获得奖励
    # 基础奖励：未来的奖励数 * 0.3
    fut_base_rewards = fut_rewards * 0.3

    # 加速奖励：用户交易量 * 用户权重 / 池子总权重 x 0.7
    fut_acc_rewards = userInfo[0] * votes / poolInfos[4][2] * 0.7

    # 最小奖励数 =（基础奖励 + 加速奖励）VS 当前的奖励数 取最小值
    fut_be_rewards = min((fut_base_rewards + fut_acc_rewards), now_rewards)

    # 预计收益奖励 = 将来 - 当前
    trading_rewards = fut_be_rewards - cur_receive_rewards

    return (fut_rewards,now_rewards)


if __name__ == '__main__':
    # minimum_received = get_minimum_received(15.3745, 0.005)
    # print("最小收到", minimum_received)
    # price_impact = get_price_impact(100, 1.33, 15.3745, 21.14)
    # print("价格影响率", "{:.2%}".format(price_impact))
    # blockNumber = get_block_number()
    # print("当前块", blockNumber)
    trading_rewards = get_trading_rewards()
    print("trading_rewards", trading_rewards)
    print("userInfo", userInfo)
    # calc_token_amount = get_calc_token_amount()
    print(calc_token_amount)
