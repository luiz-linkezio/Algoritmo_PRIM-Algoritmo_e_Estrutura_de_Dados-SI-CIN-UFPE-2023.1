from cx_Freeze import setup, Executable

executables = [Executable("Main.py")]

# Lista de arquivos a serem incluídos junto com o executável
include_files = [
    ("scripts", "assets"),      # Inclui a pasta "assets" e seu conteúdo
    ("songs", "songs"),         # Inclui a pasta "songs" e seu conteúdo
    ("database.csv", "database.csv"),
    ("README.md", "README.md"),
    ("output.csv", "output.csv"),
    ("images","images"),
    ("videos","videos")
]

setup(
    name="NomeDoSeuPrograma",
    version="0.1",
    description="Descrição do seu programa",
    options={"build_exe": {"include_files": include_files}},
    executables=executables
)
