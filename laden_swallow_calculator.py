# https://www.youtube.com/watch?v=liIlW-ovx0Y

"""
Function who calculates the amount of swallows needed.
Includes a conditional output string.
"""


def swallow_calc(coconut=454, swallow_capacity=20):
    return coconut / swallow_capacity


coconut = int(input('Coconut weight: '))
swallows = int(input('Swallow Capacity: '))
result = swallow_calc(coconut, swallows)

print(f"It would require at least "
      f"{result} {'swallows' if result > 1 else 'swallow'}"
      f" to carry a {coconut}g coconut.")
