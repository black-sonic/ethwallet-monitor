import os
import requests

ARBISCAN_API_KEYS = {
    "arbitrum_mainnet": "4CYSR4DWMBFC75FWVMFHQMK19JC1XM1WRQ",
    "arbitrum_sepolia": "4CYSR4DWMBFC75FWVMFHQMK19JC1XM1WRQ"
}

OPTIMISMSCAN_API_KEYS = {
    "optimism_mainnet": "ZVIU3VFGXHU1VHJPA6QIHAKPBS9KVQGJ8W",
    "optimism_sepolia": "ZVIU3VFGXHU1VHJPA6QIHAKPBS9KVQGJ8W"
}

POLYGONSCAN_API_KEYS = {
    "polygon_mainnet": "6Z1MTASGS9U98QDA13TF7QUZRKM3VTKVXY"
}
ETHERSCAN_API_KEYS = {
    "eth_mainnet": "EFDG86S8WVCUFD9S8EGWQ5Y1RUC1AF8XTE",
    "eth_sepolia": "EFDG86S8WVCUFD9S8EGWQ5Y1RUC1AF8XTE"
}
BSCSCAN_API_KEYS = {
    "bsc_mainnet": "J5USYZ6DDY64BTNIZRPP6XPDEVW4EU3UEE",
    "bsc_testnet": "J5USYZ6DDY64BTNIZRPP6XPDEVW4EU3UEE"
}

NETWORK_CONFIG = {
    "eth_mainnet": {
        "name": "Ethereum Mainnet",
        "url": "https://api.etherscan.io/api",
        "apikey": ETHERSCAN_API_KEYS["eth_mainnet"],
        "symbol": "ethereum",
        "unit": "ETH"
    },
    "bsc_mainnet": {
        "name": "Binance Smart Chain Mainnet",
        "url": "https://api.bscscan.com/api",
        "apikey": BSCSCAN_API_KEYS["bsc_mainnet"],
        "symbol": "binancecoin",
        "unit": "BNB"
    },
    "eth_sepolia": {
        "name": "Ethereum Sepolia Testnet",
        "url": "https://api-sepolia.etherscan.io/api",
        "apikey": ETHERSCAN_API_KEYS["eth_sepolia"],
        "symbol": "ethereum",
        "unit": "ETH"
    },
    "bsc_testnet": {
        "name": "Binance Smart Chain Testnet",
        "url": "https://api-testnet.bscscan.com/api",
        "apikey": BSCSCAN_API_KEYS["bsc_testnet"],
        "symbol": "binancecoin",
        "unit": "BNB"
    },
    "solana_mainnet": {
        "name": "Solana Mainnet",
        "url": "https://api.mainnet-beta.solana.com",
        "symbol": "solana",
        "unit": "SOL"
    },
    "solana_devnet": {
        "name": "Solana Devnet",
        "url": "https://api.devnet.solana.com",
        "symbol": "solana",
        "unit": "SOL"
    },
    "base_sepolia": {
        "name": "Base Sepolia Testnet",
        "rpc_url": "https://sepolia.base.org",
        "symbol": "ethereum",
        "unit": "ETH"
    },
    "base_mainnet": {
        "name": "Base Mainnet",
        "rpc_url": "https://mainnet.base.org",
        "symbol": "ethereum",
        "unit": "ETH"
    },
    "linea_sepolia": {
        "name": "Linea Sepolia Testnet",
        "rpc_url": "https://rpc.sepolia.linea.build",
        "symbol": "ethereum",
        "unit": "ETH"
    },
    "linea_mainnet": {
        "name": "Linea Mainnet",
        "rpc_url": "https://rpc.linea.build",
        "symbol": "ethereum",
        "unit": "ETH"
    },
        "polygon_mainnet": {
        "name": "Polygon Mainnet",
        "url": "https://api.polygonscan.com/api",
        "apikey": POLYGONSCAN_API_KEYS["polygon_mainnet"],
        "symbol": "matic-network",
        "unit": "MATIC"
    },
    "cardona_testnet": {
        "name": "Polygon zkEVM Cardona Testnet",
        "rpc_url": "https://rpc.cardona.zkevm-rpc.com",
        "symbol": "ethereum",
        "unit": "ETH"
    },
    "optimism_mainnet": {
        "name": "Optimism Mainnet",
        "url": "https://api-optimistic.etherscan.io/api",
        "apikey": OPTIMISMSCAN_API_KEYS["optimism_mainnet"],
        "symbol": "ethereum",
        "unit": "ETH"
    },
    "optimism_sepolia": {
        "name": "Optimism Sepolia Testnet",
        "url": "https://api-sepolia-optimism.etherscan.io/api",
        "apikey": OPTIMISMSCAN_API_KEYS["optimism_sepolia"],
        "symbol": "ethereum",
        "unit": "ETH"
    },
    "arbitrum_mainnet": {
        "name": "Arbitrum One Mainnet",
        "url": "https://api.arbiscan.io/api",
        "apikey": ARBISCAN_API_KEYS["arbitrum_mainnet"],
        "symbol": "ethereum",
        "unit": "ETH"
    },
    "arbitrum_sepolia": {
        "name": "Arbitrum Sepolia Testnet",
        "url": "https://api-sepolia.arbiscan.io/api",
        "apikey": ARBISCAN_API_KEYS["arbitrum_sepolia"],
        "symbol": "ethereum",
        "unit": "ETH"
    },

}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_price(symbol):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
        res = requests.get(url)
        if res.status_code == 200:
            return res.json().get(symbol, {}).get("usd")
    except Exception as e:
        print(f"Price fetch error: {e}")
    return None

def resolve_ens(name):
    if name.endswith(".eth"):
        try:
            url = f"https://api.ensideas.com/ens/resolve/{name}"
            res = requests.get(url)
            if res.status_code == 200:
                return res.json().get("address")
        except:
            return None
    return name

def check_balance(network_key):
    network = NETWORK_CONFIG[network_key]
    while True:
        clear()
        print(f"{network['name']}")
        raw_input_addr = input("Enter wallet address or ENS (or press Enter to return): ").strip()
        if raw_input_addr == "":
            break

        address = resolve_ens(raw_input_addr)
        if not address or not address.startswith("0x") or len(address) != 42:
            print("Invalid address or ENS.")
            input("Press Enter to continue...")
            continue

        # Handle networks using etherscan-like API
        if network_key in ["base_sepolia", "base_mainnet", "linea_sepolia", "linea_mainnet"]:
            print("Use dedicated menu for Base or Linea network.")
            input("Press Enter to continue...")
        else:
            url = f"{network['url']}?module=account&action=balance&address={address}&tag=latest&apikey={network.get('apikey','')}"
            try:
                response = requests.get(url)
                data = response.json()
                if data.get("status") == "1":
                    balance_wei = int(data.get("result"))
                    balance = balance_wei / 10**18
                    unit = network["unit"]
                    print(f"\n{unit} Balance : {balance:.8f} {unit}")

                    price = get_price(network["symbol"])
                    if price:
                        value_usd = balance * price
                        print(f"{unit} Value   : ${value_usd:.2f} (@ ${price:.2f}/{unit})")
                    else:
                        print("Unable to fetch USD price.")
                else:
                    print("Failed to fetch balance:", data.get("message"))
            except Exception as e:
                print("Error occurred:", e)

        input("\nPress Enter to continue...")

def check_base_balance(address, network_key):
    network = NETWORK_CONFIG[network_key]
    url = network["rpc_url"]
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            if "result" in data:
                balance_wei = int(data["result"], 16)
                balance = balance_wei / 1e18
                unit = network["unit"]
                print(f"\n{unit} Balance : {balance:.8f} {unit}")

                price = get_price(network["symbol"])
                if price:
                    value_usd = balance * price
                    print(f"{unit} Value   : ${value_usd:.2f} (@ ${price:.2f}/{unit})")
                else:
                    print("Unable to fetch USD price.")
            else:
                print("Failed to fetch balance:", data.get("error", {}).get("message", "Unknown error"))
        else:
            print(f"Error fetching balance: {response.status_code}")
    except Exception as e:
        print("Error occurred:", e)

def check_base_balance_menu(network_key):
    network = NETWORK_CONFIG[network_key]
    while True:
        clear()
        print(f"{network['name']}")
        raw_input_addr = input("Enter wallet address or ENS (or press Enter to return): ").strip()
        if raw_input_addr == "":
            break

        address = resolve_ens(raw_input_addr)
        if not address or not address.startswith("0x") or len(address) != 42:
            print("Invalid address or ENS.")
            input("Press Enter to continue...")
            continue
        
        check_base_balance(address, network_key)
        input("\nPress Enter to continue...")

def check_solana_balance(network_key):
    network = NETWORK_CONFIG[network_key]
    while True:
        clear()
        print(f"{network['name']}")
        address = input("Enter Solana wallet address (or press Enter to return): ").strip()
        if address == "":
            break

        headers = {"Content-Type": "application/json"}
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBalance",
            "params": [address]
        }

        try:
            response = requests.post(network["url"], headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                if "result" in data:
                    lamports = data["result"]["value"]
                    balance = lamports / 1e9  # 1 SOL = 1e9 lamports
                    unit = network["unit"]
                    print(f"\n{unit} Balance : {balance:.8f} {unit}")

                    price = get_price(network["symbol"])
                    if price:
                        value_usd = balance * price
                        print(f"{unit} Value   : ${value_usd:.2f} (@ ${price:.2f}/{unit})")
                    else:
                        print("Unable to fetch USD price.")
                else:
                    print("Failed to fetch balance:", data.get("error", {}).get("message", "Unknown error"))
            else:
                print(f"Error fetching balance: {response.status_code}")
        except Exception as e:
            print("Error occurred:", e)

        input("\nPress Enter to continue...")

def handle_mainnet():
    while True:
        clear()
        print("Select network (Mainnet):")
        print("1. Ethereum Mainnet")
        print("2. Binance Smart Chain Mainnet")
        print("3. Solana Mainnet")
        print("4. Base Mainnet")
        print("5. Linea Mainnet")
        print("6. Polygon Mainnet")
        print("7. Optimism Mainnet")
        print("8. Arbitrum One Mainnet")  # Tambahkan ini
        print("0. Back")
        choice = input("Enter choice (0/1/2/3/4/5): ").strip()

        if choice == "0":
            break
        elif choice == "1":
            check_balance("eth_mainnet")
        elif choice == "2":
            check_balance("bsc_mainnet")
        elif choice == "3":
            check_solana_balance("solana_mainnet")
        elif choice == "4":
            check_base_balance_menu("base_mainnet")
        elif choice == "5":
            check_base_balance_menu("linea_mainnet")
        elif choice == "6":
            check_balance("polygon_mainnet")
        elif choice == "7":
            check_balance("optimism_mainnet")
        elif choice == "8":
            check_balance("arbitrum_mainnet")
        else:
            input("Invalid choice. Press Enter to continue...")

def handle_testnet():
    while True:
        clear()
        print("Select network (Testnet):")
        print("1. Ethereum Sepolia Testnet")
        print("2. Binance Smart Chain Testnet")
        print("3. Solana Devnet")
        print("4. Base Sepolia Testnet")
        print("5. Linea Sepolia Testnet")
        print("6. zkEVM Cardona Testnet")
        print("7. Optimism Sepolia Testnet")
        print("8. Arbitrum Sepolia Testnet")
        print("0. Back")
        choice = input("Enter choice (0/1/2/3/4/5): ").strip()

        if choice == "0":
            break
        elif choice == "1":
            check_balance("eth_sepolia")
        elif choice == "2":
            check_balance("bsc_testnet")
        elif choice == "3":
            check_solana_balance("solana_devnet")
        elif choice == "4":
            check_base_balance_menu("base_sepolia")
        elif choice == "5":
            check_base_balance_menu("linea_sepolia")
        elif choice == "6":
            check_base_balance_menu("cardona_testnet")
        elif choice == "7":
            check_balance("optimism_sepolia")
        elif choice == "8":
            check_balance("arbitrum_sepolia")
        else:
            input("Invalid choice. Press Enter to continue...")

def main():
    while True:
        clear()
        print("=== Crypto Wallet Balance Checker ===")
        print("1. Mainnet")
        print("2. Testnet")
        print("0. Exit")
        choice = input("Enter choice (0/1/2): ").strip()

        if choice == "0":
            break
        elif choice == "1":
            handle_mainnet()
        elif choice == "2":
            handle_testnet()
        else:
            input("Invalid choice. Press Enter to continue...")

if __name__ == "__main__":
    main()
