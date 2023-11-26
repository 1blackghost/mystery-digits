import random
import string

def generate_pin():
    # Generate a random 4-letter PIN with lowercase letters
    pin = ''.join(random.choice(string.ascii_lowercase) for _ in range(4))
    return pin

def generate_unique_pins(num_pins):
    unique_pins = set()
    
    for _ in range(num_pins):
        pin = generate_pin()
        while pin in unique_pins:
            # Regenerate PIN if it's a duplicate
            pin = generate_pin()
        
        unique_pins.add(pin)
    
    return list(unique_pins)

def write_to_file(pin_list, filename):
    with open(filename, 'w') as file:
        file.write(f'pins = {pin_list}')

def main():
    num_pins = 300
    pin_list = generate_unique_pins(num_pins)
    
    # Print the generated PINs
    for pin in pin_list:
        print(pin)

    filename = 'generated_pins.txt'
    write_to_file(pin_list, filename)
    
    print(f'\nGenerated PINs are written to {filename}.')

if __name__ == "__main__":
    main()
