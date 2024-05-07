import unittest
from buttercms_python_testing_fork.page import Page
from buttercms_python_testing_fork.tests.mocks.page_mocks import list_pages, list_pages_without_page_type, get_page, get_non_existent_page, search_pages

try:
    from unittest.mock import patch  # Python 3
except ImportError:
    from mock import patch  # Python 2

class TestListPages(unittest.TestCase):
    @patch('buttercms_python_testing_fork.page.Page.all')
    def test_list_pages(self, mock_all):
        mock_all.return_value = list_pages('page_type')
        page = Page('<demo-token>')
        response = page.all('page_type')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertEqual(2, len(data))

        d1 = data[0]
        self.assertIn('slug', d1)
        self.assertEqual('example', d1['slug'])
        self.assertIn('page_type', d1)
        self.assertEqual('page_type', d1['page_type'])

    @patch('buttercms_python_testing_fork.page.Page.all')
    def test_list_pages_without_page_type(self, mock_all):
        mock_all.return_value = list_pages_without_page_type()
        page = Page('<demo-token>')
        response = page.all('*')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertEqual(1, len(data))

        d1 = data[0]
        self.assertIn('slug', d1)
        self.assertEqual('example', d1['slug'])
        self.assertIn('page_type', d1)
        self.assertIsNone(d1['page_type'])

class TestRetrievePage(unittest.TestCase):
    @patch('buttercms_python_testing_fork.page.Page.get')
    def test_get_page(self, mock_get):
        mock_get.return_value = get_page('page_type', 'example')
        page = Page('<demo-token>')
        response = page.get('page_type', 'example')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertNotIsInstance(data, list)
        self.assertEqual('example', data['slug'])
        self.assertIn('page_type', data['page_type'])

    @patch('buttercms_python_testing_fork.page.Page.get')
    def test_get_non_existent_page(self, mock_get):
        mock_get.return_value = get_non_existent_page()
        page = Page('<demo-token>')
        response = page.get('page_type', 'non-existent')

        self.assertIsNotNone(response)
        self.assertIn('detail', response)
        self.assertEqual('Not found', response['detail'])

class TestSearchPage(unittest.TestCase):
    @patch('buttercms_python_testing_fork.page.Page.search')
    def test_search_page(self, mock_search):
        mock_search.return_value = search_pages('key1')
        page = Page('<demo-token>')
        response = page.search('page_type')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertEqual(1, len(data))

        d1 = data[0]
        self.assertIn('slug', d1)
        self.assertEqual('example', d1['slug'])
        self.assertIn('page_type', d1['page_type'])
        self.assertIn('fields', d1)

        f1 = d1['fields']
        self.assertIsNotNone(f1)
        self.assertIsInstance(f1, list)
        self.assertIn('key', f1[0])

        k1 = f1[0]['key']
        self.assertEqual('key1', k1)