def cc20(num):
    decimal = int(num, 16)

    if decimal == 0:
        return "0"
    
    digits = []
    while decimal > 0:
        ost = decimal % 20
        if ost < 10:
            digits.append(str(ost))
        else:
            digits.append(chr(ord('A') + ost - 10))
        decimal //= 20

    return "".join(digits[::-1])

if __name__ == "__main__":
    while True:
        s = input("Введите число в 16-ричной сс(для выхода q): ")
        if s.lower() in ('q', 'quit', 'выход'):
            break
        else:
            print(f"Число из 16сс в 20сс -> {cc20(s)}")