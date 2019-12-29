#Below is a code to that will store names and birth dates such that when any of the stored names is called,the birthdate will display
Dict=({'kelvin':'20/5/1989','john':'15/10/1975','ben':'10/8/1970'})
choose=input('whose birthdate are you searching for?')
if choose in Dict:
    print(choose + "'s" + ' birthday is ' + Dict[choose]) 
elif choose not in Dict:
    print(choose + "'s" + ' birthday is not found ')