from app import *

ret = init()
gauge = ret[4]
print("池子的gauge地址", gauge.address)

# total_supply 所有人质押到该池子的lp的数量
totalSupply = gauge.functions.totalSupply().call()
print("所有人质押到该池子的lp的数量:", totalSupply / 10 ** 18)

# pending：个人质押到池子里的预计的奖励 参数：address 输入一个钱包账户
pending = gauge.functions.pending("0xdf4e614dc3e91b4D8aaB7CA1622A8771d29C7923").call()
print("个人质押到池子里的预计的奖励:", pending / 10 ** 18)

# userInfo：个人质押lp到此池子的数量 参数：address 输入一个钱包账户
userInfo = gauge.functions.userInfo("0xdf4e614dc3e91b4D8aaB7CA1622A8771d29C7923").call()
print("个人质押lp到此池子的数量", userInfo[0] / 10 ** 18)
