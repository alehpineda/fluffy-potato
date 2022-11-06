import time
import datetime
import os
from brownie import *

# FTM scan api
FTM_SCAN_API_KEY = "94QJM8YQICVFNIGPDTC7F7RZNMC54UIUYX"

os.environ["FTMSCAN_TOKEN"] = FTM_SCAN_API_KEY

# Load user
user = accounts.load(filename="test_account", password="1qaz2wsx3EDC4RFV.2023")
# Connect to blockchaing
network.connect("ftm-main")

# Load contracts

# Tokens
boo_contract = Contract.from_explorer(
    "0x841FAD6EAe12c286d1Fd18d1d525DFfA75C7EFFE"
)

xboo_contract = Contract.from_explorer(
    "0xa48d959AE2E88f1dAA7D5F611E01908106dE7598"
)

# Stables
MAI_ADDRESS = "0xfB98B335551a418cD0737375a2ea0ded62Ea213b"

mai_contract = Contract.from_explorer(MAI_ADDRESS)

DEI_ADDRESS = "0xDE1E704dae0B4051e80DAbB26ab6ad6c12262DA0"

dei_contract = Contract.from_explorer(DEI_ADDRESS)

USDC_ADDRESS = "0x04068DA6C83AFCFA0e13ba15A6696662335D5B75"

usdc_contract = Contract.from_explorer(USDC_ADDRESS)

TUSD_ADDRESS = "0x9879aBDea01a879644185341F7aF7d8343556B7a"

tusd_contract = Contract.from_explorer(TUSD_ADDRESS)

# FTM

WFTM_ADDRESS = "0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83"

wftm_contract = Contract.from_explorer(WFTM_ADDRESS)

BEFTM_ADDRESS = "0x7381eD41F6dE418DdE5e84B55590422a57917886"

beftm_contract = Contract.from_explorer(BEFTM_ADDRESS)

SFTMX_ADDRESS = "0xd7028092c830b5C8FcE061Af2E593413EbbC1fc1"

sftmx_contract = Contract.from_explorer(SFTMX_ADDRESS)

# Routers
spooky_swap_router_contract = Contract.from_explorer(
    "0xF491e7B69E4244ad4002BC14e878a34207E38c29"
)

# Declare tokens

boo = {
    "address": boo_contract.address,
    "symbol": boo_contract.symbol(),
    "decimals": boo_contract.decimals(),
}

xboo = {
    "address": xboo_contract.address,
    "symbol": xboo_contract.symbol(),
    "decimals": xboo_contract.decimals(),
}

wftm = {
    "address": wftm_contract.address,
    "symbol": wftm_contract.symbol(),
    "decimals": wftm_contract.decimals(),
}

dei = {
    "address": dei_contract.address,
    "symbol": dei_contract.symbol(),
    "decimals": dei_contract.decimals(),
}

usdc = {
    "address": usdc_contract.address,
    "symbol": usdc_contract.symbol(),
    "decimals": usdc_contract.decimals(),
}

mai = {
    "address": mai_contract.address,
    "symbol": mai_contract.symbol(),
    "decimals": mai_contract.decimals(),
}

tusd = {
    "address": tusd_contract.address,
    "symbol": tusd_contract.symbol(),
    "decimals": tusd_contract.decimals(),
}

beftm = {
    "address": beftm_contract.address,
    "symbol": beftm_contract.symbol(),
    "decimals": beftm_contract.decimals(),
}

sftmx = {
    "address": sftmx_contract.address,
    "symbol": sftmx_contract.symbol(),
    "decimals": sftmx_contract.decimals(),
}

# Token pairs

token_pairs = [
    # (boo,xboo),
    # (xboo,boo),
    # (wftm, boo),
    # (boo, wftm),
    (dei, usdc),
    (usdc, dei),
    (wftm, beftm),
    (beftm, wftm),
    (wftm, sftmx),
    (sftmx, wftm),
    (usdc, mai),
    (mai, usdc),
    (usdc, tusd),
    (tusd, usdc),
]

while True:
    for token_in, token_out in token_pairs:
        # token_in = pair[0]
        # token_out = pair[1]
        qty_out = spooky_swap_router_contract.getAmountsOut(
            1 * (10 ** token_in["decimals"]),
            [
                token_in["address"],
                # wftm["address"],
                token_out["address"],
            ],
        )[-1] / (10 ** token_out["decimals"])

        ratio_xboo_for_boo = xboo_contract.xBOOForBOO(
            1 * (10 ** xboo.get("decimals")) / (10 ** boo.get("decimals"))
        )
        ratio_boo_forx_boo = xboo_contract.BOOForxBOO(
            1 * (10 ** boo.get("decimals")) / (10 ** xboo.get("decimals"))
        )
        # if qty_out >= 1.005:
        print(
            f"{datetime.datetime.now().strftime('[%I:%M:%S %p]')} {token_in['symbol']} → {token_out['symbol']}: ({qty_out:.6f})"
        )

        time.sleep(0.1)
