import requests

# Ganti dengan API key kamu
ETHERSCAN_API_KEY = 'EFDG86S8WVCUFD9S8EGWQ5Y1RUC1AF8XTE'
BSCSCAN_API_KEY = 'J5USYZ6DDY64BTNIZRPP6XPDEVW4EU3UEE'

def get_balance(address, network):
    if network == 'eth_mainnet':
        url = f"https://api.etherscan.io/api"
        params = {
            'module': 'account',
            'action': 'balance',
            'address': address,
            'tag': 'latest',
            'apikey': ETHERSCAN_API_KEY
        }
    elif network == 'bsc_mainnet':
        url = f"https://api.bscscan.com/api"
        params = {
            'module': 'account',
            'action': 'balance',
            'address': address,
            'tag': 'latest',
            'apikey': BSCSCAN_API_KEY
        }
    else:
        return None

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if data['status'] == '1':
            return int(data['result']) / 1e18  # Convert from Wei
        else:
            print(f"Error from API: {data.get('message', 'Unknown error')}")
            return None
    except Exception as e:
        print(f"Exception occurred: {e}")
        return None

def main():
    print("Select network:")
    print("1. Ethereum Mainnet")
    print("2. Binance Smart Chain Mainnet")
    choice = input("Enter choice (1 or 2): ").strip()

    if choice == '1':
        network = 'eth_mainnet'
        unit = 'ETH'
    elif choice == '2':
        network = 'bsc_mainnet'
        unit = 'BNB'
    else:
        print("Invalid choice")
        return

    while True:
        address = input("Enter wallet address (or press Enter to quit): ").strip()
        if not address:
            break
        balance = get_balance(address, network)
        if balance is not None:
            print(f"Balance for {address} on {network}: {balance:.6f} {unit}")
        else:
            print("Failed to fetch balance.")

if __name__ == "__main__":
    main()

