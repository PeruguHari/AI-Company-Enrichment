import google.generativeai as genai
import os

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_insights(text):

    prompt = f"""
Analyze this company.

Return ONLY valid JSON.

{{
"company_name":"",
"core_service":"",
"target_customer":"",
"probable_pain_point":"",
"outreach_opener":""
}}

Do not return markdown.
Do not return explanation.

Website Content:

{text[:4000]}
"""

    response = model.generate_content(prompt)

    text = response.text

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return text.strip()