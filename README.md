# Smart-Library-System
IOT Project

1. Augment your implementation of alhabetaMinMax by making it explore only most promising states according to their H0 “static” evaluation for computing their HL value.

- Experiment and report results observed when compared to the original alhabetaMinMax



2. Generalize a bit by making it compute HL according by exploring only most promising states according to their Hl evaluation, 0<l<L

-Experiment and report results observed for different choiches of l. Try to look for an optimal l whe L=10 (or maybe more …)



3. Define your H0 as a function f(h1,…,hn) where hi are “observations ”on the state.

Import a regressor R and train it for predicting HL (s) given static h1(s),…,hn (s) by making the agent play…

Modify your previous implemenation by making it use the R predictions instead of static evaluations.

- Experiment and report comparative results with respect to previous alhabetaMinMax versions.
