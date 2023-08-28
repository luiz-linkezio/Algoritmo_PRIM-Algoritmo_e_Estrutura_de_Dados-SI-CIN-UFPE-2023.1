import tkinter as tk
import pandas
import subprocess
import pygame
from time import sleep
from scripts.time_config import time_config, time_printer
from scripts.GeneAssociations import *
from scripts.CSV_data_generation import *
from scripts.PrimAlgorithm import *

class CureApp: #Main Class
    def __init__(self, screen):
        self.screen = screen
        self.screen.title("The Cure")
        self.screen.geometry("800x480")
        self.screen.configure(bg="black")
        self.screen.resizable(False, False)

        self.current_screen = 0
        self.screens = [
            self.opening_screen,
            self.second_screen,
            self.third_screen,
            self.last_screen,
        ]

        #Algorithm results
        self.results = {}
        #Initial index/vertex (may be changed later)
        self.initial_index = 0

        #Creating the first screen
        self.opening_screen()

        #Classes initializations
        self.gene_associations = GeneAssociations()
        self.prim = PrimAlgorithm()

        #Turn CSV into DataFrame
        self.infection_db = pandas.read_csv('database.csv')

        #Create graph
        self.gene_associations.add_gene_associations(self.infection_db)
        self.infection_graph = self.gene_associations.graph

        #Botton to initialize the song
        play_music_button = tk.Button(
            screen, 
            text="Play Music", 
            bg="black",
            fg="#37B800",
            font=("Terminal", 14, "bold"), 
            command=self.play_music)
        play_music_button.pack(side="bottom", pady=30)

        #Initialization of the mixer of pygame
        pygame.mixer.init()

    #Resetting the variables after finishing the last screen of the program, for reuse.
    def reset_variables(self):
        self.results = {}
        self.initial_index = 0
        self.gene_associations = GeneAssociations()
        self.prim = PrimAlgorithm()
        self.infection_db = pandas.read_csv('database.csv')
        self.gene_associations.add_gene_associations(self.infection_db)
        self.infection_graph = self.gene_associations.graph

    #Function to load and play the song
    def play_music(self):
        pygame.mixer.music.load("songs\Dayane Singer.mp3")  # Substitua pelo caminho do seu arquivo de música
        pygame.mixer.music.play(-1)  # -1 indica que a música deve ser reproduzida em loop

    #Generating a CSV file and loading it into the Gephi application
    def open_gephi(self):
        generate_CSV_data(self.initial_index)

        #Gephi exe folder
        gephi_path = 'C:\\Arquivos de Programas\\Gephi-0.10.1\\bin\\gephi64.exe'

        #CSV folder
        csv_file_path = 'output.csv'

        try:
            #Opening the CSV in Gephi
            subprocess.run([gephi_path, "--open", csv_file_path])
        except FileNotFoundError:
            print("Gephi not found. Please check the executable path.")
        except Exception as e:
            print(f"An error occurred: {e}")

    #Starting prim algorithm and gathering/returning datas from it
    def prim_start(self, initial_vertex=0):
        prim_MST, time_to_find_cure, deaths = self.prim.MST_creation(self.infection_graph, initial_vertex) #Prim Algorithm: MST creation and the time calculation for find a cure
        years, days, hours, minutes, seconds = time_config(time_to_find_cure)

        time_printed = time_printer(years, days, hours, minutes, seconds)

        return {"pandemic_data": {"MST": prim_MST, "time_to_find_cure":time_to_find_cure, "deaths":deaths, "deaths/day": int(deaths/(days+(years*365)))}, "time_to_find_cure": time_printed}

    #Clear screen
    def clear_screen(self):
        for widget in self.screen.winfo_children():
            widget.destroy()

    #Foward to the next screen
    def next_screen(self, event=None):
        self.clear_screen()
        self.current_screen = (self.current_screen + 1) % len(self.screens)
        self.screens[self.current_screen]()
        if self.current_screen == 0: #If the program return to the first screen, this command reset the variables(for repeated use) and open a graph in Gephi application
            self.reset_variables()
            self.open_gephi()

    #Screens
    def opening_screen(self):
        label = tk.Label(
            self.screen,
            text="THE CURE",
            bg="black",
            fg="red",
            font=("Terminal", 60, "bold"),
        )
        label.pack(fill="both", expand=True, padx=20, pady=100)

        label2 = tk.Label(
            self.screen,
            text="Press Enter to continue",
            bg="black",
            fg="#37B800",
            font=("Terminal", 14, "bold"),
        )
        label2.pack(fill="both", expand=True)

        self.screen.bind("<Return>", self.next_screen)

    def second_screen(self):

        label1 = tk.Label(
            self.screen,
            text="THE CURE",
            bg="black",
            fg="#37B800",
            font=("Terminal", 40),
        )
        label1.pack(fill="both", expand=True, padx=20, pady=30)

        label2 = tk.Label(
            self.screen,
            text="The following database shows the functional associations between the genes collected to find the cure...",
            bg="black",
            fg="#37B800",
            font=("Terminal", 18),
            wraplength=700,  # Limit the text width
            justify="center",  # Center-align the text
        )
        label2.pack(fill="both", expand=True, padx=20, pady=30)

        # You can add a table or labels here to display the gene associations data

        continue_button = tk.Button(
            self.screen,
            text="Press Enter to continue",
            bd=0,
            bg="black",
            fg="#37B800",
            font=("Terminal", 14, "bold"),
            command=self.next_screen,
        )
        continue_button.pack(fill="both", expand=True, pady=20)

    def third_screen(self):
       
        def on_enter_pressed(event=None):
            #Collecting the initial vertex/index to start the prim algorithm and gather data from it
            self.initial_index = entry.get()  #Getting the value entered by the user
            self.results = self.prim_start(int(self.initial_index))#Initializating prim algorithm for the data treatment

        label1 = tk.Label(
            self.screen,
            text="THE CURE",
            bg="black",
            fg="#37B800",
            font=("Terminal", 40),
        )
        label1.pack(fill="both", expand=True, padx=20, pady=30)

        label2 = tk.Label(
            self.screen,
            text="Enter a sample index from 0 to 2222 to start the analysis and wait for processing:",
            bg="black",
            fg="#37B800",
            wraplength=700,  # Limit the text width
            font=("Terminal", 18),
        )
        label2.pack(fill="both", expand=True, padx=20, pady=20)

        entry = tk.Entry(self.screen, bg="grey", font=("Terminal", 16))
        entry.pack(fill="both", expand=True, padx=20, pady=10)
        entry.bind("<Return>", on_enter_pressed)  # Associar Enter à função

        continue_button = tk.Button(
            self.screen,
            text="Press Enter to continue",
            bd=0,
            bg="black",
            fg="#37B800",
            font=("Terminal", 15, "bold"),
            command=on_enter_pressed,  # Chamando a função na pressão do botão também
        )
        continue_button.pack(fill="both", expand=True, pady=80)
    

    def last_screen(self):
        #Show some information about the pandemic and the prim algorithm
        label1 = tk.Label(
            self.screen,
            text="THE CURE",
            bg="black",
            fg="#37B800",
            font=("Terminal", 40),
        )
        label1.pack(fill="both", expand=True, padx=20, pady=30)

        label2 = tk.Label(
            self.screen,
            text=(
                f"> Unfortunately, during this pandemic {self.results['pandemic_data']['deaths']} people died.\n\n" #deaths
                f"> {self.results['time_to_find_cure']}\n\n" #time to find the cure
                f"> As a result, approximately {self.results['pandemic_data']['deaths/day']} people died per day while the cure was being researched." #deaths per day
            ),
            bg="black",
            fg="#37B800",
            wraplength=700,  # Limit the text width
            font=("Terminal", 12),
        )
        label2.pack(fill="both", expand=True, padx=20, pady=50)

        continue_button = tk.Button(
            self.screen,
            text="Press Enter and wait to visualize the new graph",
            bd=0,
            bg="black",
            fg="#37B800",
            font=("Terminal", 14, "bold"),
            command=self.next_screen,
        )
        continue_button.pack(fill="both", expand=True, pady=20)

#Interface initilization
if __name__ == "__main__":
    screen = tk.Tk()
    app = CureApp(screen)
    screen.mainloop()
