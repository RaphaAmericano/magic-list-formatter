import os
import typer
import pandas as pd
from rich import print
from rich.console import Console
from InquirerPy import prompt
from magic_formater import MagicFormater

app = typer.Typer()

console = Console()
err_console = Console(stderr=True)

def read_file(name):
    df = pd.read_csv(f"{name}")
    return df

def filter_file_by_extension(list:list , extension:str = "csv"):
    result = filter(lambda file: file.endswith(f".{extension}") , list)
    return result

def main(list:bool = False):
    files = [item for item in os.listdir(os.getcwd()) if item.endswith('.csv') or item.endswith('.txt')]
    if list == True:
        # TODO: Fazer um gueri-gueri de cor aqui no print
        print("-- Arquivos -- ")
        for i, file in enumerate(files):
            print(f"{i+i} {file}")

    user_input_prompts = [
        {   "type": "list", 
            "message": "Escolha um arquivo:", 
            "choices": files },
        {   
            "type": "list", 
            "message": "O arquivo de entrada foi exportado de qual software/app:", 
            "choices": ["Dragon Shield", "Mana Box","Mox Field", "Ligamagic"]
        },
        {   
            "type": "list", 
            "message": "O arquivo será importado para qual software/app:", 
            "choices": ["Dragon Shield", "Mana Box", "Ligamagic"]
        },
        {   
            "type": "list", 
            "message": "O arquivo será importado para qual software/app:", 
            "choices": ["txt", "csv"]
        },
    ]
    
    user_inputs = prompt(user_input_prompts)

    try:
        file_dataframe = read_file(user_inputs[0])
    except FileNotFoundError as error:
        print(f"[bold red]Hello[/blod red] Erro ao carregar o arquivo {user_inputs[0]} :boom:")
        print(error)
        raise typer.Exit()

    formatter = MagicFormater(
        dataframe=file_dataframe,
        user_inputs=user_inputs,
    )
    success = formatter.output_file()
    if success == True:
        print(f"[bold green]Formatação concluída com sucesso[/bold green] :white_check_mark:")
    raise typer.Exit()

if __name__ == "__main__":
    typer.run(main)