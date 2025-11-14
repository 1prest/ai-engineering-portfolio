import pickle

def train_model():
    # Example simple model — replace this with your actual ML model
    model = {"message": "This is a trained model!"}

    # Save to folder "model"
    save_path = "model/model.pkl"
    with open(save_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved to {save_path}")

if __name__ == "__main__":
    train_model()
