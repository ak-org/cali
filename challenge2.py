import numpy as np 
import pandas as pd 
from scipy import stats 
import matplotlib.pyplot as plt
import math 
import statistics as st 


def getYearfromDate(d):
    return d[6:]

def getHourfromTime(t):
    if isinstance(t, str):
        if len(t) == 5: 
            return t[0:2]
        else:
            return "-1"


accidents = pd.read_csv('./Stats19_Data_2005-2014/Accidents0514.csv')
accidents['Hour'] = accidents['Time'].map(getHourfromTime)
accidents['Year'] = accidents['Date'].map(getYearfromDate)

vehicles = pd.read_csv('./Stats19_Data_2005-2014/Vehicles0514.csv')

casualties = pd.read_csv('./Stats19_Data_2005-2014/Casualties0514.csv')

combined = pd.merge(accidents, vehicles, on='Accident_Index')

combined2 = pd.merge(casualties, accidents, on='Accident_Index')

def q2a():
    urbanaccidents = accidents.ix[accidents['Urban_or_Rural_Area'] == 1]


    print('Urban Accidents  {0:.10f}'.format(
        len(urbanaccidents) / len(accidents)))

def q2b():
    accidents2005 = len(accidents.ix[accidents['Year'] == '2005'])
    accidents2006 = len(accidents.ix[accidents['Year'] == '2006'])
    accidents2007 = len(accidents.ix[accidents['Year'] == '2007'])
    accidents2008 = len(accidents.ix[accidents['Year'] == '2008'])
    accidents2009 = len(accidents.ix[accidents['Year'] == '2009'])
    accidents2010 = len(accidents.ix[accidents['Year'] == '2010'])
    accidents2011 = len(accidents.ix[accidents['Year'] == '2011'])
    accidents2012 = len(accidents.ix[accidents['Year'] == '2012'])
    accidents2013 = len(accidents.ix[accidents['Year'] == '2013'])
    accidents2014 = len(accidents.ix[accidents['Year'] == '2014'])
    accidents2015 = len(accidents.ix[accidents['Year'] == '2015'])

    accidentByYear = [accidents2005, accidents2006, accidents2007, 
                      accidents2008, accidents2009, accidents2010, accidents2011, 
                      accidents2012, accidents2013, accidents2014 ]
  
    YearRange = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]

    slope, intercept, r_value, p_value, std_err = stats.linregress(YearRange, accidentByYear)
    print('Slope {0:.10f}'.format(slope))


def q2c():

    accidentsinFineWeather = len(combined.ix[(combined['Weather_Conditions'] == 1) & ( (combined['Skidding_and_Overturning'] == 1) | 
                                                                                       (combined['Skidding_and_Overturning'] == 3) |
                                                                                       (combined['Skidding_and_Overturning'] == 5))])
 

    accidentsinBadWeather = len(combined.ix[ ( (combined['Weather_Conditions'] == 2) |
                                               (combined['Weather_Conditions'] == 3) |
                                               (combined['Weather_Conditions'] == 5) |
                                               (combined['Weather_Conditions'] == 6)) &
                                               ((combined['Skidding_and_Overturning'] == 1) |
                                                (combined['Skidding_and_Overturning'] == 3) |
                                                (combined['Skidding_and_Overturning'] == 5))])                                         
    print('B:F (jackknife) {0:.10f}'.format(accidentsinBadWeather / accidentsinFineWeather))

def q2d():
    local_authority_list = accidents['Local_Authority_(District)']
    unique_local_authority_list = list(set(local_authority_list))
    maxlatlongsum = 0
    for i in range(len(unique_local_authority_list)):
        listlong = accidents[accidents['Local_Authority_(District)'] == unique_local_authority_list[i]]['Longitude']
        listlat = accidents[accidents['Local_Authority_(District)'] == unique_local_authority_list[i]]['Latitude']
        listlong = sorted(listlong)
        listlat = sorted(listlat)
        sumlatlong = listlong[len(listlong) - 1] - listlong[0] + \
            listlat[len(listlat) - 1] - listlat[0]
        if (sumlatlong > maxlatlongsum):
            maxlatlongsum = sumlatlong
            largestdistrict = unique_local_authority_list[i]
            largestlong = listlong
            largestlat = listlat
   
    print('District Area {0:.10f}'.format(math.pi * st.stdev(largestlong) * st.stdev(largestlat)))

def q2e():
    
    accidentsHour00 = len(accidents.ix[accidents['Hour'] == '00'])
    accidentsHour01 = len(accidents.ix[accidents['Hour'] == '01'])
    accidentsHour02 = len(accidents.ix[accidents['Hour'] == '02'])
    accidentsHour03 = len(accidents.ix[accidents['Hour'] == '03'])
    accidentsHour04 = len(accidents.ix[accidents['Hour'] == '04'])
    accidentsHour05 = len(accidents.ix[accidents['Hour'] == '05'])
    accidentsHour06 = len(accidents.ix[accidents['Hour'] == '06'])
    accidentsHour07 = len(accidents.ix[accidents['Hour'] == '07'])
    accidentsHour08 = len(accidents.ix[accidents['Hour'] == '08'])
    accidentsHour09 = len(accidents.ix[accidents['Hour'] == '09'])
    accidentsHour10 = len(accidents.ix[accidents['Hour'] == '10'])

    accidentsHour11 = len(accidents.ix[accidents['Hour'] == '11'])
    accidentsHour12 = len(accidents.ix[accidents['Hour'] == '12'])
    accidentsHour13 = len(accidents.ix[accidents['Hour'] == '13'])
    accidentsHour14 = len(accidents.ix[accidents['Hour'] == '14'])
    accidentsHour15 = len(accidents.ix[accidents['Hour'] == '15'])
    accidentsHour16 = len(accidents.ix[accidents['Hour'] == '16'])
    accidentsHour17 = len(accidents.ix[accidents['Hour'] == '17'])
    accidentsHour18 = len(accidents.ix[accidents['Hour'] == '18'])
    accidentsHour19 = len(accidents.ix[accidents['Hour'] == '19'])
    accidentsHour20 = len(accidents.ix[accidents['Hour'] == '20'])
    accidentsHour21 = len(accidents.ix[accidents['Hour'] == '21'])
    accidentsHour22 = len(accidents.ix[accidents['Hour'] == '22'])
    accidentsHour23 = len(accidents.ix[accidents['Hour'] == '23'])
    
    accidentsbyHour = [
                       accidentsHour00, accidentsHour01,
                       accidentsHour02, accidentsHour03, 
                       accidentsHour04, accidentsHour05, 
                       accidentsHour06, accidentsHour07, 
                       accidentsHour08, accidentsHour09,
                        accidentsHour10, accidentsHour11,
                        accidentsHour12, accidentsHour13,
                        accidentsHour14, accidentsHour15,
                        accidentsHour16, accidentsHour17,
                        accidentsHour18, accidentsHour19,
                        accidentsHour20, accidentsHour21,
                        accidentsHour22, accidentsHour23,
                       ]

    maxAccidentsinHour = max(accidentsbyHour)
    peakAccidentHour = accidentsbyHour.index(max(accidentsbyHour))
    fatalAccidentsinPeakHour = len(accidents.ix[(accidents['Hour'] == '17') & (accidents['Accident_Severity'] == 1)])
    print('F:T  {0:.10f}'.format(fatalAccidentsinPeakHour / maxAccidentsinHour))

def q2f():
    
    bins = [10,20,30,40,50,60,70,80,90]
    ratio = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    accidentsat10 = len(accidents.ix[accidents['Speed_limit'] == 10])
    accidentsat20 = len(accidents.ix[accidents['Speed_limit'] == 20])
    accidentsat30 = len(accidents.ix[accidents['Speed_limit'] == 30])
    accidentsat40 = len(accidents.ix[accidents['Speed_limit'] == 40])
    accidentsat50 = len(accidents.ix[accidents['Speed_limit'] == 50])
    accidentsat60 = len(accidents.ix[accidents['Speed_limit'] == 60])
    accidentsat70 = len(accidents.ix[accidents['Speed_limit'] == 70])
    accidentsat80 = len(accidents.ix[accidents['Speed_limit'] == 80])
    accidentsat90 = len(accidents.ix[accidents['Speed_limit'] == 90])

    casualtiesat10 = 0
    casualtiesat20 = 0
    casualtiesat30 = 0
    casualtiesat40 = 0
    casualtiesat50 = 0
    casualtiesat60 = 0
    casualtiesat70 = 0
    casualtiesat80 = 0
    casualtiesat90 = 0
    for i in range(1,4):
        casualtiesat10 += len(combined2.ix[ (combined2['Speed_limit'] == 10) & 
                                            (combined2['Casualty_Class'] == i)])
        casualtiesat20 += len(combined2.ix[(combined2['Speed_limit'] == 20) &
                                        (combined2['Casualty_Class'] == i)])
        casualtiesat30 += len(combined2.ix[(combined2['Speed_limit'] == 30) &
                                        (combined2['Casualty_Class'] == i)])
        casualtiesat40 += len(combined2.ix[(combined2['Speed_limit'] == 40) &
                                        (combined2['Casualty_Class'] == i)])
        casualtiesat50 += len(combined2.ix[(combined2['Speed_limit'] == 50) &
                                        (combined2['Casualty_Class'] == i)])
        casualtiesat60 += len(combined2.ix[(combined2['Speed_limit'] == 60) &
                                        (combined2['Casualty_Class'] == i)])
        casualtiesat70 += len(combined2.ix[(combined2['Speed_limit'] == 70) &
                                        (combined2['Casualty_Class'] == i)])
        casualtiesat80 += len(combined2.ix[(combined2['Speed_limit'] == 80) &
                                        (combined2['Casualty_Class'] == i)])
        casualtiesat90 += len(combined2.ix[(combined2['Speed_limit'] == 90) &
                                        (combined2['Casualty_Class'] == i)])

    accidentsAtSpeed = [ accidentsat10,  accidentsat20, accidentsat30,
          accidentsat40, accidentsat50, accidentsat60, 
          accidentsat70, accidentsat80, accidentsat90 ]

    casualtiesAtSpeed = [casualtiesat10,  casualtiesat20, casualtiesat30,
                         casualtiesat40, casualtiesat50, casualtiesat60,
                         casualtiesat70, casualtiesat80, casualtiesat90]

    for i in range(len(casualtiesAtSpeed)):
        if (accidentsAtSpeed[i] == 0):
            ratio[i] = 0
        else:
            ratio[i] = casualtiesAtSpeed[i] / accidentsAtSpeed[i]
    #print(ratio, casualtiesAtSpeed, accidentsAtSpeed)
    a,b = stats.pearsonr(bins, ratio)
    print('P-Co {0: .10f}'.format(a, b))


def q2g():

    fatalAccidentsbyMale = len(combined.ix[(combined['Sex_of_Driver'] == 1) & (combined['Accident_Severity'] == 1)])
                                            
    fatalAccidentsbyFemale = len(combined.ix[(combined['Sex_of_Driver'] == 2) & (combined['Accident_Severity'] == 1)])

    print('M:Fratio {0: .10f}'.format(fatalAccidentsbyMale / fatalAccidentsbyFemale))


def q2h():
    accidentCountbyAge = [0 for i in range(110)]
    yearsList = list(range(110))

    for i in range(16,110):
        accidentCountbyAge[i] = len(combined.ix[combined['Age_of_Driver'] == i])

    expDecay = math.log(20631/2) / (101 - 17)  # 2/20631)
    print('Decay {0: .10f}'.format(expDecay))

      
q2a()
q2b()
q2c()
q2d()
q2e()
q2f()
q2g()
q2h()
