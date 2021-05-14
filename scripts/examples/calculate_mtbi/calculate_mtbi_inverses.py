from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics

DataManager.load_dataset('owid')
# epydemics.calculate_mtbi_inverse('Argentina', start=1, end=280, start_from=30, formula='approx_conditional', unit='day')
# epydemics.calculate_mtbi_inverse('Argentina', start=280, end=370, start_from=310, formula='approx_conditional', unit='day')
epydemics.calculate_mtbi_inverse('Argentina', start=370, formula='approx_conditional', unit='day')



