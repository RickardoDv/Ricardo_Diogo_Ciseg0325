#cyber INtellegence MOdule

#pip install OTXv2

from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
import json


API_KEY= "66cd9d62952cd8aff30b7b6e6809c2a2d1383ee8a923e50978a719ce81cfff69"
otx=OTXv2(API_KEY)

indicators = otx.get_all_indicators()


#for indicator in indicators:
 #   print(indicator["indicator"] + "  ---  " + indicator["type"])

resultado = otx.get_indicator_details_full(IndicatorTypes.DOMAIN, "www.jupiteralbufeirahotel.com")

#resultado = otx.get_indicator_details_full(IndicatorTypes.IPv4, "195.23.212.226")


res = json.dumps(resultado)


print(res)