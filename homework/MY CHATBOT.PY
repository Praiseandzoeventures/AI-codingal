print("Hi! I am a simple chatbot.")
name = input("What is your name? ").strip()

if name:
	print(f"Nice to meet you, {name}!")
else:
	print("Nice to meet you!")

print("You can say hello, tell me how you feel, ask how I am, or type help.")
print("Type 'bye' to end our chat.\n")

while True:
	message = input("You: ").strip().lower()

	if message in ("bye", "exit", "quit"):
		print(f"Bot: It was nice talking with you, {name or 'friend'}!")
		break
	elif message == "help":
		print("Bot: Try saying hello, 'how are you?', or 'I feel happy/sad'.")
	elif "hello" in message or "hi" in message:
		print(f"Bot: Hello, {name or 'friend'}!")
	elif "how are you" in message:
		print("Bot: I am doing well, thanks for asking! How are you?")
	elif "happy" in message or "good" in message or "great" in message:
		print("Bot: That is lovely to hear!")
	elif "sad" in message or "bad" in message or "upset" in message:
		print("Bot: I am sorry you feel that way. I hope things get better soon.")
	elif message:
		print("Bot: Interesting! Tell me a little more.")
	else:
		print("Bot: I did not catch that. Type 'help' to see what I understand.")
