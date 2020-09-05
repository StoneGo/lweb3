import json
from web3 import Web3

from web3 import Web3
ganache_url ="http://127.0.0.1:7545"
web3=Web3(Web3.HTTPProvider(ganache_url))

account_1="0xCE7Bc0d8825745D201A9D08b70Af7d1dD3D31C97"
account_2="0xE16FdEc3f61d7743Fc54E76745ca1256D2261f1C"
private_key ="7ea3fa96f35e65087ca3075668d0cfdcec28eb01e6219ba717638fa2342de660"

nonce = web3.eth.getTransactionCount(account_1)

tx = {
  'nonce': nonce,
  'to': account_2,
  'value': web3.toWei(1, 'ether'),
  'gas': 6721975,
  'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx= web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))