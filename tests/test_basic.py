import unittest

from app.checkers.user import register_params_check


class BasicTestCase(unittest.TestCase):
    '''
    TODO: 在这里补充注册相关测试用例
    '''

    def test_register_params_check(self):
        self.assertEqual(register_params_check(None), ("username", False))

        self.assertEqual(register_params_check({
            'username': 'abcdef12', 'password': 'abcdef12ABDC-',
            'nickname': 'ladf', 'mobile': '+86.123456789123',
            'url': 'http://qinguo.com', 'magic_number': '1'}), ("ok", True))

        self.assertEqual(register_params_check({
            'username': 'abcdef12', 'password': 'abcdef12ABDC-',
            'nickname': 'ladf', 'mobile': '+86.123456789123',
            'url': 'http://qinguo.com'}), ("ok", True))

        self.assertEqual(register_params_check({
            'username': 'abcdef12', 'password': 'abcdef12ABDC-',
            'nickname': 'ladf', 'mobile': '+86.123456789123',
            'url': 'http://qinguo.com.111'}), ("url", False))

        self.assertEqual(register_params_check({
            'username': 'abcdef12', 'password': 'abcdef12ABDC-',
            'nickname': 'ladf', 'mobile': '+86.1234567891231',
            'url': 'http://qinguo.com'}), ("mobile", False))

        self.assertEqual(register_params_check({
            'username': 'abcdef12', 'password': 'abcdef12ABDC-',
            'mobile': '+86.123456789123', 'url': 'http://qinguo.com'}),
            ("nickname", False))

        self.assertEqual(register_params_check({
            'username': 'abcdef12', 'password': 'abcdef12ABDC',
            'nickname': 'ladf', 'mobile': '+86.123456789123',
            'url': 'http://qinguo.com'}), ("password", False))

        self.assertEqual(register_params_check({
            'username': 'abcdef', 'password': 'abcdef12ABDC-',
            'nickname': 'ladf', 'mobile': '+86.123456789123',
            'url': 'http://qinguo.com'}), ("username", False))

        self.assertEqual(register_params_check({
            'username': 'abcdef12', 'password': 'abcdef12ABDC-',
            'nickname': 'ladf', 'mobile': '+86.123456789123',
            'url': 'http://qinguo.com', 'magic_number': 'a'}),
            ("magic_number", False))


if __name__ == '__main__':
    unittest.main()
