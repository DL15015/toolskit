from app import *

def get_gauge():
    ret = init()
    gauge = ret[4]
    return gauge
gauge = get_gauge()

def get_totalSupply():
    # total_supply 所有人质押到该池子的lp的数量
    totalSupply = gauge.functions.totalSupply().call()
    return totalSupply

def get_pending(address):
    # pending：个人质押到池子里的预计的奖励 参数：address 输入一个钱包账户
    pending = gauge.functions.pending(address).call()
    return pending

def get_userInfo(address):
    # userInfo：个人质押lp到此池子的数量 参数：address 输入一个钱包账户
    userInfo = gauge.functions.userInfo(address).call()
    return userInfo

if __name__ == '__main__':
    gauge = get_gauge()
    print("池子的gauge地址", gauge.address)
    totalSupply = get_totalSupply()
    print("所有人质押到该池子的lp的数量:", totalSupply / 10 ** 18)
    pending = get_pending("0x182d8bE296CA371Ba2e314967Ea142F4d7c0820A")
    print("个人质押到池子里的预计的奖励:", pending / 10 ** 18)
    userInfo = get_userInfo("0x182d8bE296CA371Ba2e314967Ea142F4d7c0820A")
    print("个人质押lp到此池子的数量", userInfo[0] / 10 ** 18)