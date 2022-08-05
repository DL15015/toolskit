from app import *

ken3, swap_router, swap_mining, boost, gauge = init()
print(boost.address)

# pool_length 池子数量
pool_length = boost.functions.poolLength().call()
print("池子数量:", pool_length)
print("")

# pool_info 池子信息
# pool_info 池子信息
# 0xB92524021c43f663F78dbD56Ed5007E110F94998:3pool:[0]


pool_info = boost.functions.poolInfo(3).call()
print("池子lp地址：", pool_info[0])
print("池子初始权重：", pool_info[1])
print("上次池子更新的块：", pool_info[2])
print("")

# total_weighte 所有池子权重
total_weighte = boost.functions.totalWeight().call()
print('所有池子权重', total_weighte)
print("")

# votes 个人池子权重,输入池子token和池子lp地址
votes = boost.functions.votes(30, "0xB92524021c43f663F78dbD56Ed5007E110F94998").call()
print("个人池子权重", votes)
print("")

# weights 当前池子权重,传lp地址
weights = boost.functions.weights("0xB92524021c43f663F78dbD56Ed5007E110F94998").call()
print("当前池子权重", weights)
print("")


# gauges 获取gague地址，传入池子lp地址。
# 池子lp地址：
# 工厂：crypto_factory：用加密地址在kcc链上的token方法获取；crvFactory：用非加密地址在kcc链上的token方法获取
# 合约部署：在KCC测试网文档上找

gauges = boost.functions.gauges("0x471831942aE446CfB1B6A4156e6660968c2f9924").call()
print("池子的gauges地址", gauges)


