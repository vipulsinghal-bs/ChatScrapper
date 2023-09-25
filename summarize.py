# import sys
# from gensim.summarization import summarize
# from gensim.parsing.preprocessing import remove_stopwords

# # Input text from Node.js
# input_text = sys.argv[1]

# # Remove stopwords
# filtered_text = remove_stopwords(input_text)

# # Summarize the filtered text
# summary = summarize(filtered_text)

# # Send the summarized text back to Node.js
# print(summary)


# import asyncio
import concurrent.futures
import json
from transformers import pipeline

# Define a function to perform summarization
def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=300, min_length=50, do_sample=False)[0]["summary_text"]
    return summary

# # List of large text inputs
# large_text_list = [...]

input_data = input()

# Parse the JSON string into a Python list
large_text_list = json.loads(input_data)

# large_text_list = ["Attention, everyone! I have fantastic news that I cannot wait to share with all of you. Drumroll, please! Last week, our incredible Channelize.io Team achieved a major milestone by successfully releasing our BRAND-NEW DASHBOARD. This was a highly anticipated release and its the result of weeks of relentless dedication and hard work of  @Pardeep Kumar  @Vipul Goel  @Siva Kumar  @Praveen Singh. The tireless commitment by you guys ensured the seamless and timely completion of the dashboard, guaranteeing a flawless release. Thank you guys...You all truly deserve the biggest and loudest cheer. Furthermore, kudos to @Balram Goyal for his invaluable guidance and support in bringing this milestone to fruition. And here's the cherry on top: We have already begun receiving positive feedback from our clients. This heartwarming response is a testament to the exceptional quality and value delivered by all of you. I couldn't be prouder of this remarkable accomplishment. Keep up the fantastic work, team!",
#             "Hi Everyone I am thrilled to announce that our hard work and dedication in myBalbo Phase 3 have yielded exceptional results! The client has expressed their utmost satisfaction with the project's outcome, thanks to each one of you and your remarkable efforts.I couldn't be prouder to be part of this team.  @Jeenta Devi  @Anuj Nigam  @Sachin Nagpal @Gurpreet  Together, we achieved greatness, and I'm excited for the future! Your commitment, collaboration, and expertise have been exemplary throughout the entire project journey.Let's carry this momentum forward as we embark on future projects and continue to make a positive impact.",
#            ]

# Create an event loop
# loop = asyncio.get_event_loop()

# # Define a coroutine to process the list asynchronously
# async def process_texts():
#     summaries = await asyncio.gather(*[summarize_text(text) for text in large_text_list])
#     return summaries

# # Run the coroutine and get the results
# summaries = loop.run_until_complete(process_texts())

# Close the event loop
# loop.close()


# Adjust the number of workers based on your CPU cores
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # Submit summarization tasks concurrently for each text in the list
    summaries = list(executor.map(summarize_text, large_text_list))

print("Summarized Text:")
text_list_json = json.dumps(summaries)

print(text_list_json)
