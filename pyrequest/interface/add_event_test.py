import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data


class AddEventTest(unittest.TestCase):
    ''' 添加发布会 '''
    def setUp(self):
        self.base_url = "http://localhost:8000/api/add_event/"

    def tearDown(self):
        print(self.result)

    def test_add_event_all_null(self):
        ''' 所有参数为空 '''
        payload = {'eid':'', 'name':'', 'limit_num':'', 'address':'', 'start_time':'' }
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_event_eid_exist(self):
        ''' id 已存在 '''
        payload = {'eid': 1, 'name': 'huawei', 'limit_num': 2000, 'address': 'shenzhen', 'start_time': '2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already exists')

    def test_add_event_name_exist(self):
        ''' name 已存在 '''
        payload = {'eid': 11, 'name': 'hongmi', 'limit_num': 2000, 'address': 'shenzhen', 'start_time': '2017'}
        r = requests.post(self.base_url, data=payload)
        print(r)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        ''' 日期格式错误 '''
        payload = {'eid': 11, 'name': 'hongminote', 'limit_num': 2000, 'address': 'shenzhen', 'start_time': '2017'}
        r = requests.post(self.base_url, data=payload)
        print(r)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertIn('start_time format error.', self.result['message'] )

    def test_add_event_success(self):
        ''' 添加成功 '''
        payload = {'eid': 12, 'name': 'hongminote1', 'limit_num': 2000, 'address': 'shenzhen', 'start_time': '2017-12-30 12:00:00'}
        r = requests.post(self.base_url, data=payload)
        print(r)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')



if __name__ == '__main__':
    # 初始化接口测试数据
    unittest.main()