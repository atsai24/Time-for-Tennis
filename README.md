# Exploring Serve Times of Tennis Players Under Pressure

<div class='header'> 
<!-- Your header image here -->
<div class='headingImage' id='mainHeaderImage' align="center">
    <img src="https://images.squarespace-cdn.com/content/v1/574ef19d9f7266ca965ea6af/1539723422154-QOZZR64KFEB7OMRC4JYS/ke17ZwdGBToddI8pDm48kKwk6pp6QGEAwGcw_vnYdmoUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYy7Mythp_T-mtop-vrsUOmeInPi9iDjx9w8K4ZfjXt2do8UP1IH5v8D6j72WcX-bDb10lwfWZJ2VkUT5sYler58P7cJNZlDXbgJNE9ef52e8w/20180418_120534.jpg?format=2500w" ></img>
</div>

## Sections:
 |  **[Introduction](#introduction)**  |
 **[Data](#data)**  |
 **[Main Hypothesis](#main-hypothesis)**  |
 **[Exploration](#exploration)**  |
 **[Statistical Analysis](#statistical-analysis)**  |
 **[Results](#results)**  |
 **[Future](#future)**  |<br><br>
 |  **[Takeaways](#takeaways)**  |
 **[Shoutouts](#shoutouts)**  |
 
 ---
 ## Introduction
 Singles tennis is a greuling, tiring, and highly intense form of competition. Due to the nature of the 1 vs. 1, there is no delegating or relying on teammates. Every serve, point, and hit relies entirely upon the individual player's performance, thus it is natural for players to take time between points to gather and ready themselves for the next serve. However, not every point is created equal; some points effect the game more than others. According to all-time great athlete LeBron James, "Two points is not two points. I'll explain it to you later." What did he mean by that? I'll explain it to you later.
 
In this analysis, I attempt to quantify some of the psychological factors of Tennis, by exploring a dateset of measured times after the end of a point and before the next serve in the 2015 French Open. 
 
 ## Data
 The Data was collected by Carl Bialik from FiveThirtyEight for his [analysis](https://fivethirtyeight.com/features/why-some-tennis-matches-take-forever/) of why some tennis matches take so long. Using a stopwatch, he measured the time it took for 15 players to serve in the 2015 French Open.
 
 Original Dataset:
 
  <img src="https://github.com/atsai24/Time-for-Tennis/blob/master/images/original_data.png" width="774" height="200">

 
 
 Thankfully, the data was only 7 columns and relatively clean, and the datatypes for useful columns were already ideal. My next step was to filter out columns I knew I would not be using.
 
 Filtered Dataset:
 
 <img src="https://github.com/atsai24/Time-for-Tennis/blob/master/images/filtered_data.png" width="562" height="200">
 
 ## Main Hypothesis
  What I think LeBron was trying to say is that every point shows up the same on the scoreboard, but that doesn't mean they have the same impact on the outcome of the game. A vicous dunk can rile a crowd, demoralize the opposition, and swing momentum for your team, the same way winning an intense 20 hit rally, or losing a set point on an ace can have similar effects in tennis. Thus, one would think that tennis players would give themselves more time to prepare before serving on points that matter more, like game-points or set-points.

Hypothesis: Tennis players will take more time to serve before High-Pressure points when compared to Not-High-Pressure points.

## Exploration
My First step was to determine what constitutes a High-Pressure point. I decided on any point where one player has the potential to win or lose the game on that point. In other words, any time the score included "40", "Ad-in", or "Ad-out".

<details>
  <summary>
    Show Graphs
  </summary>
<br>
    
<img src="https://github.com/atsai24/Time-for-Tennis/blob/master/images/hist_of_serve_times.png" width="432" height="288">
<img src="https://github.com/atsai24/Time-for-Tennis/blob/master/images/hist_of_hp_serve_times.png">
 <img src="https://github.com/atsai24/Time-for-Tennis/blob/master/images/hist_of_not_hp_serve_times.png">
<img src="https://github.com/atsai24/Time-for-Tennis/blob/master/images/density_comparison.png" width="432" height="288">
<img src="https://github.com/atsai24/Time-for-Tennis/blob/master/images/score_comparison.png">
</details> 

## Statistical Analysis

- Null Hypothesis: There is no difference in serve times for High-Pressure and Not-High-Pressure points (sample mean = 19.54)

- Alternative Hypothesis: The serve times for High-Pressure points is greater than those for Not-High-Pressure points (sample mean > 19.54)

- &alpha; = 0.05

- Run a z-test comparing the sample mean of High-Pressure points to the distribution of sample means for Not-High-Pressure points

First, I had to create a distribution of sample means for Not-High-Pressure points. I did this in 2 ways:

1. Fit the original data on Not-High-Pressure points to a skewed distribution, then collect the means of 1000 samples (size = 63) from the distribution.
2. The much easier way was to calculate the standard error from the Not-High-Pressure data and create a normal distribution using the original sample mean and standard error.

<img src="https://github.com/atsai24/Time-for-Tennis/blob/master/images/dist_of_sample_means_not_hp.png">

## Results
From here I was able to calculate the p-value of the High-Pressure Sample Mean (21.263). To be thorough, I calculated this value for both of the sample mean distributions I created.

- p<sub>dist from skew</sub> = 0.01970741415094779

- p<sub>dist from err</sub> = 0.023405181719318935

I wanted to go a bit deeper and find additional factors for the increase in time taken before High-Pressure Points. I split the High-Pressure Data into 2 categories:

1. About to Win: [40-0, 40-15, 40-30, Ad-in]

    - p<sub>dist from skew</sub> = 0.432394115132284

    - p<sub>dist from  err</sub> = 0.45560172546205957
    
2. About to Lose: [0-40, 15-40, 30-40, Ad-out]

    - p<sub>dist from skew</sub> = 0.00000159681100575

    - p<sub>dist from  err</sub> = 0.00000245979901891

<img src="https://github.com/atsai24/Time-for-Tennis/blob/master/images/p_val_region.png" width="1600" height="400">

                                                                                                           
                                                                                                              
