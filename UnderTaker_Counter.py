# counts "Undertaker threw Mankind" references
import praw
import config
def login():
	print("Logging bot in...")
	r = praw.Reddit(username = config.username,
					password = config.password,
					client_id = config.client_id,
					client_secret = config.client_secret,
					user_agent = "Undertaker Reference Bot v0.1")
	print("Bot Logged In!!")				
	return r

def run_bot(r):
	ref_count = 1
	print("Collecting 25 comments...")
	for comment in r.subreddit('test').comments(limit = 25):
		if "Undertaker threw Mankind off Hell in a Cell" in comment.body:
			print("Reference Found!")
			
			comment.reply("Reference to the Undertaker found!\nTotal number of references found:" + str(ref_count))
			ref_count += 1
			
			



r = login()
run_bot(r)
