## Final project, part 1

Although Pittsburgh residents are still living through a pandemic, eviction courts have returned to business as usual. My final project will explore how eviction protections have shifted throughout the pandemic and give background on why these policies matter, including who is affected by eviction and its consequences. 

### Outline

These are the major points that I plan to hit in my story:
* The potential eviction crisis at the start of the pandemic. This section will include the impact that a wave of evictions would have had at the time (from an economic and public health perspective), as well as the harm that evictions cause all the time (displacement/loss of community, increased risk of homelessness, increased risk of job loss, etc). 
* The first eviction moratorium under the CARES Act (March 2020 to July 2020). In Pittsburgh, this was the most successful tenant protection, holding eviction filings far below historical averages.
* The second eviction moratorium issued by the CDC (September 2020 to August 2021). This was less successful, but still kept eviction filings below historical averages. It was eventually struck down by the Supreme Court. 
* The situation now. Despite high Covid transmission, tenants have extremely limited protections. 
* The potential to extend better tenants protections, pandemic or not. This section will include potential policies, like mediation, as well as things that people at risk for eviction or their neighbors can do to prevent it. 

![IMG_0305](https://user-images.githubusercontent.com/71148016/153790469-e5e9741a-2a15-460d-867d-b5994e0dc1fe.jpg)

### Initial sketches

* Shifting tenant protection coverage over time:

![image](https://user-images.githubusercontent.com/71148016/153790746-7ff6de3f-b049-411f-9cb3-38ba5502c32c.png)
![image](https://user-images.githubusercontent.com/71148016/153791007-cae7b618-6fd9-41f7-b17f-bc66b00ccdfa.png)
![image](https://user-images.githubusercontent.com/71148016/153791049-935a361b-1b04-4b25-a543-bc0d074536d8.png)

The viewer would scroll to see how eviction protections have become less prevalent in the US since the beginning of the pandemic. I'm envisioning an animated map that has protected cities or states fade in and out over time. 

The sketches above were made using [this image](https://www.flickr.com/photos/donkeyhotey/24247764924) from Flickr. 

* Visualizations of the incidence and effects of eviction:

![image](https://user-images.githubusercontent.com/71148016/153791158-4ad4360c-4836-403e-b1f9-7654e4514c9e.png)

For instance, three out of ten people who are evicted will experience homelessness at some point in the next year. 

The sketch above was made using [this image](https://www.clker.com/clipart-7-out-of-10-stickman.html) from Clker. 

* Visualizations of eviction filings in Pittsburgh, pandemic period vs. historical data:

![IMG_0306](https://user-images.githubusercontent.com/71148016/153790494-2f72a8e5-bd97-4b15-ad21-caefad18802e.jpg)

### The data 

Most of the data that I will need for this project is available through Princeton's [Eviction Lab](https://evictionlab.org/). The Lab has national data on the number of eviction filings since the beginning of the pandemic as well as filing data broken out by city (including [Pittsburgh](https://evictionlab.org/eviction-tracking/pittsburgh-pa/)). There is also a list of [local tenant protections](https://evictionlab.org/covid-eviction-policies/), which shows the current protections in place across the US. Unfortunately, there is no historical data provided; however, I may be able to scrape archived versions of the webpage using the [Wayback Machine API](https://archive.org/help/wayback_api.php).

### Method and medium

I plan to experiment with [MapBox](https://www.mapbox.com/) and [Shorthand](https://shorthand.com/) to create my story. My preference is to use MapBox to create a similar visualization to this MIT Senseable City Lab [visualization](https://senseable.mit.edu/singapore-calling/) about segregation in Singapore. Their story combines maps with other types of visualizations, which show changes in the data over time as the viewer scrolls. I think it would be powerful to include a national map of tenant protections to show how coverage has deteriorated over time, from the federal CARES Act moratorium to now. However, this will only be possible if I'm able to scrape the historical data. 

If obtaining national policy data is too challenging, I may switch over to Shorthand. This seems like a good tool to present static visualizations that don't require MapBox's capacity for animations.

Click [here](https://emmayeager.github.io/DataVisPortfolio/) to return to my portfolio.
