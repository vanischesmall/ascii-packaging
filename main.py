from packaging import Package as pkg


if __name__ == '__main__':
    values: list = list(map(int, input("Enter values: ").split()))
    string_from_values = pkg.encode(values)
    print(f'Encoded package string -> {string_from_values}\n')
    
    string: str = str(input("Enter package string: "))
    values_from_string  = pkg.decode(string)
    print(f'Decoded list of values -> {values_from_string}\n')      
