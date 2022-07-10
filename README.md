# Data Analysis of the Most Trending Data Science Channels on YouTube ![YouTube Icon](res\youtube.ico "YouTube")
# Aims, objectives and background

## 1. [I]ntroduction

YouTube is a Google-owned online video sharing and social media platform based in the United States. Steve Chen, Chad Hurley, and Jawed Karim founded it on February 14, 2005. It is the second-most-visited website in the world, right after Google. YouTube has over one billion monthly users who view over one billion hours of video each day. As of May 2019, more than 500 hours of video footage were being uploaded every minute. YouTube was purchased by Google for $1.65 billion in October 2006 [[1]](https://en.wikipedia.org/wiki/YouTube). Characterized by a powerful and complex algorithm, YouTube offer lots of advantageous benefits such as the ability to promote a business and generate income [[2]](https://wearegrow.com/8-massive-benefits-of-using-youtube-for-business/). 

However, understanding how a video works is kind of difficult, as we've probably all witnessed, dead or old videos sometimes resurface out of nowhere whether it had been popular at the time or not and even without any particular interest in it. YouTube's algorithm, like those of other social media sites, has developed over time [[3]](https://sproutsocial.com/insights/youtube-algorithm/) and hence making it hard to determine the success of a Youtube video as to what characteristics a video should have to perform better? can features like video duration, likes and comments affect the performance and if so, which one impact the most?

The extent of this project is confined to data science channels. As a result, the statistics of roughly five (05) of the most popular data science Youtube channels will be investigated in this study.

## 2. [A]ims and [O]bjectives

Throughout this project, we'll be covering the following:

- Defining Youtube API, its limitations and utilizing it to retrieve data.
- Analyze video data from several YouTube channels, compare them, and analyze their performance through investigating queries such as:
    - Does the amount of likes and comments on a video affect its popularity?
    - What's the average views per channel's video?
    - Does video length influence likes and engagements ?
    - How active and popular are the channels ?
    - In the amount of tags a key factor for gaining views?
- Utilizing NLP techniques to investigate text to gain some insights such as:
    - Popular topics used in titles.
    - Sentiment analysis on videos comments in relation to each channel.

## 3. [S]teps of the project
1. Request metadata from the YouTube API and transform them into a data frame for readability and ease of usage.
2. Preprocess data and engineer additional features for further analysis.
3. Exploratory data analysis (charts + interpretation).
4. Conclusions.


#### *The approach we'll be following is simple: we'll plot a graphical representation of our data alongside a brief explanation/assumptions, then draw our final conclusion in the conclusion section.*

## 4. About the [D]ata

We're well aware that there are readily available YouTube videos datasets on the web, some of which are updated daily, but for the sake of learning, we've decided to collect the data ourselves so as we can showcase our skills in data collection from scratch and our capabilities of using APIs such as YouTube's. Besides, finding the right data for a certain niche, such as our choice of **Data Science**, is unlikely, so it's sort of necessary at this point.

That said, the dataset is created using the [Google Youtube Data API version 3.0](https://developers.google.com/youtube/v3).

### Limitations and advantages

The data size isn't optimal but since this is a small project, a selection of only 5 YouTube channels is fairly acceptable. on the other hand, we've picked up the most popular and engaging ones based on the amount of their subscriptions; nonetheless, the more data you get the better.

Despite of its size, the data is complete; by complete we mean that all of the data for each selected feature of every channel has been gathered and is not null, but there are still a few missing data points which are the result of the channel's owner not failing to provide any information about them, such as the video description or the tags.

### Data source ethics

The Youtube API is completely free; however, The cost of using the YouTube Data API is determined on the quota usage. You get 10,000 free points every day and every request costs at least one point. You may use the [Quota Calculator](https://developers.google.com/youtube/v3/determine_quota_cost) to estimate your quota expenses, and if you require more inquiries, you can ask for additional quotas by filling out a [Form](https://support.google.com/youtube/contact/yt_api_form) with YouTube API Services.