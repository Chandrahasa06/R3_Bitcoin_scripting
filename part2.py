from bitcoinrpc.authproxy import AuthServiceProxy
import json
import os
import shutil
from decimal import Decimal

rpc_user = "your_username"
rpc_password = "your_password"
rpc_port = 18443 

try:
    rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:{rpc_port}")
    print("Connected to bitcoind successfully.")
except Exception as e:
    print(f"Error connecting to bitcoind: {e}")
    exit()

wallet_name = "R3_SegWit"

try:
    wallets = rpc_connection.listwallets()
    if wallet_name in wallets:
        print(f"Wallet '{wallet_name}' is already loaded.")
    else:
        wallet_path = f"C:\\Users\\chand\\AppData\\Roaming\\Bitcoin\\regtest\\wallets\\{wallet_name}"
        if os.path.exists(wallet_path):
            rpc_connection.loadwallet(wallet_name)
            print(f"Wallet '{wallet_name}' loaded successfully.")
        else:
            rpc_connection.createwallet(wallet_name)
            print(f"Wallet '{wallet_name}' created successfully.")
except Exception as e:
    print(f"Error with wallet: {e}")
    exit()

try:
    rpc_connection_wallet = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:{rpc_port}/wallet/{wallet_name}")
    print(f"Connected to wallet '{wallet_name}' successfully.")
except Exception as e:
    print(f"Error connecting to wallet '{wallet_name}': {e}")
    exit()

try:
    address_A = rpc_connection_wallet.getnewaddress("", "p2sh-segwit")
    address_B = rpc_connection_wallet.getnewaddress("", "p2sh-segwit")
    address_C = rpc_connection_wallet.getnewaddress("", "p2sh-segwit")
    print(f"Address A': {address_A}")
    print(f"Address B': {address_B}")
    print(f"Address C': {address_C}")

    addresses = {"address_A": address_A, "address_B": address_B, "address_C": address_C}
    with open("segwit_addresses.json", "w") as f:
        json.dump(addresses, f)
    print("Addresses saved to segwit_addresses.json")
except Exception as e:
    print(f"Error generating addresses: {e}")
    exit()

try:
    rpc_connection.generatetoaddress(101, address_A)
    print(f"101 blocks mined to Address A': {address_A}")
except Exception as e:
    print(f"Error mining blocks: {e}")
    exit()

try:
    unspent_A = rpc_connection_wallet.listunspent(0, 9999999, [address_A])
    if not unspent_A:
        print("No unspent transactions found for Address A'.")
        exit()

    utxo_value = unspent_A[0]['amount']
    print(f"UTXO Value: {utxo_value} BTC")

    fee_rate = Decimal("0.00001")  # Conservative fee rate in BTC/kB
    tx_size = Decimal("200")
    fee = fee_rate * (tx_size / Decimal("1000"))

    if utxo_value <= fee:
        print(f"UTXO value ({utxo_value} BTC) too small to cover fee ({fee} BTC).")
        rpc_connection.generatetoaddress(1, address_A)  # Mine more blocks if needed
        print("1 block mined. Address A' should now have a UTXO.")
        unspent_A = rpc_connection_wallet.listunspent(0, 9999999, [address_A])
        utxo_value = unspent_A[0]['amount']

    output_amount = utxo_value - fee
    print(f"Sending {output_amount} BTC to Address B' (Fee: {fee} BTC)")

    raw_tx_A_to_B = rpc_connection_wallet.createrawtransaction(
        [{"txid": unspent_A[0]['txid'], "vout": unspent_A[0]['vout']}],
        {address_B: float(output_amount)}
    )

    signed_tx_A_to_B = rpc_connection_wallet.signrawtransactionwithwallet(raw_tx_A_to_B)
    txid_A_to_B = rpc_connection_wallet.sendrawtransaction(signed_tx_A_to_B['hex'])
    print(f"Transaction ID (A' to B'): {txid_A_to_B}")

    decoded_tx_A_to_B = rpc_connection_wallet.decoderawtransaction(signed_tx_A_to_B['hex'])
    print(f"Decoded Transaction (A' to B'): {decoded_tx_A_to_B}")

except Exception as e:
    print(f"Error creating transaction (A' to B'): {e}")
    exit()

try:
    unspent_B = rpc_connection_wallet.listunspent(0, 9999999, [address_B])
    if not unspent_B:
        print("No unspent transactions found for Address B'.")
        exit()

    utxo_value_B = unspent_B[0]['amount']
    print(f"UTXO Value at B': {utxo_value_B} BTC")

    fee = fee_rate * (tx_size / Decimal("1000"))
    output_amount_B = utxo_value_B - fee
    print(f"Sending {output_amount_B} BTC to Address C' (Fee: {fee} BTC)")

    raw_tx_B_to_C = rpc_connection_wallet.createrawtransaction(
        [{"txid": unspent_B[0]['txid'], "vout": unspent_B[0]['vout']}],
        {address_C: float(output_amount_B)}
    )

    signed_tx_B_to_C = rpc_connection_wallet.signrawtransactionwithwallet(raw_tx_B_to_C)
    txid_B_to_C = rpc_connection_wallet.sendrawtransaction(signed_tx_B_to_C['hex'])
    print(f"Transaction ID (B' to C'): {txid_B_to_C}")

    decoded_tx_B_to_C = rpc_connection_wallet.decoderawtransaction(signed_tx_B_to_C['hex'])
    print(f"Decoded Transaction (B' to C'): {decoded_tx_B_to_C}")

except Exception as e:
    print(f"Error creating transaction (B' to C'): {e}")
    exit()

