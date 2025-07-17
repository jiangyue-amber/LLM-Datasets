# Software Name: Daily_Digest
# Category: News
# Description: The Daily Digest is a news software application that provides users with a curated summary of the most important news stories of the day. Users can customize their preferences and receive a concise digest of the latest news in their chosen categories.

import datetime
import random

class NewsArticle:
    def __init__(self, category, headline, content, source):
        self.category = category
        self.headline = headline
        self.content = content
        self.source = source
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"[{self.category}] {self.headline} ({self.source})"

class UserProfile:
    def __init__(self, username, preferences=None):
        self.username = username
        self.preferences = preferences if preferences else []  # List of categories

    def add_preference(self, category):
        if category not in self.preferences:
            self.preferences.append(category)

    def remove_preference(self, category):
        if category in self.preferences:
            self.preferences.remove(category)

    def get_preferences(self):
        return self.preferences


class NewsAggregator:
    def __init__(self):
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def fetch_news(self):
        # Simulate fetching news from different sources. Replace with actual API calls in a real application.
        # Example data (replace with your actual data fetching logic)
        news_data = [
            {"category": "Technology", "headline": "New AI Model Released", "content": "A new AI model...", "source": "TechNews"},
            {"category": "Politics", "headline": "Government Announces New Policy", "content": "The government...", "source": "GovtInfo"},
            {"category": "Sports", "headline": "Team Wins Championship", "content": "The team...", "source": "SportsDaily"},
            {"category": "Technology", "headline": "Cybersecurity Threat Detected", "content": "A new cybersecurity...", "source": "CyberWatch"},
            {"category": "Business", "headline": "Stock Market Surges", "content": "The stock market...", "source": "FinReport"},
            {"category": "Politics", "headline": "Debate Held Between Candidates", "content": "Candidates...", "source": "PolitiCast"},
            {"category": "Sports", "headline": "Record Broken in Track and Field", "content": "Athlete breaks record...", "source": "AthleticsNow"},
            {"category": "World", "headline": "International Summit Concludes", "content": "World leaders...", "source": "GlobalNews"},
            {"category": "Business", "headline": "Company Announces Record Profits", "content": "Company profits...", "source": "BizToday"},
            {"category": "Health", "headline": "New Study on Healthy Eating", "content": "Researchers discover...", "source": "HealthMag"}
        ]

        for data in news_data:
            article = NewsArticle(data["category"], data["headline"], data["content"], data["source"])
            self.add_article(article)
        return self.articles #Return the list of articles

    def get_articles_by_category(self, category):
          return [article for article in self.articles if article.category == category]


class DailyDigest:
    def __init__(self, news_aggregator):
        self.news_aggregator = news_aggregator

    def generate_digest(self, user_profile):
        preferred_categories = user_profile.get_preferences()
        if not preferred_categories:
            return "No preferred categories selected. Please update your preferences."

        digest_content = f"Daily Digest for {user_profile.username}:\n"
        for category in preferred_categories:
            articles = self.news_aggregator.get_articles_by_category(category) #use of get_articles_by_category function
            if articles:
                 digest_content += f"\n--- {category} ---\n"
                 for article in articles:
                     digest_content += str(article) + "\n"
            else:
                digest_content += f"\nNo news in {category} today.\n"

        return digest_content

# Example usage:
if __name__ == "__main__":
    # Initialize components
    aggregator = NewsAggregator()
    digest_generator = DailyDigest(aggregator)

    # Create a user profile
    user = UserProfile("Alice", ["Technology", "Politics"])  #Pre-defined preferences

    # Fetch news articles
    aggregator.fetch_news()

    # Generate and print the daily digest
    digest = digest_generator.generate_digest(user)
    print(digest)

    user2 = UserProfile("Bob")
    user2.add_preference("Sports")
    user2.add_preference("Business")
    digest2 = digest_generator.generate_digest(user2)
    print(digest2)