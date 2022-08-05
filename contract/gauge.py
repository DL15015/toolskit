from app import *

ken3, swap_router, swap_mining, boost, gauge = init()
print(gauge.address)

# amount 个人质押的lp,参数输入个人钱包地址
amount = gauge.functions.userInfo("0xdf4e614dc3e91b4D8aaB7CA1622A8771d29C7923").call()
print("个人质押的lp:", amount[0]/10**18)

# total_supply 池子数量
total_supply = gauge.functions.totalSupply().call()
print("该池子总质押LP:", total_supply/10**18)
