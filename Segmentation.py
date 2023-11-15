import pandas as pd

# Load your processed tweets data from a CSV file on the desktop
desktop_path = '/Users/shahadsaeed/Desktop/processed_tweets.csv'
df = pd.read_csv(desktop_path)

# Create dictionaries to store tweets in each category
public_data_exploitation = []
personal_input_exploitation = []
unauthorized_access_to_data = []

# Define keywords for each category
keywords_a = ["public data", "open data", "sanitizing", "training process", "training data", "trained on", "publicly available data"]
keywords_b = ["conversation", "conversations", "input data", "private chat", "prompt", "prompts"]
keywords_c = ["unauthorized access", "vulnerabilities", "data breach", "data security", "security breach", "attack", "attacking", "hack", "hacking", "threat", "breach", "unauthorized entry", "data compromise"]

# Function to categorize tweets
def categorize_tweet(tweet):

    # Remove hashtags from the tweet content
    tweet = ' '.join(word for word in tweet.split() if not word.startswith('#'))

    if any(keyword in tweet.lower() for keyword in keywords_a):
        public_data_exploitation.append(tweet)
    if any(keyword in tweet.lower() for keyword in keywords_b):
        personal_input_exploitation.append(tweet)
    if any(keyword in tweet.lower() for keyword in keywords_c):
        unauthorized_access_to_data.append(tweet)

# Categorize each tweet in the DataFrame
for tweet in df['content']:
    categorize_tweet(tweet)

# Create data frames for each category
public_data_exploitation_df = pd.DataFrame({'content': public_data_exploitation, 'category': 'public_data_exploitation'})
personal_input_exploitation_df = pd.DataFrame({'content': personal_input_exploitation, 'category': 'personal_input_exploitation'})
unauthorized_access_to_data_df = pd.DataFrame({'content': unauthorized_access_to_data, 'category': 'unauthorized_access_to_data'})

# Concatenate data frames into one
combined_df = pd.concat([public_data_exploitation_df, personal_input_exploitation_df, unauthorized_access_to_data_df], ignore_index=True)

# Save categorized tweets to a single CSV file
combined_df.to_csv('categorized_tweets.csv', index=False)

print("Categorized tweets saved to a single CSV file.")
