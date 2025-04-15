import requests, random

#+------------------------------------------------------+
#| Author : L7N                                       |
#| Telegram : t.me/PyL7N                     |
#| Github : https://github.com/is-L7N  |
#+------------------------------------------------------+

class Instagram:
    def __init__(self, token: str):
        self.token = token        
        self.base_url = "https://i.instagram.com/api/v1/session"
        self.headers = {
            'User-Agent': self.user_agent(),
            'Authorization': self.token,
        }
    
    def get_sessions(self) -> int:    
        url = self.base_url + "/login_activity/"
        try:
            response = requests.get(url, headers=self.headers).json()
            print(response)
            last = max(response['sessions'], key=lambda x: x['login_timestamp'])                    
            login_timestamp = str(last['login_timestamp'])
            login_id = last['login_id']            
            return login_timestamp, login_id        
        except Exception:
            return False
                
    def agree(self) -> bool:
        res = self.get_sessions() 
        if not res:
            return False        
        login_timestamp, login_id = res
        
        url = self.base_url + "/login_activity/avow_login/"
        payload = {
            'login_timestamp': login_timestamp,
            'login_id': login_id
        }
        try:
            response = requests.post(url, data=payload, headers=self.headers).json()
            if response["status"] == "ok":
                return True
            else:
                return False       
        except Exception:
            return False
    
    def user_agent(self) -> str:
        rnd = str(random.randint(150, 999))
        agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986" + str(random.randint(111, 999)) + ")"
        return agent

token = "Bearer IGT:2:eyJ....."
L7N = Instagram(token).agree()
print(L7N)