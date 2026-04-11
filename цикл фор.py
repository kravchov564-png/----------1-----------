vegetables = ['Помидоры', 'Огурцы', 'Баклажаны', 'Перец', 'Капуста']
vegetable_yields = [6.5, 4.3, 2.8, 2.2, 3.5]

for index in range(len(vegetable_yields)):
    name = vegetables[index]

    yield_kg = int(vegetable_yields[index] * 10000)


    print(f'{name}: урожайность - {yield_kg} кг на гектар.')