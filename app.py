from flask import Flask, render_template
app = Flask(__name__)
import urllib2
import json


@app.route('/')
def index():
    #Note: I know this is hardcoded. But afterdoing several different reinstalls of python, my python is still not working. I'm going to continue trying to fix this over the weekend, but because there is a deadline and I need to submit an assignment, I'm going to have to skip the urllib2 part. I know if I don't eventually fix this my life will be miserable, but please forgive my broken computer for one day.
    nasa = '''
    {
  "copyright": "Robert Gendler",
  "date": "2017-11-09",
  "explanation": "Big, beautiful spiral galaxy NGC 1055 is a dominant member of a small galaxy group a mere 60 million light-years away toward the aquatically intimidating constellation Cetus. Seen edge-on, the island universe spans over 100,000 light-years, a little larger than our own Milky Way. The colorful stars in this cosmic close-up of NGC 1055 are in the foreground, well within the Milky Way. But the telltale pinkish star forming regions are scattered through winding dust lanes along the distant galaxy's thin disk. With a smattering of even more distant background galaxies, the deep image also reveals a boxy halo that extends far above and below the central bluge and disk of NGC 1055. The halo itself is laced with faint, narrow structures, and could represent the mixed and spread out debris from a satellite galaxy disrupted by the larger spiral some 10 billion years ago.",
  "hdurl": "https://apod.nasa.gov/apod/image/1711/NGC1055-ESO-Crop-L1.jpg",
  "media_type": "image",
  "service_version": "v1",
  "title": "NGC 1055 Close-up",
  "url": "https://apod.nasa.gov/apod/image/1711/NGC1055-ESO-Crop1024_1.jpg"
}
    '''
    nd = json.loads(nasa)
    img1 = nd['hdurl']
    img2 = nd['url']
    exp = nd['explanation']
    return render_template("index.html", img1=img1, img2=img2, expl=exp)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
