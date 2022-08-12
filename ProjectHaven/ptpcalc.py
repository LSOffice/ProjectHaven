from utils.Map import Map
import datetime

prev = None
irreg_times = 0

'''for i in range(1, 1001):


    starttime = datetime.datetime.now()
    test = Map(i)
    value = datetime.datetime.now() - starttime
    if prev is not None:
        if prev < value:
            #print("Irregular")
            irreg_times += 1
    #print(value)
    prev = value

print(f"irreg {irreg_times}/{len(range(1, 1001))}")'''
#starttime = datetime.datetime.now()
test = Map(1000)
print(test.get_height())
#print(datetime.datetime.now()-starttime)
print(test.get_route(5, 5, 10, 16))
