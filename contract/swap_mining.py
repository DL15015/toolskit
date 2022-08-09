from app import *

ken3, swap_router, swap_mining, boost, gauge = init()
print(swap_mining.address)

# poolLength 池子数量
poolLength = swap_mining.functions.poolLength().call()
print("池子数量:", poolLength)
print("")
# pool_info 池子信息 参数0：uint256 输入池子id
# 0xB92524021c43f663F78dbD56Ed5007E110F94998:3pool:[0]
# 0x7a99a241e8890922D8019238b4FE44B820fda9FE:5pool:[1]Zap
# 0xb8E0680dCdaC232e8890d8b645C06cC90F97Cd73:4ppool:[2]Zap
# 0x12B6854f4C30399fdAD45321b0Af71E04a243224:KENUSDC:[3]
# 0x106CdFe20F0cc24C936F27D5fCe73b9aCD9C1C37:skcs2pool:[4]
# 0xd1efA0F5BaCCfdcBe7c348AF3646D9B7F063702b::[5]
# 0xEedA03461D0Bd045E2251ec2eE382568d6B0707f::[6]

poolInfo = swap_mining.functions.poolInfo(1).call()
print("池子lp/Zap地址：", poolInfo[0])
print("查询该池子的总交易量：", poolInfo[1])
print("池子权重：", poolInfo[2])
print("该池子累计的奖励：", poolInfo[3])
print("上次池子更新的块：", poolInfo[4])
print("")

# totalAllocPoint 所有池子权重
totalAllocPoint = swap_mining.functions.totalAllocPoint().call()
print("所有池子权重", totalAllocPoint)

# userInfo 用户信息 参数0：uint256 输入池子id  参数1：address 输入一个钱包账户
userInfo = swap_mining.functions.userInfo(0, "0xdf4e614dc3e91b4D8aaB7CA1622A8771d29C7923").call()
print("用户交易量：", userInfo[0])
print("上次用户更新的块：", userInfo[1])
print("")

# votes：用户交易池子加速在池子的权重 参数0：uint256 输入一个tokenid 参数1: address 输入一个池子lp地址
votes = swap_mining.functions.votes(38, "0x471831942aE446CfB1B6A4156e6660968c2f9924").call()
print("用户交易池子加速在池子的权重", votes)

# weights 当前池子投票后权重
weights = swap_mining.functions.weights("0x471831942aE446CfB1B6A4156e6660968c2f9924").call()
print("当前池子投票后权重", weights)

# totalWeight 所有池子投票后权重
totalWeight = swap_mining.functions.totalWeight().call()
print('所有池子投票后权重', totalWeight)

# rewardPoolInfo：查询用户预计收到的奖励数量 参数0：uint256 输入一个池子id 参数1：address 输入一个钱包账户
rewardPoolInfo = swap_mining.functions.rewardPoolInfo(0, "0xdf4e614dc3e91b4D8aaB7CA1622A8771d29C7923").call()
print("查询用户预计收到的奖励数量", rewardPoolInfo)

# usedWeights：用户在所有池子加速的总权重 参数: uint256 输入一个tokenid
usedWeights = swap_mining.functions.usedWeights(38).call()
print("查询用户在所有池子加速的总权重", usedWeights)
