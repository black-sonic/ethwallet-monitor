# ethwallet-monitor

A simple CLI tool to check wallet balances on Ethereum and Binance Smart Chain (BSC) networks — supports both mainnet and testnet.

## Features

- Check balances for multiple wallet addresses
- Supports Ethereum and BSC networks (mainnet & testnet)
- Interactive CLI input for network and addresses
- Logs balance results with timestamps

## Requirements

- Python 3.7+
- `requests` library (`pip install requests`)

## Setup

1. Clone the repo or download the files.
2. Add your Etherscan and BscScan API keys inside `balance_checker.py`.
3. Run the script:
   ```bash
   python3 balance_checker.py

