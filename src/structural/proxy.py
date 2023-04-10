# proxy example
# In this example, we will use the proxy design pattern to
# create a retrieve service
import base64
from typing import Dict

# the service interface
class BaseService:
    def retrieve(self, query: str):
        raise NotImplementedError(
            "This is a abstract class, or the method is not implemented"
        )


# lets suppose we have a external service for retrieving data
# we do not have access to the code, this class is just an api for the external service
# normally, the retrieve proccess can take a long time
class ExternalService(BaseService):
    def retrieve(self, query: str) -> str:
        print(f"Retrieving query: {query}")
        # lets return the base64 string of query just for example purpose
        result = base64.b64encode(query.encode("ascii"))
        return result


class CachedExternalService(BaseService):
    external_service: ExternalService
    cached_result: Dict[str, str]

    def __init__(self, service: ExternalService) -> None:
        self.external_service = service
        self.cached_result = {}

    def retrieve(self, query: str):
        if query not in self.cached_result.keys():
            print("Query not cached, executing query...")
            result = self.external_service.retrieve(query)
            self.cached_result[query] = result
            return result

        print("Returning cached response...")
        return self.cached_result[query]


if __name__ == "__main__":
    external_service = ExternalService()
    service_proxy = CachedExternalService(external_service)

    print("First try")
    service_proxy.retrieve("users.all")
    print("Second Try")
    service_proxy.retrieve("users.all")
