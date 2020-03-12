from math import exp

def sigmoid(x):
    pass

def activation(x):
    pass

def neuron_calculation(x, w, b):
    pass

def matmul(x, w, b):
    
    pass

if __name__ == "__main__":

    from colorama import Fore, init
    from termcolor import cprint

    init()

    RED   = "\033[1;31m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    
    right_souts = [
        0.04742587317756678,
        0.11920292202211755,
        0.2689414213699951,
        0.5,
        0.7310585786300049,
        0.8807970779778823,
        0.9525741268224334,
    ]

    print()
    cprint(f"{'-'*10} Тест сигмоиды {'-'*10}", 'blue')
    print()

    real_souts = [sigmoid(i) for i in range(-3, 4)]
    
    if right_souts == real_souts:
        cprint('Сигмоида работает правильно', 'green')

    else:
        cprint('Cигмоида работает неправильно', 'red')
        
    print(f'\t{"При входных данных": <30} [1, 2, 3]')
    print(f'\t{"Ожидалось": <30} [0.5, 0.7310585786300049, 0.8807970779778823]')
    print(f'\t{"Получено": <30} {real_souts[3:6]}')