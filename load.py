import instaloader
from dotenv import load_dotenv
import os
 
load_dotenv()
# Get instance
loader = instaloader.Instaloader()
 
# Login using the credentials
loader.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))

# Load session created with `instaloader -l USERNAME` (load session created w/#  `instaloader -l USERNAME`)
# loader.load_session_from_file("@gariskode_", "./session/session-gariskode_")

print("Fetching data...")
# Use Profile class to access metadata of account
def getprofile(username):
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        post = profile.get_posts()
        postData = []
        for i in post:
            postData.append({
                "caption": i.caption,
                "url": i.url,
                "likes": i.likes,
                "is_video": i.is_video,
                "video_url": i.video_url,
                "date": i.date
            })
        data = {
            "status_code": 200,
            "status": "success",
            "message": "Data fetched successfully",
            "data" : {
                "username": profile.username,
                "user_id": profile.userid,
                "followers": profile.followers,
                "followees": profile.followees,
                "bio": profile.biography,
                "external_url": profile.external_url,
                "number_of_posts": profile.mediacount,
                "posts": postData
            }
        }
        return data
    except Exception as e:
        return {
            "status_code": 500,
            "status": "error",
            "message": str(e)
        }

    