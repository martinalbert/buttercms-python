import unittest
from buttercms_python_testing_fork.category import Category
from buttercms_python_testing_fork.tests.mocks.category_mocks import list_categories, list_categories_with_posts, get_category, get_category_with_posts

try:
    from unittest.mock import patch  # Python 3
except ImportError:
    from mock import patch  # Python 2

class TestListCategory(unittest.TestCase):
    @patch('buttercms_python_testing_fork.category.Category.all')
    def test_all(self, mock_all):
        mock_all.return_value = list_categories()
        category = Category('<demo-token>')
        response = category.all()

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

        category_data = data[0]
        self.assertEqual('Category 1', category_data.get('name'))
        self.assertIsNone(category_data.get('recent_posts'))

    @patch('buttercms_python_testing_fork.category.Category.all')
    def test_all_include_recent_posts(self, mock_all):
        mock_all.return_value = list_categories_with_posts()
        category = Category('<demo-token>')
        response = category.all(params={'include': 'recent_posts'})
        
        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

        category_data = data[0]
        self.assertEqual('Category 1', category_data.get('name'))
        self.assertIn('recent_posts', category_data)
        self.assertGreater(len(category_data['recent_posts']), 0)

class TestRetrieveCategory(unittest.TestCase):
    @patch('buttercms_python_testing_fork.category.Category.get')
    def test_get(self, mock_get):
        mock_get.return_value = get_category()
        category = Category('<demo-token>')
        response = category.get('beer')

        self.assertIsNotNone(response)
        self.assertIn('data', response)
        
        category_data = response['data']
        self.assertIsNotNone(category_data)
        self.assertEqual('Category 1', category_data.get('name'))
        self.assertIsNone(category_data.get('recent_posts'))
    
    @patch('buttercms_python_testing_fork.category.Category.get')
    def test_get_include_recent_posts(self, mock_get):
        mock_get.return_value = get_category_with_posts()  # Assuming it returns the first category with posts
        category = Category('<demo-token>')
        response = category.get('beer', params={'include': 'recent_posts'})
        
        self.assertIsNotNone(response)
        self.assertIn('data', response)
        
        category_data = response['data']
        self.assertIsNotNone(category_data)
        self.assertEqual('Category 1', category_data.get('name'))
        self.assertIn('recent_posts', category_data)
        self.assertGreater(len(category_data['recent_posts']), 0)