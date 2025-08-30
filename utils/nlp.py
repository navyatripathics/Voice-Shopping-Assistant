import re

def process_command(command: str):
    command = command.lower()

    # Add item with optional quantity
    match = re.search(r"(add|buy|get)\s+(\d+)?\s*(.*)", command)
    if match:
        quantity = int(match.group(2)) if match.group(2) else 1
        item = match.group(3).strip()
        return "add", item, quantity

    # Remove item with optional quantity
    match = re.search(r"(remove|delete)\s+(\d+)?\s*(.*)", command)
    if match:
        quantity = int(match.group(2)) if match.group(2) else 1
        item = match.group(3).strip()
        return "remove", item, quantity

    return None, None, 0
