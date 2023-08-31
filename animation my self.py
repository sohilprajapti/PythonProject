import sys,time

space=0
spaceincreasing = True

while True:
    try:
        print(' ' * space, end=(''))
        print('********')
        if spaceincreasing:
            space = space + 1
        if space==20:
            spaceincreasing=False

        if spaceincreasing==False:
            space = space - 1
        if space==0:
            spaceincreasing=True
        time.sleep(0.1)

    except KeyboardInterrupt:
        sys.exit()


        
