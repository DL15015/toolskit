from web3 import Web3
import json as json
import book as book

# rpc point
rpc_url = "https://rpc-testnet.kcc.network"
web3 = Web3(Web3.HTTPProvider(rpc_url))

# test connector
print("connected   ?", web3.isConnected())
print("blockNumber :", web3.eth.blockNumber)

# account
account_addr = "0x13F0b2a9691bB72cae72616b39E798a824F18271"
private_key = "a169188d442a35eff327a448d864d82523f95e07a20e76247230ba38c596d0dd"

# testing
balance = web3.eth.getBalance(account_addr)
print("account     :", account_addr)
print("balance     :", web3.fromWei(balance, "ether"))
print("")


def init():
    with open("../abi/3pool_abi.json") as f:
        _abi = json.load(f)
        ken3 = web3.eth.contract(address=book.ken3, abi=_abi["abi"])
    with open("../abi/swap_router_abi.json") as f:
        _abi = json.load(f)
        swap_router = web3.eth.contract(address=book.swap_router, abi=_abi["abi"])
    with open("../abi/swap_mining_abi.json") as f:
        _abi = json.load(f)
        swap_mining = web3.eth.contract(address=book.swap_mining, abi=_abi["abi"])
    with open("../abi/boost_abi.json") as f:
        _abi = json.load(f)
        boost = web3.eth.contract(address=book.boost, abi=_abi["abi"])
    with open("../abi/gauge_abi.json") as f:
        _abi = json.load(f)
        gauge = web3.eth.contract(address=book.gauge, abi=_abi["abi"])
    return ken3, swap_router, swap_mining, boost, gauge


def log(tag, value):
    print(tag + ":", value)


def send_transaction(_func):
    signed_txn = web3.eth.account.sign_transaction(_func, private_key=private_key)
    # ha = web3.toHex(web3.keccak(signed_txn.rawTransaction))
    # print("ha: ", ha)

    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    # print("tx_receipt: ", tx_receipt)
    return tx_receipt