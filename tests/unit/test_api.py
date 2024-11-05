from unittest import TestCase, mock
from abc import ABC, abstractmethod


class BaseAPI(ABC):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.token = "mock_token"
        self.authenticate()

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def get(self, endpoint: str, **kwargs) -> dict:
        pass

    @abstractmethod
    def put(self, endpoint: str, **kwargs) -> dict:
        pass

    @abstractmethod
    def patch(self, endpoint: str, **kwargs) -> dict:
        pass

    @abstractmethod
    def delete(self, endpoint: str, **kwargs) -> dict:
        pass


class MockAPI(BaseAPI):
    def authenticate(self):
        pass

    def get(self, endpoint: str, **kwargs) -> dict:
        raise NotImplementedError

    def put(self, endpoint: str, **kwargs) -> dict:
        raise NotImplementedError

    def patch(self, endpoint: str, **kwargs) -> dict:
        raise NotImplementedError

    def delete(self, endpoint: str, **kwargs) -> dict:
        raise NotImplementedError


class TestBaseAPI(TestCase):
    def test_init(self):
        api = MockAPI(api_key="test_key")
        self.assertEqual(api.api_key, "test_key")
        self.assertEqual(api.token, "mock_token")

    def test_authenticate_abstractmethod(self):
        with self.assertRaises(TypeError):
            BaseAPI(api_key="test_key")

    @mock.patch.object(MockAPI, "authenticate")
    def test_authenticate_called(self, mock_authenticate):
        MockAPI(api_key="test_key")
        mock_authenticate.assert_called_once()

    def test_http_methods_abstractmethod(self):
        api = MockAPI(api_key="test_key")
        with self.assertRaises(NotImplementedError):
            api.get(endpoint="/test")
        with self.assertRaises(NotImplementedError):
            api.put(endpoint="/test")
        with self.assertRaises(NotImplementedError):
            api.patch(endpoint="/test")
        with self.assertRaises(NotImplementedError):
            api.delete(endpoint="/test")
