# event-generation
This repository contains the event generation code

## Setup
Run `./install.sh`.
On future terminal sessions, source `setup.sh`.

## Generation
Run `generateEvents.sh` (see file for details). Events will be saved in the madgraph directory. The `.root` file will contain the Delphes output.


### Madgraph Syntax
NP<=X and NP=X (where NP is some new physics operator) sets the new physics order to <= X at the amplitude level (i.e., allows at most X new physics vertices in the feynman diagrams). NP==X is the same, but sets the order to exactly X, i.e., requires exactly X new physics vertices. NP^2 is as above, but is at the cross-section, i.e., amplitude squared, level.

To get only the quadratic term at the cross-section level, we can either set NP^2==2 or NP==1. However, to get the interference term 2 Re(SM* NP), we need to set NP^2==1. In fact, this is why this NP^2 syntax was added to madgraph. To get INT+QUAD, we can add two processes: one with NP^2==1 (INT) and one with NP^2==2 or NP==1 (QUAD). Finally, to get INT+QUAD+SM, we can either set NP<=1 or NP^2<=2. 