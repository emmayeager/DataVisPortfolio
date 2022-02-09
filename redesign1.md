## Redesign #1

For our redesign assignment, I chose to focus on a visualization related to affordable housing in Maryland. I found a [fact sheet](https://reports.nlihc.org/oor/maryland) from the National Low Income Housing Coalition that seemed like a good candidate. The fact sheet is rich in details about affordable housing, including its definition and data to show how affordability varies by income group and geography. While informative, this is also somewhat overwhelming, especially since redundant sections and confusing color choices pull attention away from the main points. I decided to start with redesigning the bar chart at the bottom right of the sheet.

![image](https://user-images.githubusercontent.com/71148016/153117931-eee5817c-22f9-4ff9-8751-808b9130dfd7.png)

The bar chart compares the rents that Marylanders in different income groups can afford against the estimated rents for one- and two-bedroom apartments. 

### Critique

The first thing I noticed about this plot was the lack of title and axis labels. Without these, I had to do some digging to figure out the intended message. The next thing I noticed was the colors: most bars are navy blue, but the two at the top stand out with a light blue fill and orange data labels. Using bright colors to draw the eye to these two upper bars was effective, since separating them from the rest of the data implies that they are benchmarks to compare the other bars against. Still, it's not clear why we have extra color in the labels. And I had to read the graph thoroughly before realizing the message behind this structure.

After writing down these intial thoughts, I dug into the visualization more with Stephen Few's framework for data visualization critiques. This method examines usefulness, completeness, perceptibility, truthfulness, intuitiveness, and aesthetics:

#### Usefulness
The chart makes an important point: lots of Maryland residents cannot afford housing. Some of the data reported here may be more useful to certain audiences than others. For instance, anyone can interpret the bar for minimum wage earners, but what does it mean to earn 30 percent of the area median income? The area median income bar also raises questions. Does the fact that median income earners can easily afford apartments while the average renter cannot imply an income inequality problem? The data visualization does not provide enough context for the non-expert to draw useful conclusions on these points. 

#### Completeness
Crucially, the chart is missing a title. This is a missed opportunity to add context to the data being presented. In addition, we're missing some background on the information in the chart. How did the chart creator define affordable? This question is answered elsewhere on the fact sheet, but might be lost when focusing only on the chart. 

#### Perceptibility
This is the area where the chart struggles the most. The takeaway is not immediately clear. Instead, we need to spend a lot of time analyzing the chart before the message becomes clear. 

#### Truthfulness
Overall, the chart is not misleading. The eventual takeaway that many renters cannot afford housing is supported by the rest of the fact sheet. However, I could see the lack of background on how the estimates were calculated causing incorrect inferences about Maryland renters -- for instance, someone might conclude that the average renter is missing payments due to the gap between what they can afford and average rents, when really they may be working extra hours or foregoing saving -- but this seems like too much explanation to include in a visualization. 

#### Intuitiveness
The chart is not intuitive. We're missing the title and axis labels, some of the most important cues to understanding a chart. And the use of color is distracting. 

#### Aesthetics
While the appearance is clean and simple, the chart is not particularly aesthetically pleasing. There's a lot of small text and the colors are fighting for attention. 

#### Engagement
Because it's unclear, the chart will only work for an engaged viewer who is invested in figuring out what to conclude about affordable housing in Maryland. It is too confusing to be engaging to a less interested viewer. 

### Wireframing and Testing

Based on my critique, I wireframed three potential redesigns of the housing affordability visualization using [Infogram](https://infogram.com/). Feedback from two interviewees is included with the questions below each wireframe. The number in parentheses at the end of a comment indicates the number of times I received each comment (1 if only one person mentioned it, 2 if both did).

#### Wireframe 1

<div class="infogram-embed" data-id="49efcf68-d963-4d31-9cd5-2f052483d0bd" data-type="interactive" data-title="Bar Chart"></div><script>!function(e,i,n,s){var t="InfogramEmbeds",d=e.getElementsByTagName("script")[0];if(window[t]&&window[t].initialized)window[t].process&&window[t].process();else if(!e.getElementById(n)){var o=e.createElement("script");o.async=1,o.id=n,o.src="https://e.infogram.com/js/dist/embed-loader-min.js",d.parentNode.insertBefore(o,d)}}(document,0,"infogram-async");</script><div style="padding:8px 0;font-family:Arial!important;font-size:13px!important;line-height:15px!important;text-align:center;border-top:1px solid #dadada;margin:0 30px"><a href="https://infogram.com/49efcf68-d963-4d31-9cd5-2f052483d0bd" style="color:#989898!important;text-decoration:none!important;" target="_blank">Bar Chart</a><br><a href="https://infogram.com" style="color:#989898!important;text-decoration:none!important;" target="_blank" rel="nofollow">Infogram</a></div>

For the first iteration, I didn't stray far from the original design. I added a descriptive title and axis label. Instead of highlighting the bars with one- and two-bedroom rents, I included them as annotations to make the comparison between estimated rent and affordable rent for each group more natural. I picked muted colors for the bars and made the benchmarks pop with bright red and orange annotations. 

##### What do you think this is? Can you describe what this is telling you?
* It's a bar chart (1)
* It's showing income for different groups (1)
* It's showing the the cost of different types of apartments (1)
* The vast majority of people can't afford apartments in Maryland (2)

##### Is there anything you find surprising or confusing?
* What is FMR? (2)
* It's surprising that the mean renter can't afford a one-bedroom (2)
* The one-bedroom and two-bedroom costs are really similar (1)
* What are the numbers in the bars? (1)

##### Who do you think is the intended audience for this?
* Policymakers (1)
* General public (2)
* Developers (1)

##### Is there anything you would change or do differently?
* Include what it means to make 30 percent of AMI (1)
* Define FMR (1)

#### Wireframe 2

<div class="infogram-embed" data-id="8d4cf1fb-6ab7-4fb2-9604-08c7b0072623" data-type="interactive" data-title="Grouped Chart"></div><script>!function(e,i,n,s){var t="InfogramEmbeds",d=e.getElementsByTagName("script")[0];if(window[t]&&window[t].initialized)window[t].process&&window[t].process();else if(!e.getElementById(n)){var o=e.createElement("script");o.async=1,o.id=n,o.src="https://e.infogram.com/js/dist/embed-loader-min.js",d.parentNode.insertBefore(o,d)}}(document,0,"infogram-async");</script><div style="padding:8px 0;font-family:Arial!important;font-size:13px!important;line-height:15px!important;text-align:center;border-top:1px solid #dadada;margin:0 30px"><a href="https://infogram.com/8d4cf1fb-6ab7-4fb2-9604-08c7b0072623" style="color:#989898!important;text-decoration:none!important;" target="_blank">Grouped Chart</a><br><a href="https://infogram.com" style="color:#989898!important;text-decoration:none!important;" target="_blank" rel="nofollow">Infogram</a></div>

For the second iteration, I switched the reported measure to the hours of work needed to afford each type of apartment for different income groups. I focused on just two groups: minimum wage earners and the average renter. I wanted to try framing the data in terms of hours worked because I thought it might help the viewer understand the trade-offs needed for Maryland renters to live in "unaffordable" homes. Focusing on the hours worked made it hard to include the fixed-income SSI group, so they are omitted here. In addition, I thought the reasons for including the area median income and 30 percent of area median income groups were unclear, so they are omitted as well.

This iterations uses a similar title and color palette.

##### What do you think this is? Can you describe what this is telling you?
* The number of hours each income group would have to work to afford each type of apartment (2)

##### Is there anything you find surprising or confusing?
* What does the red line mean? (1)
* How many hours can someone work in a week? Are the big numbers possible? (1)

##### Who do you think is the intended audience for this?
* Same as wireframe 1 (2)

##### Is there anything you would change or do differently?
* Make the 40 hour label stand out more so the red line makes sense (1)
* Include the average prices for each type of apartment (1)

#### Wireframe 3

<div class="infogram-embed" data-id="59b73e75-76f4-4556-8b2c-ec4801b56d1d" data-type="interactive" data-title="Copy: Grouped Chart"></div><script>!function(e,i,n,s){var t="InfogramEmbeds",d=e.getElementsByTagName("script")[0];if(window[t]&&window[t].initialized)window[t].process&&window[t].process();else if(!e.getElementById(n)){var o=e.createElement("script");o.async=1,o.id=n,o.src="https://e.infogram.com/js/dist/embed-loader-min.js",d.parentNode.insertBefore(o,d)}}(document,0,"infogram-async");</script><div style="padding:8px 0;font-family:Arial!important;font-size:13px!important;line-height:15px!important;text-align:center;border-top:1px solid #dadada;margin:0 30px"><a href="https://infogram.com/59b73e75-76f4-4556-8b2c-ec4801b56d1d" style="color:#989898!important;text-decoration:none!important;" target="_blank">Copy: Grouped Chart</a><br><a href="https://infogram.com" style="color:#989898!important;text-decoration:none!important;" target="_blank" rel="nofollow">Infogram</a></div>

Finally, I reframed the presentation of the data again, this time focusing on how much income residents in each group would have to set aside to afford rent for each type of apartment. This framing is useful because it makes it possible to compare the data against the definition of a housing cost burdened household, which spends more than 30 percent of its income on housing. This iteration focuses on the same income groups as wireframe 2, for similar reasons. The title and color palette are similar to previous iterations. 

##### What do you think this is? Can you describe what this is telling you?
* Showing how much of income is allocated to rent in each category of apartment (2)
* Comparing to "arbitrary" 30 percent benchmark (1)
* Showing that minimum wage earners can't afford rent (1)

##### Is there anything you find surprising or confusing?
* What does the red line mean? (1)

##### Who do you think is the intended audience for this?
* Same as wireframe 1 (2)

##### Is there anything you would change or do differently?
* Add the minimum wage (1)
* Make the title shorter (1)

### Testing

Detailed feedback from the testing stage is included above. Overall, respondents liked the aesthetics of the graphs but had questions about background information such as specifics on wages, average rents, and the definition of affordability. The format of the annotations also caused some confusion.

At the end of each feedback session, I asked the interviewee which wireframe they liked best. Both interviewees chose wireframe #2, which frames the data in terms of hours of worked needed to afford rent. The first interviewee preferred this graph because they thought it was the most intuitive for a non-subject matter expert. They pointed out that the 30 percent benchmark used as the comparison point in wireframe 3 was a less well-known measure than the 40-hour work week. The second interviewee preferred the hours graph because they thought it was striking to imagine someone working that many hours to afford a home. 

Given this feedback, I decided to rework wireframe #2 for my final visualization. My interviewees were often confused by the annotations pointing out the 40-hour work week or the 30 percent benchmark, so I planned to make the significance of these lines clearer in my final version. In addition, one interviewee had a question about the significance of the data labels inside the bars, so I decided to rework these too. I considered adding information about the Maryland minimum wage and the average rent for different categories of apartments but ultimately decided to omit these to avoid cluttering the graph. 

### Solution

I built my final version of the visualization in [Flourish](https://flourish.studio/). 

<div class="flourish-embed flourish-chart" data-src="visualisation/8648849"><script src="https://public.flourish.studio/resources/embed.js"></script></div>

This version of the chart includes a "full-time" label on the benchmark comparison line to explain why this annotation is included to viewers. The "full-time" text connects to the subtitle and should prompt readers to compare the line against the length of the bars. I moved the data labels to the end of the bars to make it more intuitive that they represent each bar's length. Finally, I swapped the colors of the bars in order to add color coding to the subtitle and remove the legend. This makes the chart less cluttered and lets the reader spend more time focusing on the title and data. 

It is worth noting that my reworked visualization presents slightly different data than the original chart and therefore may have a different audience. My solution pulls out the easiest data for a non-expert to understand (affordability for minimum wage earners and average renters) and frames it in a visceral, easily-interpretable way (the number of hours of work needed to afford rent). I think this would appeal more to people who were not previously engaged with the subject matter. Experts, on the other hand, might prefer the original graph. For instance, data on affordability for people who make 30 percent of the area median income may be an important benchmark for policymakers that would be missed in the reworked version. 

Click [here](https://emmayeager.github.io/DataVisPortfolio/) to return to my Portfolio.
