import re

def asap_check(asap, has_asap):
    return (asap and has_asap) or (not asap)

def get_install_number_from_message(message, asap=False):
    install_numbers = re.findall("(\d{5,})", message)
    has_asap = re.findall("asap", message, re.IGNORECASE)

    if not install_numbers:
        return None
        
    try:
        if (not asap) or (asap and has_asap):
            return int(install_numbers[0])
    except Exception as e:
        return None
    