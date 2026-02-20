#From temperatures = [30,22,35,19,40], print those above average....


temperatures = [30, 22, 35, 19, 40]

average = sum(temperatures) / len(temperatures)


print("Average temperature:", average)
print("Temperatures above average:")

for temperature in temperatures:
    if temperature > average:
        print(temperature)