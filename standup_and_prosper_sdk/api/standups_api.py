# coding: utf-8


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from standup_and_prosper_sdk.api_client import ApiClient


class StandupsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_standup_threads(self, team_id, standup_id, **kwargs):
        """Get the recent threads for a standup

        Includes the original configuration information.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_standup_threads(team_id, standup_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: The unique identifier for the workspace team
        :param str standup_id: The unique identifier for the standup
        :return: ThreadCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_standup_threads_with_http_info(team_id, standup_id, **kwargs)
        else:
            (data) = self.get_standup_threads_with_http_info(team_id, standup_id, **kwargs)
            return data

    def get_standup_threads_with_http_info(self, team_id, standup_id, **kwargs):
        all_params = ['team_id', 'standup_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_standup_threads" % key
                )
            params[key] = val
        del params['kwargs']
        if ('standup_id' not in params or params['standup_id'] is None):
          raise ValueError("Missing the required parameter `standup_id`.")
        if ('team_id' not in params or params['team_id'] is None):
          raise ValueError("Missing the required parameter `team_id`.")

        collection_formats = {}

        path_params = {
          "teamId": params['team_id'],
          "standupId": params['standup_id'],
        }

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        header_params['Accept'] = self.api_client.select_header_accept(['application/links+json'])

        return self.api_client.call_api(
          '/v1/teams/{teamId}/standups/{standupId}/threads', 'GET',
          path_params,
          query_params,
          header_params,
          body=body_params,
          post_params=form_params,
          files=local_var_files,
          response_type='ThreadCollection',

          async_req=params.get('async_req'),
          _return_http_data_only=params.get('_return_http_data_only'),
          _preload_content=params.get('_preload_content', True),
          _request_timeout=params.get('_request_timeout'),
          collection_formats=collection_formats)