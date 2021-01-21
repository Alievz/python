import time


class TrafficLights:
    __colors = ("red", "yellow", "green")

    def running(self):
        for el in TrafficLights.__colors:
            print(TrafficLights.__colors[0])
            time.sleep(7)
            print(TrafficLights.__colors[1])
            time.sleep(5)
            print(TrafficLights.__colors[2])
            time.sleep(10)
            continue # светофор будет работать вечно! :)


start = TrafficLights()
print(start.running())



