import grpc
import music_recommendation_pb2 as music_pb2
import music_recommendation_pb2_grpc as music_pb2_grpc

def create_recommendation(stub):
    title = input("Enter the title of the song: ")
    artist = input("Enter the artist's name: ")
    genre = input("Enter the genre: ")

    response = stub.CreateRecommendation(music_pb2.CreateRecommendationRequest(
        title=title,
        artist=artist,
        genre=genre
    ))
    print(f"Create Response: {response.message}, ID: {response.id}")
    return response.id

def get_recommendation(stub):
    recommendation_id = input("Enter the recommendation ID to retrieve: ")
    try:
        response = stub.GetRecommendation(music_pb2.GetRecommendationRequest(id=recommendation_id))
        print(f"Recommendation: {response.title} by {response.artist}, Genre: {response.genre}")
    except grpc.RpcError as e:
        print(f"Error: {e.details()}")

def update_recommendation(stub):
    recommendation_id = input("Enter the recommendation ID to update: ")
    title = input("Enter the new title of the song: ")
    artist = input("Enter the new artist's name: ")
    genre = input("Enter the new genre: ")

    response = stub.UpdateRecommendation(music_pb2.UpdateRecommendationRequest(
        id=recommendation_id,
        title=title,
        artist=artist,
        genre=genre
    ))
    print(f"Update Response: {response.message}")

def delete_recommendation(stub):
    recommendation_id = input("Enter the recommendation ID to delete: ")
    response = stub.DeleteRecommendation(music_pb2.DeleteRecommendationRequest(id=recommendation_id))
    print(f"Delete Response: {response.message}")

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = music_pb2_grpc.MusicRecommendationServiceStub(channel)

        while True:
            print("\n--- Music Recommendation Service ---")
            print("1. Create a new recommendation")
            print("2. Get a recommendation by ID")
            print("3. Update an existing recommendation")
            print("4. Delete a recommendation by ID")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                create_recommendation(stub)
            elif choice == '2':
                get_recommendation(stub)
            elif choice == '3':
                update_recommendation(stub)
            elif choice == '4':
                delete_recommendation(stub)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    run()