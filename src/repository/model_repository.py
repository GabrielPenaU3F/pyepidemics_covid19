from src.domain.models.model import ContagionModel
from src.domain.models.model import DelayedSShapedModel
from src.domain.models.model import GoelOkumotoModel


class ModelRepository:

    models = {
        'contagion': ContagionModel(),
        'goel_okumoto': GoelOkumotoModel(),
        'delayed_s_shaped': DelayedSShapedModel()
    }

    @classmethod
    def retrieve_model(cls, model_id):
        return cls.models.get(model_id)

    @classmethod
    def list_models(cls):
        return list(cls.models.keys())
