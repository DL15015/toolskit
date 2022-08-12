import contract.boost as boost
import contract.gauge as gauge
from web3 import Web3
# rpc point
rpc_url = "https://rpc-testnet.kcc.network"
web3 = Web3(Web3.HTTPProvider(rpc_url))
# 当前块
blockNumber = web3.eth.blockNumber

def test1():
    pool_info = boost.get_pool_info()
    userinfo = gauge.get_userinfo("")
    tokenPerBlock = boost.get_tokenPerBlock()
    # Current boots
    # 块产出
    Pieceofoutput = (tokenPerBlock / 10 ** 18) * (blockNumber - pool_info[4])
    print("块产出", Pieceofoutput)
    # normalreward = ()
