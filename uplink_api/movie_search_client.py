import requests
import uplink


@uplink.json
class MovieSearchClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url="http://movie_service.talkpython.fm/")

    @uplink.get("/api/search/{keyword}")
    def movies_by_keyword(self, keyword) -> requests.models.Response:
        """ Gets movies by keywords """

    @uplink.get("/api/director/{director_name}")
    def movies_by_director(self, director_name) -> requests.models.Response:
        """ Gets movies by director """
