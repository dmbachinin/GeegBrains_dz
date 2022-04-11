from time import sleep

class TrafficLight:
    __color_list = ["красный", "желтый", "зеленый"]
    _color = __color_list[0]
    def running(self):
        while True:
            print(f"Цвет светофора: {self._color}")
            if self._color == self.__color_list[0]:
                sleep(7)
                self._color = self.__color_list[1]
            elif self._color == self.__color_list[1]:
                sleep(2)
                self._color = self.__color_list[2]
            elif self._color == self.__color_list[2]:
                sleep(5)
                self._color = self.__color_list[0]
            else:
                raise ValueError("Неверные исходные данные")

traffic_lights = TrafficLight()
traffic_lights.running()
