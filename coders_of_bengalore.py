import json

# Read the data from the file and store it in a variable

with open("finaldata.txt", encoding="utf-8") as f:
    data = f.read()

# Split the data into chunks based on double newlines and filter out any chunks that are too short to be valid

chunks = data.split("\n\n")
chunks = [c for c in chunks if len(c)>3]


# Define a function to parse each chunk and extract the relevant information

def parse_chunk(chunk): 
        chunk = chunk.strip()
        sep_chunk = chunk.split('\n')
        username = sep_chunk[0]
        num_of_posts = int(sep_chunk[1].split(" post")[0].replace(",", ""))
        num_of_followers = float(sep_chunk[2].split(" follower")[0].replace(",", "").replace("K", "").replace("M", ""))
        if("K" in sep_chunk[2]):
            num_of_followers = int(num_of_followers * 1000)
        elif("M" in sep_chunk[2]):
            num_of_followers = int(num_of_followers * 1000000)
        else:
            num_of_followers = int(num_of_followers)
             

    
        num_of_following = float(sep_chunk[3].split(" following")[0].replace(",", "").replace("K", "").replace("M", ""))
        if("K" in sep_chunk[3]):
            num_of_following = int(num_of_following * 1000)
        elif("M" in sep_chunk[3]):
            num_of_following = int(num_of_following * 1000000)
        else:
            num_of_following = int(num_of_following)

            
        name = sep_chunk[4]
        if(len(sep_chunk)> 5):
            category = sep_chunk[5]
            bio = "\n".join(sep_chunk[6:])
        else:
            category = "Unknown"
            bio = "" 
        return {"username": username, "num_of_posts": num_of_posts, "num_of_followers": num_of_followers, "num_of_following": num_of_following, "name": name, "category": category, "bio": bio}


 # Parse all the chunks and store the results in a list, then write the list to a JSON file   
all_chunks = [] 
for chunk in chunks:  
    parsed_chunk = parse_chunk(chunk)
    all_chunks.append(parsed_chunk)

s = json.dumps(all_chunks, indent=4, ensure_ascii=False)  
with open("output.json", "w", encoding="utf-8") as f:
    f.write(s)


# Who has the maximum number of posts?
max_posts = 0
chunk_with_max_post = None

for chunk in all_chunks:
    if max_posts < chunk['num_of_posts']:
        max_posts = chunk['num_of_posts']
        chunk_with_max_post = chunk

if chunk_with_max_post:
    print(chunk_with_max_post['username'])
else:
    print("No data available")


# Who has the maximum number of followers?
max_followers = 0
chunk_with_max_followers = None

for chunk in all_chunks:
    if max_followers < chunk['num_of_followers']:
        max_followers = chunk['num_of_followers']
        chunk_with_max_followers = chunk

if chunk_with_max_followers:
    print(chunk_with_max_followers['username'])
else:
    print("No data available")


# Who follows the maximum number of people?
max_following = 0
chunk_with_max_following = None

for chunk in all_chunks:
    if max_following < chunk['num_of_following']:
        max_following = chunk['num_of_following']
        chunk_with_max_following = chunk
if chunk_with_max_following:
    print(chunk_with_max_following['username'])
else:
    print("No data available")


# How many categories are there?
categories = set()
for chunk in all_chunks:
    categories.add(chunk['category'])
print(len(categories))


# printing all the answers in a json file with the questions as keys and the answers as values

answers = {
    "max_posts_username": chunk_with_max_post['username'] if chunk_with_max_post else "No data available",
    "max_followers_username": chunk_with_max_followers['username'] if chunk_with_max_followers else "No data available",
    "max_following_username": chunk_with_max_following['username'] if chunk_with_max_following else "No data available",
    "num_categories": len(categories),
    "name of the categories": list(categories)
}
with open("answers.json", "w", encoding="utf-8") as f:
    json.dump(answers, f, indent=4, ensure_ascii=False)