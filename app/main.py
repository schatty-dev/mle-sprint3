# импортируем библиотеку для работы со случайными числами
import random
import catboost

# импортируем класс для создания экземпляра FastAPI-приложения
from fastapi import FastAPI

# создаём экземпляр FastAPI-приложения
app = FastAPI()

# обрабатываем запросы к корню приложения
@app.get("/")
def read_root():
    return {"Hello": "World"}

# обрабатываем запросы к специальному пути для получения предсказания модели
# временно имитируем предсказание со случайной генерацией score
@app.get("/api/churn/{user_id}")
def get_prediction_for_item(user_id: str):
    return {"user_id": user_id, "score": random.random()}

@app.get("/service-status")
def health_check():
    return {"status": "ok"}


@app.get("/api/credit/{client_id}")
def get_approval():
    score = random.random()
    if score > 0.8:
        return {"approved": 1}
    return {"approved": 0}

from catboost import CatBoostClassifier


def load_churn_model(model_path: str):
    """Загружаем обученную модель оттока.
    Args:
        model_path (str): Путь до модели.
    """
    try:
        # ваш код здесь — загрузите модель
        model = CatBoostClassifier()
        model.load_model(model_path)
        print("Model loaded successfully")
    except Exception as e:
        print(f"Failed to load model: {e}")
    return model

if __name__ == "__main__":
    model = load_churn_model("models/catboost_churn_model.bin")
    print(f"Model parameter names: {model.feature_names_}") 