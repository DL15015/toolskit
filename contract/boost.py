from app import *

ken3, swap_router, swap_mining, boost, gauge = init()
print(boost.address)

# pool_length 池子数量
pool_length = boost.functions.poolLength().call()
print("池子数量:", pool_length)

# pool_info 池子信息
print("[池子lp地址", "池子权重", "上次池子更新的块]")
for i in range(pool_length):
    poolInfo = boost.functions.poolInfo(i).call()

    # totalAllocPoint：查询所有池子的总权重
    totalAllocPoint = boost.functions.totalAllocPoint().call()

    # 📚Farming APR（仅克莱因有）
    # = (KEN单块产量*28800 )*（该池子权重 / 所有池子权重 ）* KEN价格 / 池子TVL*365/3.33*100%
    farming_apr = (0.4 * 28800) * (poolInfo[1] / totalAllocPoint) * 0.57 / 27.97 * 365 / 3.33
    print("池子:{}".format(i + 1), poolInfo)
    print('该池子的farm APR:: {:.10%}'.format(farming_apr))

print("")


print('查询所有池子的总权重', totalAllocPoint)

# votes：查询加速之后个人池子权重 参数0 uint256:输入tokenID 参数1 address:输入池子lp地址，不是加密池子可使用池子地址
votes = boost.functions.votes(50, "0xB92524021c43f663F78dbD56Ed5007E110F94998").call()
print("查询加速之后个人池子权重", votes)

# usedWeights：查询加速之后个人池子总权重 参数 address:输入池子lp地址
weights = boost.functions.weights("0xB92524021c43f663F78dbD56Ed5007E110F94998").call()
print("查询加速之后个人池子总权重", weights)






