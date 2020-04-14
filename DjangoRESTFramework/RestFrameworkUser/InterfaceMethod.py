import requests


class InterfaceRunMain(object):

    def interfacesendpost(self, url, data, headers):

        interfaceresult = requests.post(url=url, data=data, headers=headers, verify=False)
        interfaceresult.raise_for_status()
        return interfaceresult.json()

    def interfacesendget(self, url, data, headers):

        interfaceresult = requests.get(url=url, params=data, headers=headers, verify=False)
        interfaceresult.raise_for_status()
        return interfaceresult.json()

    def run_main(self, method, url=None, data=None, headers=None):

        try:
            interfaceresult = None

            if method == "POST":
                interfaceresult = self.interfacesendpost(url, data, headers)

            elif method == "GET":
                interfaceresult = self.interfacesendget(url, data, headers)

            return interfaceresult

        except Exception as Methodexc:

            return "Method error: %s" % Methodexc


InterRunMainS = InterfaceRunMain()
