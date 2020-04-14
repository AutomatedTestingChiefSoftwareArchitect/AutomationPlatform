import urllib3
import logging
from rest_framework import status
from DjangoRESTFramework import models
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DjangoRESTFramework.RestFrameworkUser import InterfaceMethod, Analyze
from DjangoRESTFramework.SerializersModelSData import InterfaceSerializers

logger = logging.getLogger(__name__)


class AutomatedPlatformView(ViewSet):

    def platforminterface(self, request, *args, **kwargs):
        """接口测试
                仅仅用于测试 与项目无关(可保存)"""

        try:
            urllib3.disable_warnings()
            interfaceResults = InterfaceMethod.InterRunMainS.run_main(url=request.data.get('url'),
                                                                      method=request.data.get('method'),
                                                                      data=request.data.get('data'),
                                                                      headers=request.data.get('headers'))
            return Response(status=status.HTTP_200_OK, data=interfaceResults)

        except Exception as InterfaceError:

            return Response(status=status.HTTP_400_BAD_REQUEST, data={"msg": "Run errror: %s" % InterfaceError})

    def interfaceproject(self, request, *args, **kwargs):
        """接口测试
                项目关联"""

        for api_id in request.data.get("apilist"):

            queryset = models.UserApiInfo.objects.get(id=api_id, user=request.user)
            verified_queryset = InterfaceSerializers.InterfaceSerializers(instance=queryset, many=False)

            expectedresult = verified_queryset.data.get("expectedresults", None)
            queryanalyzeslist_value = eval(verified_queryset.data.get("data", None))
            queryanalyzelist_value = eval(verified_queryset.data.get("headers", None))

            querydata = models.DataPool.objects.filter(user=request.user)
            verified_data = InterfaceSerializers.DataPoolSerializer(instance=querydata, many=True)

            queryheaders = models.HeadersPool.objects.filter(user=request.user)
            verified_headers = InterfaceSerializers.HeadersPoolSerializer(instance=queryheaders, many=True)

            queryanalyzelist = [rows for items in verified_headers.data for rows in items.values()]
            queryanalyzeslist = [rows for items in verified_data.data for rows in items.values()]

            for queryanalyzekey in queryanalyzelist:
                if queryanalyzekey:

                    queryanalyze_value = models.HeadersPool.objects.filter(datakey=queryanalyzekey,
                                                                           user=request.user).first()
                    verified_queryanalyze_value = InterfaceSerializers.HeadersPoolSerializers(
                        instance=queryanalyze_value, many=False)

                    for item_key, item_value in verified_queryanalyze_value.data.items():
                        queryanalyzelist_value.update({queryanalyzekey: item_value})

            for queryanalyzeskey in queryanalyzeslist:
                if queryanalyzeskey:

                    queryanalyzes_value = models.DataPool.objects.filter(datakey=queryanalyzeskey,
                                                                         user=request.user).first()
                    verified_queryanalyzes_value = InterfaceSerializers.DataPoolSerializers(
                        instance=queryanalyzes_value, many=False)

                    for item_keys, item_values in verified_queryanalyzes_value.data.items():
                        queryanalyzeslist_value.update({queryanalyzeskey: item_values})

            urllib3.disable_warnings()
            interfaceResults = InterfaceMethod.InterRunMainS.run_main(
                data=queryanalyzeslist_value,
                headers=queryanalyzelist_value,
                url=verified_queryset.data.get("url", None),
                method=verified_queryset.data.get("method", None))

            Analyzelist = [Analyze.AnalyzeData.dict_response(interfaceResults, queryanalyzekey)
                           for queryanalyzekey in queryanalyzelist if queryanalyzekey]

            for Analyzedict in Analyzelist:
                if Analyzedict:

                    for key, value in Analyzedict.items():
                        models.HeadersPool.objects.filter(datakey=key, user=request.user).update(datavalue=value)

            Analyzedicts = [Analyze.AnalyzeData.dict_response(interfaceResults, queryanalyzeskey)
                            for queryanalyzeskey in queryanalyzeslist if queryanalyzeskey]

            for Analyzedicts in Analyzedicts:
                if Analyzedicts:

                    for keys, values in Analyzedicts.items():
                        models.DataPool.objects.filter(datakey=keys, user=request.user).update(datavalue=values)

            if expectedresult:
                expectedresults = eval(expectedresult)

                for expectedresults_key, expectedresults_value in expectedresults.items():
                    listpath = Analyze.AnalyzeData.json_path(interfaceResults, expectedresults_key)

                    if not listpath:
                        return Response(status=status.HTTP_400_BAD_REQUEST,
                                        data={"msg": "%s assert error" % expectedresults_key})

                    if expectedresults_value in listpath:
                        logger.info(expectedresults_value)

        return Response(status=status.HTTP_200_OK, data={"msg": "run successful"})
