import nanoid

def generate_randomest_string(length=10):
    """
    Generate a random string using nanoid.

    Parameters:
    - length (int): Length of the generated string.

    Returns:
    - str: The generated random string.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[{]};:'\",<.>/?`~"
    return nanoid.generate(alphabet, size=length)

if __name__ == "__main__":
    # Example: Generate a random string of length 20
    random_string = generate_randomest_string(20)
    print("Randomest String:", random_string)
