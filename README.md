# Habitable Zone Calculator
This Python 3.X script calculates both the AU (distance) region boundaries (of Recent Venus, Runaway Greenhouse, Maximum Greenhouse, and Early Mars), along with the S<sub>eff</sub> value for these regions. 

Additionally, any object of an AU distance can be calculated to see if it's in one of these zones, or if it's outside (if it is outside, you'll be told if it's beyond Recent Venus or Early Mars). 


## How are the calculations made?
The calculations are made using [Kopparapu et al. 2014](https://ui.adsabs.harvard.edu/abs/2014ApJ...787L..29K/abstract)'s paper. The comments in the code line up with the arXiv version of the paper.

NOTE: The only exception of this is the flux calculation, which is a simplified version (mathematically equal since this is simplified because it ONLY uses IAU units, not SI) from [NASA's Exoplanet Archive Isolation Flux formula](https://exoplanetarchive.ipac.caltech.edu/docs/poet_calculations.html).