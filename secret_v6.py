#this python program use to encrypt and decrypt messages using Caesar cipher

try:
    import getpass #password module
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #print (alphabet[0])
    #print (alphabet[7])
    #print (alphabet1[17])

    new_message = ''
#- - - - - - - - - - - - - - - -

    number = int(raw_input("Do you want to encrypt or decrypt? (press 1 to encrypt, press 2 to decrypt):"))

    if number == 1:

        message = raw_input("Plain text message:")
        hash1 = hash(message)
        key = int(getpass.getpass())
        #print 'You entered:', key
        #key = int(raw_input("Enter key:"))
        #key = 5

        for character in message:
            if character in alphabet:
                position = alphabet.find(character)
                #print "Current position:", position
                new_position = (position + key) % 26
                #print "New position:", new_position
                new_character = alphabet[new_position]
                #print "Encrypted message:", new_character
                new_message += new_character

            elif character in alphabet1:
                position = alphabet1.find(character)
                new_position = (position + key) % 26
                new_character = alphabet1[new_position]
                new_message += new_character

            else:
                new_message += character

        print "Encrypted message:", new_message
        print "Message hash:", hash1
#- - - - - - - - - - - - - - - - 

    elif number == 2:

        message = raw_input("Cypher text message:")
        hash1 = int(raw_input("Enter hash:"))
        key = int(getpass.getpass())
        #key = int(raw_input("Enter key:"))
    
        for character in message:
            if character in alphabet:
                position = alphabet.find(character)
                #print "Current position:", position
                new_position = (position - key) % 26
                #print "New position:", new_position
                new_character = alphabet[new_position]
                #print "Encrypted message:", new_character
                new_message += new_character

            elif character in alphabet1:
                position = alphabet1.find(character)
                new_position = (position - key) % 26
                new_character = alphabet1[new_position]
                new_message += new_character

            else:
                new_message += character

        print "Decrypted message:", new_message
        hash2 = int(hash(new_message))
        #print hash2

        if hash2 == hash1:
            print "Message correct"
        else:
            print "Message wrong"
#- - - - - - - - - - - - - - - - 

    else:
        print ("invalid, retry")
#- - - - - - - - - - - - - - - -

except KeyboardInterrupt:
    print ("Program aborted by user")
    exit()
