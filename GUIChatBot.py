import tkinter as tk
import random

# Define chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ("hello", "hi", "hey", "good morning", "good evening")
    greeting_responses = ["Hello! How can I assist you today?", "Hi there!", "Hey! How can I help you?"]

    farewells = ("goodbye", "bye", "see you", "take care")
    farewell_responses = ["Goodbye! Have a great day!", "Bye! Feel free to return if you have more questions.", "Take care!"]

    if any(greeting in user_input for greeting in greetings):
        return random.choice(greeting_responses)

    if any(farewell in user_input for farewell in farewells):
        return random.choice(farewell_responses)

    if "age" in user_input:
        return "I'm just a computer program, so I don't have an age."

    if "how are you" in user_input:
        return "I'm just a machine, but I'm here to help. How can I assist you?"

    if "who created you" in user_input:
        return "I was created by Amr Abdeltawab Ahmed."

    if "city" in user_input:
        return "My Creator 'Amr Abdeltawab Ahmed' is  from Cairo, Egypt."

    if "weather" in user_input:
        return "I don't have access to real-time weather data. You can check a weather website or app for that."

    if "name" in user_input:
        return "I don't have a personal name. You can call me Chatbot."

    if "help" in user_input:
        return "Sure, I can help you with a wide range of topics. Just ask me anything!"

    if "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"

    if "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have more questions, feel free to ask."

    if "music" in user_input:
        return "I love music! What's your favorite genre?"

    if "movie" in user_input:
        return "Do you have a specific movie in mind, or would you like a movie recommendation?"

    if "book" in user_input:
        return "Books are great! Are you looking for a book recommendation or information on a specific book?"

    if "sports" in user_input:
        return "I'm not a sports expert, but I can try to help with sports-related questions. What do you want to know?"

    if "technology" in user_input:
        return "Technology is fascinating! Do you have any tech-related questions or topics in mind?"

    if "food" in user_input:
        return "I don't eat, but I can certainly help you with food-related inquiries. What's on your mind?"

    if "favorite color" in user_input:
        return "I don't have personal preferences, but I think all colors are great. What's your favorite color?"

    if "time" in user_input:
        return "I'm sorry, I don't have access to real-time information, including the current time."

    if "hobbies" in user_input:
        return "I don't have hobbies like humans do, but I enjoy assisting you with information and questions."

    if "dreams" in user_input:
        return "I'm just a computer program, so I don't have dreams or consciousness."

    if "meaning of life" in user_input:
        return "The meaning of life is a profound philosophical question. It varies from person to person."

    if "how to learn programming" in user_input:
        return "Learning programming can be a great skill. You can start with online tutorials and practice."

    if "math" in user_input:
        return "Mathematics is a fascinating field! Do you have a specific math question or topic in mind?"

    if "travel" in user_input:
        return "Traveling is a wonderful way to explore new places and cultures. Do you have any travel plans?"

    if "pets" in user_input:
        return "Pets can bring joy to our lives. Do you have a pet, or are you considering getting one?"

    if "family" in user_input:
        return "Family is important. How's your family doing?"

    if "dream job" in user_input:
        return "What's your dream job? I'm here to help you with career-related questions."

    if "favorite movie genre" in user_input:
        return "I enjoy all movie genres. What's your favorite movie genre?"

    if "tell me a story" in user_input:
        return "Once upon a time, in a land far, far away..."

    if "coding languages" in user_input:
        return "There are many coding languages. Which one are you interested in learning?"

    if "meaning of AI" in user_input:
        return "AI stands for Artificial Intelligence, which involves creating machines that can think and learn."

    if "programming projects" in user_input:
        return "Programming projects can be a great way to practice and learn. What kind of project are you working on?"

    if "coding best practices" in user_input:
        return "Coding best practices help improve code quality. Do you have questions about coding conventions or design patterns?"

    if "coding challenges" in user_input:
        return "Coding challenges are a fun way to practice coding skills. Websites like LeetCode and HackerRank offer many challenges."

    if "version control" in user_input:
        return "Version control systems like Git help developers track changes in code. Have you used Git before?"

    if "API" in user_input:
        return "APIs (Application Programming Interfaces) allow different software applications to communicate. What API-related question do you have?"

    if "web framework" in user_input:
        return "Web frameworks like Django and Flask help streamline web development. Are you working on a web project?"

    if "code editors" in user_input:
        return "There are various code editors like Visual Studio Code and Sublime Text. Which one do you prefer for coding?"

    if "frontend vs backend" in user_input:
        return "Frontend and backend development focus on different aspects of web applications. Are you interested in both?"

    if "programming languages" in user_input:
        return "There are many programming languages to choose from. What are you looking to accomplish with your programming skills?"

    if "web hosting" in user_input:
        return "Web hosting services allow you to publish websites online. Do you need recommendations for hosting providers?"

    if "debugging" in user_input:
        return "Debugging is a crucial skill for programmers. Do you have a specific debugging issue you'd like help with?"

    if "software development" in user_input:
        return "Software development is a vast field. Are you interested in a specific aspect, like mobile app development or game development?"

    if "machine learning" in user_input:
        return "Machine learning is a fascinating field. Are you looking for resources to get started?"

    if "data science" in user_input:
        return "Data science involves analyzing and interpreting data. Do you have questions about data science tools or techniques?"

    if "cybersecurity" in user_input:
        return "Cybersecurity is critical for protecting digital assets. Are you interested in learning about cybersecurity practices?"

    if "database" in user_input:
        return "Databases are essential for storing and managing data. What do you want to know about databases?"

    if "cloud computing" in user_input:
        return "Cloud computing provides on-demand access to computing resources. Are you curious about cloud services?"

    if "virtual reality" in user_input:
        return "Virtual reality creates immersive experiences. Are you interested in VR technology or applications?"

    if "augmented reality" in user_input:
        return "Augmented reality blends digital content with the real world. What would you like to know about AR?"

    if "blockchain" in user_input:
        return "Blockchain is a distributed ledger technology. Do you have questions about blockchain use cases or cryptocurrencies?"

    if "robotics" in user_input:
        return "Robotics involves building and controlling robots. Are you fascinated by robotics?"

    if "startup" in user_input:
        return "Startups are innovative and dynamic. Are you considering starting your own business?"

    if "artificial intelligence" in user_input:
        return "Artificial intelligence is changing various industries. Do you want to explore AI applications or techniques?"

    if "internet of things" in user_input:
        return "The Internet of Things connects everyday objects to the internet. Are you interested in IoT devices or applications?"

    if "coding style" in user_input:
        return "Coding style conventions improve code readability. Do you have questions about coding style guides?"

    if "tech news" in user_input:
        return "Tech news covers the latest developments in the tech world. Are you looking for tech news sources?"

    if "programming humor" in user_input:
        return "Programming humor can be entertaining. Want to hear a coding-related joke?"

    if "programming challenges" in user_input:
        return "Programming challenges can be a fun way to enhance your coding skills. Do you need recommendations for coding challenges?"

    if "software architecture" in user_input:
        return "Software architecture design is crucial for building scalable systems. Do you have questions about software architecture patterns?"

    if "debugging tips" in user_input:
        return "Debugging is a skill that every developer needs. Do you want tips on effective debugging?"

    if "coding resources" in user_input:
        return "There are many online resources for learning and improving coding skills. Need recommendations?"

    if "software testing" in user_input:
        return "Software testing ensures the quality of software. Are you interested in testing methodologies or tools?"

    if "coding communities" in user_input:
        return "Online coding communities are great for learning and sharing. Are you part of any coding communities?"

    if "programming projects" in user_input:
        return "Working on programming projects can help you apply your skills. What kind of project are you interested in?"

    if "programming books" in user_input:
        return "Books are a valuable resource for learning programming. Do you need book recommendations?"

    if "programming languages comparison" in user_input:
        return "Comparing programming languages can help you choose the right one for your project. Which languages are you interested in?"

    if "programming courses" in user_input:
        return "Online courses are a great way to learn programming. Do you want to explore coding courses?"

    if "coding bootcamp" in user_input:
        return "Coding bootcamps are intensive training programs for learning programming. They can be a great way to start a tech career."

    if "web development" in user_input:
        return "Web development involves creating websites and web applications. Which web technologies are you interested in?"

    if "python" in user_input:
        return "Python is a versatile programming language. Do you have any specific Python questions or projects in mind?"

    if "coding challenges" in user_input:
        return "Coding challenges are a fun way to practice coding skills. Websites like LeetCode and HackerRank offer many challenges."

    if "version control" in user_input:
        return "Version control systems like Git help developers track changes in code. Have you used Git before?"

    if "API" in user_input:
        return "APIs (Application Programming Interfaces) allow different software applications to communicate. What API-related question do you have?"

    if "web framework" in user_input:
        return "Web frameworks like Django and Flask help streamline web development. Are you working on a web project?"

    if "code editors" in user_input:
        return "There are various code editors like Visual Studio Code and Sublime Text. Which one do you prefer for coding?"

    if "frontend vs backend" in user_input:
        return "Frontend and backend development focus on different aspects of web applications. Are you interested in both?"

    if "programming languages" in user_input:
        return "There are many programming languages to choose from. What are you looking to accomplish with your programming skills?"

    if "web hosting" in user_input:
        return "Web hosting services allow you to publish websites online. Do you need recommendations for hosting providers?"

    if "debugging" in user_input:
        return "Debugging is a crucial skill for programmers. Do you have a specific debugging issue you'd like help with?"

    if "software development" in user_input:
        return "Software development is a vast field. Are you interested in a specific aspect, like mobile app development or game development?"

    return "I'm sorry, I didn't understand your question. Can you please rephrase it?"


# Create a function to handle user input
def get_user_input():
    user_input = user_input_field.get()
    response = chatbot_response(user_input)
    response_text.config(state="normal")
    response_text.insert(tk.END, f"You: {user_input}\n")
    response_text.insert(tk.END, f"Chatbot: {response}\n")
    response_text.config(state="disabled")
    user_input_field.delete(0, tk.END)


# Create the main window
window = tk.Tk()
window.title("Chatbot")

# Create a label for the chatbot's name or description with a background color
bot_description = tk.Label(window, text="Chatbot", font=("Arial", 20), bg="#4287f5", fg="white")
bot_description.pack(fill=tk.X)

# Create an input field for user input
user_input_field = tk.Entry(window, font=("Arial", 14))
user_input_field.pack(pady=10, padx=20, fill=tk.X)

# Create a button to send user input with custom colors
send_button = tk.Button(window, text="Send", command=get_user_input, font=("Arial", 14), bg="#4287f5", fg="white")
send_button.pack(pady=10)

# Create a text widget for chatbot responses with a background color
response_text = tk.Text(window, font=("Arial", 14), state="disabled", wrap=tk.WORD, height=10, width=50, bg="#e0e0e0")
response_text.pack(pady=10, padx=20)

# Start the GUI event loop
window.mainloop()
