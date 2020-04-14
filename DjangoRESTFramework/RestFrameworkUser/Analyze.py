import jsonpath


class AnalyzeDatas(object):

    def dict_getValue(self, targetDict, serchKey, default=None):
        """
        通过参数key，在jsons中进行递归匹配并输出{key:value}
        :param targetDict: 需要解析的json串
        :param serchKey: 需要查找的key
        :param default: :查不到符合的serchKey，就返回默认值None
        :return: true is dict false is none
        """

        rowslist = ["data", "headers"]

        for key, value in targetDict.items():

            if key in rowslist:
                if not isinstance(value, dict):
                    value = eval(value)

            if key == serchKey:
                return {serchKey: targetDict}

            elif isinstance(value, dict):
                item = self.dict_getValue(value, serchKey, default)
                if item is not default:
                    return item

        return default

    def dict_response(self, targetDict, serchKey, default=None):
        """
        通过参数key，在jsons中进行递归匹配并输出{key:value}
        :param targetDict: 需要解析的json串
        :param serchKey: 需要查找的key
        :param default: :查不到符合的serchKey，就返回默认值None
        :return: true is dict false is none
        """

        for key, value in targetDict.items():

            if key == serchKey:
                return {serchKey: targetDict}

            elif isinstance(value, dict):
                item = self.dict_getValue(value, serchKey, default)
                if item is not default:
                    return item

        return default

    def json_path(self, jsons, key):
        """
        通过参数key，在jsons中进行正则匹配并输出该key对应的list value
        :param jsons: 需要解析的json串
        :param key: 需要查找的key
        :return: true is list false is none
        """

        return jsonpath.jsonpath(jsons, "$..%s" % key)


AnalyzeData = AnalyzeDatas()