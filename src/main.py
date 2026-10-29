"""
Main entry point for the application, Will ask the user to check whether the current content
of the data folder is the correct input for the run
"""



def run_process():
    """
    Primary entry point and runner function that asks the user for his confirmation
    then processes the data found in the data/ folder
    
    Args:

    Returns:

    """
    print("Assurez vous que le contenu du dossier data est cle souhaitable")
    if not input("Tapez ENTREE pour lancer l'application:"):

        pass # define function calls from other modules

    return

if __name__ == "__main__":
    run_process()
    