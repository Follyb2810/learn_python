weight = input('IInsert you weight? ')
unit =input('(l)lbs or (k)kbs')
if unit.upper() == 'L':
    convert =int(weight) * 0.45
    print(f"you weight {convert} kilis")
elif unit.upper() == 'k':
    convert =int(weight) / 0.45
    print(f"you weight {convert} kilis")
else:
    print('invalid input')
    print(f"")