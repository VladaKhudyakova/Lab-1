salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
mes = 0
m_capital = 0
while mes < months:
    m_capital -= round(salary)
    m_capital += round(spend)
    spend *= (1 + increase)
    mes += 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", m_capital)
