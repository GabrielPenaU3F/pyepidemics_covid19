import numpy as np
import pandas

from src.argument_verifier import ArgumentVerifier
from src.data_io.data_writer import DataWriter
from src.data_io.path_utils import get_project_root

pandas.options.mode.chained_assignment = None  # default='warn'


class DataManager:

    data_source = None
    data = None
    default_path = str(get_project_root() + '\\resources\\data\\')
    default_filename = 'full_dataset.csv'

    @classmethod
    def setup(cls, data_source_url, path=default_path, filename=default_filename):
        cls.data_source = data_source_url
        cls.data = pandas.read_csv(cls.data_source)
        full_path = path + filename
        DataWriter.write_to_csv(cls.data, full_path)

    @classmethod
    def load_dataset(cls, rel_path=default_path + default_filename):
        cls.data = pandas.read_csv(rel_path)

    @classmethod
    def get_country_list(cls):
        return cls.data['location'].unique()

    @classmethod
    def get_country_data(cls, country_id, dataset='total_cases', start=1, end=-1):
        data = cls.data.copy()
        ArgumentVerifier.validate_country(data, country_id)
        country_data = data[data['location'] == country_id]
        ArgumentVerifier.validate_dataset_arguments(country_data, dataset, start, end)
        requested_columns_df = country_data[['date', dataset]]
        return cls.prepare_dataset(requested_columns_df, dataset, start, end)

    @classmethod
    def prepare_dataset(cls, data, dataset_column, start, end):
        nonnan_dataset = data.dropna().reset_index(drop=True)
        requested_subset = cls.slice_data_by_index(nonnan_dataset, start, end)
        accumulated_events_previous_to_start = 0
        if start > 1:
            accumulated_events_previous_to_start = nonnan_dataset[dataset_column].iloc[start-2]
        requested_subset.loc[:, dataset_column] -= accumulated_events_previous_to_start
        correctly_indexed_dataset = requested_subset.set_index(np.arange(1, len(requested_subset) + 1), drop=True)
        return correctly_indexed_dataset.astype({dataset_column: 'int32'})

    @classmethod
    def slice_data_by_index(cls, data, start, end):
        return data.iloc[start-1:end, :].reset_index(drop=True)
