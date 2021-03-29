from flask import Flask, make_response, jsonify
from flask_mongoengine import mongoengine
from api_constants import Mongodb_password
import venv
from datetime import datetime

app = Flask(_name_)
database_name = 'API'
DB_URI = "mongodb+srv://secret2307:{}@pythoncluster.t9n3z.mongodb.net/{}?retryWrites=true&w=majority".format(Mongodb_password, database_name)
app.config["MONGODB_HOST"] = DB_URI
db = mongoEngine()
db.init_app(app)

class Song(db.Document):
    song_id = db.IntField()
    name = db.StringField()
    duration = db.IntField()
    uploadedtime = db.StringField()

    def to_json(self):
        #convert this document to json
        return {
            "Uploadedtime":now.strftime("%H:%M:%S"),
            "song_id": self.song_id,
            "name": self.name,
            "duration": self.duration,
            "uploadedtime": self.uploadedtime
        }

@app.route('/api/db_populate', method=['POST'])
def db_populate():
    song1 = Song(song_id=1,name='Closer', duration='240', uploadedtime='')
    song2 = Song(song_id=2,name='At my worst', duration='210', uploadedtime='')
    song3 = Song(song_id=3,name='Life goes on', duration='230', uploadedtime='')
    song1.save()
    song2.save()
    song3.save()
    return make_response("",201)

@app.route('/api/songs', methods=['GET','POST'])
def api_songs():
    if request.method == 'GET':
        song = []
        for song in Song.objects:
            song.append(song)
        return make_response(jsonify(songs),200)
    elif request.method == 'POST':

        content = request.json
        song = Song(song_id=content['song_id'], name=content['name'],duration=content['duration'],uploadedtime=content['uploadedtime'])
        song.save()
        return make_response("",201)


@app.route('/api/songs/<song_id>', methods=['GET','PUT','DELETE'])
def api_each_song(song_id):
    if request.method == 'GET':
       song_obj = Song.objects(song_id=song_id).first()
       if song_obj:
           return make_response(jsonify(song_obj.to.json()),200)

               


    elif request.method == 'PUT':
       content = request.json
       song_obj = Song.pbjects(song_id=song_id).first()
       song_obj.update(duration=content['duration'], name= content['name'])
       return make_response("",204)
       
    elif request.method == 'DELETE':
        song_obj = Song.objects(song_id=song_id).first()
        song_obj.delete()
        return make_response()


if _name_ == '_main_':
    app.run()