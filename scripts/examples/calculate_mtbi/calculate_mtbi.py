from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics

# DataManager.load_dataset('owid')
# epydemics.calculate_mtbi('Argentina', start=420, formula='approx_conditional', unit='sec')

DataManager.load_dataset('mapache_arg')
epydemics.calculate_mtbi('CABA', unit='sec', start=400, formula='approx_conditional')
