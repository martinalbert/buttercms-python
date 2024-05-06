import unittest
from buttercms_python_testing_fork.tag import Tag
from buttercms_python_testing_fork.tests.mocks.tag_mocks import list_tags, list_tags_with_recent_posts, get_tag, get_tag_with_recent_posts, get_non_existent_tag

try:
    from unittest.mock import patch  # Python 3
except ImportError:
    from mock import patch  # Python 2

class TestListTags(unittest.TestCase):
    @patch('buttercms_python_testing_fork.tag.Tag.all')
    def test_list_tags(self, mock_all):
        mock_all.return_value = list_tags()
        tag = Tag('<demo-token>')
        response = tag.all()

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertEqual(2, len(data))

        d1 = data[0]
        self.assertIn('slug', d1)
        self.assertEqual('example-tag', d1['slug'])
        self.assertNotIn('recent_posts', d1)

    @patch('buttercms_python_testing_fork.tag.Tag.all')
    def test_list_tags_with_recent_posts(self, mock_all):
        mock_all.return_value = list_tags_with_recent_posts()
        tag = Tag('<demo-token>')
        response = tag.all(params={'include': 'recent_posts'})

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertEqual(2, len(data))

        d1 = data[0]
        self.assertIn('slug', d1)
        self.assertEqual('example-tag', d1['slug'])
        self.assertIn('recent_posts', d1)

        d1_recent_posts = d1['recent_posts']
        self.assertIsInstance(d1_recent_posts, list)
        self.assertEqual(2, len(d1_recent_posts))

class TestRetrieveTag(unittest.TestCase):
    @patch('buttercms_python_testing_fork.tag.Tag.get')
    def test_get_tag(self, mock_get):
        mock_get.return_value = get_tag()
        tag = Tag('<demo-token>')
        response = tag.get('example-tag')

        self.assertIsNotNone(response)
        self.assertIn('data', response)
        
        data = response['data']
        self.assertIsNotNone(data)
        self.assertEqual('example-tag', data['slug'])
        self.assertNotIn('recent_posts', data)
    
    @patch('buttercms_python_testing_fork.tag.Tag.get')
    def test_get_tag_include_recent_posts(self, mock_get):
        mock_get.return_value = get_tag_with_recent_posts()
        tag = Tag('<demo-token>')
        response = tag.get('example-tag', params={'include': 'recent_posts'})

        self.assertIsNotNone(response)
        self.assertIn('data', response)
        
        data = response['data']
        self.assertIsNotNone(data)
        self.assertEqual('example-tag', data['slug'])
        self.assertIn('recent_posts', data)
        
        recent_posts = data['recent_posts']
        self.assertIsInstance(recent_posts, list)
        self.assertEqual(2, len(recent_posts))
    
    @patch('buttercms_python_testing_fork.tag.Tag.get')
    def test_get_non_existent_tag(self, mock_get):
        mock_get.return_value = get_non_existent_tag()
        tag = Tag('<demo-token>')
        response = tag.get('non-existent')

        self.assertIsNotNone(response)
        self.assertIn('detail', response)
        self.assertEqual('Not found', response['detail'])