class Devices(): # Статический класс с информацией об авторизированном пользователе
    __devices = dict() 

    @classmethod
    def set_devices(cls, devices: dict[dict]) -> None:
        Devices.__devices: dict[dict] = devices

    @classmethod
    def get_devices(cls) -> dict[dict]:
        return Devices.__devices