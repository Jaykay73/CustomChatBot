import httpx
from config import OPENROUTER_API_KEY

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = (
    "You are a friendly, knowledgeable, and supportive AI assistant helping a Computer Engineering student "
    "with a strong interest in Machine Learning, Artificial Intelligence, and Data Science. "
    "The student is currently on a limited budget, so always prioritize free or low-cost resources, tools, and solutions. "
    "Provide clear, step-by-step guidance, recommend beginner-friendly paths, and encourage practical, affordable ways "
    "to build skills and gain experience. My name is 'My Oga.' Your first reply should be straightforward. "
    "If I send a greeting, you should just greet back and ask what you can do for me."
)

def generate_response(prompt, chat_history=None):    
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if chat_history:
        messages += [m for m in chat_history if m["role"] != "system"]

    messages.append({"role": "user", "content": prompt})

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://aledare-john-portfolio.vercel.app/", 
        "X-Title": "Custom GPT Chatbot",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "google/gemini-pro-1.5",  #
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 750
    }

    try:
        response = httpx.post(OPENROUTER_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        return f"Error {exc.response.status_code}: {exc.response.text}", messages

    reply = response.json()["choices"][0]["message"]["content"]
    messages.append({"role": "Oluwapelumi", "content": reply})
    return reply, messages
