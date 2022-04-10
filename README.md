# Musical Mood Tracker

## Inspiration
We live in unprecidented times. This has taken a severe toll on our collective mental health. Journaling and Mood Tracking have proven to be effective in helping people be more proactive about their mental well being. Wouldn't it be convinent if you could track your mental health automatically based on your behaviour? Our choice of music often reflects the way we're feeling.


## What it does
We use the Spotify API to get a users recently played songs. We extract audio features from these songs and feed it into a Mage.AI categorization model to get the users mood. We then Update our Calender to reflect our mood for the day.

## How we built it
We used React for the front end of our app. The backend is a Python script hosted on a Flask server using ngrok. We used Spotipy for the Spotify API calls. We collected our dataset using Python as well. We selected playsits with descriptions that we categorized into a 5 point scale ranging from Great to Very Sad. We used a Mage.AI categorization model to predict a users mood using Spotify audio features.

## Challenges we ran into
This is our first hackathon


## Accomplishments that we're proud of

## What we learned

## What's next for VibeCheck
