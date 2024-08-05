
import gradio as gr
from data_loader import load_data
from chromadb_client import initialize_client
from specialist_finder import find_specialist

def main():
    # Load data
    data_file_path = 'data/MayoClinic_Diseases(Custom Sheet).xlsx'
    data = load_data(data_file_path)
    
    # Initialize ChromaDB client and collection
    collection = initialize_client()

    # Prepare data for adding
    documents = data['Symptoms'].tolist()
    ids = [str(index) for index in data.index]
    metadatas = [{'specialist': row['Specialist Doctor']} for _, row in data.iterrows()]

    # Add data to the collection
    collection.add(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )
    
    # Define the function to be used by Gradio
    def gradio_find_specialist(symptoms):
        return find_specialist(symptoms, collection)
    
    # Create Gradio interface
    iface = gr.Interface(
        fn=gradio_find_specialist,
        inputs=gr.Textbox(label="Enter Symptoms"),
        outputs=gr.Textbox(label="Specialist Doctor"),
        title="Specialist Doctor Recommender",
        description="Enter symptoms to get the name of the specialist doctor."
    )
    
    # Launch the app
    iface.launch()

if __name__ == "__main__":
    main()
