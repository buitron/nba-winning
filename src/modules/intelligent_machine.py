import os
import pandas as pd
from sklearn.externals import joblib
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


class NBAChickenDinner:
    def __init__(self, model=None, season_data=None):
        self.model = joblib.load(os.path.join('static', 'model', model))
        self.season_data = season_data

    def prepare_data(self):
        class DropFeatures(BaseEstimator, TransformerMixin):
            def __init__(self, columns):
                self.columns = columns

            def fit(self, X, y=None):
                return self

            def transform(self, X):
                assert isinstance(X, pd.DataFrame)
                return X.drop(self.columns, axis=1)

        class ConvertDtypes(BaseEstimator, TransformerMixin):
            def __init__(self, dtype):
                self.dtype = dtype

            def fit(self, X, y=None):
                return self

            def transform(self, X):
                assert isinstance(X, pd.DataFrame)
                return X.astype(self.dtype)

        transformer = Pipeline([
            ('drp_features', DropFeatures(['TEAM', 'W', 'L'])),
            ('convert_dtypes', ConvertDtypes(float)),
            ('std_scaler', StandardScaler()),
        ])

        self.transformed_data = transformer.fit_transform(self.season_data)
        return self.transformed_data

    def run_model(self, X=None):
        if not X:
            X = self.transformed_data
        model = self.model
        self.predictions = model.predict(X)
        return self.predictions
