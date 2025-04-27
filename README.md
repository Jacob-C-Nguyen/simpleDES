SIMPLE DES PYTHON PROGRAM

Summary:
This program takes a ".txt" file, and uses two 8 bit keys to encrypt the text using a simplified version
of the DES algorithm (S-DES). Unlike normal DES, S-DES is simpler by having smaller keys, and taking only
8 bits per-plain-text character. My version of S-DES outputs the cipher text as a long string of binary. 
Good luck reading that!



##################################################
How to use the program:

	When running the program in terminal, you will see this menu: 
		##################################
		What would you like to do? 
		  1) Load Keys
		  2) Generate Keys
		  3) Encrypt File
		  4) Decrypt File
		  5) Exit Program
		##################################
	The number you type in corresponds to the options listed above



	How to Encrypt:

	1) Create the ".txt" file and save your message inside of it.
		- Make sure to move the ".txt" message into the same directory/folder as the "main.py"
		  file is contained in.
		
	2) Load or generate a pair of keys:
		- In order to encrypt your message you must load a pair of keys. You have 2 options to do
		  so:
			- Option 1: type in 2 8-bit keys
			- Option 2: randomly generates 2 keys and loads them into the program for use.
			
	3) Encryption (use option 3)
		- Type the name of the ".txt" file you want to encrypt. (".txt" must be omitted)
		- Name the encrypted output file.
		- The program will output an encrypted version of the file. It will appear in the 
		  directory by the name you just chose.
	
	
	How to Decrypt:
	
	1) Locate encrypted ".txt" file
		- Make sure it is in the same directory as the python files and is also a ".txt" file.
	2) Load in previously used keys:
		- I hope you saved the keys somewhere because you'll have to input them into the program
		  to decrypt. If the keys are different, the decryption WILL NOT WORK. If you have just 
		  encrypted a file, the keys used in the previous operation should still already be 
		  loaded in.
	3) Decryption (use option 4)
		- Type the name of the encrypted version of the text. (".txt" must be omitted)
		- Name the decrypted output file.
		- The program will output a decrypted version of the cipher text. It will appear in the 
		  directory by the name you just chose.
	
	How to Exit:
		1) Use option 5.
			- It can't be that hard can it?
			
##################################################
