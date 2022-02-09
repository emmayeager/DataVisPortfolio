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

### Wireframing

Based on my critique, I wireframed three potential redesigns of the housing affordability visualization.

#### Wireframe 1

<div class="infogram-embed" data-id="49efcf68-d963-4d31-9cd5-2f052483d0bd" data-type="interactive" data-title="Bar Chart"></div><script>!function(e,i,n,s){var t="InfogramEmbeds",d=e.getElementsByTagName("script")[0];if(window[t]&&window[t].initialized)window[t].process&&window[t].process();else if(!e.getElementById(n)){var o=e.createElement("script");o.async=1,o.id=n,o.src="https://e.infogram.com/js/dist/embed-loader-min.js",d.parentNode.insertBefore(o,d)}}(document,0,"infogram-async");</script><div style="padding:8px 0;font-family:Arial!important;font-size:13px!important;line-height:15px!important;text-align:center;border-top:1px solid #dadada;margin:0 30px"><a href="https://infogram.com/49efcf68-d963-4d31-9cd5-2f052483d0bd" style="color:#989898!important;text-decoration:none!important;" target="_blank">Bar Chart</a><br><a href="https://infogram.com" style="color:#989898!important;text-decoration:none!important;" target="_blank" rel="nofollow">Infogram</a></div>







