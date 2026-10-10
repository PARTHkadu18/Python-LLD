from tv_display import TVDisplay
from mobile_display import MobileDisplay
from weather_station import WeatherStation

ws=WeatherStation()
tv=TVDisplay()
mobile=MobileDisplay()

ws.addObserver(tv)
ws.addObserver(mobile)

ws.updateTemp(34)
ws.notifyObservers()
