# Хакатон

## Исходные данные
* ```data.csv```  
* ```bacterial_descriptors.csv```  
* ```drug_descriptors.csv```  

См. [описание данных](data_description.md)

## Новые данные
* ```pKa.csv``` -- данные рКа для лекарств из ```drug_descriptors.csv```  
Вычисляли с помощью J. Chem. Inf. Mod. 61(1)  
http://dx.doi.org/10.1021/acs.jcim.1c00075

* ```clean_data.csv``` -- очищенные и объединенные данные.

## Блокноты
* ```main.ipynb``` -- основная часть с обработкой данных, обучением моделей и их сохранением.
* ```predict.ipynb``` -- указания к запуску готовых к предсказанию моделей и выполнению предсказаний на новых данных.

## pkl-файлы
* ```best_models.pkl``` -- CatBoostRegressor и ExtraTreesRegressor, с подобранными на кросс-валидации гиперпараметрами.
* ```fitted_models.pkl``` -- CatBoostRegressor, ExtraTreesRegressor, VotingRegressor, обученные к предсказанию на новых данных.  
(Features для отображения необходимых фич)
* ```best_nn.pkl``` -- обученная нейросеть для предсказания.
* ```scaler.pkl``` -- обученный скейлер для нейросети.

## Представление результатов
[_Team 3 Datacon.pdf](_Team 3 Datacon.pdf)

## Участники
* Артем В., Артем Г., Антон С. -- код предобработки и обучения моделей
* Андрей Б., Ангелина С. -- лит. поиск
