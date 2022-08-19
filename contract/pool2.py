from app import *

ret = init()
pool2 = ret[0]


# print("pool5lp的地址", pool5lp.address)


# calc_token_amount 计算用户输入后未来交易量ken
# False交易的交易量,True是流动性，计算预计可得到的lp
def get_calc_token_amount(token1, token2):
    calc_token_amount = pool2.functions.calc_token_amount(
        [token1 * 10 ** 18, token2 * 10 ** 18], True).call()
    return calc_token_amount


calc_token_amount = get_calc_token_amount(100, 100)
print("计算用户输入后计算预计可得到的lp", calc_token_amount)
