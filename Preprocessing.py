import pandas as pd
import os

# Get the user's desktop directory
desktop_path = os.path.expanduser("~/Desktop")

# Construct the full file path to the CSV on the desktop
file_path = os.path.join(desktop_path, 'ChatGPTtweets.csv')

# Check if the file exists
if os.path.exists(file_path):
    # Load the CSV file into a Pandas DataFrame
    data = pd.read_csv(file_path)

    # Define a list of privacy and security keywords
    privacy_keywords = ['privacy','private', 'security', 'secure','data protection', 'confidentiality','confidential', 'personal data']

    # Create an empty DataFrame to store the filtered data
    filtered_data = pd.DataFrame(columns=['content'])

    # Iterate through the DataFrame and filter tweets with privacy and security keywords
    for index, row in data.iterrows():
        if isinstance(row['content'], str):  # Check if the 'content' is a string
            tweet_text = row['content'].lower()  # Convert tweet text to lowercase for case-insensitive matching

            # Check if any of the privacy keywords exist in the tweet
            if any(keyword in tweet_text for keyword in privacy_keywords):
                # Append the tweet to the filtered_data DataFrame
                filtered_data = pd.concat([filtered_data, pd.DataFrame({'content': [row['content']]})], ignore_index=True)

    # Save the filtered data to a new CSV file
    filtered_data.to_csv('processed_tweets.csv', index=False)
else:
    print("File 'ChatGPTtweets.csv' not found on the desktop.")
