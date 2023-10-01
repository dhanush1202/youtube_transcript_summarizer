from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

app = Flask(__name__)
@app.get('/summary')
#Hello




def summary_api():
    url=request.args.get('url','')
    vid=url.split("=")[1]
    summary= get_summary(get_transcript(vid))
    return summary, 200



def get_transcript(vid):
    trans= YouTubeTranscriptApi.get_transcript(vid)
    d=[]
    for i in trans:
        d.append(i['text'])
    d=" ".join(d)
    return d
def get_summary(trans):
    summariser = pipeline('summarization')
    summary=''
    for i in range(0, (len(trans)//2000)+1):
        sum=summariser(trans[i*2000:(i+1)*2000])[0]['summary_text']
        summary=summary+sum+' '
    return summary

if __name__=='__main__':
    app.debug=True
    app.run()
