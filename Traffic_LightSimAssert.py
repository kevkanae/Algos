market = {'ns': 'green', 'ew': 'red'}
mission = {'ns': 'red', 'ew': 'green'}


def switchLights(light):
    for key in light.keys():
        if light[key] == 'green':
            light[key] = 'yellow'
            print(f'1. {light.values()}')
        elif light[key] == 'yellow':
            light[key] = 'red'
            print(f'2. {light.values()}')
        elif light[key] == 'red':
            light[key] = 'green'
            print(f'3. {light.values()}')
    assert 'red' in light.values(), 'no light is red' + str(light)


switchLights(mission)
