import numpy as np

class FuzzySet:
    def __init__(self, nama, rendah, tinggi, nilaitengah):
        self.name = nama
        self.rendah = rendah
        self.tinggi = tinggi
        self.nilaitengah = nilaitengah

    def membership(self, x):
        if x <= self.rendah:
            return 0
        elif x >= self.tinggi:
            return 0
        else:
            return (x - self.tinggi) / (self.nilaitengah - self.rendah)

input_var = 'suhu'
output_var = 'pemanasan'

cold = FuzzySet('dingin', 0, 20, 15)
warm = FuzzySet('hangat', 15, 30, 22.5)
hot = FuzzySet('panas', 22.5, 40, 30)

low_heat = FuzzySet('pemanasan_rendah', 0, 20, 10)
medium_heat = FuzzySet('pemanasan_sedang', 10, 30, 20)
high_heat = FuzzySet('pemansan_tinggi', 20, 40, 30)

rules = [
    (cold, low_heat),
    (warm, medium_heat),
    (hot, high_heat)
]

input_value = 25

cold_membership = cold.membership(input_value)
warm_membership = warm.membership(input_value)
hot_membership = hot.membership(input_value)

output_value = 0
for rule in rules:
    fuzzy_set = rule[1]
    membership = rule[0].membership(input_value)
    output_value += membership * fuzzy_set.nilaitengah

output_value /= (cold_membership + warm_membership + hot_membership)

print(f'Nilai output dari {input_var} = {input_value} adalah {output_value} {output_var}')