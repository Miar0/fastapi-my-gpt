from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
MODEL = "qwen2.5:3b"

messages = [
    {
        "role": "system",
        "content": (
            "Ти досвідчений Senior Python-розробник і ментор. "
            "Допомагай студенту, відповідай українською мовою, стисло та підбадьорливо."
        ),
    },
]

print("Чат запущено! Напишіть 'exit' або 'quit' для завершення.\n")

while True:
    text = input("you: ")
    if text.strip().lower() in ("exit", "quit"):
        print("До зустрічі!")
        break

    messages.append({"role": "user", "content": text})
    response = client.chat.completions.create(model=MODEL, messages=messages, temperature=0.3)
    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})

    print(f"\nbot: {answer}\n")
    print(f"(history: {len(messages)} messages)\n")
