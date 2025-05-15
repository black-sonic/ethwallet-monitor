import os
import requests

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
    }
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_price(symbol):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()[symbol]["usd"]
    except:
        pass
    return None

def main():
    while True:
        clear()
        print("="*40)
        print("        WALLET BALANCE CHECKER        ")
        print("="*40)
        print("Choose Network Environment:")
        print("1. Mainnet")
        print("2. Testnet")
        print("0. Exit")
        env_choice = input("Enter choice (0/1/2): ").strip()

        if env_choice == "0":
            break
        elif env_choice == "1":
            handle_mainnet()
        elif env_choice == "2":
            handle_testnet()
        else:
            input("Invalid choice. Press Enter to continue...")

def handle_mainnet():
    while True:
        clear()
        print("Select network (Mainnet):")
        print("1. Ethereum Mainnet")
        print("2. Binance Smart Chain Mainnet")
        print("0. Back")
        choice = input("Enter choice (0/1/2): ").strip()

        if choice == "0":
            break
        elif choice == "1":
            check_balance("eth_mainnet")
        elif choice == "2":
            check_balance("bsc_mainnet")
        else:
            input("Invalid choice. Press Enter to continue...")

def handle_testnet():
    while True:
        clear()
        print("Select network (Testnet):")
        print("1. Ethereum Sepolia")
        print("2. Binance Smart Chain Testnet")
        print("0. Back")
        choice = input("Enter choice (0/1/2): ").strip()

        if choice == "0":
            break
        elif choice == "1":
            check_balance("eth_sepolia")
        elif choice == "2":
            check_balance("bsc_testnet")
        else:
            input("Invalid choice. Press Enter to continue...")

def check_balance(network_key):
    network = NETWORK_CONFIG[network_key]
    while True:
        clear()
        print(f"{network['name']}")
        address = input("Enter wallet address (or press Enter to return): ").strip()
        if address == "":
            break

        url = f"{network['url']}?module=account&action=balance&address={address}&tag=latest&apikey={network['apikey']}"
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
            print("Error:", e)

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
