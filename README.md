# PoliTwitting
## Twitter-based NLP Classifications
This NLP classification model aims to predict Twitter users’ political inclinations. 
This model is trained by scraping the Twitter accounts of 508 US Congress members.
Currently, the model aims to predict if the user stated opinions are more similar to being Democrat or a Republican. If further developed, this model could be utilized to identify other users’ politics (on a scale) for the purpose of targeting specific messages to them.

After EDA, I created two  sub-models comprising of nearly 10,000 features, based on the most common words, which went through tokenization and stemming algorithm.

The first model makes this prediction based on single tweet, whereas the second does that based on all tweets made by the user over the past five months.

Following is a summary of the process of creating the model.
_____
Using the Library “Twint”, I scraped all the tweets of the US Congress members (House & Senate) between January 1, 2019, and June 12, 2019. For the twitter accounts names I used the website "Tweet Congress": http://www.tweetcongress.org/home. I saved all the tweets on a json file.

<img src = "./mode_5/images/image1.png" width="527" height="340">

One of the first thing one can notice in the EDA is that the democrats tweet much more. 267 Democrats responsible for 112,044 tweets while 241 democrats were responsible for 64,236 tweets

<img src = "./mode_5/images/image3.png">

From the top 5 of the  Congressman with  highest number of Tweets ( for the time being researched), 4 are democrats (Patty Murray, Debbie Mucarsel Powell, Pramila Jayapal, Sheldon Whitehouse) and only one is a republican (Rob Portman).

<img src = "./mode_5/images/image2.png">

I decided to have approximately 10,000 features/stem-words in my future model. Therefore, I used different NLP methods with the Library NLTK. I first merged all the twits of the democrats to one list and all the republican tweets to another list. I then used Tokenization and exclude stop words.

<img src = "./mode_5/images/image4.png">

After exluding the list of stop words i created, the total number of words was 3,744,823. The total vocabulry of the entire corpus was still relatively big: 181,194 words. 

<img src = "./mode_5/images/image5.png">

I did some research regarding the most common unique words in each group:

<img src = "./mode_5/images/image6.png">


-

more images of NGRAMs

-

In order to reduce the number of words and create more efficient model, I used the Porter Stemming Algorithm over the tokenized words:

<img src = "./mode_5/images/image7.png">

My next step was selecting all the words which appear more than 14 times in each party's tweets corpus, and created my final list of 9639 features. The list was saved as Json file. 

<img src = "./mode_5/images/image8.png">

After selecting the final features ,  I created the data frame which will be used in my models. I used again tokenization and stemming algorithm to fit my data frame  with the list of  the selected features.

<img src = "./mode_5/images/image9.png">

To be able to train and validate the model, I will use the Sklearn Train_Test_Split method. I split the data frame to data and target.

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

