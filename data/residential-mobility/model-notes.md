
# TOD residential mobility prediction modelling

## Summary

Use historical residential mobility data (from LAD) and residential built environment data (from census) to predict and present the following for TOD scenarios.

- If a scenario of development happens, estimate the total and percent of out-movers, by income status (i.e. for low- and not low-income residents). 

- Compare moving probabilities by low- and non-low income movers within the transit station area (e.g. are low-income residents more likely to move away, if so by how much)

- Compare moving rates of the station area to overall predicted moving rates for the same time period (e.g. are moving rates higher near the station?)

Overall analysis steps.

1) Create global propensity to move model to predict overall moving rates by income group. 

2) Create TOD-focused propensity to move model to predict moving rates with inputs of residential development before and after station opens

3) Use individual models to simulate and predict average moving rates


## Global propensity to move model (Model 1)

Data are tax-filers in Canadian CMAs with major transit (metro or LRT) who appear in the sample in subsequent pairs of years ($t=0$ and $t=1$). Larger sample the better, but there might be limitations on RDC computing. If so, take random samples of LAD.

$P_{i,t=0,t=1} = \beta_I X_{I,i,t=0} + \beta_{LI} X_{LI,i, t=0} + \beta_{y} X_{y,i,t=0} + \epsilon$

- $P_{i,t=0,t=1}$ whether or not someone moves away from their census tract between year $t=0$ and $t=1$

- $\beta_I X_{I,i,t=0}$ individual and household effects (age, gender, household size, period of immigrant, employment status, etc.) at $t=0$

- $\beta_{LI} X_{LI,i, t=0}$ whether or not individual is Low Income (0 or 1) at $t=0$

- $\beta_{Y} X_{Y,i,t=0}$ non-linear function of the year (to account for how moving rates have changed over time). Try polynomial to start?

- Potentially add interaction of low-income status and the year


## Propensity to move based on transit development model (Model 2)

Data are only tax-filers who live near a transit station between period $t=A$ and $t=B$ where $A - B$ is a 10 year window of census years (e.g. 1996-2006, 2011-2021, etc.) best centred around when the transit station opened. For example if the station opened in 2017, then use then $A=2011$ and $B=2021$.

$P_{i,t=0,t=1} = \beta_I X_{I,i,t=0} + \beta_{LI} X_{LI,i, t=0} + \beta_{y} X_{y,i,t=0} + \beta_{T} X_{T,i,t=0} + \beta_{D,t=A} X_{D,c,t=A} + \beta_{D,t=B} X_{D,c,t=A} + \epsilon$

- $P_{i,t=0,t=1}$ whether or not someone moves away from their census tract between year $t=0$ and $t=1$

- $\beta_I X_{I,i,t=0}$ individual and household effects (age, gender, household size, period of immigrant, employment status, etc.) at $t=0$

- $\beta_{LI} X_{LI,i, t=0}$ whether or not individual is Low Income (0 or 1) at $t=0$

- $\beta_{Y} X_{Y,i,t=0}$ non-linear function of the year (to account for how moving rates have changed over time). Try polynomial to start?

- Potentially add interaction of low-income status and the year

- $\beta_{D,t=A} X_{D,c,t=A}$ dwelling characteristics for the individual's census tract, $c$, at $t=A$ (number of dwellings, % rent, average number of bedrooms, % of dwellings by type e.g. apartment, single detached, etc.)

- $\beta_{D,t=B} X_{D,c,t=A}$ dwelling characteristics for the individual's  census tract, $c$, at $t=B$ (number of dwellings, % rent, average number of bedrooms, % of dwellings by type e.g. apartment, single detached, etc.)


## Prediction via simulation

We can export the parameters of these two models from the RDC. 

Then for any case study station, we would Monte Carlo simulate both models to return the following:

1. Probability of low-income residents moving overall (Model 1)

2. Probability of non-low-income residents moving overall (Model 1)

3. Probability of low-income residents moving from the station area (Model 2). Include current and future scenario dwelling characteristics.

4. Probability of non-low income residents moving from the station area (Model 2). Include current and future scenario dwelling characteristics.

The individual pieces of the model (e.g. age, gender, household size, etc.) would be sampled probabilistically from census data.

With the result of these probabilities, we could then have two key results

- Comparison of probability to move in station areas relative to overall (e.g. comparing 1. to 3.)

- Multiply probability in 1. and 2. to the population characteristics at $t=A$ (likely 2021) to estimate total number of out-movers by income status.


## Open questions

- Should we include random effects for census tract? there are likely to be local variations we are not capturing

- I would like to add a categorical variable for region/city/province, but that then limits the model being usable in areas that have not had a transit station open during this historical time period. I'm not sure how to account for this in these cases (e.g. applying to Waterloo ION when the region never had LRT before).

- I'm wondering if it would be possible to instead of having two models, combine into a single multi-level model where the dwelling change data is a sub below the 1,0 of if near transit.

- Should probably generate both models on subset of the data and test on the remaining sample?

- Will need new model for in-movers.


## Other ideas

- Markov Chain / Agent Based residential sorting model to simulate moving within a region based on neighbourhood and individual effects. Would be much more complicated I think.