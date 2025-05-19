from typing import Any, Dict, Optional
from .api_segment_base import APISegmentBase

class SpacesApi(APISegmentBase):

    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def find_spaces_by_ids(self, ids, space_fields=None, expansions=None, user_fields=None, topic_fields=None) -> dict[str, Any]:
        """

        Retrieves detailed information about specified spaces using the "GET" method, allowing customization through parameters such as space IDs, space fields, space expansions, user fields, and topic fields, while requiring authentication via Bearer or OAuth2 tokens for authorized access.

        Args:
            ids (array): Required array of IDs for the requested spaces.
            space_fields (array): A comma separated list of Space fields to display. Example: "['created_at', 'creator_id', 'ended_at', 'host_ids', 'id', 'invited_user_ids', 'is_ticketed', 'lang', 'participant_count', 'scheduled_start', 'speaker_ids', 'started_at', 'state', 'subscriber_count', 'title', 'topic_ids', 'updated_at']".
            expansions (array): A comma separated list of fields to expand. Example: "['creator_id', 'host_ids', 'invited_user_ids', 'speaker_ids', 'topic_ids']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            topic_fields (array): A comma separated list of Topic fields to display. Example: "['description', 'id', 'name']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces
        """
        url = f'{self.main_app_client.base_url}/2/spaces'
        query_params = {k: v for k, v in [('ids', ids), ('space.fields', space_fields), ('expansions', expansions), ('user.fields', user_fields), ('topic.fields', topic_fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def find_spaces_by_creator_ids(self, user_ids, space_fields=None, expansions=None, user_fields=None, topic_fields=None) -> dict[str, Any]:
        """

        Retrieves a list of spaces by their creator IDs using the specified user IDs, with optional filtering by space fields, space expansions, user fields, and topic fields.

        Args:
            user_ids (array): **user_ids**: Required array of user IDs for filtering spaces by their creators.
            space_fields (array): A comma separated list of Space fields to display. Example: "['created_at', 'creator_id', 'ended_at', 'host_ids', 'id', 'invited_user_ids', 'is_ticketed', 'lang', 'participant_count', 'scheduled_start', 'speaker_ids', 'started_at', 'state', 'subscriber_count', 'title', 'topic_ids', 'updated_at']".
            expansions (array): A comma separated list of fields to expand. Example: "['creator_id', 'host_ids', 'invited_user_ids', 'speaker_ids', 'topic_ids']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            topic_fields (array): A comma separated list of Topic fields to display. Example: "['description', 'id', 'name']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces
        """
        url = f'{self.main_app_client.base_url}/2/spaces/by/creator_ids'
        query_params = {k: v for k, v in [('user_ids', user_ids), ('space.fields', space_fields), ('expansions', expansions), ('user.fields', user_fields), ('topic.fields', topic_fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def search_spaces(self, query, state=None, max_results=None, space_fields=None, expansions=None, user_fields=None, topic_fields=None) -> dict[str, Any]:
        """

        Searches for spaces using the specified query and optional filters like state, and returns the results with customizable fields and expansions.

        Args:
            query (string): The "query" parameter is a required string input for the GET operation at path "/2/spaces/search", used to specify search terms for finding spaces. Example: 'crypto'.
            state (string): Optional query parameter to filter search results by space state, which can be "live," "scheduled," or "all" (default).
            max_results (integer): Limits the number of search results returned, with a default of 100.
            space_fields (array): A comma separated list of Space fields to display. Example: "['created_at', 'creator_id', 'ended_at', 'host_ids', 'id', 'invited_user_ids', 'is_ticketed', 'lang', 'participant_count', 'scheduled_start', 'speaker_ids', 'started_at', 'state', 'subscriber_count', 'title', 'topic_ids', 'updated_at']".
            expansions (array): A comma separated list of fields to expand. Example: "['creator_id', 'host_ids', 'invited_user_ids', 'speaker_ids', 'topic_ids']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            topic_fields (array): A comma separated list of Topic fields to display. Example: "['description', 'id', 'name']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces
        """
        url = f'{self.main_app_client.base_url}/2/spaces/search'
        query_params = {k: v for k, v in [('query', query), ('state', state), ('max_results', max_results), ('space.fields', space_fields), ('expansions', expansions), ('user.fields', user_fields), ('topic.fields', topic_fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def find_space_by_id(self, id, space_fields=None, expansions=None, user_fields=None, topic_fields=None) -> dict[str, Any]:
        """

        Retrieves details about a specific space by its ID, allowing optional customization through space fields, space expansions, user fields, and topic fields, using a Bearer or OAuth2 token for authentication.

        Args:
            id (string): id
            space_fields (array): A comma separated list of Space fields to display. Example: "['created_at', 'creator_id', 'ended_at', 'host_ids', 'id', 'invited_user_ids', 'is_ticketed', 'lang', 'participant_count', 'scheduled_start', 'speaker_ids', 'started_at', 'state', 'subscriber_count', 'title', 'topic_ids', 'updated_at']".
            expansions (array): A comma separated list of fields to expand. Example: "['creator_id', 'host_ids', 'invited_user_ids', 'speaker_ids', 'topic_ids']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            topic_fields (array): A comma separated list of Topic fields to display. Example: "['description', 'id', 'name']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f'{self.main_app_client.base_url}/2/spaces/{id}'
        query_params = {k: v for k, v in [('space.fields', space_fields), ('expansions', expansions), ('user.fields', user_fields), ('topic.fields', topic_fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def space_buyers(self, id, pagination_token=None, max_results=None, user_fields=None, expansions=None, tweet_fields=None) -> dict[str, Any]:
        """

        Retrieves a list of buyers for a specific space using the "GET" method, allowing optional pagination and customization of returned user and tweet fields.

        Args:
            id (string): id
            pagination_token (string): Optional token used for pagination to retrieve the next set of results in a sequence.
            max_results (integer): The maximum number of buyer results to return, defaulting to 100 if not specified.
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['affiliation.user_id', 'most_recent_tweet_id', 'pinned_tweet_id']".
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces, Tweets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f'{self.main_app_client.base_url}/2/spaces/{id}/buyers'
        query_params = {k: v for k, v in [('pagination_token', pagination_token), ('max_results', max_results), ('user.fields', user_fields), ('expansions', expansions), ('tweet.fields', tweet_fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def space_tweets(self, id, max_results=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> dict[str, Any]:
        """

        Retrieves a list of tweets from a specified Twitter Space by its ID, with optional parameters to customize the fields and expansions included in the response.

        Args:
            id (string): id
            max_results (integer): The `max_results` parameter limits the number of tweets returned in the response for the GET operation at "/2/spaces/{id}/tweets", with a default of 100. Example: '25'.
            tweet_fields (array): A comma separated list of Tweet fields to display. Example: "['article', 'attachments', 'author_id', 'card_uri', 'context_annotations', 'conversation_id', 'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 'note_tweet', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'scopes', 'source', 'text', 'username', 'withheld']".
            expansions (array): A comma separated list of fields to expand. Example: "['article.cover_media', 'article.media_entities', 'attachments.media_keys', 'attachments.media_source_tweet', 'attachments.poll_ids', 'author_id', 'edit_history_tweet_ids', 'entities.mentions.username', 'geo.place_id', 'in_reply_to_user_id', 'entities.note.mentions.username', 'referenced_tweets.id', 'referenced_tweets.id.author_id', 'author_screen_name']".
            media_fields (array): A comma separated list of Media fields to display. Example: "['alt_text', 'duration_ms', 'height', 'media_key', 'non_public_metrics', 'organic_metrics', 'preview_image_url', 'promoted_metrics', 'public_metrics', 'type', 'url', 'variants', 'width']".
            poll_fields (array): A comma separated list of Poll fields to display. Example: "['duration_minutes', 'end_datetime', 'id', 'options', 'voting_status']".
            user_fields (array): A comma separated list of User fields to display. Example: "['affiliation', 'connection_status', 'created_at', 'description', 'entities', 'id', 'location', 'most_recent_tweet_id', 'name', 'pinned_tweet_id', 'profile_banner_url', 'profile_image_url', 'protected', 'public_metrics', 'receives_your_dm', 'subscription_type', 'url', 'username', 'verified', 'verified_type', 'withheld']".
            place_fields (array): A comma separated list of Place fields to display. Example: "['contained_within', 'country', 'country_code', 'full_name', 'geo', 'id', 'name', 'place_type']".

        Returns:
            dict[str, Any]: The request has succeeded.

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Spaces, Tweets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'.")
        url = f'{self.main_app_client.base_url}/2/spaces/{id}/tweets'
        query_params = {k: v for k, v in [('max_results', max_results), ('tweet.fields', tweet_fields), ('expansions', expansions), ('media.fields', media_fields), ('poll.fields', poll_fields), ('user.fields', user_fields), ('place.fields', place_fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [self.find_spaces_by_ids, self.find_spaces_by_creator_ids, self.search_spaces, self.find_space_by_id, self.space_buyers, self.space_tweets]