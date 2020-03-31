from facebook_business.adobjects.adspixel import AdsPixel
from facebook_business.api import FacebookAdsApi

from secrets import *

fields = [
]

params = {
    "data": [
        {
            "event_name": "Purchase",
            "event_time": 1585640728,
            "event_id": "event.id.90763767",
            "event_source_url": "http:\/\/jaspers-market.com\/product\/123",
            "user_data": {
                "client_ip_address": "2620:10d:c094:200::1:9c87",
                "client_user_agent": "demo s2s ua",
                "em": "309a0a5c3e211326ae75ca18196d301a9bdbd1a882a4d2569511033da23f0abd",
                "fbc": "fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890",
                "fbp": "fb.1.1558571054389.1098115397"
            },
            "custom_data": {
                "value": 100.2,
                "currency": "USD",
                "content_ids": [
                    "product.id.123"
                ],
                "content_type": "product"
            },
            "opt_out": False
        }
    ],
    "test_event_code": "TEST76025"
    # to see events in events manager's test live events tool
}
func_call = AdsPixel(pixel_id).create_event(
    fields=fields,
    params=params,
)

print(func_call)

# Output:
# <AdsPixel> {
#     "events_received": 1,
#     "fbtrace_id": "AzDc726cCmCAVu5bnFrmqaR",
#     "messages": []
# }
