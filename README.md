# PoliTwitting
## Twitter-based NLP Classifications
This NLP classification model aims to predict Twitter users’ political inclinations. 
This model is trained by scraping the Twitter accounts of 508 US Congress members.
Currently, both models aim to predict if the user is more close to being Democrat or a Republican. If further developed, this model could be utilized to identify other users’ politics (on a scale) for the purpose of targeting specific messages to them.
After EDA, I created two models comprising of nearly 10,000 features, based on the most common words, which went through tokenization and stemming.

The firs model makes this prediction based on single tweets, whereas the second does that based on all tweets made by the user over the past five months.

Following is a summarry of the process of creating the model.
_____
Using the Library “Twint”, I scraped all the tweets of the US Congress members (House & Senate) between January 1, 2019, and June 12, 2019. For the twitter accounts names I used the website "Tweet Congress": http://www.tweetcongress.org/home. I saved all the tweets on a json file.

<img src = "./mode_5/images/image1.png" width="527" height="340">

One of the first thing one can notice in the EDA is that the democrats tweet much more. 267 Democrats responsible for 112,044 tweets while 241 democrats were responsible for 64,236 tweets

<img src = "./mode_5/images/image3.png">

From the top 5 highest number of Tweets by Congressman( for the time being researched), 4 are democrats (Patty Murray, Debbie Mucarsel Powell, Pramila Jayapal, Sheldon Whitehouse) and only one is republican (Rob Portman).

<img src = "./mode_5/images/image2.png">

I decided to have approximately 10,000 features/stem-words in my future model. Therefore, I used different NLP methods with the Library NLTK. I first merged all the twits of the democrats to one list and all the republican tweets to another list. I then used Tokenization and exclude stop word.

<img src = "./mode_5/images/image4.png">

Vocabulary

<img src = "./mode_5/images/image5.png">

I did some research regarding the most common words in each group, and later used porter stemming for the vocabulry.

<img src = "./mode_5/images/image6.png">

Stemming

<img src = "./mode_5/images/image7.png">

in later stage I chose all the words which appear more than 14 times in every group and created my final list of 9639 features and export it to json files.

<img src = "./mode_5/images/image8.png">

after having the final fetures I ran tokenization and stemming process on my data 

<img src = "./mode_5/images/image9.png">

train, test, split

<img src = "./mode_5/images/image10.png">

and create vectors from each tweet


<img src = "./mode_5/images/image12.png">

Tf- Idf

<img src = "./mode_5/images/image12.1.png">

NB confudion matrix


<img src = "./mode_5/images/image13.png">

count vector

<img src = "./mode_5/images/image14.png">

<img src = "./mode_5/images/image12.2.png">

NB confusion matrix

<img src = "./mode_5/images/image15.png">

feature importance

<img src = "./mode_5/images/image16.png">

prediction on databased based on individual user

<img src = "./mode_5/images/image17.png">

NB Cunfusion and accuracy

<img src = "./mode_5/images/image18.png">

summary of all models

<img src = "./mode_5/images/image18.1.png">

wrong predictions

<img src = "./mode_5/images/image19.png">

feature importance

<img src = "./mode_5/images/image20.png">

Future development: In this model, I used a simple R vs. D classification, but future models can also use cosine similarity and other methods to check difference between users and therefore be utilized for targeted messaging.
Twint is also able to scrape followers, retweets and additional features that could potentially be layered into this model.

