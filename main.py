import requests

def get_address_info(address):
    url = f"https://trailblazer.hekla.taiko.xyz/api/address?address={address}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Ошибка: {e}"

def read_addresses_from_file(filename):
    try:
        with open(filename, 'r') as file:
            addresses = file.readlines()
        return [address.strip() for address in addresses]
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        return []

def main():
    print("""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                                                                           $
$   TTTTTTTTTTT     AAAAAA     IIIIIIIIII  KKK     KK   OOOOOOOO             $
$        TT        AA    AA        II      KK  KK        OO    OO            $
$        TT       AA      AA       II      KKKK          OO    OO            $
$        TT       AAAAAAAAAA       II      KKKK          OO    OO            $
$        TT       AA      AA       II      KK  KK        OO    OO            $
$        TT       AA      AA   IIIIIIIIII  KK    KK   OOOOOOOO               $
$                                                                           $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    """)

    filename = 'adress.txt'
    addresses = read_addresses_from_file(filename)
    
    if not addresses:
        return

    total_value = 0
    
    for index, address in enumerate(addresses, start=1):
        address_info = get_address_info(address)
        print(f"Аккаунт {index}: {address_info}")
        
        # Добавление value к общей сумме, если запрос успешен
        if isinstance(address_info, dict) and 'value' in address_info:
            total_value += address_info['value']
    
    print(f"Всего токенов: {total_value}")

if __name__ == "__main__":
    main()
