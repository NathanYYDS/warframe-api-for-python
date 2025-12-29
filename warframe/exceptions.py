class WarframeAPIError(Exception):
    """Base exception for Warframe API"""
    pass

class APIRequestError(WarframeAPIError):
    """Exception raised for API request errors"""
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error {status_code}: {message}")

class TimeoutError(WarframeAPIError):
    """Exception raised for timeouts"""
    pass

class InvalidParameterError(WarframeAPIError):
    """Exception raised for invalid parameters"""
    pass
