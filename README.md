# Demo for the Server Side event stack from Facebook

Python SDK is listed [here](https://github.com/facebook/facebook-python-business-sdk) and Server side FB events API is listed [here](https://developers.facebook.com/docs/marketing-api/server-side-api).

# Steps to launch demo

1. Copy `secrets_store_sample.py` into `secrets_store.py`.

2. Edit all variable especially `access_token`, `app_id`, `app_secret` and `pixel_id`.

3. Install FB Business SDK:

```
virtualenv venv
source venv/bin/activate
pip install facebook_business
```

4. Run the following commands:

```
python3 s2s_demo.py
```
# Previews

Demo previews below:

## 1. S2S API Design
![S2S API Design Diagram](https://raw.githubusercontent.com/vishwarajanand/server_side_events_api_fb_demo/master/demos/s2s_api_design.png "S2S design")

## 2. S2S API Events Manager flow
![S2S API Events Manager flow](https://raw.githubusercontent.com/vishwarajanand/server_side_events_api_fb_demo/master/demos/events_manager_demo.png "Events Manager Flow")

## 3. S2S Script Sample Output
![S2S API call output](https://raw.githubusercontent.com/vishwarajanand/server_side_events_api_fb_demo/master/demos/s2s_script_output.png "S2S API call output")
