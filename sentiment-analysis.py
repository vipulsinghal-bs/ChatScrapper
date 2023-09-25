from nltk.sentiment.vader import SentimentIntensityAnalyzer
import concurrent.futures
import json

# Initialize the sentiment analyzer
sid = SentimentIntensityAnalyzer()

input_data = input()

# Parse the JSON string into a Python list
text_list = json.loads(input_data)

# Sample text for sentiment analysis
# text_list = ["Congratulations  @Manaswi Dubey 🎉🎉",
#             "Bigstep is thrilled to announce yet another 5-star clutch review, recognizing our exceptional work in website restoration. This achievement reinforces our position as a leader in the industry and serves as a testament to our team's unmatched expertise and relentless pursuit of excellence. We are grateful for their dedication, passion, and innovative approach that consistently deliver remarkable outcomes.",
#             "Riya Sharma and Himanshu Singh tweet their thanks to Sanjeev Kumar for his work. @RiyaSharma and @HimanshuSingh thank you for your great work. Keep doing great! @SanjeevKumar tweets back.",
#             "Business Analysis and Requirements Gathering Phase is the cornerstone of achieving success in project execution. Do like, share, and comment!!https://www.linkedin.com/feed/update/urn:li:activity:7105904753439625217.",
#             "Shivani Gaddi, Program Manager on Bespoke Augmented Reality and Video Editing Solutions with Banuba. We really appreciate Shivani's contribution to BigStep and the information that she has shared is really valuable for our readers. Give it a read and share your thoughts in the comments!!",
#                 ]

# Perform sentiment analysis

def filter_messages(text):
 sentiment_scores = sid.polarity_scores(text)
# Interpret the sentiment scores
 compound_score = sentiment_scores['compound']
 return compound_score >= 0.90

# if compound_score >= 0.05:
#     sentiment = "Positive"
# elif compound_score <= -0.05:
#     sentiment = "Negative"
# else:
#     sentiment = "Neutral"

# with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # Submit summarization tasks concurrently for each text in the list
filtered_messages = list(filter(filter_messages, text_list))

filtered_messages_list_json = json.dumps(filtered_messages)

print(filtered_messages_list_json)

# print(f"Sentiment: {sentiment}")
# print(f"compound score:{compound_score}")
