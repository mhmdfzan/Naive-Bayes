import csv
import pandas #install pandas with command pip3 install pandas

dataTest = pandas.read_csv("Testset.csv")
dataTrain = pandas.read_csv("Trainset.csv")

def rumus(jumlah,tipeCome):
    total = jumlah/tipeCome
    return total

def naivebayes(kol1, kat1, kol2, kat2, tipeCome):
    jumlah = 0
    for i in range(len(dataTrain)):
        if (dataTrain[kol1][i] == kat1) & (dataTrain[kol2][i] == kat2):
            jumlah += 1
    hasil = rumus(jumlah,tipeCome)
    return hasil

def main():
    income=[]; age=[]; workclass=[]; education=[]; status=[]; occupation=[]; relationship=[]; hours=[] #array for TebakanTugas1ML.csv
    row = len(dataTrain) #for get length of row in data train
    lebih = 0; kurang = 0
    i=0; j=0; x=0

    for i in range(len(dataTrain)):
        if (dataTrain['income'][i]=='>50K'):
            lebih += 1
        elif (dataTrain['income'][i]=='<=50K'):
            kurang += 1

    More = lebih/row; Less = kurang/row
    y = 0; z=0
    for j in range(len(dataTest)):
        AgeMore = naivebayes('age',dataTest['age'][j],'income','>50K',lebih)
        AgeLess = naivebayes('age',dataTest['age'][j],'income','<=50K',kurang)        
        WorkMore = naivebayes('workclass',dataTest['workclass'][j],'income','>50K',lebih)
        WorkLess = naivebayes('workclass',dataTest['workclass'][j],'income','<=50K',kurang)
        EduMore = naivebayes('education',dataTest['education'][j],'income','>50K',lebih)
        EduLess = naivebayes('education',dataTest['education'][j],'income','<=50K',kurang)
        StatusMore = naivebayes('marital-status',dataTest['marital-status'][j],'income','>50K',lebih)
        StatusLess = naivebayes('marital-status',dataTest['marital-status'][j],'income','<=50K',kurang)
        OccupationMore = naivebayes('occupation',dataTest['occupation'][j],'income','>50K',lebih)
        OccupationLess = naivebayes('occupation',dataTest['occupation'][j],'income','<=50K',kurang)
        RelationshipMore = naivebayes('relationship',dataTest['relationship'][j],'income','>50K',lebih)
        RelationshipLess = naivebayes('relationship',dataTest['relationship'][j],'income','<=50K',kurang)
        HoursMore = naivebayes('hours-per-week',dataTest['hours-per-week'][j],'income','>50K',lebih)
        HoursLess = naivebayes('hours-per-week',dataTest['hours-per-week'][j],'income','<=50K',kurang)

        PeluangMore = More*(AgeMore*WorkMore*EduMore*StatusMore*OccupationMore*RelationshipMore*HoursMore)
        PeluangLess = Less*(AgeLess*WorkLess*EduLess*StatusLess*OccupationLess*RelationshipLess*HoursLess)
        if (PeluangMore > PeluangLess):   
            income.append('>50K'); y += 1
        else:
            income.append('<=50K'); z +=1
            
    for x in range(len(dataTest)):  #looping for duplicate data datatest to TebakanTugas1ML.csv
        age.append(dataTest['age'][x])
        workclass.append(dataTest['workclass'][x])
        education.append(dataTest['education'][x])
        status.append(dataTest['marital-status'][x])
        occupation.append(dataTest['occupation'][x])
        relationship.append(dataTest['relationship'][x])
        hours.append(dataTest['hours-per-week'][x])
    
    print ("Jumlah >50K :", y); print ("Jumlah <=50K :", z); print("Silahkan lihat hasil di file TebakanTugas1ML.csv")
    df = pandas.DataFrame({'age' : age, 'workclass' : workclass, 'education' : education, 'marital-status' : status, 'occupation' : occupation, 
        'relationship' : relationship, 'hours-per-week' : hours, 'income' : income}, index=dataTest['id'])
    df.to_csv("Tebakan.csv")

main()       
