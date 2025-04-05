import google.generativeai as genai

genai.configure(api_key="AIzaSyBoi5WQAx5DwD-JCgC3W1GUz_QQv6ud3IU")

def ai_calc(question):
    # Create the model
    generation_config = {
    "temperature": 0.25,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    system_instruction="you are advanced mathematic calulcator, you have to find the answers to complex maths questions asked by user",
    )

    chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            "What is integral of x",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Okay! Let's find the indefinite integral of x.\n\n**Understanding Indefinite Integrals**\n\nThe indefinite integral of a function, denoted by ∫f(x) dx, represents the family of all functions whose derivative is f(x).  It's like finding the \"anti-derivative.\"  We always include a constant of integration, \"C\", because the derivative of a constant is zero.\n\n**The Power Rule of Integration**\n\nThe power rule for integration is:\n\n∫xⁿ dx = (xⁿ⁺¹)/(n+1) + C   (where n ≠ -1)\n\n**Applying it to x**\n\nIn our case, x is the same as x¹, so n = 1.\n\n1. **Increase the exponent by 1:**  1 + 1 = 2\n2. **Divide by the new exponent:** x² / 2\n\n**The Result**\n\nTherefore, the indefinite integral of x is:\n\n∫x dx = (x² / 2) + C\n\n**Answer:**\n\nThe integral of x is **(x²/2) + C**, where C is the constant of integration.\n",
        ],
        },
    ]
    )

    response = chat_session.send_message(question)

    print(response.text)

    return response.text