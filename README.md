# fluffy-potato

A fluffy potato

Create venv and install requirements

```bash
sudo apt install gcc python3-dev
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Check brownie

```bash
brownie --version
```

Create test account

```bash
brownie accounts generate test_account
```

Check if avax-main is there

```bash
brownie networks modify avax-main
```

Add a network to brownie

```bash
brownie networks add Avalanche avax-main 
host=https://api.avax.network/ext/bc/C/rpc 
explorer=https://api.snowtrace.io/api 
chainid=43114 
name=Mainnet
```
