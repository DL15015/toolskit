from app import *

ken3, swap_router, swap_mining, boost, gauge = init()
print(swap_mining.address)

# pool_length 池子数量
pool_length = swap_mining.functions.poolLength().call()
print("池子数量:", pool_length)

# pool_info 池子信息
pool_info = swap_mining.functions.poolInfo(0).call()
# print("池子lp地址：", pool_info[0])
print("池子初始权重：", pool_info[1])
print("上次池子更新的块：", pool_info[2])

# total_weighte 所有池子权重
total_weighte = swap_mining.functions.totalWeight().call()
print('所有池子权重', total_weighte)

# votes 个人池子权重,输入池子token和池子lp地址
votes = swap_mining.functions.votes(28, "0xB92524021c43f663F78dbD56Ed5007E110F94998").call()
print("个人池子权重", votes)

# weights 当前池子权重
weights = swap_mining.functions.weights("0xB92524021c43f663F78dbD56Ed5007E110F94998").call()
print("当前池子权重", weights)