from app import *

ken3, swap_router, swap_mining, boost, gauge = init()
print(boost.address)

# # updateAll：刷新所有池子,无法调钱包
# updateAll = boost.functions.updateAll().call()
# print("刷新所有池子", updateAll)

# pool_length 池子数量
pool_length = boost.functions.poolLength().call()
print("池子数量:", pool_length)
print("[池子lp地址", "池子权重", "上次池子更新的块]")
for i in range(pool_length):
    # pool_info 池子信息
    # 0xB92524021c43f663F78dbD56Ed5007E110F94998:3pool:[0]
    # 0x5FA2AcE9F8415F1C07cB732494e6FC4510C1b017:5pool:[1]
    # 0x9192fc75B96356e1C999D46E5e2735522C9e4290:usdteth:[6]
    # 0x24A9b8565834E23C5AA8A9cce6949DB0AB00A9F4:dev_kenWKCSUSD:[2]
    pool_info = boost.functions.poolInfo(i).call()
    print("池子:{}".format(i + 1), pool_info)
print("")

# totalAllocPoint：查询所有池子的总权重
totalAllocPoint = boost.functions.totalAllocPoint().call()
print('查询所有池子的总权重', totalAllocPoint)
print("")

# votes 个人池子权重,输入池子token和池子lp地址
votes = boost.functions.votes(30, "0xB92524021c43f663F78dbD56Ed5007E110F94998").call()
print("个人池子权重", votes)
print("")

# weights 当前池子权重,传lp地址
weights = boost.functions.weights("0xB92524021c43f663F78dbD56Ed5007E110F94998").call()
print("当前池子权重", weights)
print("")

# gauges 获取gague地址，参数：传入池子lp地址（remix查询）。
# 池子lp地址：
# 工厂：crypto_factory：用加密地址在kcc链上的token方法获取；crvFactory：用非加密地址在kcc链上的token方法获取
# 合约部署：在KCC测试网文档上找
gauges1 = boost.functions.gauges("0xB92524021c43f663F78dbD56Ed5007E110F94998").call()
print("池子的gauges地址", gauges1)
