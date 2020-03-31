# Demo for the Server Side event stack from Facebook

Python SDK is listed [here](https://github.com/facebook/facebook-python-business-sdk) and Server side events API is listed [here](https://developers.facebook.com/docs/marketing-api/server-side-api).

# Steps to launch demo

1. Create a folder

2. Paste contents as below in send_events.py:

3. Change `secrets.py` file with `access_token`, `app_id`, `app_secret` and `pixel_id`.

4. Run the following commands:

```
virtualenv venv
source venv/bin/activate
pip install facebook_business
python3 send_events.py
```
# Previews

Demo previews below:

## 1. S2S API Design
![S2S API Design Diagram](https://raw.githubusercontent.com/vishwarajanand/server_side_events_api_fb_demo/master/s2s%20API%20design.png "S2S design")

## 2. S2S API Events Manager flow
![S2S API Events Manager flow](https://raw.githubusercontent.com/vishwarajanand/server_side_events_api_fb_demo/master/events_manager_demo.png "Events Manager Flow")


