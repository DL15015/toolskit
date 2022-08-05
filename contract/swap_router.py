from app import *

ken3, swap_router, boost, gauge = init()
print(swap_router.address)

# swapMining
swap_mining = swap_router.functions.swapMining().call()
print(swap_mining)
