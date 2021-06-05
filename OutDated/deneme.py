import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\TULPAR\\Desktop\\BİTİRME\\braided-tracker-315323-28d9ddadc2b9.json"


def translate_text(target, text):
    
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language="en")

    """    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
        print(lol)
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))"""
    
    lol = str(result["translatedText"])

    return lol

    

anan =translate_text("tr","tavuk bonfile")

print(anan)
