from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.media
# import anvil.tables as tables
import anvil.tables.query as q
from anvil.google.drive import app_files
from anvil.tables import app_tables
import anvil.google.drive
from datetime import datetime, time , date , timedelta

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("export_to_csv")  

  def list_tables_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    list_of_tables =['cases_arriving','changes','charts'
                     ,'printing_problems','problem_cases_over_3_days', \
                     'problem_cases_per_week','problem_cases_with_4s', \
                     'problem_cases_with_customer','problem_cases_with_customer_over_7_days', 'projects', \
                     'projects_with_4s','projects_with_customers', \
                     'test','unassigned_cases','users','waiting_on_4s']
    folder = app_files.spc_support_system_backup
    today = datetime.now()
    new_folder = folder.create_folder('spc_backup'+'_'+str(today))
    for item in list_of_tables:
       print(item)
             # rows = getattr(app_tables, 'tablename').search()
       db_name = item
        
       # waitinglist= getattr(app_tables, db_name).search()
       table_csv = getattr(app_tables, db_name).search().to_csv()
       filename0 = item + '_' +str(today)+' .csv'
       new_file0 = new_folder.create_file(filename0, table_csv)

