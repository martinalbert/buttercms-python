import unittest
from buttercms_python_testing_fork.feed import Feed
from buttercms_python_testing_fork.tests.mocks.feed_mocks import get_sitemap_feed, get_rss_feed, get_atom_feed, get_non_existent_feed

try:
    from unittest.mock import patch  # Python 3
except ImportError:
    from mock import patch  # Python 2

class TestFeed(unittest.TestCase):
    @patch('buttercms_python_testing_fork.feed.Feed.get')
    def test_get_sitemap_feed(self, mock_get):
        mock_get.return_value = get_sitemap_feed()
        feed = Feed('<demo-token>')
        response = feed.get('sitemap')

        self.assertIsNotNone(response)
        self.assertIn('data', response)
        self.assertEqual('<?xml version="1.0" encoding="UTF-8"?><hello>World</hello>', response['data'])

    @patch('buttercms_python_testing_fork.feed.Feed.get')
    def test_get_rss_feed(self, mock_get):
        mock_get.return_value = get_rss_feed()
        feed = Feed('<demo-token>')
        response = feed.get('rss')

        self.assertIsNotNone(response)
        self.assertIn('data', response)
        self.assertEqual('<?xml version="1.0" encoding="UTF-8"?><hello>World</hello>', response['data'])

    @patch('buttercms_python_testing_fork.feed.Feed.get')
    def test_get_atom_feed(self, mock_get):
        mock_get.return_value = get_atom_feed()
        feed = Feed('<demo-token>')
        response = feed.get('atom')

        self.assertIsNotNone(response)
        self.assertIn('data', response)
        self.assertEqual('<?xml version="1.0" encoding="UTF-8"?><hello>World</hello>', response['data'])

    @patch('buttercms_python_testing_fork.feed.Feed.get')
    def test_get_non_existent_feed(self, mock_get):
        mock_get.return_value = get_non_existent_feed()
        feed = Feed('<demo-token>')
        response = feed.get('non-existent')

        self.assertIsNotNone(response)
        self.assertIn('detail', response)
        self.assertEqual('Not found', response['detail'])