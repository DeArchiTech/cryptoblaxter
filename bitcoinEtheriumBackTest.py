#1 Load in historical Bitcoin Price to Time data
#2 Load in historical Ehterium Price to Time data
#3 Run Bitcoin Price as input, and excute algorithm to figure out should we buy or not buy

#4 algorithm
#- TO determing if we want to buy etherium in Time X, we check I at X -t and I(x-t) is computed by
#5 Formulae to compute I(x-t)

#Notes

# FIRST FIT

#1)First compute the I For the current day
#2)If we havn't bought anything
#2i)Let I = the total dy/dx for the past (N days)
#2ii)If I is > A , than we buy
#2iii)Minus the buying price from the total sum of Cash Equity
#3)Else Compute dy/dx for the following days
#3i)If dy/dx is <B, than we sell
#3ii)Add the sold price to the total sum of cash Equity
#4)We compute the Sold Price minus the Buying Price = Transcaction Value
#4i)Add the Transcation value to the total Sum of Cash Equity
#4ii)Save the Transcation Value somewhere for further analysis

# Second FIT

#1)For all the given T, compute the save dy/dx Sum but for Bitcoin Data
#2)Figure out the inflection points and point them on a graph

# Third FIT
#1)Perform a least squares fit on the Bitcoin and Ehterium Data
#2)Now compute the avg deviation from the fitted line with the Sample Data and
#2i)Figure out what is the Ampitute of the graph
#2ii)If we are on a deivation of ampitute away, we buy,
#2iii)Else if we are a deviation of amplitute away, we sell

# Fourth FIT, if we sum First Fit and Second Fit together, than we can summarizes that
# My Algorithm, computes the Is for the bitcoin, and will automatically buy if the coin
# Fits a certain shape, which is the J looking shape, and we buy at the hook

# Algorithm,
# For Bitcoin, I need to calculate inflection point and specficially bottom infection point, buy and hold
# For Etherium, I need to excute trades to earn money through transcations from going bottom to top
