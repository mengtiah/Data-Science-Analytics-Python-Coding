## 2. Sets ##


gender=[]
for item in legislators:
    new=item[3]
    gender.append(new)
gender=set(gender)
print(gender)


## 3. Exploring the Dataset ##

party=[]
for item in legislators:
    party.append(item[6])
party=set(party)
print(party)
print(legislators)

## 4. Missing Values ##

for item in legislators:
    if item[3]=='':
        item[3]='M'

## 5. Parsing Birth Years ##

birth_years=[]
for item in legislators:
    parts=item[2].split('-')
    birth_years.append(parts[0])

## 6. Try/except Blocks ##

try:
    float('hello')
except Exception:
    print('Error converting to float.')

## 7. Exception Instances ##

try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []
for year in birth_years:
    try:
        int_year=int(year)
        converted_years.append(int_year)
    except Exception:
        pass

## 9. Convert Birth Years to Integers ##

birth_year=[]
for each in legislators:
    birth_year=each[2].split('-')[0]
    try:
        birth_year=int(birth_year)
    except Exception:
        birth_year=0
    each.append(birth_year)

## 10. Fill in Years Without a Value ##

last_value=1
for row in legislators:
    if row[7]==0:
        row[7]=last_value
    last_value=row[7]