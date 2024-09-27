import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    Encrypts the email string by shifting each character's ASCII value up by 3.

    Args:
        email (str): The email string to be encrypted.

    Returns:
        str: The encrypted email string.
    """
    output = ""
    len_flag = len(email) != 6
    anum_flag = email[:3] != 'abc' or not email[3:].isdigit()

    if len_flag:
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output

    if anum_flag:
        output = "Alphanumeric check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output

    # Convert email string to list to modify individual characters
    email_lst = list(email)

    # Encrypt each character by shifting its ASCII value up by 3
    for i in range(len(email_lst)):
        char = email_lst[i]
        new_ascii = ord(char) + 3
        if char.islower():
            if new_ascii > ord('z'):
                new_ascii -= 26
        elif char.isupper():
            if new_ascii > ord('Z'):
                new_ascii -= 26
        email_lst[i] = chr(new_ascii)

    # Convert list back to string
    encrypted_email = ''.join(email_lst)
    return encrypted_email

# Testing the function
encrypted_result = encrypt("abc012")
print("Encrypted result:", encrypted_result)l

def decrypt(email="def345"):
    """
    TODO: What is the objective? 

    Args:
        TODO: what arguments and data types are expected? (i.e., email)

    Returns:
        TODO: what varibale and data types are being returned?   
    """
    # input validation
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = email[:3] != 'def' or email[3:] != '345' 

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # TODO: apply the encrypt pseudocode but shift down 3
    
    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = "aef345"
    return retVal
