# Family name, given name, phone number, e-mail address

#q -- quit from the program
#a -- add a new person to the database
#  -- ask 4 questions, enter the 4 answers into the database
#l -- list all of the perople in the database
#f -- ask the user for a search string,
#     print all records where the search string is anywhere
#     in the name and/or the e-mail address
# w -- write the database to disk(overwriting previous saves)
# r -- read the database from disk(overwriting what's in memory)

#use cat -T filename to 

contact = []
user_choice = []
filename = './contact.txt'
print 'Welcome MyContact!'
while True:
    #print contact --for debug the list
    enter_key = raw_input();
    if enter_key == 'q':
        break
    if enter_key == 'a':
        #for field in ['family_name', 'given_name', 'phone', 'email']:
        #    p[field] = raw_input('Enter the {}: '.format(field) )
        #contact.append(p)
        fname = raw_input('Enter the family name: ')
        gname = raw_input('Enter the given name: ')
        phone = raw_input('Enter the phone number: ')
        email = raw_input('Enter the e-mail address: ')
        contact.append({'family-name':fname, 'given-name': gname, 'phone': phone, 'e-mail': email})
        print 'Update Successfully!'
        continue
    if enter_key == 'l':
        #list all of the perople in the database
        for person in contact:
            print'Family name: {}, Given name: {}, phone: {}, e-mail: {}'.format(person['family-name'],person['given-name'],person['phone'],person['e-mail'])
        continue
    if enter_key == 'f':
        # ask the user for a search string
        search_word = raw_input('Please enter your keyword: ')
        count = 0
        for person in contact:
           # if search_word in person['family-name'] or
            # person['given-name'] or
            #  person['e-mail']:
                  
            
            if person['family-name'] == search_word:
                print'found {}, {}, phone: {}, e-mail: {}'.format(person['family-name'],person['given-name'],person['phone'],person['e-mail'])
                count+=1
            if person['given-name'] == search_word:
                print'found {}, {}, phone: {}, e-mail: {}'.format(person['family-name'],person['given-name'],person['phone'],person['e-mail'])
                count+=1
            if person['phone'] == search_word:
                print'found {}, {}, phone: {}, e-mail: {}'.format(person['family-name'],person['given-name'],person['phone'],person['e-mail'])
                count+=1
            if person['e-mail'] == search_word:
                print'found {}, {}, phone: {}, e-mail: {}'.format(person['family-name'],person['given-name'],person['phone'],person['e-mail'])
                count+=1
        if count == 0:
            print 'Sorry not found'
        else: 
            print 'Result: {} person(s)'.format(count)
        continue
    if enter_key == 'w':
        print 'Saving processing ...'
        with open(filename','w') as f:
            for person in contact:
                print 'writing {} {} {} {} to Database'.format(person['family-name'],person['given-name'],person['phone'],person['e-mail'])
                f.write('{}\t{}\t{}\t{}\n'.format(person['family-name'],person['given-name'],person['phone'],person['e-mail']))
        print 'Overwiting successfully!'
        continue
    if enter_key == 'r':
        print 'Loading database...'
        for line in open(filename,'r'):
            aperson = line.strip().split()
            contact.append({'family-name':aperson[0], 'given-name': aperson[1], 'phone': aperson[2], 'e-mail': aperson[3]})
        print 'Loading successfully!'
        continue
print'Thank you for using, Bye!'
        
        
            