import contract.boost as boost
import contract.gauge as gauge
from web3 import Web3

# rpc point
rpc_url = "https://rpc-testnet.kcc.network"
web3 = Web3(Web3.HTTPProvider(rpc_url))
# 当前块
blockNumber = web3.eth.blockNumber

def currentboots ():
    pool_Info = boost.get_pool_Info()
    tokenPerBlock = boost.get_tokenPerBlock()
    userInfo = gauge.get_userInfo("0x182d8bE296CA371Ba2e314967Ea142F4d7c0820A")
    totalSupply = gauge.get_totalSupply()
    totalAllocPoint = boost.get_totalAllocPoint()
    # Current boots
    # 块产出
    pieceofoutput = (tokenPerBlock / 10 ** 18) * (blockNumber - pool_Info[2])
    return pieceofoutput

    normalreward = (userInfo[0] / totalSupply) * pieceofoutput * (pool_Info[1] / totalAllocPoint)
    return normalreward

if __name__ == '__main__':
    pieceofoutput = currentboots()
    normalreward = currentboots()
    print("块产出", pieceofoutput)
    print("正常Reward",normalreward)
