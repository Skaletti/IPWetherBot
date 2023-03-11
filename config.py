API_TOKEN = '6253511492:AAHKve6QP85DPE3dYw-Z2TvJpWQu7i2Nuww'

WEATHER_API_KEY = '28206f1ba9de00604b7f7956cd663c54'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)