import unittest
from buttercms_python_testing_fork.content_field import ContentField
from buttercms_python_testing_fork.tests.mocks.content_field_mocks import list_content_fields_without_filtering, list_filtered_content_fields, list_non_existent_content_field, get_content_field_without_filtering, get_non_existent_content_field, get_filtered_content_field

try:
    from unittest.mock import patch  # Python 3
except ImportError:
    from mock import patch  # Python 2

class TestListContentField(unittest.TestCase):
    @patch('buttercms_python_testing_fork.content_field.ContentField.get')
    def test_list_content_fields_without_filtering(self, mock_get):
        mock_get.return_value = list_content_fields_without_filtering()
        content_field = ContentField('<demo-token>')
        response = content_field.get()

        self.assertIsNotNone(response)
        self.assertNotIn('data', response)

    @patch('buttercms_python_testing_fork.content_field.ContentField.get')
    def test_list_filtered_content_fields(self, mock_get):
        mock_get.return_value = list_filtered_content_fields('key1', 'key2')
        content_field = ContentField('<demo-token>')
        response = content_field.get(keys=['key1', 'key2'])

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIn('key1', data)
        self.assertIn('key2', data)

        k1 = data['key1']
        self.assertEqual(2, len(k1))
        self.assertIn('meta', k1[0])
        self.assertIn('id', k1[0]['meta'])
        
        k2 = data['key2']
        self.assertEqual(1, len(k2))
        self.assertIn('meta', k2[0])
        self.assertIn('id', k2[0]['meta'])

    @patch('buttercms_python_testing_fork.content_field.ContentField.get')
    def test_list_non_existent_content_field(self, mock_get):
        mock_get.return_value = list_non_existent_content_field('non-existent-key')
        content_field = ContentField('<demo-token>')
        response = content_field.get(keys=['non-existent-key'])

        self.assertIsNotNone(response)
        self.assertIn('detail', response)
        self.assertEqual('Content key non-existent-key not found', response['detail'])

class TestRetrieveContentField(unittest.TestCase):
    @patch('buttercms_python_testing_fork.content_field.ContentField.get')
    def test_get_content_field_without_filtering(self, mock_get):
        mock_get.return_value = get_content_field_without_filtering('field')
        content_field = ContentField('<demo-token>')
        response = content_field.get('field')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIn('field', data)

        f = data['field']
        self.assertEqual(2, len(f))
        self.assertIn('meta', f[0])
        self.assertIn('id', f[0]['meta'])

    @patch('buttercms_python_testing_fork.content_field.ContentField.get')
    def test_get_filtered_content_field(self, mock_get):
        mock_get.return_value = get_filtered_content_field('field', 'key')
        content_field = ContentField('<demo-token>')
        response = content_field.get('field', fields=[{'key': 'example'}])

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIn('field', data)

        f = data['field']
        self.assertEqual(1, len(f))
        self.assertIn('meta', f[0])
        self.assertIn('id', f[0]['meta'])
        self.assertIn('key', f[0])
        self.assertEqual('example', f[0]['key'])

    @patch('buttercms_python_testing_fork.content_field.ContentField.get')
    def test_get_non_existent_content_field(self, mock_get):
        mock_get.return_value = get_non_existent_content_field()
        content_field = ContentField('<demo-token>')
        response = content_field.get('key')

        self.assertIsNotNone(response)
        self.assertIn('detail', response)
        self.assertEqual('Not found', response['detail'])