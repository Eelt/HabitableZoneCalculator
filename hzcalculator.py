#!/usr/bin/env python3

# This python script is WRITTEN FROM SCRATCH using the equations and data from https://arxiv.org/pdf/1404.5292.pdf (DOI: 10.1088/2041-8205/787/2/L29 arXiv:1404.5292 Bibcode:  2014ApJ...787L..29K)
# The purpose of this script is to determine the HZ, both Conservative and Optimistic, as accurately as possible using the formulas and table data from Kopparapu et al. 2014
# and to determine if an object (presumably a planet) is within either habitable zones, or not.

# Adapted from NASA Exoplanet Archive Insolation Flux formula. (https://exoplanetarchive.ipac.caltech.edu/docs/poet_calculations.html)
def flux(l,semi): 
    return ((1 / semi)**2)*l # Reciprical of the Semi-Major axis, squared, then multiplied by the Luminosity in Lsun

# From Kopparapu et al. 2014. Equation 5, Section 3.1, Page 9
def auFromSeff(l, seff):
    return (l / seff)**0.5 # luminosity divided by the Seff, to the power of a half

# Values from Kopparapu et al. 2014. Table 1, Page 12
def getSeffBoundry(temp,zone):
    tS = temp - 5780 # Temperature delta
    #Adapted Formula: Seff = SeffSUN + a*tS + b*tS^2 + c*tS^3 + d*tS^4
    
    # Recent Venus 1 Me
    if (zone == "recentVenus" or zone == "rv"):
        SeffSUN = 1.766
        a = 2.136*(10**-4)
        b = 2.533*(10**-8)
        c = -1.332*(10**-11)
        d = -3.097*(10**-15)

        return Kopparapu2014(SeffSUN,a,b,c,d,tS)

    # Runnaway Greenhouse 1 Me
    if (zone == "runnawayGreenhouse" or zone == "rg"):
        SeffSUN = 1.107
        a = 1.332*(10**-4)
        b = 1.580*(10**-8)
        c = -8.308*(10**-12)
        d = -1.931*(10**-15)

        return Kopparapu2014(SeffSUN,a,b,c,d,tS)

    # Maximum Greenhouse 1 Me
    if (zone == "maximumGreenhouse" or zone == "mg"):
        SeffSUN = 0.356
        a = 6.171*(10**-5)
        b = 1.689*(10**-9)
        c = -3.198*(10**-12)
        d = -5.575*(10**-16)

        return Kopparapu2014(SeffSUN,a,b,c,d,tS)

    # Early Mars 1 Me
    if (zone == "earlyMars" or zone == "em"):
        SeffSUN = 0.320
        a = 5.547*(10**-5)
        b = 1.526*(10**-9)
        c = -2.874*(10**-12)
        d = -5.011*(10**-16)

        return Kopparapu2014(SeffSUN,a,b,c,d,tS)

    
# From Kopparapu et al. 2014. Equation 4, Section 3.1, Page 9
def Kopparapu2014(SeffSUN, a, b, c, d, tS):
    return SeffSUN + a*tS + b*((tS)**2) + c*((tS)**3) + d*((tS)**4)

def init():
    luminosity=float(input("Please enter the star's luminosity (Lsun)\n"))
    semimajor=float(input("Please enter the object's semi-major axis (AU)\n"))
    starTemp=int(input("Please enter the star's temperature (K)\n"))
    a=flux(luminosity,semimajor)

    print("This object's Seff: " + str(a))

    recentVenus = getSeffBoundry(starTemp,"rv")
    runnawayGreenhouse = getSeffBoundry(starTemp,"rg")
    maximumGreenhouse = getSeffBoundry(starTemp,"mg")
    earlyMars = getSeffBoundry(starTemp,"em")

    print ("\n*** This systems HZ stats: ***")

    print ("\n DISTANCES IN AU\n")

    print("Recent Venus (1 Me): " + str(auFromSeff(luminosity,recentVenus)))
    print("Runnaway Greenhouse (1 Me): " + str(auFromSeff(luminosity,runnawayGreenhouse)))
    print("Maximum Greenhouse (1 Me): " + str(auFromSeff(luminosity,maximumGreenhouse)))
    print("Early Mars (1 Me): " + str(auFromSeff(luminosity,earlyMars)))

    print("\n STELLAR FLUX (EFFECTIVE) \n")

    print("Recent Venus (1 Me): " + str(recentVenus))
    print("Runnaway Greenhouse (1 Me): " + str(runnawayGreenhouse))
    print("Maximum Greenhouse (1 Me): " + str(maximumGreenhouse))
    print("Early Mars (1 Me): " + str(earlyMars))

    print(" \n")
    if (a < earlyMars):
        print("This object is NOT in the Habitable Zone (Beyond Early Mars)")
    elif (a <= maximumGreenhouse and a >= earlyMars):
        print("This object is in the Optimistic Habitable Zone (Early Mars)")
    elif (a <= runnawayGreenhouse and a >= maximumGreenhouse):
        print ("This object is in the Conservative Habitable Zone (Between Runnaway Greenhouse and Maximum Greenhouse)")
    elif (a <= recentVenus and a >= runnawayGreenhouse):
        print ("This object is in the Optimistic Habitable Zone (Between Recent Venus and Runnaway Greenhouse)")

init()