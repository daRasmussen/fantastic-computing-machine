from abc import ABC, abstractmethod

from typing import List


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass


class Subject(ABC):
    @abstractmethod
    def register(self, observer: Observer):
        pass

    @abstractmethod
    def remove(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class WeatherData(Subject):
    _observers = List[Observer]
    _temperature: float
    _humidity: float
    _pressure: float

    def __init__(self) -> None:
        self._observers = []

    def register(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def measurementsChanged(self):
        self.notify()

    def setMeasurements(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurementsChanged()


class CurrentConditionsDisplay(Observer, DisplayElement):
    _temperature: float
    _humidity: float
    _weather_data: WeatherData

    def __init__(self, w_data: WeatherData):
        self._weather_data = w_data
        self._weather_data.register(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self):
        print(f"""
            Current conditions: {self._temperature} + F degrees and {self._humidity} humidity.
        """)


class StatisticsDiaplay(Observer, DisplayElement):
    _temperature: float
    _humidity: float
    _stats: float
    _weather_data: WeatherData

    def __init__(self, w_data: WeatherData) -> None:
        self._weather_data = w_data
        self._weather_data.register(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._stats = temperature * humidity
        self.display()

    def display(self):
        print(f"""
                This is the stats display: {self._stats}
                Which is {self._temperature} * {self._stats}
        """)


if __name__ == '__main__':
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDiaplay(weather_data)
    # forecast_display = ForecastDisplay(weather_data)

    weather_data.setMeasurements(80, 65, 30.4)
    weather_data.setMeasurements(82, 70, 29.2)
    weather_data.setMeasurements(78, 90, 28.9)
