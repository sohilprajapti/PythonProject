#! Python3
from pathlib import Path
import random

country_capital = {'Afghanistan':'Kabul',
                   'Armenia':'Yerevan',
                   'Azerbaijan':	'Baku',
                   'Bahrain':'Manama',
                   'Bangladesh'	:'Dhaka',
                   'Bhutan'	:'Thimphu',
                   'Brunei'	:'Bandar Seri Begawan',
                   'Cambodia':	'Phnom Penh',
                   'China'	:'Beijing',
                   'Cyprus'	:'Nicosia',
                   'East Timor':'Dili',
                   'Georgia':'Tbilisi',
                   'Hong Kong':	'Hong Kong',
                   'India':'New Delhi',
                   'Indonesia':	'Jakarta',
                   'Iran':'Tehran',
                   'Iraq':'Baghdad',
                   'Israel':'Jerusalem',
                   'Japan':'Tokyo'	,
                   'Jordan':'Amman'	,
                   'Kazakhstan':'Nursultan',
                   'Kuwait'	:'Kuwait City'	,
                   'Kyrgyzstan':'Bishkek',
                   'Laos':	'Vientiane',
                   'Lebanon':'Beirut',
                   'Macao':	'Concelho de Macau',
                   'Malaysia':'Kuala Lumpur',
                   'Maldives':'Male'	,
                   'Mongolia':'Ulaanbaatar',
                   'Myanmar':'Nay Pyi Taw',
                   'Nepal':'Kathmandu',
                   'North Korea':'Pyongyang',
                   'Oman':'Muscat',
                   'Pakistan':'Islamabad',
                   'Palestine':'Ramallah',
                   'Philippines':'Manila',
                   'Qatar':	'Doha',
                   'Saudi Arabia':'Riyadh',
                   'Singapore':	'Singapore',
                   'South Korea':'Seoul',
                   'Sri Lanka':'Colombo',
                   'Syria':'Damascus',
                   'Taiwan':'Taipei',
                   'Tajikistan':'Dushanbe',
                   'Thailand':'Bangkok',
                   'Turkey'	:'Ankara',
                   'Turkmenistan':'Ashgabat',
                   'United Arab Emirates':	'Abu Dhabi',
                   'Uzbekistan':'Tashkent',
                   'Vietnam':'Hanoi',
                   'Yemen':	'Sanaa'
                   }

for a in range(1,3):
    quizfile = Path(f'c:\\Users\\Anjal\\Documents\\GitHub\\PythonProject\\QuizGame\\CapitalQuiz{a}.txt').open('w')
    answerkeyfile = Path(f'c:\\Users\\Anjal\\Documents\\GitHub\\PythonProject\\QuizGame\\Answers_of_Quiz{a}.txt').open('w')

    quizfile.write('                                         Asian Capital Cities Quiz \n')
    quizfile.write('\n\n')

    country = list(country_capital.keys())
    random.shuffle(country)
    for i in range(51):
        correctanswer = country_capital[country[i]]
        wronganswer = list(country_capital.values())
        del wronganswer[wronganswer.index(correctanswer)]
        wronganswer = random.sample(wronganswer, 3)
        answeroptions = wronganswer + [correctanswer]
        random.shuffle(answeroptions)

        quizfile.write(f'{i+1}.What is the capital of {country[i]}?\n')

        for a in range(4):
            quizfile.write(f'          {"ABCD"[a]}.{answeroptions[a]} \n')

        answerkeyfile.write(f"{i+1}. {'ABCD'[answeroptions.index(correctanswer)]}\n")

