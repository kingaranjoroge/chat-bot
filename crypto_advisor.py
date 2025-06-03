import random

# Predefined crypto database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

class CryptoAdvisor:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.greetings = [
            "Hey there! Let's find you a green and growing crypto!",
            "Welcome! Ready to explore some crypto opportunities?",
            "Hi! I'm here to help you make informed crypto decisions!"
        ]
    
    def get_greeting(self):
        return random.choice(self.greetings)
    
    def analyze_query(self, user_query):
        user_query = user_query.lower()
        
        # Check for sustainability-related queries
        if any(word in user_query for word in ["sustainable", "eco", "green", "environment"]):
            return self.get_sustainable_recommendation()
        
        # Check for trend-related queries
        if any(word in user_query for word in ["trend", "trending", "growing", "growth"]):
            return self.get_trending_recommendation()
        
        # Check for general investment advice
        if any(word in user_query for word in ["invest", "buy", "purchase", "recommend"]):
            return self.get_general_recommendation()
        
        return "I'm not sure I understand. Could you ask about crypto trends, sustainability, or investment recommendations?"

    def get_sustainable_recommendation(self):
        sustainable_coins = {coin: data for coin, data in crypto_db.items() 
                           if data["sustainability_score"] >= 6/10}
        if sustainable_coins:
            best_coin = max(sustainable_coins.items(), 
                          key=lambda x: x[1]["sustainability_score"])
            return f"🌱 {best_coin[0]} is your best sustainable option! It has a sustainability score of {best_coin[1]['sustainability_score']*10}/10 and uses {best_coin[1]['energy_use']} energy."
        return "I couldn't find any highly sustainable cryptocurrencies in our database."

    def get_trending_recommendation(self):
        trending_coins = {coin: data for coin, data in crypto_db.items() 
                         if data["price_trend"] == "rising"}
        if trending_coins:
            best_coin = max(trending_coins.items(), 
                          key=lambda x: x[1]["sustainability_score"])
            return f"📈 {best_coin[0]} is trending up! It has a {best_coin[1]['market_cap']} market cap and a sustainability score of {best_coin[1]['sustainability_score']*10}/10."
        return "I couldn't find any trending cryptocurrencies in our database."

    def get_general_recommendation(self):
        # Balance between sustainability and market performance
        scored_coins = {
            coin: (data["sustainability_score"] * 0.6 + 
                  (1 if data["price_trend"] == "rising" else 0.5) * 0.4)
            for coin, data in crypto_db.items()
        }
        best_coin = max(scored_coins.items(), key=lambda x: x[1])
        return f"Based on both sustainability and market performance, I recommend {best_coin[0]}! 🚀"

def main():
    advisor = CryptoAdvisor()
    print(f"{advisor.name}: {advisor.get_greeting()}")
    print("\nDisclaimer: Crypto is risky—always do your own research! 💡")
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print(f"{advisor.name}: Goodbye! Remember to stay informed about your investments! 👋")
            break
        
        response = advisor.analyze_query(user_input)
        print(f"{advisor.name}: {response}")

if __name__ == "__main__":
    main() 