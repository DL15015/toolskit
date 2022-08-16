from app import *

# ken3, swap_router, boost = init()
ret = init()
ken3 = ret[0]
print("ken3的地址", ken3.address)

# totalSupply
totalSupply = ken3.functions.totalSupply().call()
log("totalSupply", web3.fromWei(totalSupply, 'ether'))

# A
A = ken3.functions.A().call()
print(A)

# admin_fee
admin_fee = ken3.functions.admin_fee().call()
print(admin_fee)

# calc_token_amount
# calc_token_amount = ken3.functions.calc_token_amount([0,10000000000000000000,0], True).call()
# print(calc_token_amount)

"""
    =============== write ===============
"""
# withdraw_admin_fees
func = ken3.functions.withdraw_admin_fees().build_transaction(
    {
        "from": account_addr,
        "gasPrice": web3.eth.gas_price,
        "nonce": web3.eth.get_transaction_count(account_addr),
        "chainId": 322
    }
)
# print(func)
print(send_transaction(func))

allowance = ken3.functions.allcwance().call()

balanceOf = ken3.functions.balanceOf().call()

symbol = ken3.functions.symbol().call()

name = ken3.functions.name().call()

future_A_time = ken3.functions.future_A_time().call()
