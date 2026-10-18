import requests
import json
import base64
import os
from userservice.userrequest import ImageRequest
from dotenv import load_dotenv
from random import randint
import time





load_dotenv()

llm_service_url = os.getenv("OPENROUTER_URL_IMAGE")
api_key = os.getenv("OPENROUTER_API_KEY")


print("service url =======", llm_service_url)

print("api key  =======", api_key)



def create_image(data):
   # print("request============",data)
    response = requests.post(
            url=str(llm_service_url),
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            data=json.dumps(data)
    )
    result = response.json()
    return result
  # print(time.time())
   # image_type = f"output_{time.time()}" + f".{data["output"]}"
    #for i, image in enumerate(result.get("data", [])):
    #    image_bytes = base64.b64decode(image["b64_json"])
    #    with open(image_type, "wb") as f:
     #       f.write(image_bytes) 
   
    
    
   