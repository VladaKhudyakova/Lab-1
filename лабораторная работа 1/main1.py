numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO заменить значение пропущенного элемента средним арифметическим
v_numbers = [number for number in numbers if number is not None]
arif = sum(v_numbers) / (len(v_numbers) + 1)

for a in range(len(numbers)):
    if numbers[a] is None:
        numbers[a] = arif
print("Измененный список:", numbers)
