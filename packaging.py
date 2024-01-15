class Package:
    def decode(string: str) -> list:
        ''' Decode input string to list of values '''
        return [ord(character) for character in string]
            
    def encode(values: list) -> str:
        ''' Encode input list of values in string '''
        return ''.join([chr(value) for value in values if value < 55296])
