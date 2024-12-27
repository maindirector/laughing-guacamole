def main():
    print('____________________WELCOME TO THE GAME "NEW YEAR\'S STORY".____________________')
    choosing_hero()
      
def choosing_hero():
    print('<The hall is full.')
    print('The students know why they have gathered, the New Year is coming soon and each student will')
    print('be given extra points as a gift.')
    print('Festive music is heard. The hall becomes quiet.')
    print('At the moment when they are about to congratulate the students and hand out points, a terrible scream is heard.')
    print('Panic and complete incomprehension of what is happening.')
    print('The host comes out with a sad face and makes an announcement.>')
    print('HOST:')
    print('Friends, we have bad news for you.')
    print('It so happened that all the extra points for the New Year are hidden.')
    print('To find them, you need to pass the challenge.')
    print('Are there any volunteers who are ready to try their hand?')
    print('<You hold your breath waiting for this time to get')
    print('away with it, because you can\'t be such an unlucky person...>')
    choice = int(input('What would you choose?\n 1. Raise your hand\n 2. Not to raise your hand\n '))
    if choice == 1:
        print('HOST:\n Excellent! Now we have discuss the rules of your challenge')
        rules_discussing()
    elif choice == 2:
        print('<Silence reigned in the hall.')
        print('Suddenly you felt a strong push in the back,')
        print('which made you take a few steps forward.')
        print('All eyes were on you at that moment.')
        print('It became clear who would be the lucky one who would have')
        print('to take on the responsibility of returning all the points...>')
        print('HOST:\n Excellent! Now we have discuss the rules of your challenge')
        rules_discussing()
    else:
        print('TRY AGAIN')
        choosing_hero()

def rules_discussing():
    print('<After a while you are already standing in a huge office decorated for the New Year.>')
    print('HOST:')
    print('Yes, now a difficult task lies ahead, we were only told that for each test one letter will be given out.')
    print('Having collected all the letters you will be able to find out where all your holiday')
    print('points are hidden.')
    print('By the way, your first task is already known!')
    print('<A shiver ran down your spine, because it was not')
    print('clear what you would have to do. It was scary to receive an incomprehensible stupid task.>')
    print('HOST:\n Your first task is rather... unusual.')
    print('Do you remember those guys, who clean the snow?')
    choice = int(input('1. Yes 2. No:\n'))
    if choice == 1:
        print('HOST:\nGreat cause your next task is to help them')
        first_task()
    elif choice == 2:
        print('HOST:\n Well, now you will know them, cause your first task is to help them!')
        first_task()
    else:
        print('TRY AGAIN')
        rules_discussing()
    print('...')
    print('FIRST TASK')

def first_task():
    print('<This year, especially for me, there was a lot of snow, despite the fact that at the beginning')
    print('of December there was practically no snow.')
    print('It looks like I\'ll have to sweat a lot.>')
    print('STRANGER:')
    print('Grab a shovel and get to work quickly,')
    print('we don\'t have much time.')
    print('YOU:\n Is my first task really going to be clearing snow from the university grounds?')
    print('STRANGER:\n Yes, of course. This will help you feel what it\'s like.')
    print('Have you ever cleared snow?')
    choice = int(input('YOU:\n 1. (No, I haven\'t 2. Yes, I have): '))
    if choice == 1:
        print('YOU:\nNo, I haven\'t')
        print('STRANGER:\nThat\'s great, you\'ll try something new in your life')
    elif choice == 2:
        print('YOU:\nYes, I have')
        print('STRANGER:')
        print('That\'s great, that means you have enough experience and knowledge and you')
        print('won\'t have to be taught anything.')
    else:
        print('TRY AGAIN')
        first_task()
    print('<You already had a small shovel in your hands.')
    print('You start clearing the path from the thick layer')
    print('of snow that had fallen during the evening.>')
    choice1 = int(input('How to throw snow?: (1. carelessly, without trying 2. trying to remove as much as possible):\n'))
    if choice1 == 1:
        print('<You start casually throwing snow from side to side>')
        print('STRANGER:\nWhat are you doing, your work is useless, try harder')
    elif choice1 == 2:
        print('<You start to shovel snow with special diligence, even in school and university you never tried so hard>')
        print('STRANGER:\nYou are doing pretty well, after graduating you can come work with us')
    else:
        print('TRY AGAIN')
        first_task()
    print('<After removing the snow you felt how the muscles in your arms')
    print('were really working, it reminded you of physical education classes>')
    print('STRANGER:\nWell, you have done your job, congratulations.\nNEXT TASK')
    print('...')
    print('SECOND TASK')
    second_task()
    
def second_task():
    print('<The second test turned out to be no less interesting than previous.')
    print('This time you had a chance to try yourself as a cleaner.>')
    print('CLEANER:')
    print('You know, we decided not to burden you too much, so you will')
    print('only have to wash the floor on 3 floors, I think you can handle it.')
    choice = int(input('1. Are you sure this is a real task? 2. Ok, the sooner I start, the sooner I\'ll finish: '))
    if choice == 1:
        print('YOU:\nAre you sure this is a real task?')
        print('CLEANER:')
        print('And it doesn\'t bother you that we do this every day anyway,')
        print('but as you can see there are more than 3 floors, so stop whining and get to work')
    elif choice == 2:
        print('YOU:\nOk, the sooner I start, the sooner I\'ll finish')
        print('CLEANER:\nThat\'s great, we\'ve already got you a mop')
    else:
        print('TRY AGAIN')
        second_task() 
    print('<Students passing by looked at me like I was a savage.>')  
    print('What to do?\n(1. Say: What you are staring at? 2. Continue washing the floors with your head held high):')
    choice1 = int(input('(1 or 2):'))
    if choice1 == 1:
        print('YOU:\nWhat you are staring at?') 
        print('<Peopleo were not only the passing by staring at you,')
        print('but they also managed to walk on the clean spots on the')
        print('floor with their dirty shoes, which really pissed you off>')
        print('YOU:\nThat\'s it, I finally washed these damn three floors..')
        print('CLEANER:\nYes, you did a good job, even if it wasn\'t very high-quality')
        print('YOU:\n...')
        print('NEXT TASK')
        third_task()

def third_task():
    print('SECURITY GUARD:')
    print('Now you won\'t have to walk around the floors, but our job is no less difficult.')
    print('Now you will be watching the entrance, checking the students\' cards.')
    choice = int(input('YOU:\n (1. okay, I\'m ready 2. Or maybe you could just consider the task completed, please?): '))
    if choice == 1:
        print('YOU:\nOkay, I\'m ready')
        print('STUDENT GUARD:\nThat\'s great, you can take my place.')
    elif choice == 2:
        print('YOU:\nOr maybe you could just consider the task completed, please?')   
        print('STUDENT GUARD:\nStop whining, take my place and watch the people coming in more carefully.')
    else:
        print('TRY AGAIN')
        third_task()  
    print('STUGENT:\n: So, how are you doing at your post?') 
    choice1 = int(input('YOU:\n1. it\'s been better 2. great, I\'m not complaining\n3. who came up with these stupid assignments??:\n'))  
    if choice1 == 1:
        print('YOU:\nIt\'s been better')
    elif choice1 == 2:
        print('YOU:\nGreat, I\'m not complaining')
    elif choice1 == 3:
        print('YOU:\nWho came up with these stupid assignments??')
    else:
        print('TRY AGAIN')
        third_task()
    print('STUDENT: I see you\'re busy, i won\'t bother you')
    print('<Well, you had to sit for a couple of hours and scold students who for various')
    print('reasons forgot their student cards.')
    print('At least it\'s not physically exhausting>')
    print('SECURITY GUARD:')
    print('Okay, you can go. Your work day is over, the test is passed')
    print('...')
    print('LAST TASK')
    last_task()
    
def last_task():
    print('YOU:\n Finally the last assignment, i\'ll be free soon.')
    print('CLOACKROOM ATTENDANT:')
    print('Well, here\'s your last assignment, soon you\'ll get an answer')
    print('to where your New Year\'s points are.')
    print('CHOOSE: 1. yeah, i don\'t know who came up with these stupid tasks')
    print('2. right, today i got a chance to try myself in different professions.')
    choice = int(input('(1 or 2): '))
    if choice == 1:
        print('YOU: Yeah, i don\'t know who came up with these stupid tasks')
        print('CLOACKROOM ATTENDANT:\nThese seem like very good tasks to me. do i need to explain your duties to you?')
    elif choice == 2:
        print('YOU: Right, today i got a chance to try myself in different professions.')
        print('CLOACKROOM ATTENDANT:\nyou\'re right, you can\'t know what job you\'ll')
        print('be working on after graduating. do i need to explain your duties to you?')
    else:
        print('TRY AGAIN')
        last_task()
    print('CHOOSE: 1. that would be nice 2. i think i can figure it out')
    choice1 = int(input('(1 or 2)'))
    if choice1 == 1:
        print('YOU:\nThat would be nice')
        print('CLOACKROOM ATTENDANT:')
        print('Well, you need to take jackets and give numbers, and you also need to')
        print('keep an eye on the security of things. i think you can handle it')
    elif choice1 == 2:
        print('YOU:\nI think i can figure it out')
        print('CLOACKROOM ATTENDANT:\nGreat, then you can get started')
    else:
        print('TRY AGAIN')
        last_task()
    print('<At some point there was a terrible influx of students, everyone')
    print('was pushing their way to this tiny window to take or give their jacket.')
    print('You had to try to remember faces so you could give numbers to the right people.')
    print('Another problem was the students\' constant reminding that they couldn\'t')
    print('give their shoes in a bag. Strength was running out>')
    print('CLOACKROOM ATTENDANT:')
    print('Well, you did a great job. so here are your New Year\'s points on the site')
    print('and already entered in your electronic journals')
    print('CHOOSE:')
    print('1. laugh hysterically, fall down and start rolling on the floor 2. say: really, how wonderful, have a nice day')
    choice2 = int(input('(1 or 2): '))
    if choice2 == 1:
        print('<YOU laugh hysterically, fall down and start rolling on the floor>')
        print('THE END')
    elif choice2 == 2:
        print('YOU:\nReally? How wonderful, have a nice day!')
        print('<After standing in line for the elevator, you went in and rode up to the')
        print('coveted 15th floor to go to the dean\'s office and be expelled>')
        print('THE END')
    else:
        print('TRY AGAIN')
        last_task()

main()