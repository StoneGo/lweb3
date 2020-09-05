from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/add0c570ed374fb69ef44b7265327bd7"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())
print(web3.eth.blockNumber)

address = '0x0cB6E830CC593b5aCA88B1D4E373C10f95dEFb92'
# address = '0x0cb6e830cc593b5aca88b1d4e272c10f95defb92'
# address = Web3.toChecksumAddress(address)

balance = web3.eth.getBalance(address)
print(web3.fromWei(balance, 'ether'))