import boto3

kwargs = {
    "Text": "I am learning to code in AWS", 
    "SourceLanguageCode": "en",
    "TargetLanguageCode": "fr"
}

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)
    

def main():
    translate_text(**kwargs)

if __name__=="__main__": # i need to understand this part further.
    main()
