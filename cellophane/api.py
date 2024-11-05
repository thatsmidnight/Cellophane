from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """Abstract base class for API wrappers.
    """

    def __init__(self, api_key: str, **kwargs) -> None:
        """Initializes the API wrapper.

        Parameters
        ----------
        api_key : str
            The API Key for authentication.
        **kwargs : dict
            Additional keyword arguments for the specific API.
        """
        self.api_key = api_key
        self.token = self.authenticate()

    @abstractmethod
    def authenticate(self) -> str:
        """Authenticates the API.

        Returns
        -------
        str
            The authentication token.
        """
        pass

    @abstractmethod
    def get(self, endpoint: str, **kwargs) -> dict:
        """Makes a GET request to the API.

        Parameters
        ----------
        endpoint : str
            The API endpoint to request.
        **kwargs : dict
            Additional keyword arguments for the request.

        Returns
        -------
        dict
            The response from the API.
        """
        pass

    @abstractmethod
    def post(self, endpoint: str, **kwargs) -> dict:
        """Makes a POST request to the API.

        Parameters
        ----------
        endpoint : str
            The API endpoint to request.
        **kwargs : dict
            Additional keyword arguments for the request.

        Returns
        -------
        dict
            The response from the API.
        """
        pass

    @abstractmethod
    def put(self, endpoint: str, **kwargs) -> dict:
        """Makes a PUT request to the API.

        Parameters
        ----------
        endpoint : str
            The API endpoint to request.
        **kwargs : dict
            Additional keyword arguments for the request.

        Returns
        -------
        dict
            The response from the API.
        """
        pass

    @abstractmethod
    def patch(self, endpoint: str, **kwargs) -> dict:
        """Makes a PATCH request to the API.

        Parameters
        ----------
        endpoint : str
            The API endpoint to request.
        **kwargs : dict
            Additional keyword arguments for the request.

        Returns
        -------
        dict
            The response from the API.
        """
        pass

    @abstractmethod
    def delete(self, endpoint: str, **kwargs) -> dict:
        """Makes a DELETE request to the API.

        Parameters
        ----------
        endpoint : str
            The API endpoint to request.
        **kwargs : dict
            Additional keyword arguments for the request.

        Returns
        -------
        dict
            The response from the API.
        """
        pass
