# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import pandas as pd

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # read in yhr video_ids
    df = pd.read_csv('video_ids.csv')
    # intialize lists that will hold the stats for each video
    views, likes, dislikes, comments = [], [], [], []

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "secret_keys/client_secret_852805443845-7gi6p9n4qdv9oqd1o91bqd2kot6nf9gn.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # do for each movie
    for i in range(len(df)):
        print(i)
        # get video id
        vid_id = df['vid_ids'][i]

        # if no video id, set stats to None
        if vid_id is None:
            views += [None]
            likes +=[None]
            comments += [None]
            dislikes += [None]
            continue

        # API call to get stats
        stats_request = youtube.videos().list(
            part="statistics",
            id=vid_id
        )

        stats_response = stats_request.execute()

        # if stats don't exist, set stats to None
        if len(stats_response['items']) == 0:
            views += [None]
            likes +=[None]
            comments += [None]
            dislikes += [None]
            continue

        else:
            # extract stats from API return value
            vid_stats = stats_response['items'][0]['statistics']
            vid_stats_keys = vid_stats.keys()

            # add stats to respective lists, if the stat exists
            if 'viewCount' in vid_stats_keys:
                views += [vid_stats['viewCount']]
            else:
                views += [None]

            if 'likeCount' in vid_stats_keys:
                likes += [vid_stats['likeCount']]
            else:
                likes +=[None]

            if 'dislikeCount' in vid_stats_keys:
                dislikes += [vid_stats['dislikeCount']]
            else:
                dislikes += [None]

            if 'commentCount' in vid_stats_keys:
                comments += [vid_stats['commentCount']]
            else:
                comments += [None]

    # write stats to new file
    df['views'] = views
    df['likes'] = likes
    df['dislikes'] = dislikes
    df['comments'] = comments

    df.to_csv("vid_stats.csv")

if __name__ == "__main__":
    main()
