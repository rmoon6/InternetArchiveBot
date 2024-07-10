from typing import Dict

def get_bot_token() -> str:
    return _read_properties_map()[_TOKEN_KEY]

_PROPERTIES_FILE = "auth.properties"
_TOKEN_KEY = "token"

def _read_properties_map() -> Dict[str, str]:
    properties: Dict[str, str] = {}
    with open(_PROPERTIES_FILE, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                properties[key.strip()] = value.strip()
    return properties


if __name__ == '__main__':
    bot_token = get_bot_token()
    print(f'Bot Token: {bot_token}')
