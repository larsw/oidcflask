import unittest

import oidcflask


class OidcflaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = oidcflask.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(302, rv.status_code)

if __name__ == '__main__':
    unittest.main()
