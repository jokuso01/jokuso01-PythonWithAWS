import boto3

def translate_text(a,b,c):
    client = boto3.client('translate')
    response = client.translate_text(
        Text=a, 
        SourceLanguageCode= b, # useing positional argument
        TargetLanguageCode= c
    )
    print(response) 

def main():
    translate_text('I am learning to code in AWS', 'en','fr')

if __name__=="__main__":
    main()
