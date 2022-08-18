from app import *

# ken3, swap_router, boost = init()
from mainnet_book import pool3lp

ret = init()
ken3 = ret[0]
# print("pool3lp的地址", pool3lp.address)

# totalSupply
# totalSupply = ken3.functions.totalSupply().call()
# log("totalSupply", web3.fromWei(totalSupply, 'ether'))

# A
A = ken3.functions.A().call()
# print("A", A)

# admin_fee
admin_fee = ken3.functions.admin_fee().call()
# print("admin_fee", admin_fee)


# calc_token_amount 计算用户输入后未来交易量ken
# False交易的交易量
def get_calc_token_amount(token1, token2, token3):
    calc_token_amount = ken3.functions.calc_token_amount(
        [token1 * 10 ** 18, token2, token3], False).call()
    return calc_token_amount


calc_token_amount = get_calc_token_amount(3, 0, 0)
# print("计算用户输入后未来交易量ken", calc_token_amount)


#  get_dy 计算用户输入后未来的token量
def get_dy(token1, token2, amount):
    get_dy = ken3.functions.get_dy(token1, token2, amount * 10 ** 18).call()
    return get_dy


get_dy = get_dy(1, 2, 100)
# print("计算用户输入后未来的token量", get_dy)

"""
    =============== write ===============
"""
# withdraw_admin_fees
# func = ken3.functions.withdraw_admin_fees().build_transaction(
#     {
#         "from": account_addr,
#         "gasPrice": web3.eth.gas_price,
#         "nonce": web3.eth.get_transaction_count(account_addr),
#         "chainId": 321
#     }
# )
# print(func)
# print(send_transaction(func))

# allowance = ken3.functions.allcwance().call()
#
# balanceOf = ken3.functions.balanceOf().call()
#
# symbol = ken3.functions.symbol().call()
#
# name = ken3.functions.name().call()
#
# future_A_time = ken3.functions.future_A_time().call()
