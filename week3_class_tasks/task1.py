#write a python code that classifies items in the list as Low, Medium, or High...

sales = [120, 450, 800, 50, 900, 300]

low = []
medium = []
high = []

for sale in sales:
    if sale <= 300:
        low.append(sale)
    elif 300 < sale <= 700:
        medium.append(sale)
    elif sale > 700:
        high.append(sale)

# for the count
print("Low count:", len(low))
print("Medium count:", len(medium))
print("High count:", len(high))

#for the sum
print("Low sum:", sum(low))
print("Medium sum:", sum(medium))
print("High sum:", sum(high))
