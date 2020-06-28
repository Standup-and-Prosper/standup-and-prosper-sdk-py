from __future__ import absolute_import

import unittest
import nose
import time

from standup_and_prosper_sdk import ApiClient, StandupsApi


class GetStandupThreadsTest(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def get_standup_threads(self):
    """Test case for getting standup threads

    Get the standup threads
    """

    access_key = "eyARB5k-..."
    team_id = ""
    standup_id = ""
    api_client = ApiClient(access_key)

    api = StandupsApi(api_client)
    threadResponse = api.get_standup_threads(team_id, standup_id)
    print(threadResponse.threads)
    pass

if __name__ == '__main__':
  unittest.main()