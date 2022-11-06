import time
import datetime
from brownie import *
from abi import ERC20

# Load user
user = accounts.load(filename="test_account", password="1qaz2wsx3EDC4RFV.2023")
# Connect to blockchaing
network.connect("pls-testnet2b")

# Load contracts
# Load contracts from abi
# spell = Contract.from_abi(name="SPELL Token",
# address="0x3e6648c5a70a150a88bce65f4ad4d506fe15d2af", abi=ERC20_ABI)

wpls_contract = Contract.from_explorer(
    "0x8a810ea8B121d08342E9e7696f4a9915cBE494B7"
)

pls_contract = Contract.from_abi(
    name="Pulse Token",
    address="0xe919A09DF295cEb8eC6a13fe4606f9020afafbA9",
    abi=ERC20,
)

# plsx_contract = Contract.from_explorer(
#    "0x07895912f3AB0E33aB3a4CEFbdf7a3e121eb9942"
# )
plsx_contract = Contract.from_abi(
    name="PulseX Token",
    address="0x07895912f3AB0E33aB3a4CEFbdf7a3e121eb9942",
    abi=ERC20,
)

# usdc_contract = Contract.from_explorer(
#    "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
# )

usdc_contract = Contract.from_abi(
    name="USDC Token",
    address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    abi=ERC20,
)

# inc_contract = Contract.from_explorer(
#    "0x083F559993227395009596f77496FDc48e84C69a"
# )

inc_contract = Contract.from_abi(
    name="INC Token",
    address="0x083F559993227395009596f77496FDc48e84C69a",
    abi=ERC20,
)

# prt_contract = Contract.from_explorer(
#    "0x89130eCf4044E3E12992FEcCF354F26F8e96D3C7"
# )

prt_contract = Contract.from_abi(
    name="PRT Token",
    address="0x89130eCf4044E3E12992FEcCF354F26F8e96D3C7",
    abi=ERC20,
)

plsx_router_contract = Contract.from_explorer(
    "0xb4A7633D8932de086c9264D5eb39a8399d7C0E3A"
)

# hex_contract = Contract.from_explorer(
#    "0x2b591e99afe9f32eaa6214f7b7629768c40eeb39"
# )

hex_contract = Contract.from_abi(
    name="HEX Token",
    address="0x2b591e99afE9f32eAA6214f7B7629768c40Eeb39",
    abi=ERC20,
)

# Declare tokens

wpls = {
    "address": pls_contract.address,
    "symbol": pls_contract.symbol(),
    "decimals": pls_contract.decimals(),
}

plsx = {
    "address": plsx_contract.address,
    "symbol": plsx_contract.symbol(),
    "decimals": plsx_contract.decimals(),
}

usdc = {
    "address": usdc_contract.address,
    "symbol": usdc_contract.symbol(),
    "decimals": usdc_contract.decimals(),
}

inc = {
    "address": inc_contract.address,
    "symbol": inc_contract.symbol(),
    "decimals": inc_contract.decimals(),
}

prt = {
    "address": prt_contract.address,
    "symbol": prt_contract.symbol(),
    "decimals": prt_contract.decimals(),
}

token_pairs = [
    (wpls, plsx),
    (plsx, wpls),
    (wpls, usdc),
    (usdc, wpls),
    (wpls, prt),
    (prt, wpls),
    (wpls, inc),
    (inc, wpls),
    (plsx, inc),
    (inc, plsx),
]

while True:
    for token_in, token_out in token_pairs:
        # token_in = pair[0]
        # token_out = pair[1]
        qty_out = plsx_router_contract.getAmountsOut(
            1 * (10 ** token_in["decimals"]),
            [
                token_in["address"],
                token_out["address"],
            ],
        )[-1] / (10 ** token_out["decimals"])
        # if qty_out >= 1.01:
        print(
            f"{datetime.datetime.now().strftime('[%I:%M:%S %p]')} {token_in['symbol']} → {token_out['symbol']}: ({qty_out:.6f})"
        )
        time.sleep(1)
