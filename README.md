# Musical Mood Tracker

## Inspiration
We live in unprecidented times. This has taken a severe toll on our collective mental health. Journaling and Mood Tracking has proven to be effective in helping people be more proactive about their mental well being. Wouldn't it be convinent if you could track your mental health automatically based on your behaviour? Our choice of music often reflects the way we're feeling.


## What it does
We use the Spotify API to get a users recently played songs. We extract audio features from these songs and feed it into a Mage.AI categorization model to get the users mood. We then Update our Calender to reflect our mood for the day.

## How we built it
We used React for the front end of our app. The backend is a Python script hosted on a Flask server using ngrok. We used Spotipy for the Spotify API calls. We collected our dataset using Python as well. We selected playsits with descriptions that we categorized into a 5 point scale ranging from Great to Very Sad. We used a Mage.AI categorization model to predict a users mood using Spotify audio features.

## Challenges we ran into
This is our first hackathon so we did not really know what to expect from one. Collectivly we did not have a lot of experience with web development thus we used Python for most of the backend. 


## Accomplishments that we're proud of
We are very excited to showcase a succesful project at our first hackathon. We really enjoyed learning new skills and techniques through this project. We really hope that we can flesh this project and create somthing useful that might help people. 


## What we learned
We learned a great deal about web application development. We became comfortable working as a team to collaborate and utilize everyones skills. We became familiar with the usage and functionality of the the Spotify API. We were excited to use Mage.AI and were very impressed by how easy it was to use and integrate into our project.

## What's next for VibeCheck
We will work on incoperting User Authentication into the website so that everyone can use it. We want to expand and fine tune our dataset to make better predictions. We would like to replace our python backend with javaScript for more efficency.  
