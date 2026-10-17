import requests
import json
import os
from .airequestmodel import ChatRequest
from dotenv import load_dotenv



load_dotenv()

llm_service_url = os.getenv("OPENROUTER_URL")
api_key = os.getenv("OPENROUTER_API_KEY")
website_name = os.getenv("WEBSITE_NAME")
website_url = os.getenv("WEBSITE_URL")


print("service url =======", llm_service_url)


def get_response_from_ai(body_data: ChatRequest):
    SYSTEM = "Format every reply as Markdown. Use headings for sections, bullet lists for steps, bold for key terms, and fenced code blocks with a language tag for code."
 
    payload = body_data.model_dump(mode="json", exclude_none=True)
    payload["messages"].append({"role":"system","content": SYSTEM}) 
    print("payload. =======", payload)
    response = requests.post(
            url= str(llm_service_url),
            headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": str(website_url), # Optional. Site URL for rankings on openrouter.ai.
            "X-OpenRouter-Title": str(website_name), # Optional. Site title for rankings on openrouter.ai.
        },
            data=json.dumps(payload)
    )
    print("response. =======", response.json())
    return response.json()