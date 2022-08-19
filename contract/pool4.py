from app import *
from testnet_book import ken3_busd_pool_address

ret = init()
pool4 = ret[2]


# calc_token_amount 计算用户输入后未来交易量ken
# False交易的交易量,True是流动性，计算预计可得到的lp
def get_calc_token_amount(pool_address, token1, token2, token3, token4):
    calc_token_amount = pool4.functions.calc_token_amount(pool_address,
                                                          [token1 * 10 ** 18, token2 * 10 ** 18, token3 * 10 ** 18,
                                                           token4 * 10 ** 18], True).call()
    return calc_token_amount


calc_token_amount = get_calc_token_amount(ken3_busd_pool_address, 100, 100, 100, 100)
print("计算用户输入后计算预计可得到的lp", calc_token_amount)
