
class RoutingError(Exception):
    """
    Exception levée quand aucun itinéraire n'a pu être calculé.
    """
    def __init__(self, message: str = "Aucun intinéraire trouvé entre les points donnés."):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"RoutingError: {self.message}"