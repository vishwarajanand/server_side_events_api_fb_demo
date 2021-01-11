# Demo for the Server Side event stack from Facebook

Python SDK is listed [here](https://github.com/facebook/facebook-python-business-sdk) and Server side FB events API is listed [here](https://developers.facebook.com/docs/marketing-api/server-side-api).

# Steps to launch demo

1. Copy `secrets_store_sample.py` into `secrets_store.py`.

2. Edit all variable especially `pixel_id` and `test_code` - each available from pixel events manager's implementation. `app_id` and `app_secret` are needed if more APIs need to be called and can be optained from app dashboard.

3. `access_token` has been generated from business manager system user where both pixel and app are added. Alternatively, a token from events manager can be generated too.

4. Install FB Business SDK:

```
virtualenv venv
source venv/bin/activate
pip install facebook_business
```

5. Run the following commands:

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
