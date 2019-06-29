# PoliTwitting
## Twitter-based NLP Classifications
This NLP classification model aims to predict Twitter users’ political views based on the contents of their Twitter accounts (tweets).
This model is trained by scraping the Twitter accounts of 508 US Congress members. 
The first step in building the model was applying an EDA which included tokenization, stemming, and exclusion of stopwords. The EDA yielded nearly 10,000 features/stem words, narrowed down from over 180,000, based on the most common words in the corpus.   
After the EDA, I compared two methods of word vectorization: Count Vector and TF-IDF, by applying three algorithms to them: Naive Bayes, Random Forest and XGBoost. The ultimate combination of word vectorization method & algorithm was identified for each of the two sub-models created in this project: The single tweet-based prediction, and the user's past five months' tweets-based prediction.

This model, if further developed, will be able to identify other users’ politics, and even place them on a scale (as opposed to simply determine R or D).  That ability should be valuable for targeting specific messages to users based on their politics.




Following is a summary of the process of creating the model.
_____
Using the Library “Twint”, I scraped all the tweets of the US Congress members (House & Senate) between January 1, 2019, and June 12, 2019. For the Twitter accounts names I used the website "Tweet Congress": http://www.tweetcongress.org/home. I saved all the tweets on a json file.

<img src = "./images/image1.png" width="527" height="340">

Interestingly, Democrat Congress Members tweet more than Republicans ones. 267 Democrats posted 112,044 tweets during the period in question, whereas 241 Democrats posted 64,236 tweets.

<img src = "./images/image3.png">
 
Of the 5 Congressman with the highest number of tweets, 4 are Democrats: Patty Murray, Debbie Mucarsel Powell, Pramila Jayapal, Sheldon Whitehouse. The only Republican of the top 5 is congressman Rob Portman.

<img src = "./images/image2.png">

The goal for the future model was set at around 10,000 features/stem-words.  To select those features, Tweets were first combined into "Democrat" and "Republican" lists.  Then, in order to make the selection, certain NLP methods, such as  tokenization, stemming, and exclusion of stopwords, were applied with the  NLTK Library.

<img src = "./images/image4.png">

After excluding the list of stop words created for the project, the total number of words was 3,744,823. The total vocabulary of the entire corpus was still relatively large: 181,194 words. 

<img src = "./images/image5.png">

The next step was researching the most common unique words and bigrams in each group:

<img src = "./images/image6.png">
<img src = "./images/image23.png" style = max width = 85%>
<img src = "./images/image24.png" style = max width = 85%>


In order to reduce the number of words and create more efficient model, the Porter Stemming Algorithm was applied to the tokenized words:

<img src = "./images/image7.png">

As a final step of comprising the corpus - words appearing more than 14 times in a party's tweets corpus were selected, yielding a final list with 9,639 features. That list was saved as a Json file. 

<img src = "./images/image8.png">

Next, tokenization and a stemming algorithm were used to fit the new data frame - namely, the content scraped from Twitter - with the list of the selected features.

<img src = "./images/image9.png">

After dividing the data frame into 'data' and 'target', the Sklearn Train_Test_Split method was applied in order to train and validate the model.

<img src = "./images/image10.png">

The first method of word vectorization tested under this model was TF-IDF (term frequency–inverse document frequency). Three different classifiers were tested: Multinomial Naive Bayes, Random Forest, and XGBoost.

<img src = "./images/image12.png">

Summary of the results:

<img src = "./images/image12.1.png">

Confusion matrix (Left-Democrats, Right- Republicans) for the most accurate model (Naive Bayes):

<img src = "./images/image13.png">

Another NLP method tested under this project was Count Vectorization (including bigrmas and trigrams) with SKLearn. Again, three different classifier were tested: Multinomial Naive Bayes, Random Forest and XGBoost.

<img src = "./images/image14.png">

<img src = "./images/image12.2.png">

With the following confusion matrix, Naive Bayes scored the highest under the Count Vectorization method as well.

<img src = "./images/image15.png">

Below are the top 35 features with the highest probability toward each side:

<img src = "./images/image16.png">

The above process was repeated to create the second sub-model.  This time, it has been applied to all tweets made by each individual user over the past 5 months.

<img src = "./images/image17.png">

The results of the Naive Bayes and Count Vectorization were found to be the most accurate.

<img src = "./images/image18.png">

Below is a summary of all the classifier and methods used under this model:

<img src = "./images/image18.1.png">

Interestingly, miss-classified Congress members are known to be either progressive Republicans or conservative Democrats.

<img src = "./images/image19.png">
<img src = "./images/image25.png" style = max width = 10%>

Below are the top 35 features with the highest probability toward each side (per user model):

<img src = "./images/image20.png">

Future development:

this model delivered a binary R or D classification.  Further development will focus on utilizing cosine similarity and other methods to achieve a more scaled classification output.  In additional next step for the model would be to apply it to other users for targeted messaging. Finally, certain Twint capabilities, including scraping followers and retweets, and additional data, could be potentially layered into this model.

<img src = "./images/image22.png" style = max width = 75%>

