coupleapi

/api/bid/#заявки
/api/forms/#анкеты
/api/offers/#предложения

что стоит знать:

  - для запуска приложения в докере следуюет учитывать 
  неисследованную разработчиком проблему зависимостей между Django 3 + и dynamic_raw_id.
  Костыльный вариант решения уже применен если клонировать и вручную ставить в venv:
    меняем ```render_to_response``` на ```render``` в lib/python3.8/site-packages/dynamic_raw_id/views.py
    
  - не заведена группа пользователей под кредитные организации. не установленна аутентификация при стуке в api
