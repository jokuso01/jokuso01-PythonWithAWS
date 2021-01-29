import boto3

client = boto3.client('translate')

#### Add the new text below this line ####

def translate_text(): # declare the function using def, name, braces for parameters and a colon  
    response = client.translate_text(
        Text='I am learning to code in AWS', # Assigning the value of the string to the variable Text
        SourceLanguageCode='en', # We are using a two letter language code from the documentation (en = English)
        TargetLanguageCode='fr' # We use a second two letter language code from the documentation (fr = French)
    )
#### Add the new text below this line ####
    print(response) # this code is inside the function and will print the contents of the variable 'response' 

def main():
    translate_text()
    
if __name__ == "__main__":
    main()