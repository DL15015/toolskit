from app import *

ken3, swap_router, swap_mining, boost, gauge = init()
print(swap_mining.address)

# pool_length 池子数量
pool_length = swap_mining.functions.poolLength().call()
print("池子数量:", pool_length)

# pool_info 池子信息
# 0xB92524021c43f663F78dbD56Ed5007E110F94998:3pool:[0]
# 0x7a99a241e8890922D8019238b4FE44B820fda9FE:5pool:[1]Zap
# 0xb8E0680dCdaC232e8890d8b645C06cC90F97Cd73:4ppool:[2]Zap
# 0x12B6854f4C30399fdAD45321b0Af71E04a243224:KENUSDC:[3]
# 0x106CdFe20F0cc24C936F27D5fCe73b9aCD9C1C37:skcs2pool:[4]
# 0xd1efA0F5BaCCfdcBe7c348AF3646D9B7F063702b::[5]
# 0xEedA03461D0Bd045E2251ec2eE382568d6B0707f::[6]

pool_info = swap_mining.functions.poolInfo(6).call()
print("池子lp/Zap地址：", pool_info[0])
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