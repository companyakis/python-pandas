import seaborn as sns

df = sns.load_dataset('planets')

print(df.head(5))

print("**************************************************************************")

print(df.method.unique())

print("**************************************************************************")

print(df.groupby("method")["orbital_period"].max())

"""
            method  number  orbital_period   mass  distance  year
0  Radial Velocity       1         269.300   7.10     77.40  2006
1  Radial Velocity       1         874.774   2.21     56.95  2008
2  Radial Velocity       1         763.000   2.60     19.84  2011
3  Radial Velocity       1         326.030  19.40    110.62  2007
4  Radial Velocity       1         516.220  10.50    119.47  2009
**************************************************************************
['Radial Velocity' 'Imaging' 'Eclipse Timing Variations' 'Transit'
 'Astrometry' 'Transit Timing Variations' 'Orbital Brightness Modulation'
 'Microlensing' 'Pulsar Timing' 'Pulsation Timing Variations']
**************************************************************************
method
Astrometry                         1016.000000
Eclipse Timing Variations         10220.000000
Imaging                          730000.000000
Microlensing                       5100.000000
Orbital Brightness Modulation         1.544929
Pulsar Timing                     36525.000000
Pulsation Timing Variations        1170.000000
Radial Velocity                   17337.500000
Transit                             331.600590
Transit Timing Variations           160.000000
Name: orbital_period, dtype: float64

"""
