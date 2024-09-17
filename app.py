from flask import Flask, render_template, request, redirect, url_for
import grpc
import music_recommendation_pb2 as music_pb2
import music_recommendation_pb2_grpc as music_pb2_grpc

app = Flask(__name__)

def get_grpc_stub():
    channel = grpc.insecure_channel('localhost:50051')
    stub = music_pb2_grpc.MusicRecommendationServiceStub(channel)
    return stub

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_recommendation():
    title = request.form['title']
    artist = request.form['artist']
    genre = request.form['genre']
    
    stub = get_grpc_stub()
    response = stub.CreateRecommendation(music_pb2.CreateRecommendationRequest(
        title=title,
        artist=artist,
        genre=genre
    ))
    
    return redirect(url_for('index'))

@app.route('/get', methods=['POST'])
def get_recommendation():
    recommendation_id = request.form['id']
    
    stub = get_grpc_stub()
    try:
        response = stub.GetRecommendation(music_pb2.GetRecommendationRequest(id=recommendation_id))
        return render_template('index.html', recommendation=response)
    except grpc.RpcError as e:
        return render_template('index.html', error=f"Error: {e.details()}")

@app.route('/update', methods=['POST'])
def update_recommendation():
    recommendation_id = request.form['id']
    title = request.form['title']
    artist = request.form['artist']
    genre = request.form['genre']
    
    stub = get_grpc_stub()
    response = stub.UpdateRecommendation(music_pb2.UpdateRecommendationRequest(
        id=recommendation_id,
        title=title,
        artist=artist,
        genre=genre
    ))
    
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_recommendation():
    recommendation_id = request.form['id']
    
    stub = get_grpc_stub()
    response = stub.DeleteRecommendation(music_pb2.DeleteRecommendationRequest(id=recommendation_id))
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
