import sys
import requests


def get_headers(url, method="OPTIONS", show_headers=False):
  headers = {
    "Referer": "https://google.com"
  }
  try:
    response = requests.request(method, url, headers=headers)
    if show_headers:
      print(response.headers)
    print("Response OK?: ", response.ok)
    
    # Inspect the headers for CORS information
    cors_headers = {
      "Access-Control-Allow-Origin": response.headers.get("Access-Control-Allow-Origin"),
      "Access-Control-Allow-Methods": response.headers.get("Access-Control-Allow-Methods"),
      "Access-Control-Allow-Headers": response.headers.get("Access-Control-Allow-Headers")
    }
    for header, value in cors_headers.items():
      if value:
        print(f"{header}: {value}")
      else:
        print(f"{header}: None")

    response.raise_for_status()

    if response.ok:
      print("OK: ", response.status_code)
    else:
      print("ERROR: ", response.status_code)

  except requests.exceptions.Timeout:
    print("Timeout")
  except requests.exceptions.ConnectionError:
    print("Connection Error")
  except requests.exceptions.HTTPError as err:
    print("HTTP Error: ", err)
  except requests.exceptions.RequestException as err:
    print("Request Exception: ", err)
  except Exception as err:
    print("General Failure: ", err)


domain = "https://example.com"
if len(sys.argv) > 1:
  domain = sys.argv[1]
print(f"Domain: {domain}")

methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS']
for method in methods:
  print(f"Method: {method}")
  get_headers(domain, method)
  print("\n")
