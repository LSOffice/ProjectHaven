speed = 999
distance = 1000
fuel = 10
fuel_eff = 99

if (distance%speed) == 0:
    times = int(distance/speed)
else:
    times = int(distance/speed)+1

for a in range(1, times):
    print(speed*a)
    fuel -= 1/(fuel_eff/100)
print("----END OF LOOP----")
print(times)
if fuel < 0:
    raise ValueError("Not enough fuel")
else:
    print(fuel)


if int(speed*(range(1, times)[-1])) == range(1, distance)[-1]:
    print(True)
