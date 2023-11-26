from new import generate_and_get_digits

num_digits = 5  # Your desired number of digits
width, height = 800, 600

digits_in_image = generate_and_get_digits(width, height, num_digits)
print("Digits in the image:", digits_in_image)
print("Image generated and saved as 'save.png'.")

