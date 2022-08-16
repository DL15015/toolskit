from app import *

ken3, swap_router, swap_mining, boost, gauge = init()
print(boost.address)

def get_pool_length():
    # pool_length 池子数量
    pool_length = boost.functions.poolLength().call()
    return pool_length
pool_length = get_pool_length()

def get_pool_Info():
    # pool_info 池子信息
    print("池子lp地址", "池子权重", "上次池子更新的块 Farming APR")
    for i in range(pool_length):
        poolInfo = boost.functions.poolInfo(i).call()

        # totalAllocPoint：查询所有池子的总权重
        totalAllocPoint = boost.functions.totalAllocPoint().call()

        # 📚Farming APR（仅克莱因有）
        # = (KEN单块产量*28800 )*（该池子权重 / 所有池子权重 ）* KEN价格 / 池子TVL*365/3.33*100%
        farming_apr = (0.4 * 28800) * (poolInfo[1] / totalAllocPoint) * 0.57 / 27.97 * 365 / 3.33
        print("池子:{}".format(i + 1), poolInfo, '{:.10%}'.format(farming_apr))
    return poolInfo

def get_votes(tokenID,address):
    # votes：查询加速之后个人池子权重 参数0 uint256:输入tokenID 参数1 address:输入池子lp地址，不是加密池子可使用池子地址
    votes = boost.functions.votes(tokenID, address).call()
    return votes

def get_weights(address):
    # usedWeights：查询加速之后个人池子总权重 参数 address:输入池子lp地址
    weights = boost.functions.weights(address).call()
    return weights

def get_tokenPerBlock():
    # tokenPerBlock 每个块产生的奖励数量
    tokenPerBlock = boost.functions.tokenPerBlock().call()
    return tokenPerBlock

def get_totalAllocPoint():
    totalAllocPoint = boost.functions.totalAllocPoint().call()
    return totalAllocPoint

if __name__ == '__main__':
    pool_length = get_pool_length()
    print("池子数量",pool_length)
    poolInfo = get_pool_Info()
    print("")
    votes = get_votes(50,"0xB92524021c43f663F78dbD56Ed5007E110F94998")
    print("查询加速之后个人池子权重", votes)
    weights = get_weights("0xB92524021c43f663F78dbD56Ed5007E110F94998")
    print("查询加速之后池子总权重", weights)
    tokenPerBlock = get_tokenPerBlock()
    print("每个块产生的奖励数量",tokenPerBlock / 10 ** 18)
    totalAllocPoint = get_totalAllocPoint()
    print("所有池子总权重",totalAllocPoint)

