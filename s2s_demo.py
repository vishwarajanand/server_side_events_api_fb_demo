from facebook_business.adobjects.adspixel import AdsPixel
from facebook_business.api import FacebookAdsApi

from secrets_store import *
import time

FacebookAdsApi.init(app_id, app_secret, access_token)

fields = []

params = {
    "data": [
        {
            "event_name": "Purchase",
            # Unix timestamp example: 1598927035
            "event_time": int(time.time()),
            "event_id": "event.id.12346",
            "event_source_url": "http://jaspers-market.com/product/some_product_url",
            "user_data": {
                "client_ip_address": "2620:10d:c094:200::1:9c87",
                "client_user_agent": "demo s2s ua",
                "em": [
                    "309a0a5c3e211326ae75ca18196d301a9bdbd1a882a4d2569511033da23f0abd"
                ],
                "fbc": "fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890",
                "fbp": "fb.1.1558571054389.1098115397",
            },
            "custom_data": {
                "value": 100.2,
                "currency": "USD",
                "content_ids": ["product.id.123"],
                "content_type": "product",
            },
            "data_processing_options": [],
            "action_source": "website",
            "opt_out": "false",
        }
    ]
}

# to see events in events manager's test live events tool
if len(test_event_code) > 0:
    params["test_event_code"] = test_event_code

func_call = AdsPixel(pixel_id).create_event(
    fields=fields,
    params=params,
)

print(func_call)

# Output:
# <AdsPixel> {
#     "events_received": 1,
#     "fbtrace_id": "AhZex4M7cOQtj-zvlyDsHFi",
#     "messages": []
# }

# Check events here:
# https://business.facebook.com/events_manager2/list/pixel/351725288935559/test_events?business_id=269028820483935&act=288563226

# API doc here:
# https://developers.facebook.com/docs/marketing-api/conversions-api/guides/end-to-end-implementation
