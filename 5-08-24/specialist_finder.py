# src/specialist_finder.py
def find_specialist(symptoms, collection):
    """Find a specialist based on symptoms using ChromaDB."""
    try:
        # Perform retrieval
        results = collection.query(
            query_texts=[symptoms]  # Pass query as a list of texts
        )
        
        # Print results for debugging
        print("Results:", results)
        
        # Check if results contain documents and metadata
        documents = results.get('documents', [])  # Ensure it's a list
        metadatas = results.get('metadatas', [])  # Ensure it's a list

        # Print documents and metadata for debugging
        print("Documents:", documents)
        print("Metadatas:", metadatas)
        
        # Ensure there are results
        if documents and metadatas:
            # `metadatas` is a list of lists, so access the first list
            best_metadatas = metadatas[0]  # Get the metadata list of the first result
            
            # Print best_metadatas for debugging
            print("Best Metadatas:", best_metadatas)
            
            # Iterate through metadata entries to find the specialist
            specialists = [metadata.get('specialist') for metadata in best_metadatas if isinstance(metadata, dict)]
            
            # Return the first specialist found or a message if not found
            if specialists:
                return specialists[0]  # You can modify this to return all specialists if needed
            else:
                return "Specialist not found"
        else:
            return "No documents or metadata found"
    except Exception as e:
        return f"An error occurred: {str(e)}"
