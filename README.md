# Vector_Twitter

Using the Twitter API and some simple code from the SDK, we are able to have Vector read out Tweets that contain a certain word or phrase as they are tweeted.

*Instructions to get the Twitter API working in a python script adapted from here*
https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api

Requirements:
Vector Robot
Active Twitter developer account
Twitter API keys

To get the Twitter API keys yo uneed to first register for a developer account on Twitter:
https://developer.twitter.com/en

Once your developer account has been confirmed, go to the Twitter developer portal and create a new app.
This should give you the API keys you need to read and write to Twitter via your account.

Edit the auth.py script with the required keys and save.

Install the Twython module for python:
sudo pip3 install twython

Then edit which keywords/phrases you want to be alerted to in the vector_twitter.py script on line 41. Seperate different keywords with a comma.

You may want to change the sleep time after an alert is announced to stop a constant barrage of alerts. Useful if you have set alot of popular keywords. You may miss some tweets inbetween though.
