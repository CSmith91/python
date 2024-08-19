
ROMAN_DICT = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def convert(input):
    output = 0
    for i in range(len(input)):
        value_char = ROMAN_DICT[input[i]]

        if(i == len(input)-1):
            output += value_char

        elif(ROMAN_DICT[input[i]] < ROMAN_DICT[input[i+1]]):
            output -= value_char
        
        else:
            output += value_char
    
        print(f"i is: {i}. Value char is: {value_char}. Output so far is: {output}")

    print(f"Output is {output}")
        

while True:
    roman = str(input("Enter the roman numeral you want to convert to digits, or type q to quit: "))
    if(roman == "q"):
        break
    convert(roman)
