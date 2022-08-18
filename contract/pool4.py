from app import *

ret = init()
ken3 = ret[1]


# print("pool4lp的地址", pool3lp.address)

# calc_token_amount 计算用户输入后未来交易量ken
# False交易的交易量
def get_calc_token_amount(token1, token2, token3, token4):
    calc_token_amount = ken3.functions.calc_token_amount(
        [token1 * 10 ** 18, token2, token3, token4], False).call()
    return calc_token_amount
