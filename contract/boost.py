from app import *

ken3, swap_router, swap_mining, boost, gauge = init()
print(boost.address)

# pool_length 池子数量
pool_length = boost.functions.poolLength().call()
print("池子数量:", pool_length)

# pool_info 池子信息
pool_info = boost.functions.poolInfo(3).call()




# print("池子lp地址：", pool_info[0])
print("池子初始权重：", pool_info[1])

print("上次池子更新的块：", pool_info[2])

# total_weighte 所有池子权重
total_weighte = boost.functions.totalWeight().call()

print('所有池子权重', total_weighte)

# votes 个人池子权重,输入池子token和池子lp地址
votes = boost.functions.votes(30, "0xB92524021c43f663F78dbD56Ed5007E110F94998").call()
print("个人池子权重", votes)

# weights 当前池子权重
weights = boost.functions.weights("0xB92524021c43f663F78dbD56Ed5007E110F94998").call()
print("当前池子权重", weights)


"""
块产出 =39060
正常Reward = (个人质押LP / 该池子总质押LP) * 块产出*（当前池子权重boost->abstracthboost环境->weights:池子lp地址/所有池子权重boost.sol->totalweighter） 
BaseReward = 正常Reward * (3 / 10) 
SpeedReward = (个人池子权重 boost.sol->votes:1️⃣🔒token值2️⃣池子lp/ 该池子总权重boost->abstracthboost环境->weights:池子lp地址) * 该池子总质押LP * 0.7 / 该池子总权重) * 该池子总质押LP * 0.7 
取最小加速奖励SpeedReward = MIN(正常Reward * (7 / 10) , SpeedReward) 
Speed = (BaseReward + SpeedReward) / BaseReward """

