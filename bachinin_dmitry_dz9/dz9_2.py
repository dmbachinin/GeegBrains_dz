
class Road:
    def __init__(self,length,wigth,weight_meter = 25,thickness = 5):
        self.__length = length
        self.__wigth = wigth
        self.__thickness_canvas = thickness
        self.__weight_meter = weight_meter
    def road_surface(self):
        res = self.__length * self.__wigth * self.__thickness_canvas * self.__weight_meter
        return f"{int(res//1000)} т." if res!=0 else "Неверные входные данные"

Road_s = Road(20,5000,25,5)
print(Road_s.road_surface())
