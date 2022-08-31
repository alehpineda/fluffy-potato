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
brownie networks add Avalanche avax-main host=https://api.avax.network/ext/bc/C/rpc explorer=https://api.snowtrace.io/api chainid=43114 name=Mainnet
```

Add PulseChain Testnet 2b to brownie

```bash
brownie networks add Pulsechain pls-testnet2b host=https://rpc.v2b.testnet.pulsechain.com explorer=https://scan.v2b.testnet.pulsechain.com chainid=941 name=Testnet2b
```

Check pulsechain

```bash
brownie networks modify pls-testnet2b
```

Start brownie console with avax switch

```bash
brownie console --network avax-main
>>>
```

Start brownie console with pls switch

```bash
brownie console --network pls-testnet2b
>>>
```

Load user account in brownie console

```python
>>> user = accounts.load('test_account')  # Will ask for password
```

Check functions and parameters of object user

```python
>>> dir(user)
[address, balance, deploy, estimate_gas, gas_used, get_deployment_address, nonce, private_key, public_key, save, sign_defunct_message, sign_message, transfer]

>>> user.address  # Variable
'0x56FEd647eE25f723656BE94e61EB914Ed220B8C2'

>>> user.balance()  # Method
0

>>> user.public_key
'0x2cc8c4b6367b0e4b1f2650c573e879aa5bc6b6efefe05efe6bc82ef3ed18eb93514d686879f231e469cc02d6c5b8c8faaa64a5395007c78cfcec0bef2954b128'

>>> someone_else = network.account.PublicKeyAccount('0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7')  # wrapped avax contract
>>> someone_else.balance()
1718383260750216476

>>> hex = network.account.PublicKeyAccount('0x2b591e99afE9f32eAA6214f7B7629768c40Eeb39')  # Hex contract
>>> hex.balance()
920462812133182713256000
```

Get a contract from explorer

```python
>>> wavax_contract = Contract.from_explorer('0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7')
```

Troubleshooting

```python
SolcInstallationError: Downloaded binary would not execute, or returned unexpected output. If this issue persists, you can try to compile from source code using `solcx.compile_solc('>
```

Install pyenv

```bash
bash <(curl -sSL https://raw.githubusercontent.com/zaemiel/ubuntu-pyenv-installer/master/ubuntu-pyenv-installer.sh)

# Selected option 1.

pyenv install --list  # list all python versions available to install

```

[Pyenv Tutorial](https://towardsdatascience.com/python-how-to-create-a-clean-learning-environment-with-pyenv-pyenv-virtualenv-pipx-ed17fbd9b790)

3.7.13
3.8.10
3.8.13
3.9.13
3.10.6

