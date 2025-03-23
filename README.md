# Bitcoin_scripting
# 🚀 Bitcoin Scripting: Legacy & SegWit Transactions

## 📌 Introduction
This project is designed as part of **CS 216: Introduction to Blockchain**, focusing on Bitcoin transactions and scripting using **Legacy (P2PKH)** and **SegWit (P2SH-P2WPKH)** formats. The primary goals include:

✔️ Setting up a **Bitcoin Core regtest environment**  
✔️ Generating and signing **Bitcoin transactions** programmatically  
✔️ Understanding **locking and unlocking scripts**  
✔️ Evaluating **transaction size and efficiency**  
✔️ Utilizing **Bitcoin Debugger (`btcdeb`)** for validation  

---

## 👥 Team Members
- Rachakonda Chandrahasa (230001065)  
- Reena Meena (230003057)  
- Rahul Kumar (230001066)    

---

## 🎯 Objectives
### **1️⃣ Legacy Transactions (P2PKH)**
- Create **Bitcoin addresses (A, B, C)**  
- Execute transactions **A → B → C**  
- Extract **ScriptPubKey and ScriptSig**  
- Debug transactions with **btcdeb**  

### **2️⃣ SegWit Transactions (P2SH-P2WPKH)**
- Generate **SegWit addresses (A', B', C')**  
- Conduct transactions **A' → B' → C'**  
- Analyze **witness data and signature separation**  
- Compare **P2PKH vs. SegWit**  

### **3️⃣ Comparative Analysis**
- Measure and contrast **transaction sizes**  
- Explain **P2PKH vs. P2SH-P2WPKH scripts**  
- Discuss **SegWit’s impact on scalability and malleability**  

---

## ⚙️ Required Tools
- **Bitcoin Core (`bitcoind`)** – Full Bitcoin node  
- **Bitcoin CLI (`bitcoin-cli`)** – Command-line utility  
- **Python (`python-bitcoinlib`, `bitcoinrpc`)** – Scripting automation  
- **Bitcoin Debugger (`btcdeb`)** – Transaction verification  
- **C (`libbitcoin`, `curl` for RPC)** – Alternative implementation  

---

## 🛠️ Setup Instructions
### **1️⃣ Install Bitcoin Core**
#### **Windows**
1. Download from [Bitcoin Core official site](https://bitcoincore.org/en/download/).
2. Run the installer and follow the setup instructions.
3. Open **Command Prompt**, navigate to the Bitcoin installation directory.

#### **Linux (Ubuntu/Debian)**
```bash
sudo apt update && sudo apt install bitcoin-core
bitcoind --version
```

### **2️⃣ Start Bitcoin Core in Regtest Mode**
```bash
bitcoind -regtest
```
This initializes a **local test environment** for Bitcoin transactions.

### **3️⃣ Configure `bitcoin.conf`**
```ini
[regtest]
regtest=1
server=1
rpcuser=admin
rpcpassword=securepass
rpcallowip=127.0.0.1
rpcport=18443
txindex=1
fallbackfee=0.0002
mintxfee=0.00001
txconfirmtarget=6
```
🔹 *Update `rpcuser` and `rpcpassword` accordingly.*

### **4️⃣ Python Script for RPC Calls**
```python
import requests

rpc_user = 'admin'
rpc_password = 'securepass'
rpc_port = 18443

url = f"http://127.0.0.1:{rpc_port}"
headers = {"content-type": "application/json"}
auth = (rpc_user, rpc_password)

response = requests.get(url, auth=auth)
print(response.json())
```

### **5️⃣ Running the Script**
```bash
python3 bitcoin_script.py
```

### **Essential Bitcoin Commands**
```bash
# Check wallet balance
bitcoin-cli -regtest getbalance

# Generate new blocks
bitcoin-cli -regtest generatetoaddress 1 <your_address>

# List wallet transactions
bitcoin-cli -regtest listtransactions
```

---

## 🔄 Transaction Execution
### **1️⃣ Legacy Transactions (P2PKH)**
- Generate **Legacy Bitcoin addresses** (A, B, C)
- Fund **Address A** and send Bitcoin to **B**
- Extract **ScriptPubKey and ScriptSig**
- Sign and broadcast transactions
- Debug transactions using **btcdeb**

### **2️⃣ SegWit Transactions (P2SH-P2WPKH)**
- Generate **SegWit addresses** (A', B', C')
- Fund **Address A'** and transfer to **B'**
- Extract **witness data and signature**
- Sign and validate transactions
- Analyze using **btcdeb**

---

