import requests

class ApIclient:
    base_url = "https://gorest.co.in/public/v2"
    
    def __init__(self):
        self.header = { 
            "Content-Type": "application/json",
            "Authorization": "Bearer f3b1a3ded0b6c8034fc228c8e8658829c393bb2555fc7d3659f336a5e329a0df"
        }
    
    def get_task(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.header)
        return response
    
    def create_task(self, endpoint, payload):
        url = f"{self.base_url}/{endpoint}"
        return requests.post(url, json=payload, headers=self.header)
    
    def update_task(self, endpoint, user_id, payload):
     return requests.put(f"{self.base_url}/{endpoint}/{user_id}", headers=self.header, json=payload)
 
    def delete_task(self, endpoint, user_id):
     return requests.delete(f"{self.base_url}/{endpoint}/{user_id}", headers=self.header)
    
    
 