def load_secrets(filename: str)-> str:
    """Loads secret file, needs fullpath

    Args:
        filename (str): Filename with secret

    Returns:
        str: Secret
    """
    with open(file=filename, mode='r') as file:
        secret = file.readline()
    return secret
