noodle_timers = {'small_rice_noodles': [45,90,120],
                 'wide_rice_noodles': [15,30,50],
                 'thin_rice_noodles': [30,50,90],
                 'egg_nooldes': [60,90,150],
                 'instant_noodles': [120,150,210]
                 }
noodles_doneness = ['Al dente','Normal','Soft']

def check_timer(noodle_type,texture):
    key = list(noodle_timers.keys())[noodle_type]
    value = noodle_timers[key][texture]
    print(f'You choose {key} and you should cooked your noodles fot {value} to get the {noodles_doneness[texture]} result')
def ui():
    print('Chooose Which noodles type u want')
    for i in range(len(noodle_timers)):
        key = list(noodle_timers.keys())[i]
        print(f"Press {i+1} for '{key}'")
    type = int(input('Enter type of noodle you want : '))
    type = type -1
    print("Choose which doneness you want")
    for i in range(len(noodles_doneness)):
        print(f"Press {i+1} for '{noodles_doneness[i]}'")
    doneness = int(input('Enter doneness of noodle you want : '))
    doneness = doneness-1
    return type,doneness

type,doneness = ui()
check_timer(type,doneness)