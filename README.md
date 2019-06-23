# Twitter_Classification
This NLP classification model aims to predict Twitter users’ political inclinations by scraping their tweets. 
This model is training by scraping the Twitter accounts of all 508 Congress members whose politics are already known.
If further developed, this model could be utilized to identify other users’ politics (on a scale) for the purpose of targeting specific messages to them.
After EDA, I created two models comprising of nearly 10,000 features, based on the most common words, which went through tokenization and stemming.
Both models aim to predict if the user is a Democrat or a Republican.
The model makes this prediction based on single tweets, whereas the second does that based on all tweets made by the user over the past five months.


Using the Library “Twint”, I scraped all the tweets of the US Congress members (House & Senate) between January 1, 2019, and June 12, 2019.

<img src = "./mode_5/images/image1.png" width="527" height="340">

One of the first thing we can see is that the democrats tweet much more. 267 Democrats responsible for 112,044 tweets while 241 democrats were responsible for 64,236 tweets
<img src = "./mode_5/images/image3.png">

from the top 5 highest number of Tweets by Congressman for the time being researched, 4 are democrats (Patty Murray, Debbie Mucarsel Powell, Pramila Jayapal, Sheldon Whitehouse) and only one is republican (Rob Portman).
<img src = "./mode_5/images/image2.png">
I decided to aim to aproximatly 10,000 featurs/stem words in my model. in order to do it I used different NLP technicks with the Library NLTK. I first merged all the twitts of the democrats to one list and all the republican tweets to other list. I then used Tokenizion and exclude stop word.
<img src = "./mode_5/images/image4.png">

a
<img src = "./mode_5/images/image5.png">
a
<img src = "./mode_5/images/image6.png">
a
<img src = "./mode_5/images/image7.png">
a
<img src = "./mode_5/images/image8.png">
a
<img src = "./mode_5/images/image9.png">
a
<img src = "./mode_5/images/image10.png">
a
<img src = "./mode_5/images/image11.png">
a
<img src = "./mode_5/images/image12.png">
a
<img src = "./mode_5/images/image12.1.png">
a
<img src = "./mode_5/images/image12.2.png">
a
<img src = "./mode_5/images/image13.png">
a
<img src = "./mode_5/images/image14.png">
a
<img src = "./mode_5/images/image15.png">
a
<img src = "./mode_5/images/image16.png">
a
<img src = "./mode_5/images/image17.png">
a
<img src = "./mode_5/images/image18.png">
a
<img src = "./mode_5/images/image18.1.png">
a
<img src = "./mode_5/images/image19.png">
a
<img src = "./mode_5/images/image20.png">
a
