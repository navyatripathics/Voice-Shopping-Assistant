**🛒 Voice Shopping Assistant**


**WEBSITE URL** : https://voice-shopping-assistant-agcg.onrender.com/

A voice-powered shopping cart web application built using Flask (Python backend) and HTML, CSS, JavaScript frontend.
This project allows users to add/remove items from a shopping cart using voice commands and provides smart suggestions, price tracking, and a dark/light theme toggle.

_Features_

-Voice Command Recognition
Add or remove items by speaking commands (e.g., “Add 2 breads”, “Remove 1 milk”).

-Dynamic Shopping Cart
Items are added with their price, category, and quantity.

-Smart Suggestions
Suggests related items (e.g., if you add bread, it suggests butter and milk).

-Available Items Grid
Displays all available products in a grid with emoji, price, and category.

_Modern UI_

Card-style shopping list with category badges

Circular mic button with glowing animation when listening

Scrollable smart suggestion bar

Total cart price calculation

_Theme Toggle_
Switch between Dark Mode and Light Mode.

_Tech Stack_

Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

Speech Recognition: Web Speech API

Template Engine: Jinja2

_Project Structure_
Voice-Shopping-Assistant/
│
├── app.py                 # Flask backend
│
├── utils/
│   └── nlp.py             # Command processing (parses add/remove + quantities)
│
├── templates/
│   └── index.html         # Frontend (Jinja2 + JS)
│
├── static/
│   └── style.css          # Custom styles (Light/Dark theme, UI design)
│
└── README.md              # Project documentation

_Installation & Setup_

Clone the repository

git clone https://github.com/yourusername/voice-shopping-assistant.git
cd voice-shopping-assistant


Create a virtual environment

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows


Install dependencies

pip install flask


Run the Flask app

python app.py


Open your browser and go to:
👉 http://127.0.0.1:5000

_Usage_

Click on the mic button and say:

"Add 2 breads" → Adds 2 breads to your cart

"Remove 1 milk" → Removes 1 milk from your cart

"Add rice" → Adds rice to your cart

View your cart with quantities, price, and category badges.

Explore the available items grid and add products manually.

Check smart suggestions for related items.

Toggle 🌙/☀️ for dark/light theme.

_Demo Commands_

Here are some example voice/text commands you can try:

➕ "Add 3 apples"

➕ "Add 1 bread" → suggests butter and milk

➕ "Add 2 milk" → suggests bread, coffee, chocolate

➖ "Remove 1 apple"

➖ "Remove 2 rice"

<img width="1919" height="1003" alt="image" src="https://github.com/user-attachments/assets/24c14258-8062-45f5-b29f-e34597b66a9c" />


📌 Future Improvements

User authentication and persistent carts

Checkout system with discounts/offers

Mobile-first responsive design

Voice feedback (text-to-speech responses)
