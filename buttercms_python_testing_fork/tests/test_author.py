import unittest
from buttercms_python_testing_fork.author import Author
from buttercms_python_testing_fork.tests.mocks.author_mocks import list_authors, list_authors_with_posts, get_author, get_author_with_posts

try:
    from unittest.mock import patch  # Python 3
except ImportError:
    from mock import patch  # Python 2

class TestListAuthor(unittest.TestCase):
    @patch('buttercms_python_testing_fork.author.Author.all')
    def test_all(self, mock_all):
        mock_all.return_value = list_authors()
        author = Author('<demo-token>')
        response = author.all()

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

        author_data = data[0]
        self.assertEqual('John', author_data.get('first_name'))
        self.assertIsNone(author_data.get('recent_posts'))

    @patch('buttercms_python_testing_fork.author.Author.all')
    def test_all_include_recent_posts(self, mock_all):
        mock_all.return_value = list_authors_with_posts()
        author = Author('<demo-token>')
        response = author.all(params={'include': 'recent_posts'})
        
        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

        author_data = data[0]
        self.assertEqual('John', author_data.get('first_name'))
        self.assertIn('recent_posts', author_data)
        self.assertGreater(len(author_data['recent_posts']), 0)

class TestRetrieveAuthor(unittest.TestCase):
    @patch('buttercms_python_testing_fork.author.Author.get')
    def test_get(self, mock_get):
        mock_get.return_value = get_author()
        author = Author('<demo-token>')
        response = author.get('john-doe')

        self.assertIsNotNone(response)
        self.assertIn('data', response)
        
        author_data = response['data']
        self.assertIsNotNone(author_data)
        self.assertEqual('John', author_data.get('first_name'))
        self.assertIsNone(author_data.get('recent_posts'))
    
    @patch('buttercms_python_testing_fork.author.Author.get')
    def test_get_include_recent_posts(self, mock_get):
        mock_get.return_value = get_author_with_posts()
        author = Author('<demo-token>')
        response = author.get('john-doe', params={'include': 'recent_posts'})
        
        self.assertIsNotNone(response)
        self.assertIn('data', response)

        author_data = response['data']
        self.assertIsNotNone(author_data)
        self.assertEqual('John', author_data.get('first_name'))
        self.assertIn('recent_posts', author_data)
        self.assertGreater(len(author_data['recent_posts']), 0)


