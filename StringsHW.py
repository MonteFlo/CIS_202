#Define Main Function
def main():
#Call NameComp_Creator Function
    NameComp = NameComp_Creator()
    NameCompList = NameComp.split(', ')

    FullNameFormattedList = ''
    for Name in NameCompList:
         NameParts = Name.split()
         FirstName = NameParts[0]
         LastName = NameParts[1]
         FullNameFormatted = (f'{LastName}, {FirstName}; ')
         FullNameFormattedList += FullNameFormatted
    FullNameFormattedList = FullNameFormattedList.rstrip()
    FullNameFormattedList = FullNameFormattedList.rstrip(';')
    print(FullNameFormattedList)

#NameComp_Creator Suite
def NameComp_Creator():
    Name = ''
    NameComp = ''
    while Name != '0':
        Name = input('Please enter a first and last name (Type 0 to terminate): ')
        if Name != '0':
            CompFormatName = Name + ', '
            NameComp += CompFormatName
        else:    
                NameCompFormatted = NameComp.rstrip()
                NameCompFormatted = NameCompFormatted.rstrip(',')
                return NameCompFormatted

#Call Main Function
main()
