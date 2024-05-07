import unittest
from buttercms_python_testing_fork.post import Post
from buttercms_python_testing_fork.tests.mocks.post_mocks import list_posts, list_posts_without_body, get_post, get_non_existent_post, search_posts

try:
    from unittest.mock import patch  # Python 3
except ImportError:
    from mock import patch  # Python 2

class TestListPosts(unittest.TestCase):
    @patch('buttercms_python_testing_fork.post.Post.all')
    def test_list_posts(self, mock_all):
        mock_all.return_value = list_posts()
        post = Post('<demo-token>')
        response = post.all()

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertEqual(2, len(data))

        d1 = data[0]
        self.assertIn('slug', d1)
        self.assertEqual('title', d1['slug'])
        self.assertIn('body', d1)

    @patch('buttercms_python_testing_fork.post.Post.all')
    def test_list_posts_without_body(self, mock_all):
        mock_all.return_value = list_posts_without_body()
        post = Post('<demo-token>')
        response = post.all(params={'exclude_body': True})

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertEqual(2, len(data))

        d1 = data[0]
        self.assertIn('slug', d1)
        self.assertEqual('title', d1['slug'])
        self.assertNotIn('body', d1)

class TestRetrievePost(unittest.TestCase):
    @patch('buttercms_python_testing_fork.post.Post.get')
    def test_get_post(self, mock_get):
        mock_get.return_value = get_post()
        post = Post('<demo-token>')
        response = post.get('title')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertNotIsInstance(data, list)
        self.assertEqual('title', data['slug'])
        self.assertIn('body', data)

    @patch('buttercms_python_testing_fork.post.Post.get')
    def test_get_non_existent_post(self, mock_get):
        mock_get.return_value = get_non_existent_post()
        post = Post('<demo-token>')
        response = post.get('non-existent')

        self.assertIsNotNone(response)
        self.assertIn('detail', response)
        self.assertEqual('Not found', response['detail'])

class TestSearchPost(unittest.TestCase):
    @patch('buttercms_python_testing_fork.post.Post.search')
    def test_search_post(self, mock_search):
        mock_search.return_value = search_posts('query')
        post = Post('<demo-token>')
        response = post.search('title')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

        d1 = data[0]
        self.assertEqual('title', d1.get('slug'))
        self.assertIn('body', d1)
        
        body = d1['body']
        self.assertIn('query', body)