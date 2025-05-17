# ethwallet-monitor

A simple CLI tool to check wallet balances on Ethereum, Binance Smart Chain (BSC), Solana, Base, and Linea networks (Mainnet & Testnet/Devnet).

## Features
- Check balances for multiple wallet addresses
- Supports Ethereum, BSC, Solana, and Base networks
- Interactive CLI input for selecting network environment and addresses
- Resolves ENS names for Ethereum addresses
- Displays wallet balances with USD value
- Clear console interface for easy use

## Requirements
- Python 3.7+
- `requests` library (`pip install requests`)

## Setup
1. Clone the repo or download the files.
2. Add your Etherscan, BscScan, and other necessary API keys inside the script (`balance_checker.py`).
3. Run the script:
   ```bash
   python3 balance_checker.py


| Network Type | Network              | Notes                       |
| ------------ | -------------------- | --------------------------- |
| Mainnet      | Ethereum Mainnet     | Uses Etherscan API          |
| Mainnet      | Binance Smart Chain  | Uses BscScan API            |
| Mainnet      | Solana Mainnet       | Uses Solana JSON-RPC        |
| Mainnet      | Base Mainnet         | Uses Base Mainnet JSON-RPC  |
| Testnet      | Ethereum Sepolia     | Uses Etherscan Sepolia API  |
| Testnet      | Binance Smart Chain  | Uses BscScan Testnet API    |
| Testnet      | Solana Devnet        | Uses Solana Devnet JSON-RPC |
| Testnet      | Base Sepolia Testnet | Uses Base Sepolia JSON-RPC  |


Notes
Make sure your API keys are valid and have enough quota for requests.

For Base network support, the script uses direct JSON-RPC calls due to lack of public API scan endpoints.

ENS resolution works only for .eth domains.