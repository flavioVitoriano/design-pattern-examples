# facade example

# the facade pattern provides a simple facade object to simplify complex operations

class HTMLPage:
    def create_page(self):
        print("Page created")

    def modify_header(self, header: str):
        print("Modifying header")

    def apply_styles(self):
        print("Applying styles")


class API:
    def expose_endpoints(self):
        print("Exposing endpoints")
    
    def generate_config(self) -> str:
        return "the config"
    
    def set_homepage(self, page: HTMLPage):
        print("Setting up the homepage")


class WSGIServer:
    def start_server(self):
        print("Starting server")

    def set_config(self, _: str):
        print("Setting config")


# this class will help us to encapsulate all the needed operations to deploy a site
class Facade:
    def deploy_site(self) -> float:
        api = API()
        server = WSGIServer()
        page = HTMLPage()

        page.create_page()
        page.modify_header("Superb page")
        page.apply_styles()
        api.set_homepage(page)

        config = api.generate_config()
        server.set_config(config)

        api.expose_endpoints()
        server.start_server()
