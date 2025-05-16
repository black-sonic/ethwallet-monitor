# ethwallet-monitor

A simple CLI tool to check wallet balances on Ethereum, Binance Smart Chain (BSC), and Solana networks (Mainnet & Testnet/Devnet).

## Features
- Check balances for multiple wallet addresses
- Supports Ethereum, BSC, and Solana networks
- Interactive CLI input for selecting network environment and addresses
- Resolves ENS names for Ethereum addresses
- Displays wallet balances with USD value
- Clear console interface for easy use

## Requirements
- Python 3.7+
- `requests` library (`pip install requests`)

## Setup
1. Clone the repo or download the files.
2. Add your Etherscan and BscScan API keys inside the script (`balance_checker.py`).
3. Run the script:
   ```bash
   python3 balance_checker.py



## Supported Networks

| Network Type | Network                | Notes                        |
|--------------|------------------------|------------------------------|
| Mainnet      | Ethereum Mainnet       | Uses Etherscan API           |
| Mainnet      | Binance Smart Chain    | Uses BscScan API             |
| Mainnet      | Solana Mainnet         | Uses Solana JSON-RPC         |
| Testnet      | Ethereum Sepolia       | Uses Etherscan Sepolia API   |
| Testnet      | Binance Smart Chain    | Uses BscScan Testnet API     |
| Testnet      | Solana Devnet          | Uses Solana Devnet JSON-RPC  |
