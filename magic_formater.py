import time
import pandas as pd
from rich.console import Console
from rich.progress import track
from rich.table import Table
from enum import Enum

console = Console()
err_console = Console(stderr=True)

class AppFormat(Enum):
    DRAGON_SHIELD = "Dragon Shield"
    MANA_BOX = "Mana Box"
    MOX_FIELD = "Mox Field"
    LIGAMAGIC = "Ligamagic"

# AppFormat = Enum("AppFormat", ["DRAGON_SHIELD"])

def table():
    table = Table("Name", "Item")
    table.add_row("Jorge", "Portal Gun")
    console.print(table)

class MagicFormater:
    
    def __init__(self, dataframe, user_inputs):

        self._dataframe = dataframe
            # {0: 'ixidor.csv', 1: 'Dragon Skin', 2: 'Dragon Skin', 3: 'txt'}
        self._user_inputs = user_inputs
        
    def output_file(self):
        # todo: transaformar todas as entradas em um dataframe padrao e depois formatar de acordo com o output

        final_df = pd.DataFrame(columns=["quantity", "name"])
        match self._user_inputs[1]:
            case "Dragon Shield":
                final_df = self._format_dragon_shield_to_dataframe(final_dataframe=final_df)
                pass
            case "Mox Field":
                final_df = self._format_mox_field_to_dataframe(final_dataframe=final_df)
                pass
            # case "Mana Box":
            # case "Ligamagic":
            case _:
                final_df = self._format_quantity_name_default_to_dataframe(final_dataframe=final_df)
                
    
        list = ""
        # TODO: corrigir gambix para exprotar um csv de fato, caso seja a opcao escolhida
        list_name = self._user_inputs[0].split(".")[0]
        output_app = self._user_inputs[2].replace(" ", "_").lower()
        extension = self._user_inputs[3]
        filename = "./" + list_name + "." + output_app + "." + extension

        progress_total = 0
        for i, row in track(final_df.iterrows(), description="Processing cards..."):
            quantity, name = row.iloc
            list += f"{quantity} {name}\n"
            time.sleep(0.01)
            progress_total += 1
        
        with open(filename, "w") as text_file:
            print(f"{list}", file=text_file)


        return True

    def _format_dragon_shield_to_dataframe(self, final_dataframe):
        columns = ["Quantity","Name","Card Type","Deck Card Type"]
        final_dataframe['quantity'] = self._dataframe.iloc[:, 0]
        final_dataframe['name'] = self._dataframe.iloc[:, 1]
        return final_dataframe
    
    def _format_quantity_name_default_to_dataframe(self, final_dataframe):
        columns = ["Quantity","Name","Card Type","Deck Card Type"]
        final_dataframe['quantity'] = self._dataframe.iloc[:, 0]
        final_dataframe['name'] = self._dataframe.iloc[:, 1]
        return final_dataframe

    def _format_mox_field_to_dataframe(self, final_dataframe):
        name_quantity_arr = []
    
        for row in self._dataframe.to_numpy():
            split_row = row[0].split(" (")
            split_name = split_row[0].split(" ", 1)
            name_quantity_arr.append(split_name)
        
        mox_field_df = pd.DataFrame(name_quantity_arr, columns=["quantity", "name"])

        combined = pd.concat([final_dataframe, mox_field_df], ignore_index=True)
        print(combined)
        return combined
        
        
    
    def _format_to_ligamagic_output(self):
        return self._dataframe