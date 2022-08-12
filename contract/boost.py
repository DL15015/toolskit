from app import *

ken3, swap_router, swap_mining, boost, gauge = init()
print(boost.address)

# pool_length 池子数量
pool_length = boost.functions.poolLength().call()
print("池子数量:", pool_length)

# pool_info 池子信息
print("[池子lp地址", "池子权重", "上次池子更新的块]")
for i in range(pool_length):
    # 0xB92524021c43f663F78dbD56Ed5007E110F94998:3pool:[0]
    # 0x5FA2AcE9F8415F1C07cB732494e6FC4510C1b017:5pool:[1]
    # 0x9192fc75B96356e1C999D46E5e2735522C9e4290:usdteth:[6]
    # 0x24A9b8565834E23C5AA8A9cce6949DB0AB00A9F4:dev_kenWKCSUSD:[2]
    # 0x471831942aE446CfB1B6A4156e6660968c2f9924::dev_KCSSKCS:[4]
    pool_info = boost.functions.poolInfo(i).call()
    print("池子:{}".format(i + 1), pool_info)
print("")

# totalAllocPoint：查询所有池子的总权重
totalAllocPoint = boost.functions.totalAllocPoint().call()
print('查询所有池子的总权重', totalAllocPoint)

# votes：查询加速之后个人池子权重 参数0 uint256:输入tokenID 参数1 address:输入池子lp地址，不是加密池子可使用池子地址
votes = boost.functions.votes(50, "0xB92524021c43f663F78dbD56Ed5007E110F94998").call()
print("查询加速之后个人池子权重", votes)

# usedWeights：查询加速之后个人池子总权重 参数 address:输入池子lp地址
weights = boost.functions.weights("0xB92524021c43f663F78dbD56Ed5007E110F94998").call()
print("当前池子权重", weights)
print("")


# 📚Farming APR（仅克莱因有）
# = (KEN单块产量*28800 )*（该池子权重 / 所有池子权重 ）* KEN价格 / 池子TVL*365/3.33*100%
def farming_apr():
    farming_apr = (0.4 * 28800) * (17472995148401748205 / totalAllocPoint) * 0.57 / 27.97 * 365 / 3.33
    return farming_apr


if __name__ == '__main__':
    farming_apr = farming_apr()
    print('该池子的farm APR:: {:.10%}'.format(farming_apr))
