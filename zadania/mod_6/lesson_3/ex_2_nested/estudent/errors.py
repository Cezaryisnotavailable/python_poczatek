
class PlaceLimitError(Exception):
    
    def __init__(self, places_limit, message=None, *args):
        self.places_limit = places_limit
        if message is None:
            message = f"Niewystarczająca liczba miejsc w klasach - limit to: {places_limit}"
        super().__init__(message, *args)

        


class LogicError(Exception):
    pass

