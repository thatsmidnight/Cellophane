import unittest
from unittest import mock
from cellophane.api import RequestsMixin


class TestRequestsMixin(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        self.mixin = RequestsMixin()
        self.mock_session = mock.Mock()
        self.mixin.session = self.mock_session

    def test_get(self):
        """Test get method."""
        self.mixin.get(
            "http://example.com",
            headers={"X-Test": "test"},
            params={"param": "value"},
        )
        self.mock_session.get.assert_called_once_with(
            "http://example.com",
            headers={"X-Test": "test"},
            params={"param": "value"},
        )

    def test_post(self):
        """Test post method."""
        self.mixin.post(
            "http://example.com",
            headers={"X-Test": "test"},
            data={"key": "value"},
        )
        self.mock_session.post.assert_called_once_with(
            "http://example.com",
            headers={"X-Test": "test"},
            data={"key": "value"},
            json=None,
        )

    def test_put(self):
        """Test put method."""
        self.mixin.put(
            "http://example.com",
            headers={"X-Test": "test"},
            data={"key": "value"},
        )
        self.mock_session.put.assert_called_once_with(
            "http://example.com",
            headers={"X-Test": "test"},
            data={"key": "value"},
            json=None,
        )

    def test_patch(self):
        """Test patch method."""
        self.mixin.patch(
            "http://example.com",
            headers={"X-Test": "test"},
            data={"key": "value"},
        )
        self.mock_session.patch.assert_called_once_with(
            "http://example.com",
            headers={"X-Test": "test"},
            data={"key": "value"},
            json=None,
        )

    def test_delete(self):
        """Test delete method."""
        self.mixin.delete(
            "http://example.com",
            headers={"X-Test": "test"},
            params={"param": "value"},
        )
        self.mock_session.delete.assert_called_once_with(
            "http://example.com",
            headers={"X-Test": "test"},
            params={"param": "value"},
        )
