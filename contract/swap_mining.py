from app import *

ken3, swap_router, swap_mining, boost, gauge = init()
print(swap_mining.address)

# poolLength 池子数量
poolLength = swap_mining.functions.poolLength().call()
print("池子数量:", poolLength)


def get_poolinfo():
    arr = []
    for i in range(poolLength):
        # pool_info 池子信息 参数0：uint256 输入池子id
        # 0xB92524021c43f663F78dbD56Ed5007E110F94998:3pool:[0]
        # 0xd1efA0F5BaCCfdcBe7c348AF3646D9B7F063702b:5pool:[1]Zap
        # 0xb8E0680dCdaC232e8890d8b645C06cC90F97Cd73:4ppool:[2]Zap
        # 0x12B6854f4C30399fdAD45321b0Af71E04a243224:KENUSDC:[3]
        # 0x106CdFe20F0cc24C936F27D5fCe73b9aCD9C1C37:skcs2pool:[4]
        # 0xd1efA0F5BaCCfdcBe7c348AF3646D9B7F063702b::[5]
        # 0xEedA03461D0Bd045E2251ec2eE382568d6B0707f::[6]
        poolInfo = swap_mining.functions.poolInfo(i).call()
        arr.append(poolInfo)
        # return "池子{}".format(i+1), poolInfo
    return arr


# totalAllocPoint 所有池子权重
def get_totalAllocPoint():
    totalAllocPoint = swap_mining.functions.totalAllocPoint().call()
    return totalAllocPoint


# userInfo 用户信息 参数0：uint256 输入池子id  参数1：address 输入一个钱包账户
def get_userInfo(id, address):
    userInfo = swap_mining.functions.userInfo(id, address).call()
    return userInfo


# votes：用户交易池子加速在池子的权重 参数0：uint256 输入一个tokenid 参数1: address 输入一个池子lp地址
def get_votes(token_id, address):
    votes = swap_mining.functions.votes(token_id, address).call()
    return votes


# weights 当前池子投票后权重
def get_weights(pool_lp):
    weights = swap_mining.functions.weights(pool_lp).call()
    return weights


# totalWeight 所有池子投票后权重
def get_totalWeight():
    totalWeight = swap_mining.functions.totalWeight().call()
    return totalWeight


# rewardPoolInfo：交易后，该账户该池子即将获得奖励 参数0：uint256 输入一个池子id 参数1：address 输入一个钱包账户
def get_rewardPoolInfo(id, address):
    rewardPoolInfo = swap_mining.functions.rewardPoolInfo(id, address).call()
    return rewardPoolInfo


# usedWeights：用户在所有池子加速的总权重 参数: uint256 输入一个tokenid
def get_usedWeights(token_id):
    usedWeights = swap_mining.functions.usedWeights(token_id).call()
    return usedWeights


if __name__ == '__main__':
    poolinfo = get_poolinfo()
    print("所有池子信息", poolinfo)
    totalAllocPoint = get_totalAllocPoint()
    print("所有池子权重", totalAllocPoint)
    userInfo = get_userInfo(5, "0xdf4e614dc3e91b4D8aaB7CA1622A8771d29C7923")
    print("用户交易量：", userInfo[0])
    print("上次用户更新的块：", userInfo[1])
    votes = get_votes(38, "0x471831942aE446CfB1B6A4156e6660968c2f9924")
    print("用户交易池子加速在池子的权重", votes)
    weights = get_weights("0x106CdFe20F0cc24C936F27D5fCe73b9aCD9C1C37")
    print("当前池子投票后权重", weights)
    totalWeight = get_totalWeight()
    print('所有池子投票后权重', totalWeight)
    rewardPoolInfo = get_rewardPoolInfo(0, "0xdf4e614dc3e91b4D8aaB7CA1622A8771d29C7923")
    print("交易后，该账户在该池子即将获得奖励", rewardPoolInfo / 10 ** 18)
    usedweights = get_usedWeights(38)
    print("查询用户在所有池子加速的总权重", usedweights)
