from abc import ABC, abstractmethod
from typing import Optional

from requests import Session


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


class RequestsMixin:
    """Mixin class for making HTTP requests using the requests library.
    """

    def __init__(self) -> None:
        self.session = Session()

    def get(
        self,
        url: str,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
    ) -> dict:
        """Makes a GET request.

        Parameters
        ----------
        url : str
            The URL to make the request to.
        headers : Optional[dict], optional
            Headers to include in the request, by default None
        params : Optional[dict], optional
            Query parameters to include in the request, by default None

        Returns
        -------
        dict
            The response from the request.
        """
        return self.session.get(url, headers=headers, params=params).json()

    def post(
        self,
        url: str,
        headers: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
    ) -> dict:
        """Makes a POST request.

        Parameters
        ----------
        url : str
            The URL to make the request to.
        headers : Optional[dict], optional
            Headers to include in the request, by default None
        data : Optional[dict], optional
            Data to include in the request, by default None
        json : Optional[dict], optional
            JSON data to include in the request, by default None

        Returns
        -------
        dict
            The response from the request.
        """
        return self.session.post(
            url, headers=headers, data=data, json=json
        ).json()

    def put(
        self,
        url: str,
        headers: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
    ) -> dict:
        """Makes a PUT request.

        Parameters
        ----------
        url : str
            The URL to make the request to.
        headers : Optional[dict], optional
            Headers to include in the request, by default None
        data : Optional[dict], optional
            Data to include in the request, by default None
        json : Optional[dict], optional
            JSON data to include in the request, by default None

        Returns
        -------
        dict
            The response from the request.
        """
        return self.session.put(
            url, headers=headers, data=data, json=json
        ).json()

    def patch(
        self,
        url: str,
        headers: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
    ) -> dict:
        """Makes a PATCH request.

        Parameters
        ----------
        url : str
            The URL to make the request to.
        headers : Optional[dict], optional
            Headers to include in the request, by default None
        data : Optional[dict], optional
            Data to include in the request, by default None
        json : Optional[dict], optional
            JSON data to include in the request, by default None

        Returns
        -------
        dict
            The response from the request.
        """
        return self.session.patch(
            url, headers=headers, data=data, json=json
        ).json()

    def delete(
        self,
        url: str,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
    ) -> dict:
        """Makes a DELETE request.

        Parameters
        ----------
        url : str
            The URL to make the request to.
        headers : Optional[dict], optional
            Headers to include in the request, by default None
        params : Optional[dict], optional
            Query parameters to include in the request, by default None

        Returns
        -------
        dict
            The response from the request.
        """
        return self.session.delete(url, headers=headers, params=params).json()
