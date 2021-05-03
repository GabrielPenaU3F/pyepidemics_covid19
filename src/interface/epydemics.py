from src.data_io.console_manager import ConsoleManager
from src.data_manipulation.data_manager import DataManager
from src.data_io.plot_manager import PlotManager
from src.fitters.fitter import Fitter

console = ConsoleManager.get_instance()
plotter = PlotManager.get_instance()


def show_available_locations():
    countries = DataManager.get_location_list()
    console.print_countries(countries)


def show_data_from_location(country_id, dataset='total_cases'):
    country_data = DataManager.get_location_data(country_id, dataset)
    console.print_data_from_country(country_data, country_id, dataset)


def fit_contagion_model(country_name, dataset='total_cases', start=1, end=-1, x0=(0.1, 1), output=True, plot=True):
    fit = Fitter.fit(country_name, dataset, start, end, x0)

    if output is True:
        console.show_fit_results(fit)
        
    if plot is True:
        plotter.plot_fit_results(fit)


def analyze_model_parameters_over_time(country_name, dataset='total_cases', start=1, end=-1, start_from=30,
                                       fit_x0=(0.1, 1)):
    parameter_tuples = Fitter.perform_range_fits(country_name, dataset, start, end, start_from, fit_x0)
    plotter.plot_parameters_over_time(parameter_tuples, start_from)
