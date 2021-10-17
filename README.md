# headline_sentiment_analysis
During the summer of 2020 I noticed how political the coverage of COVID-19 in different states was, and I wondered if it was enough to measure. 
So I set up scripts to scrape thousands of headlines from CNN and Fox, and fed the headlines pertaining to high-profile governors into a sentiment analyzing library to measure how positively/negatively they were treated. 
The results were not super groundbreaking, but especially with CNN the political bias was very clear to see. 
At the time this data was created the governors of the Republican states had comparable or significantly fewer cases and deaths than the Democratic states, so the headline sentiments are not a function of COVID-19 severity.

# Results

![CNN](https://user-images.githubusercontent.com/50871836/137641210-bdee08b8-2ea8-4ae6-bed2-8b67b643fb16.png)

![Fox](https://user-images.githubusercontent.com/50871836/137641211-eee098c9-9a2d-4c68-affd-052cff679856.png)

# Confounding Variables
To show that headline polarity is not simply a function of COVID-19 severity I plotted COVID-19 stats from these states

![image](https://user-images.githubusercontent.com/50871836/137641304-8f4c0a7b-bd75-4274-b6d7-066630596eef.png)
![image](https://user-images.githubusercontent.com/50871836/137641361-7d98d450-67cd-484d-b432-8186dc397a50.png)


