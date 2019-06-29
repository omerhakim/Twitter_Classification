# PoliTwitting
## Twitter-based NLP Classifications
This NLP classification model aims to predict Twitter users’ political views based on the contents of their Twitter accounts (tweets).
This model is trained by scraping the Twitter accounts of 508 US Congress members. 
The first step in building the model was applying an EDA which included tokenization, stemming, and exclusion of stopwords. The EDA yielded nearly 10,000 features, selected based on the most common words in the corpus.   
After the EDA, I compared two methods of word vectorizion: Count Vector and TF-IDF, by applying three algorithms to them: Naive Bayes, Random Forest and XGBoost. The ultimate combination of word vectorization method & algorithm was identified for each of the two sub-models created in this project: the single tweet-based predicition, and the user's past five months' tweets-based prediction.

This model, if further developed, will be able to identify other users’ politics, and even place them on a scale (as opposed to simply determine R or D).  That ability should be vaulable for targeting specific messages to users based on their politics.




Following is a summary of the process of creating the model.
_____
Using the Library “Twint”, I scraped all the tweets of the US Congress members (House & Senate) between January 1, 2019, and June 12, 2019. For the Twitter accounts names I used the website "Tweet Congress": http://www.tweetcongress.org/home. I saved all the tweets on a json file.

<img src = "./images/image1.png" width="527" height="340">

One of the most predomonent things about the EDA, is that Democrat Congress Members tweet more than Republicans ones. 267 Democrats posted 112,044 tweets during the period in question, wheareas 241 Democrats posted 64,236 tweets.

<img src = "./images/image3.png">

From the top 5 of the  Congressman with  highest number of Tweets ( for the time being researched), 4 are democrats (Patty Murray, Debbie Mucarsel Powell, Pramila Jayapal, Sheldon Whitehouse) and only one is a republican (Rob Portman).

<img src = "./images/image2.png">

I decided to have approximately 10,000 features/stem-words in my future model. Therefore, I used different NLP methods with the Library NLTK. I first merged all the twits of the democrats to one list and all the republican tweets to another list. I then used Tokenization and exclude stop words.

<img src = "./images/image4.png">

After exluding the list of stop words i created, the total number of words was 3,744,823. The total vocabulry of the entire corpus was still relatively big: 181,194 words. 

<img src = "./images/image5.png">

I did some research regarding the most common unique words and bigrams in each group:

<img src = "./images/image6.png">
<img src = "./images/image23.png">
<img src = "./images/image24.png">


In order to reduce the number of words and create more efficient model, I used the Porter Stemming Algorithm over the tokenized words:

<img src = "./images/image7.png">

My next step was selecting all the words which appear more than 14 times in each party's tweets corpus, and created my final list of 9639 features. The list was saved as Json file. 

<img src = "./images/image8.png">

After selecting the final features ,  I created the data frame which will be used in my models. I used again tokenization and stemming algorithm to fit my data frame  with the list of  the selected features.

<img src = "./images/image9.png">

To be able to train and validate the model, I will used Sklearn Train_Test_Split method. I split the data frame to data and target.

<img src = "./images/image10.png">

The first method of word vectorization I tested was TF-IDF (term frequency–inverse document frequency). I checked three different classifier: Multinomial Naive Bayes, Random Forest and XGBoost.


<img src = "./images/image12.png">

Summary of the results:

<img src = "./images/image12.1.png">

Confusion matrix (Left-Democrats, Right- Republicans) for the most accurate model (Naive Bayes):


<img src = "./images/image13.png">

Another NLP method I tested was Count Vectorization (including bigrmas and trigrams) with scikit-learn. I checked again three different classifier: Multinomial Naive Bayes, Random Forest and XGBoost.

<img src = "./images/image14.png">

<img src = "./images/image12.2.png">

Also with the count vector the Naive Bayes had the best results with the following confusion matrix:

<img src = "./images/image15.png">

These are the top 35 features with the highest probability toward each side:

<img src = "./images/image16.png">



I followed the same process, but this time based the prediction on all the tweets of individual user in the last 5 months.

<img src = "./images/image17.png">

The results of the Naive Bayes and count vector were the most accurate.

<img src = "./images/image18.png">

Here is a summary of all the classifier and methods I used:

<img src = "./images/image18.1.png">

It is interesting to see who are the congress members were the model miss-classified. some of them are to be either progressive republicans are conservative democrats. 

<img src = "./images/image19.png">
<img src = "./images/image25.png">

These are the top 35 features with the highest probability toward each side (per user model):

<img src = "./images/image20.png">

Future development: In this model, I used a simple R vs. D classification, but future models can also use cosine similarity and other methods to check difference between users and therefore be utilized for targeted messaging.
Twint is also able to scrape followers, retweets and additional features that could potentially be layered into this model.


<img src = "./images/image22.png">

