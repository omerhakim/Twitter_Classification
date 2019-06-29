# PoliTwitting
## Twitter-based NLP Classifications
This NLP classification model aims to predict Twitter users’ political views based on the contents of their Twitter accounts (tweets).
This model is trained by scraping the Twitter accounts of 508 US Congress members. 
The first step in building the model was applying an EDA which included tokenization, stemming, and exclusion of stopwords. The EDA yielded nearly 10,000 features/stem words, narrowed down from over 180,000, based on the most common words in the corpus.   
After the EDA, I compared two methods of word vectorizion: Count Vector and TF-IDF, by applying three algorithms to them: Naive Bayes, Random Forest and XGBoost. The ultimate combination of word vectorization method & algorithm was identified for each of the two sub-models created in this project: The single tweet-based predicition, and the user's past five months' tweets-based prediction.

This model, if further developed, will be able to identify other users’ politics, and even place them on a scale (as opposed to simply determine R or D).  That ability should be vaulable for targeting specific messages to users based on their politics.




Following is a summary of the process of creating the model.
_____
Using the Library “Twint”, I scraped all the tweets of the US Congress members (House & Senate) between January 1, 2019, and June 12, 2019. For the Twitter accounts names I used the website "Tweet Congress": http://www.tweetcongress.org/home. I saved all the tweets on a json file.

<img src = "./images/image1.png" width="527" height="340">

Interestingly, Democrat Congress Members tweet more than Republicans ones. 267 Democrats posted 112,044 tweets during the period in question, wheareas 241 Democrats posted 64,236 tweets.

<img src = "./images/image3.png">
 
Of the 5 Congressman with the highest number of tweets, 4 are Democrats: Patty Murray, Debbie Mucarsel Powell, Pramila Jayapal, Sheldon Whitehouse. The only Republican of the top 5 is congressman Rob Portman.

<img src = "./images/image2.png">

The goal for the future model was set at around 10,000 features/stem-words.  To select those features, Tweets were first combined into "Democrat" and "Republican" lists.  Then, in order to make the selection, certain NLP methods, such as  tokenization, stemming, and exclusion of stopwords, were applied with the  NLTK Library.

<img src = "./images/image4.png">

After exluding the list of stop words created for the project, the total number of words was 3,744,823. The total vocabulry of the entire corpus was still relatively large: 181,194 words. 

<img src = "./images/image5.png">

The next step was researchong the most common unique words and bigrams in each group:

<img src = "./images/image6.png">
<img src = "./images/image23.png">
<img src = "./images/image24.png">


In order to reduce the number of words and create more efficient model, the Porter Stemming Algorithm was applied to the tokenized words:

<img src = "./images/image7.png">

As a final step of comprising the corpus - words appearing more than 14 times in a party's tweets corpus were selected, yielding a final list with 9,639 features. That list was saved as a Json file. 

<img src = "./images/image8.png">

Upon finalizing the list, the data frame to be used for the models was created. Once again, tokenization and a stemming algorithm were ised to tie between the data frame with the list of  the selected features.

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

