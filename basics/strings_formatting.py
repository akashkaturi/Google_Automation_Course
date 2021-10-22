def convert_to_farrenheit(temperature):
    farenheit = (5/9)*temperature
    return farenheit


for i in range(10, 100, 10):
    # print("{:>4.2f}".format(convert_to_farrenheit(i)))
    print(f"Original Temperature:{i:>3} | Farrenheit Temperature: {convert_to_farrenheit(i):^4.2f} sup?")
