from typing import Any, Dict, Optional
from .api_segment_base import APISegmentBase

class TrendsApi(APISegmentBase):

    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def get_trends(self, woeid, trend_fields=None) -> dict[str, Any]:
        """

        Retrieves trending information by WOEID (Where On Earth ID) using the specified trend fields and returns a response with a valid Bearer token.

        Args:
            woeid (string): woeid
            trend_fields (array): A comma separated list of Trend fields to display. Example: "['trend_name', 'tweet_count']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Trends
        """
        if woeid is None:
            raise ValueError("Missing required parameter 'woeid'.")
        url = f'{self.main_app_client.base_url}/2/trends/by/woeid/{woeid}'
        query_params = {k: v for k, v in [('trend.fields', trend_fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [self.get_trends]