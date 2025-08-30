from flask import Flask, render_template, request, jsonify
from utils.nlp import process_command

app = Flask(__name__)

# In-memory cart
cart = []

# Product catalog with emojis
PRODUCT_CATALOG = {
    "milk": {"price": 2.5, "category": "Dairy", "emoji": "🥛"},
    "bread": {"price": 1.5, "category": "Bakery", "emoji": "🍞"},
    "apple": {"price": 0.8, "category": "Produce", "emoji": "🍎"},
    "banana": {"price": 0.5, "category": "Produce", "emoji": "🍌"},
    "eggs": {"price": 3.0, "category": "Dairy", "emoji": "🥚"},
    "rice": {"price": 10.0, "category": "Grains", "emoji": "🍚"},
    "chocolate": {"price": 5.0, "category": "Snacks", "emoji": "🍫"},
    "butter": {"price": 2.0, "category": "Dairy", "emoji": "🧈"},
    "coffee": {"price": 6.0, "category": "Beverages", "emoji": "☕"},
}

# Smart suggestion map
SUGGESTIONS = {
    "bread": ["butter", "milk"],
    "milk": ["bread", "coffee", "chocolate"],
    "apple": ["banana", "chocolate"],
    "rice": ["eggs", "milk"]
}


@app.route("/")
def home():
    total = sum(item["price"] * item["quantity"] for item in cart)
    return render_template(
        "index.html",
        cart=cart,
        total=total,
        PRODUCT_CATALOG=PRODUCT_CATALOG,
        suggestions=[]
    )


@app.route("/add-item", methods=["POST"])
def add_item():
    data = request.get_json()
    command = data.get("command", "")

    action, item_name, quantity = process_command(command)
    item_name = item_name.lower().strip()

    if item_name not in PRODUCT_CATALOG:
        return jsonify({"status": "error", "message": f"{item_name} not found in catalog"})

    product = PRODUCT_CATALOG[item_name]

    if action == "add":
        # If item already in cart, increase quantity
        for item in cart:
            if item["name"] == item_name:
                item["quantity"] += quantity
                total = sum(i["price"] * i["quantity"] for i in cart)
                return jsonify({
                    "status": "success",
                    "message": f"Added {quantity} {item_name}",
                    "cart": cart,
                    "total": total,
                    "suggestions": SUGGESTIONS.get(item_name, [])
                })

        # Otherwise add new item
        cart.append({
            "name": item_name,
            "price": product["price"],
            "category": product["category"],
            "emoji": product["emoji"],
            "quantity": quantity
        })

    elif action == "remove":
        for item in cart:
            if item["name"] == item_name:
                item["quantity"] -= quantity
                if item["quantity"] <= 0:
                    cart.remove(item)
                total = sum(i["price"] * i["quantity"] for i in cart)
                return jsonify({
                    "status": "success",
                    "message": f"Removed {quantity} {item_name}",
                    "cart": cart,
                    "total": total,
                    "suggestions": []
                })
        return jsonify({"status": "error", "message": f"{item_name} not in cart"})

    # Default return after cart update
    total = sum(i["price"] * i["quantity"] for i in cart)
    return jsonify({
        "status": "success",
        "message": "Cart updated",
        "cart": cart,
        "total": total,
        "suggestions": SUGGESTIONS.get(item_name, [])
    })


if __name__ == "__main__":
    # ✅ Important: host="0.0.0.0" and port from environment for deployment
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
