# Tweetifire

### Repo for CodeFunDo Plus Plus
 
Tweetifire is a python based web app to provide instant response to a tweet during a disaster. It uses a machine learning model trained on sample tweets, pre classified in need and availability classes, to predict the probability of each tweet into availability and need related tweets.

• Need tweets refer to tweets showing requirement of some resources.<br>
• Availability tweets are the tweets depicting the extra resources available.

It then segregates need related tweets and availability related tweets into separate sections.
The backend of the model is a machine learning model based on logistic regression, which classifies the tweets in need and availability classes, with an accuracy of 85-90%.

The working of this app has been provided in the video file attached.

 This app would be useful for the govt. and army officials to provide help to people who are in need and also those who have extra resources available can be helpful to those in need through this app. The even distribution of excess resources can be facilitated by the use of this app.
 
### An important issue

There is some issue in deploying the app on the azure due to issue in support for Tkinter. The app runs perfectly on the localhost and you can check that the files in the GitHub when downloaded and run after installing all the files given in requirements.txt along with Tkinter, it works perfectly.


