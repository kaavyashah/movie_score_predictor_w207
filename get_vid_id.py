import os
import pandas as pd

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # read in movie data
    df = pd.read_csv("../w207-final/data/cleaned_movies.csv")

    # set start and end indices for API requests for the movies
    start = 4800
    end = start + 100
    # get movies from df
    movies = list(df['title'])[start:end]

    vid_ids = []

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "secret_keys/youtube12.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # do for each movie
    for movie in movies:
        print(movie)
        # find the top search video for movie title + Official Trailer
        video_request = youtube.search().list(
            part="snippet",
            maxResults=1,
            q= movie + " Official Trailer",
            type = "video"
        )
        video_response = video_request.execute()

        # deal with no responses and specific error cases
        if len(video_response['items']) == 0 or movie == "Mozart's Sister" or movie == "High Noon":
            vid_id = None
        else:
            # extract video id from API return value
            vid_id = video_response['items'][0]['id']['videoId']

        # append video id to list of all video ids
        vid_ids += [vid_id]

    # combine old video_id df with the new video_ids just found, and write over old file
    old_ids = pd.read_csv('video_ids.csv')
    data = {'movie': movies,
            'vid_ids': vid_ids}
    new_ids = pd.DataFrame(data)
    all_ids = pd.concat([old_ids, new_ids])
    correct_df = all_ids[['movie', 'vid_ids']]
    correct_df.to_csv("video_ids.csv", index = False)

if __name__ == "__main__":
    main()
