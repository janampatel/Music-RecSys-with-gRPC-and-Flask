from concurrent import futures
import grpc
import music_recommendation_pb2_grpc as music_pb2_grpc
import music_recommendation_pb2 as music_pb2
import uuid

# In-memory storage for music recommendations
music_store = {}

class MusicRecommendationServicer(music_pb2_grpc.MusicRecommendationServiceServicer):
    def CreateRecommendation(self, request, context):
        recommendation_id = str(uuid.uuid4())
        music_store[recommendation_id] = {
            'title': request.title,
            'artist': request.artist,
            'genre': request.genre
        }
        return music_pb2.CreateRecommendationResponse(id=recommendation_id, message="Recommendation created successfully!")

    def GetRecommendation(self, request, context):
        recommendation = music_store.get(request.id)
        if recommendation:
            return music_pb2.GetRecommendationResponse(
                id=request.id,
                title=recommendation['title'],
                artist=recommendation['artist'],
                genre=recommendation['genre']
            )
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details('Recommendation not found')
        return music_pb2.GetRecommendationResponse()

    def UpdateRecommendation(self, request, context):
        if request.id in music_store:
            music_store[request.id] = {
                'title': request.title,
                'artist': request.artist,
                'genre': request.genre
            }
            return music_pb2.UpdateRecommendationResponse(message="Recommendation updated successfully!")
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details('Recommendation not found')
        return music_pb2.UpdateRecommendationResponse()

    def DeleteRecommendation(self, request, context):
        if request.id in music_store:
            del music_store[request.id]
            return music_pb2.DeleteRecommendationResponse(message="Recommendation deleted successfully!")
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details('Recommendation not found')
        return music_pb2.DeleteRecommendationResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    music_pb2_grpc.add_MusicRecommendationServiceServicer_to_server(MusicRecommendationServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
